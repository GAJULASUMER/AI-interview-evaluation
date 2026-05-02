from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database.db import get_db
from utils.security import hash_password, verify_password

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        db = get_db()
        with db.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE email=%s", (email,))
            if cur.fetchone():
                flash("Email already exists", "danger")
                return redirect(url_for("auth.register"))
            cur.execute(
                "INSERT INTO users(name,email,password_hash) VALUES(%s,%s,%s)",
                (name, email, hash_password(password)),
            )
        db.commit()
        flash("Registration successful. Please login.", "success")
        return redirect(url_for("auth.login"))
    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        db = get_db()
        with db.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE email=%s", (email,))
            user = cur.fetchone()

        if not user or not verify_password(password, user["password_hash"]):
            flash("Invalid credentials", "danger")
            return redirect(url_for("auth.login"))

        session["user_id"] = user["id"]
        session["user_name"] = user["name"]
        return redirect(url_for("resume.upload_resume"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("auth.login"))
