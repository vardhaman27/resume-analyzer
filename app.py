from flask import Flask, render_template, request
import fitz
import os
from skills import extract_skills, extract_email, extract_phone, extract_linkedin, extract_github, extract_education, extract_experience
from database import init_db, save_report, get_all_reports

app = Flask(__name__)
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    resume = request.files["resume"]
    job_description = request.form["job_description"]

    resume_path = os.path.join("uploads", resume.filename)
    resume.save(resume_path)

    doc = fitz.open(resume_path)
    resume_text = ""
    for page in doc:
        resume_text += page.get_text()
    doc.close()

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)
    email = extract_email(resume_text)
    phone = extract_phone(resume_text)
    linkedin = extract_linkedin(resume_text)
    github = extract_github(resume_text)
    education = extract_education(resume_text)
    experience = extract_experience(resume_text)

    matched = [skill for skill in resume_skills if skill in jd_skills]
    missing = [skill for skill in jd_skills if skill not in resume_skills]

    if len(jd_skills) > 0:
        score = round((len(matched) / len(jd_skills)) * 100)
    else:
        score = 0

    recommendations = [f"Learn {skill}" for skill in missing]

    save_report(resume.filename, score, matched, missing)

    return render_template(
        "result.html",
        score=score,
        matched=matched,
        missing=missing,
        recommendations=recommendations,
        email=email,
        phone=phone,
        linkedin=linkedin,
        github=github,
        education=education,
        experience=experience
    )

@app.route("/history")
def history():
    reports = get_all_reports()
    return render_template("history.html", reports=reports)

if __name__ == "__main__":
    app.run(debug=True)