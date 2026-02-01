import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from job_matcher import recommend_jobs

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer & Job Recommender")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    skills = extract_skills(resume_text)

    st.subheader("✅ Extracted Skills")
    if skills:
        st.write(skills)
    else:
        st.warning("No skills detected")

    job_recommendations = recommend_jobs(skills)

    st.subheader("💼 Recommended Job Roles")
    if job_recommendations:
        for job, score in job_recommendations:
            st.write(f"**{job}** – Skill Match: {score}")
    else:
        st.info("No matching jobs found")

    st.subheader("📌 Missing Skills (Suggestion)")
    all_skills = {"python","java","sql","machine learning","html","css","javascript"}
    missing = all_skills - set(skills)
    st.write(list(missing))
