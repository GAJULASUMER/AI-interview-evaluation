from flask import Blueprint, request
from ..extensions import mongo

admin_bp = Blueprint("admin", __name__)


@admin_bp.get("/users")
def list_users():
    users = list(mongo.db.users.find())
    for user in users:
        user["id"] = str(user.pop("_id"))
        user.pop("password", None)
    return {"items": users}


@admin_bp.delete("/users/<user_id>")
def delete_user(user_id: str):
    mongo.db.users.delete_one({"_id": user_id})
    return {"message": "User deleted"}


@admin_bp.get("/interviews")
def list_interviews():
    interviews = list(mongo.db.interviews.find())
    for interview in interviews:
        interview["id"] = str(interview.pop("_id"))
    return {"items": interviews}


@admin_bp.post("/roles")
def add_role():
    payload = request.json or {}
    mongo.db.roles.insert_one({"name": payload.get("name")})
    return {"message": "Role added"}, 201


@admin_bp.post("/questions")
def add_question():
    payload = request.json or {}
    mongo.db.questions.insert_one(payload)
    return {"message": "Question added"}, 201
