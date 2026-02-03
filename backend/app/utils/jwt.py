import datetime
import jwt
from flask import current_app


def encode_token(payload: dict) -> str:
    exp = datetime.datetime.utcnow() + datetime.timedelta(hours=12)
    token_payload = {**payload, "exp": exp}
    return jwt.encode(token_payload, current_app.config["JWT_SECRET"], algorithm="HS256")


def decode_token(token: str) -> dict:
    return jwt.decode(token, current_app.config["JWT_SECRET"], algorithms=["HS256"])
