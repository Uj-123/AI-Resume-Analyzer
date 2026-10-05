# 🤖 AI Resume Analyzer

An AI/ML-powered web application that analyzes a resume against a job description and provides resume matching, skill-gap analysis, ATS-style checks, and improvement recommendations.

## 🚀 Features

- 📄 Upload resume in PDF format
- 📝 Enter a job description
- 🎯 Calculate resume-job similarity score
- 🤖 TF-IDF text vectorization
- 📐 Cosine similarity
- 🛠️ Skill matching
- ❌ Missing skill detection
- 📋 ATS-style resume assessment
- 💪 Resume strengths and weaknesses
- 💡 Job-specific learning recommendations
- 📝 Resume quality checks
- 🔑 Job keyword analysis
- 🏆 Custom resume readiness score
- 📥 Downloadable analysis report

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- PyPDF
- TF-IDF
- Cosine Similarity

## ⚙️ How It Works

1. User uploads a resume PDF.
2. The application extracts text from the PDF using PyPDF.
3. The resume and job description are converted into TF-IDF vectors.
4. Cosine similarity is used to calculate their textual similarity.
5. Required skills are detected from the job description.
6. Resume skills are compared with the required skills.
7. Missing skills and recommendations are displayed.
8. Additional ATS-style resume checks are performed.
9. A custom Resume Readiness Score is calculated.
10. The user can download the analysis report.

## 📊 Machine Learning Approach

The project uses **TF-IDF (Term Frequency-Inverse Document Frequency)** to represent text numerically.

Cosine similarity is then used to measure how similar the resume and job description are.

### Formula

Cosine Similarity:

`cos(θ) = (A · B) / (||A|| × ||B||)`

The resulting similarity value is converted into a percentage to create the Resume Match Score.

## 🎯 Purpose

This project was developed to demonstrate practical skills in:

- Python
- Machine Learning
- Natural Language Processing fundamentals
- Scikit-learn
- Data processing
- Streamlit application development
- Deployment

## 🔮 Future Improvements

- Advanced NLP-based skill extraction
- Named Entity Recognition
- Semantic embeddings
- LLM-based resume feedback
- Better ATS scoring
- Resume section classification
- Multiple job-description comparison
- Database integration

## 👩‍💻 Author

**Ujala Yadav**

B.Tech Computer Science & Engineering  
Garden City University, Bengaluru
