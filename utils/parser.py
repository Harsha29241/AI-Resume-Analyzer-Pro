import pdfplumber
import re


def extract_text(pdf_path):
    """
    Extract all text from PDF
    """

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_phone(text):

    pattern = r"(\+91[- ]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line.split()) >= 2 and len(line.split()) <= 4:

            return line

    return "Unknown"