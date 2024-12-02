# Job Matching and Interview Analysis System

An AI-powered tool to streamline recruitment by automating resume-job alignment and evaluating interview performance with insightful analytics.

## Features

### 1. **Job Matching System**
- **Upload Job Descriptions**: Parse and extract key details like skills, qualifications, and experience.
- **Upload Resumes**: Extract skills, experience, education, and tools from uploaded resumes.
- **Profile-Job Matching**: Calculate match scores for resumes based on job requirements.
- **Detailed Analytics**: Provide breakdowns of skill, experience, education, and tool matches.

### 2. **Interview Analysis Module**
- **Video Upload**: Process interview videos to extract transcriptions.
- **Analysis**: Assess communication style, active listening, engagement, and sentiment.
- **Detailed Summary**: Generate a comprehensive report for interview performance.

## How It Works
- Leverages **natural language processing (NLP)** with transformer-based models like BERT and BART for content analysis.
- Uses **vector databases (FAISS)** for similarity-based analysis and data retrieval.
- Employs advanced text and video processing for accurate evaluation.

## Technologies Used
- **Python Libraries**: Streamlit, Transformers, FAISS, OpenCV, PyPDF2, docx.
- **Models**: Hugging Face models for classification and sentiment analysis.
- **Tools**: PDF/DOCX parsing, video processing, and transcription extraction.

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd job-matching-interview-analysis

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

4. Open the app in your browser at http://localhost:8501.


Project Structure
```bash
.
├── app.py                 # Main Streamlit application
├── utils/
│   ├── resume_parser.py   # Resume parsing logic
│   ├── job_parser.py      # Job description parsing logic
│   ├── matcher.py         # Matching algorithm implementation
│   ├── video_processing.py # Video processing utilities
│   ├── analysis.py        # Interview analysis functions
│   ├── vector_database.py # Vector storage and search
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation

```