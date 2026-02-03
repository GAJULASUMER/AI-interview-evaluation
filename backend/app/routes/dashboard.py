from flask import Blueprint, request
from ..extensions import mongo

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.get("/profile")
def profile():
    user_id = request.args.get("user_id")
    user = mongo.db.users.find_one({"_id": user_id})
    if not user:
        return {"error": "User not found"}, 404
    return {
        "name": user.get("name"),
        "phone": user.get("phone"),
        "email": user.get("email"),
    }


@dashboard_bp.get("/history")
def history():
    user_id = request.args.get("user_id")
    interviews = list(mongo.db.interviews.find({"user_id": user_id}))
    for interview in interviews:
        interview["id"] = str(interview.pop("_id"))
    return {"items": interviews}
