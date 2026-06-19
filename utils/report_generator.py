from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


def generate_pdf(name,email,phone,score,role,skills,suggestions):

    pdf = SimpleDocTemplate("reports/report.pdf")

    story=[]

    story.append(Paragraph("<b>AI Resume Analyzer Report</b>",styles["Title"]))

    story.append(Paragraph(f"<b>Name:</b> {name}",styles["BodyText"]))

    story.append(Paragraph(f"<b>Email:</b> {email}",styles["BodyText"]))

    story.append(Paragraph(f"<b>Phone:</b> {phone}",styles["BodyText"]))

    story.append(Paragraph(f"<b>ATS Score:</b> {score}",styles["BodyText"]))

    story.append(Paragraph(f"<b>Predicted Role:</b> {role}",styles["BodyText"]))

    story.append(Paragraph("<b>Detected Skills</b>",styles["Heading2"]))

    for skill in skills:
        story.append(Paragraph(skill,styles["BodyText"]))

    story.append(Paragraph("<b>Suggestions</b>",styles["Heading2"]))

    for item in suggestions:
        story.append(Paragraph(item,styles["BodyText"]))

    pdf.build(story)

    return "reports/report.pdf"