def generate_suggestions(score):

    suggestions = []

    if score < 50:

        suggestions.append(
            "Add more technical skills."
        )

        suggestions.append(
            "Include academic projects."
        )

        suggestions.append(
            "Mention certifications."
        )

        suggestions.append(
            "Improve resume formatting."
        )

    elif score < 75:

        suggestions.append(
            "Add measurable achievements."
        )

        suggestions.append(
            "Include GitHub profile."
        )

        suggestions.append(
            "Mention internships."
        )

    else:

        suggestions.append(
            "Excellent Resume!"
        )

        suggestions.append(
            "Keep updating new projects."
        )

    return suggestions