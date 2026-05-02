from functools import wraps
from flask import session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(raw_password):
    return generate_password_hash(raw_password)


def verify_password(raw_password, hashed_password):
    return check_password_hash(hashed_password, raw_password)


def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get("user_id"):
            flash("Please login first.", "warning")
            return redirect(url_for("auth.login"))
        return fn(*args, **kwargs)

    return wrapper
