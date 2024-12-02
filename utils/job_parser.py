import json
import re

def parse_job_description(file):
    if file.name.endswith('.txt'):
        content = file.read().decode('utf-8')
    elif file.name.endswith('.json'):
        content = json.load(file)
    return extract_job_data(content)

def extract_job_data(content):
    # Dynamic extraction based on text content
    skills = extract_skills(content)
    experience = extract_experience(content)
    education = extract_education(content)
    tools = extract_tools(content)

    return {
        'title': extract_title(content),
        'skills': skills,
        'experience': experience,
        'education': education,
        'tools': tools
    }

def extract_title(content):
    match = re.search(r'Title:\s*(.+)', content)
    return match.group(1).strip() if match else 'Unknown'

def extract_skills(content):
    skill_keywords = ['Python', 'SQL', 'Tableau', 'Power BI', 'R', 'Excel', 'Hadoop', 'Spark']
    return [skill for skill in skill_keywords if skill.lower() in content.lower()]

def extract_experience(content):
    match = re.search(r'(\d+)\s+years? of experience', content.lower())
    return int(match.group(1)) if match else 0

def extract_education(content):
    education_keywords = ["Bachelor's", "Master's", "PhD", "Data Science", "Computer Science"]
    for keyword in education_keywords:
        if keyword.lower() in content.lower():
            return keyword
    return 'Unknown'

def extract_tools(content):
    tools_keywords = ['Hadoop', 'Spark', 'TensorFlow', 'PyTorch', 'Excel', 'Power BI']
    return [tool for tool in tools_keywords if tool.lower() in content.lower()]
