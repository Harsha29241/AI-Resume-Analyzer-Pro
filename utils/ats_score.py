import re

def calculate_ats_score(text):

    score = 0

    text = text.lower()

    keywords = [
        "python",
        "java",
        "sql",
        "machine learning",
        "ai",
        "flask",
        "django",
        "git",
        "html",
        "css",
        "javascript",
        "react",
        "node",
        "api",
        "data analysis"
    ]

    matched = []

    for word in keywords:
        if word in text:
            matched.append(word)
            score += 6

    score = min(score,100)

    return score, matched