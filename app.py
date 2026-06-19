from flask import Flask, render_template, request, send_file
import os

from utils.parser import (
    extract_text,
    extract_name,
    extract_email,
    extract_phone
)

from utils.ats_score import calculate_ats_score
from utils.role_predictor import predict_role
from utils.suggestions import generate_suggestions
from utils.report_generator import generate_pdf

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return "No Resume Uploaded"

    file = request.files["resume"]

    if file.filename == "":
        return "Choose a PDF"

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    text = extract_text(filepath)

    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)

    ats_score, matched_skills = calculate_ats_score(text)
    predicted_role = predict_role(text)
    suggestions = generate_suggestions(ats_score)

    generate_pdf(
        name,
        email,
        phone,
        ats_score,
        predicted_role,
        matched_skills,
        suggestions
    )

    return render_template(
        "dashboard.html",
        filename=file.filename,
        name=name,
        email=email,
        phone=phone,
        resume_text=text,
        ats_score=ats_score,
        matched_skills=matched_skills,
        predicted_role=predicted_role,
        suggestions=suggestions
    )


@app.route("/download")
def download():
    return send_file(
        "reports/report.pdf",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)