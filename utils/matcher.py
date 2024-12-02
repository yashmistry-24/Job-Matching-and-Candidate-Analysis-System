def calculate_match(job, resume):
    skill_match = calculate_skill_match(job['skills'], resume['skills'])
    experience_match = calculate_experience_match(job['experience'], resume['experience'])
    education_match = calculate_education_match(job['education'], resume['education'])
    tool_match = calculate_tool_match(job['tools'], resume['tools'])

    match_score = (skill_match + experience_match + education_match + tool_match) / 4
    return match_score, skill_match, experience_match, education_match, tool_match

def calculate_skill_match(job_skills, resume_skills):
    common_skills = set(job_skills).intersection(resume_skills)
    return len(common_skills) / len(job_skills) * 100 if job_skills else 0

def calculate_experience_match(job_experience, resume_experience):
    return min(job_experience, resume_experience) / job_experience * 100 if job_experience else 0

def calculate_education_match(job_education, resume_education):
    return 100 if job_education.lower() == resume_education.lower() else 0

def calculate_tool_match(job_tools, resume_tools):
    common_tools = set(job_tools).intersection(resume_tools)
    return len(common_tools) / len(job_tools) * 100 if job_tools else 0
