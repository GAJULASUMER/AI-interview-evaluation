from flask import Blueprint, request
from ..extensions import mongo
from ..services.otp import generate_otp
from ..utils.security import hash_password, verify_password
from ..utils.jwt import encode_token

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/signup")
def signup():
    payload = request.json or {}
    required = {"name", "phone", "email", "password"}
    if not required.issubset(payload):
        return {"error": "Missing required fields"}, 400

    user = mongo.db.users.find_one({"email": payload["email"]})
    if user:
        return {"error": "User already exists"}, 409

    otp_code = generate_otp()
    mongo.db.otp.insert_one({"phone": payload["phone"], "otp": otp_code})

    mongo.db.users.insert_one(
        {
            "name": payload["name"],
            "phone": payload["phone"],
            "email": payload["email"],
            "password": hash_password(payload["password"]),
            "verified": False,
        }
    )

    return {"message": "OTP sent", "otp": otp_code}, 201


@auth_bp.post("/verify-otp")
def verify_otp():
    payload = request.json or {}
    otp_entry = mongo.db.otp.find_one({"phone": payload.get("phone"), "otp": payload.get("otp")})
    if not otp_entry:
        return {"error": "Invalid OTP"}, 400
    mongo.db.users.update_one({"phone": payload.get("phone")}, {"$set": {"verified": True}})
    return {"message": "Verified"}


@auth_bp.post("/login")
def login():
    payload = request.json or {}
    user = mongo.db.users.find_one({"email": payload.get("email")})
    if not user:
        user = mongo.db.users.find_one({"phone": payload.get("phone")})
    if not user:
        return {"error": "Invalid credentials"}, 401
    if not verify_password(payload.get("password", ""), user["password"]):
        return {"error": "Invalid credentials"}, 401

    token = encode_token({"user_id": str(user["_id"])})
    return {"token": token, "user": {"name": user["name"], "email": user["email"]}}


@auth_bp.post("/forgot-password")
def forgot_password():
    payload = request.json or {}
    user = mongo.db.users.find_one({"email": payload.get("email")})
    if not user:
        return {"error": "User not found"}, 404
    otp_code = generate_otp()
    mongo.db.otp.insert_one({"phone": user["phone"], "otp": otp_code})
    return {"message": "OTP sent", "otp": otp_code}


@auth_bp.post("/reset-password")
def reset_password():
    payload = request.json or {}
    otp_entry = mongo.db.otp.find_one({"phone": payload.get("phone"), "otp": payload.get("otp")})
    if not otp_entry:
        return {"error": "Invalid OTP"}, 400
    mongo.db.users.update_one(
        {"phone": payload.get("phone")},
        {"$set": {"password": hash_password(payload.get("password", ""))}},
    )
    return {"message": "Password updated"}
