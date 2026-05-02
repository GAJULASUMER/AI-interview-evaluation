import json
from flask import Blueprint, render_template, session
from database.db import get_db
from utils.security import login_required

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard_bp.route("/")
@login_required
def dashboard():
    db = get_db()
    with db.cursor() as cur:
        cur.execute(
            "SELECT id, overall_score, summary, created_at FROM interviews WHERE user_id=%s ORDER BY created_at DESC",
            (session["user_id"],),
        )
        interviews = cur.fetchall()

        latest = None
        if interviews:
            cur.execute("SELECT details_json FROM interviews WHERE id=%s", (interviews[0]["id"],))
            latest = cur.fetchone()
    details = json.loads(latest["details_json"]) if latest else []
    return render_template("dashboard.html", interviews=interviews, details=details)
