from docx import Document
from PyPDF2 import PdfReader
import re

def parse_resume(file):
    if file.name.endswith('.docx'):
        return parse_docx(file)
    elif file.name.endswith('.pdf'):
        return parse_pdf(file)

def parse_docx(file):
    doc = Document(file)
    content = " ".join([paragraph.text for paragraph in doc.paragraphs])
    return extract_resume_data(content)

def parse_pdf(file):
    reader = PdfReader(file)
    content = " ".join([page.extract_text() for page in reader.pages])
    return extract_resume_data(content)

def extract_resume_data(content):
    # Dynamic extraction based on keywords
    skills = extract_skills(content)
    experience = extract_experience(content)
    education = extract_education(content)
    tools = extract_tools(content)

    return {
        'skills': skills,
        'experience': experience,
        'education': education,
        'tools': tools
    }

def extract_skills(content):
    skill_keywords = ['Python', 'SQL', 'R', 'Tableau', 'Power BI', 'Excel', 'Hadoop', 'Spark', 'TensorFlow', 'PyTorch']
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
