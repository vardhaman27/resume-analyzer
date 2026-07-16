import re

SKILLS = [
    "Python", "C++", "C", "SQL", "Git", "Docker",
    "AWS", "Flask", "Java", "Linux"
]

def extract_skills(text):
    text_lower = text.lower()
    found = []
    for skill in SKILLS:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found.append(skill)
    return found

def extract_email(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(pattern, text)
    if match:
        return match.group()
    return None

def extract_phone(text):
    pattern = r'(\+?\d{1,3}[\s-]?)?\d{10}'
    match = re.search(pattern, text)
    if match:
        return match.group()
    return None

def extract_linkedin(text):
    pattern = r'(https?://)?(www\.)?linkedin\.com/in/[a-zA-Z0-9\-_/]+'
    match = re.search(pattern, text)
    if match:
        return match.group()
    return None

def extract_github(text):
    pattern = r'(https?://)?(www\.)?github\.com/[a-zA-Z0-9\-_/]+'
    match = re.search(pattern, text)
    if match:
        return match.group()
    return None
def extract_education(text):
    keywords = ["Bachelor", "Bachelors", "Master", "Masters", "B.Tech", "B.E.", "BCA", "MCA", "PhD", "Diploma", "12th", "10th"]
    lines = text.split("\n")
    found_lines = []
    for line in lines:
        for keyword in keywords:
            if keyword.lower() in line.lower():
                found_lines.append(line.strip())
                break
    return found_lines

def extract_experience(text):
    pattern = r'\b(19|20)\d{2}\s*[-–]\s*(Present|present|(19|20)\d{2})\b'
    matches = re.findall(pattern, text)
    lines = text.split("\n")
    found_lines = []
    for line in lines:
        if re.search(pattern, line):
            found_lines.append(line.strip())
    return found_lines