import json
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database.db import get_db
from utils.security import login_required
from models.evaluator import generate_questions, evaluate_answer

interview_bp = Blueprint("interview", __name__, url_prefix="/interview")


@interview_bp.route("/start", methods=["GET"])
@login_required
def start_interview():
    db = get_db()
    with db.cursor() as cur:
        cur.execute("SELECT * FROM resumes WHERE user_id=%s ORDER BY created_at DESC LIMIT 1", (session["user_id"],))
        resume = cur.fetchone()
    if not resume:
        flash("Upload your resume first.", "warning")
        return redirect(url_for("resume.upload_resume"))

    questions = generate_questions(resume["parsed_text"], (resume["skills"] or "").split(", "))
    return render_template("interview.html", questions=questions)


@interview_bp.route("/submit", methods=["POST"])
@login_required
def submit_interview():
    answers = request.get_json(force=True).get("answers", [])

    db = get_db()
    with db.cursor() as cur:
        cur.execute("SELECT * FROM resumes WHERE user_id=%s ORDER BY created_at DESC LIMIT 1", (session["user_id"],))
        resume = cur.fetchone()

    questions = generate_questions(resume["parsed_text"], (resume["skills"] or "").split(", "))
    details, total = [], 0

    for i, question in enumerate(questions):
        answer = answers[i] if i < len(answers) else ""
        score, feedback = evaluate_answer(question, answer, resume["parsed_text"])
        details.append({"question": question, "answer": answer, "score": score, "feedback": feedback})
        total += score

    avg_score = round(total / max(len(questions), 1), 2)
    summary = "Excellent performance." if avg_score >= 75 else "Average performance with room for improvement."

    with db.cursor() as cur:
        cur.execute(
            "INSERT INTO interviews(user_id, resume_id, overall_score, summary, details_json) VALUES(%s,%s,%s,%s,%s)",
            (session["user_id"], resume["id"], avg_score, summary, json.dumps(details)),
        )
    db.commit()

    return {"overall_score": avg_score, "summary": summary, "details": details}
