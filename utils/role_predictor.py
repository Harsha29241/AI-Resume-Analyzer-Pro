def predict_role(text):

    text = text.lower()

    if "tensorflow" in text or "pytorch" in text or "machine learning" in text:
        return "AI / Machine Learning Engineer"

    elif "flask" in text or "django" in text:
        return "Python Backend Developer"

    elif "react" in text or "node" in text:
        return "Full Stack Developer"

    elif "html" in text and "css" in text and "javascript" in text:
        return "Frontend Developer"

    elif "sql" in text or "power bi" in text or "tableau" in text:
        return "Data Analyst"

    else:
        return "Software Developer"