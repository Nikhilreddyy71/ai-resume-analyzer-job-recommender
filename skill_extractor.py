SKILLS = [
    "python", "java", "c++", "sql", "machine learning",
    "deep learning", "nlp", "html", "css", "javascript",
    "react", "node", "data analysis", "django", "flask"
]

def extract_skills(resume_text):
    extracted = []
    for skill in SKILLS:
        if skill in resume_text:
            extracted.append(skill)
    return extracted
