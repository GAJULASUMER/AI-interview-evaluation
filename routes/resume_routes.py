import os
from uuid import uuid4
from flask import Blueprint, current_app, render_template, request, redirect, url_for, flash, session
from database.db import get_db
from utils.security import login_required
from utils.resume_parser import extract_resume_text, extract_skills

resume_bp = Blueprint("resume", __name__, url_prefix="/resume")


@resume_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload_resume():
    if request.method == "POST":
        resume = request.files.get("resume")
        if not resume:
            flash("Please select a resume file.", "warning")
            return redirect(request.url)

        ext = os.path.splitext(resume.filename)[1].lower()
        if ext not in {".pdf", ".doc", ".docx", ".txt"}:
            flash("Unsupported file format.", "danger")
            return redirect(request.url)

        os.makedirs(current_app.config["UPLOAD_FOLDER"], exist_ok=True)
        file_name = f"{uuid4().hex}{ext}"
        file_path = os.path.join(current_app.config["UPLOAD_FOLDER"], file_name)
        resume.save(file_path)

        text = extract_resume_text(file_path)
        skills = ", ".join(extract_skills(text))

        db = get_db()
        with db.cursor() as cur:
            cur.execute(
                "INSERT INTO resumes(user_id, file_path, parsed_text, skills) VALUES(%s,%s,%s,%s)",
                (session["user_id"], file_path, text, skills),
            )
        db.commit()
        flash("Resume uploaded and parsed.", "success")
        return redirect(url_for("interview.start_interview"))

    return render_template("upload_resume.html")
