from flask import Blueprint, request
from ..extensions import mongo
from ..services.ats import score_resume

resume_bp = Blueprint("resume", __name__)


@resume_bp.post("/upload")
def upload_resume():
    payload = request.json or {}
    resume_text = payload.get("resume_text", "")
    jd_text = payload.get("jd_text")
    result = score_resume(resume_text, jd_text)

    record = {
        "user_id": payload.get("user_id"),
        "ats_score": result.score,
        "strengths": result.strengths,
        "missing_keywords": result.missing_keywords,
        "formatting_issues": result.formatting_issues,
        "summary_quality": result.summary_quality,
        "match_percentage": result.match_percentage,
    }
    mongo.db.resumes.insert_one(record)
    return record, 201
