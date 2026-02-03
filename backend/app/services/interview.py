from dataclasses import dataclass


@dataclass
class QuestionScore:
    question: str
    score: int
    strengths: list[str]
    weaknesses: list[str]
    missing_points: list[str]


@dataclass
class InterviewScore:
    overall_score: int
    category_scores: dict
    questions: list[QuestionScore]
    suggestions: dict


def evaluate_interview(transcript: str, role: str) -> InterviewScore:
    questions = [
        QuestionScore(
            question="Tell me about yourself",
            score=8,
            strengths=["Concise summary"],
            weaknesses=["Add measurable impact"],
            missing_points=["Recent achievements"],
        )
    ]
    category_scores = {
        "communication": 82,
        "confidence": 78,
        "relevance": 80,
        "eye_contact": 75,
        "emotion": 77,
    }
    suggestions = {
        "communication": "Speak a bit slower and pause after key points.",
        "confidence": "Maintain steady tone and avoid filler words.",
        "eye_contact": "Look at the camera for 3-4 seconds at a time.",
        "fluency": "Use simple, crisp sentences; avoid over-explaining.",
        "answer_structure": "Use STAR format for behavioral questions.",
        "resume": "Add impact metrics to your last two roles.",
        "role_specific": f"Highlight core skills for {role} in the first answer.",
        "hr_fit": "Show curiosity about team culture and growth.",
    }
    return InterviewScore(
        overall_score=80,
        category_scores=category_scores,
        questions=questions,
        suggestions=suggestions,
    )
