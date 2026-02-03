from dataclasses import dataclass


@dataclass
class ATSResult:
    score: int
    strengths: list[str]
    missing_keywords: list[str]
    formatting_issues: list[str]
    summary_quality: str
    match_percentage: int | None = None


def score_resume(resume_text: str, jd_text: str | None = None) -> ATSResult:
    strengths = ["Clear experience section", "Relevant skills present"]
    missing_keywords = ["leadership", "cloud"]
    formatting_issues = ["Use consistent bullet points"]
    summary_quality = "Good"
    score = 78
    match_percentage = 82 if jd_text else None
    return ATSResult(
        score=score,
        strengths=strengths,
        missing_keywords=missing_keywords,
        formatting_issues=formatting_issues,
        summary_quality=summary_quality,
        match_percentage=match_percentage,
    )
