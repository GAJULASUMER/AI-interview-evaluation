from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def generate_questions(resume_text, skills):
    base = [
        "Tell me about yourself and your most relevant project experience.",
        "Describe a challenging bug you fixed and your debugging process.",
        "How do you ensure code quality and maintainability in your work?",
    ]
    skill_questions = [f"Explain your hands-on experience with {skill.upper()} and a real use case." for skill in skills[:5]]
    project_q = "Based on your resume, how would you design a scalable solution for your domain?"
    return base + skill_questions + [project_q]


def evaluate_answer(question, answer, resume_text):
    if not answer.strip():
        return 0, "No answer submitted."

    corpus = [question + " " + resume_text[:1500], answer]
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(corpus)
    relevance = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    word_count = len(answer.split())
    depth_score = min(word_count / 120, 1.0)
    final = round((relevance * 0.7 + depth_score * 0.3) * 100, 2)

    feedback = []
    feedback.append("Good relevance to the question." if relevance >= 0.25 else "Answer should be more aligned with the question and resume context.")
    feedback.append("Good depth and clarity." if word_count >= 60 else "Add more concrete examples and technical details.")

    return final, " ".join(feedback)
