import pandas as pd

def recommend_jobs(user_skills):
    jobs = pd.read_csv("jobs.csv")
    recommendations = []

    for _, row in jobs.iterrows():
        job_skills = row["skills"].split(",")
        match_count = len(set(user_skills) & set(job_skills))
        if match_count > 0:
            recommendations.append((row["job_role"], match_count))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations
