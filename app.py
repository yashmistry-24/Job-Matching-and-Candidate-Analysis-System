import streamlit as st
from utils.resume_parser import parse_resume
from utils.job_parser import parse_job_description
from utils.matcher import calculate_match
from utils.video_processing import process_video
from utils.analysis import analyze_interview_v3

# Streamlit App
st.set_page_config(page_title="Job Matching and Interview Analysis", page_icon=":guardsman:", layout="wide")

# Title and Heading
st.title("Job Matching and Interview Analysis System")
st.write("Welcome to the system that helps you match job descriptions with resumes and analyze interview content.")

# Main Navigation
st.sidebar.header("Choose Module")
choice = st.sidebar.radio("Select an option", ["Home", "Job Matching System", "Interview Analysis Module"])

# Home Page
if choice == "Home":
    st.write("This project is a Job Matching and Interview Analysis System that uses artificial intelligence to automate recruitment tasks. It consists of two primary modules:")
    st.write("1. Job Matching System: This module allows users to upload job descriptions and resumes to automatically match candidates with job requirements based on skills, experience, education, and tools. It provides detailed match percentages for each resume against each job.")
    st.write("2. Interview Analysis Module: This module analyzes interview videos to assess candidates' communication style, active listening, and engagement using advanced natural language processing.")

# Job Matching System Page
elif choice == "Job Matching System":
    st.header("Job Matching System")

    # Job Descriptions Section
    st.subheader("Upload Job Descriptions")
    job_files = st.file_uploader("Upload Job Descriptions (Text or JSON)", accept_multiple_files=True, type=['txt', 'json'])
    if job_files:
        job_descriptions = [parse_job_description(file) for file in job_files]
        st.success(f"{len(job_descriptions)} Job Descriptions Processed!")

    # Resumes Section
    st.subheader("Upload Resumes")
    resume_files = st.file_uploader("Upload Resumes (PDF or DOCX)", accept_multiple_files=True, type=['pdf', 'docx'])
    if resume_files:
        resumes = [parse_resume(file) for file in resume_files]
        st.success(f"{len(resumes)} Resumes Processed!")

    # Matching Section
    if job_files and resume_files:
        st.subheader("Matching Results")
        for i, job in enumerate(job_descriptions):
            st.write(f"**Job {i+1}: {job['title']}**")
            for j, resume in enumerate(resumes):
                match_score, skill_match, experience_match, education_match, tool_match = calculate_match(job, resume)
                st.write(f"Candidate {j+1} Match Score: {match_score:.1f}%")
                st.write(f"**Skill Match**: {skill_match:.1f}%")
                st.write(f"**Experience Match**: {experience_match:.1f}%")
                st.write(f"**Education Match**: {education_match:.1f}%")
                st.write(f"**Tool Match**: {tool_match:.1f}%")
                st.write("---")

# Interview Analysis Module Page
elif choice == "Interview Analysis Module":
    st.header("Interview Analysis Module")

    # Upload Interview Video
    st.subheader("Upload Interview Video")
    video_file = st.file_uploader("Upload Video (MP4 format)", type=['mp4'])
    if video_file:
        processed_video = process_video(video_file)
        st.success("Video Processed Successfully!")

        # Analyze Interview
        st.subheader("Interview Analysis")
        analysis_result = analyze_interview_v3(processed_video)

        st.write("### Analysis Summary")
        st.write(f"**Communication Style**: {analysis_result['communication_style']}")
        st.write(f"**Active Listening**: {analysis_result['active_listening']}")
        st.write(f"**Engagement with Interviewer**: {analysis_result['engagement']}")
