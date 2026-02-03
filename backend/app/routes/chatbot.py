from flask import Blueprint, request
from ..services.chatbot import hr_reply

chatbot_bp = Blueprint("chatbot", __name__)


@chatbot_bp.post("/ask")
def ask():
    payload = request.json or {}
    response = hr_reply(payload.get("prompt", ""))
    return {"response": response}
