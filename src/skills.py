import re

SKILLS = [
    "python","java","c++","c#","sql","javascript","typescript",
    "machine learning","deep learning","nlp","pandas","numpy","scikit-learn",
    "tensorflow","pytorch","docker","aws","gcp","azure",
    "react","node","flask","fastapi","streamlit",
    "git","linux","kubernetes"
]

def extract_skills(text: str, skills=SKILLS):
    found = set()
    for s in skills:
        pattern = r"\b" + re.escape(s) + r"\b"
        if re.search(pattern, text):
            found.add(s)
    return found

def missing_skills(resume_text: str, job_text: str):
    r = extract_skills(resume_text)
    j = extract_skills(job_text)
    return sorted(list(j - r)), sorted(list(j & r))