import os
from flask import Blueprint, request
from ..extensions import mongo
from ..services.interview import evaluate_interview
from ..utils.pdf import generate_report
from ..utils.emailer import send_email

interview_bp = Blueprint("interview", __name__)


@interview_bp.post("/submit")
def submit_interview():
    payload = request.json or {}
    transcript = payload.get("transcript", "")
    role = payload.get("role", "")
    result = evaluate_interview(transcript, role)

    report_payload = {
        "user_id": payload.get("user_id"),
        "role": role,
        "overall_score": result.overall_score,
        "category_scores": result.category_scores,
        "questions": [q.__dict__ for q in result.questions],
        "suggestions": result.suggestions,
    }
    mongo.db.interviews.insert_one(report_payload)
    return report_payload, 201


@interview_bp.post("/report")
def generate_pdf_report():
    payload = request.json or {}
    output_path = os.path.join(os.getcwd(), "interview_report.pdf")
    report_path = generate_report(payload, output_path)
    return {"report_path": report_path}


@interview_bp.post("/email-report")
def email_report():
    payload = request.json or {}
    send_email(
        to_email=payload.get("email", ""),
        subject="Your AI Interview Report",
        body="Dear Candidate,\n\nPlease find your interview report attached.\n\nRegards,\nHR Team",
        attachment_path=payload.get("report_path"),
    )
    return {"message": "Email sent"}
