import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")

# Sidebar
with st.sidebar:
    st.header("🤖 AI Resume Analyzer")

    st.write("### How it works")

    st.write("1️⃣ Upload your resume")
    st.write("2️⃣ Paste the job description")
    st.write("3️⃣ Click Analyze")
    st.write("4️⃣ Review your results")

    st.divider()

    st.write("### Features")
    st.write("📊 Resume Matching")
    st.write("🛠️ Skill Analysis")
    st.write("📋 ATS Assessment")
    st.write("💡 Learning Recommendations")
    st.write("📥 Download Report")

st.write("Upload your resume and compare it with a job description.")

# Resume upload
resume = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

# Job description
job_description = st.text_area(
    "📋 Paste Job Description",
    height=200
)

# Analyze button
if st.button("🔍 Analyze Resume"):

    if resume is None:
        st.warning("Please upload your resume.")

    elif job_description.strip() == "":
        st.warning("Please enter a job description.")

    else:
        # Read PDF
        reader = PdfReader(resume)

        resume_text = ""

        for page in reader.pages:
            text = page.extract_text()

            if text:
                resume_text += text

        # TF-IDF
        documents = [resume_text, job_description]

        vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        tfidf_matrix = vectorizer.fit_transform(documents)

        # Similarity
        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )

        score = similarity[0][0] * 100

        # Result
        st.success("Analysis completed!")

        st.subheader("🎯 Resume Match Score")

        st.metric(
            "Match Score",
            f"{score:.2f}%"
        )

        # ATS Score Category
        if score >= 80:
            ats_status = "🟢 Excellent Match"
        elif score >= 60:
            ats_status = "🟡 Good Match"
        elif score >= 40:
            ats_status = "🟠 Moderate Match"
        else:
            ats_status = "🔴 Needs Improvement"

        st.subheader("📋 ATS Assessment")

        st.write("**Overall Status:**", ats_status)

        if score >= 80:
            st.success("Your resume strongly matches this job description.")
        elif score >= 60:
            st.info("Your resume has a good match, but some improvements can increase the score.")
        elif score >= 40:
            st.warning("Your resume has a moderate match. Consider adding relevant skills and project experience.")
        else:
            st.error("Your resume needs improvement for this particular job.")

        # Skills list
        skills = [
            "python",
            "sql",
            "machine learning",
            "pandas",
            "numpy",
            "scikit-learn",
            "tensorflow",
            "pytorch",
            "nlp",
            "deep learning",
            "streamlit",
            "git",
            "github",
            "data analysis",
            "data visualization",
            "generative ai",
            "llm",
            "computer vision"
        ]

        # Convert resume and job description to lowercase
        resume_lower = resume_text.lower()
        job_lower = job_description.lower()

        # Skill aliases
        skill_aliases = {
            "python": ["python"],
            "sql": ["sql"],
            "machine learning": ["machine learning", "ml"],
            "pandas": ["pandas"],
            "numpy": ["numpy"],
            "scikit-learn": ["scikit-learn", "sklearn"],
            "tensorflow": ["tensorflow"],
            "pytorch": ["pytorch"],
            "nlp": ["nlp", "natural language processing"],
            "deep learning": ["deep learning"],
            "streamlit": ["streamlit"],
            "git": ["git"],
            "github": ["github"],
            "data analysis": ["data analysis", "data analytics"],
            "data visualization": ["data visualization"],
            "generative ai": ["generative ai", "genai"],
            "llm": ["llm", "large language model", "large language models"],
            "computer vision": ["computer vision", "opencv"]
        }

        # Detect skills from resume
        detected_resume_skills = []

        for skill, keywords in skill_aliases.items():
            for keyword in keywords:
                if keyword in resume_lower:
                    detected_resume_skills.append(skill)
                    break

        # Detect skills from job description
        detected_job_skills = []

        for skill, keywords in skill_aliases.items():
            for keyword in keywords:
                if keyword in job_lower:
                    detected_job_skills.append(skill)
                    break

        # Find matching skills
        matching_skills = [
            skill
            for skill in detected_resume_skills
            if skill in detected_job_skills
        ]

        # Find missing skills
        missing_skills = [
            skill
            for skill in detected_job_skills
            if skill not in detected_resume_skills
        ]

        # Calculate skill match percentage
        total_required_skills = len(detected_job_skills)

        matched_skill_count = len(matching_skills)

        if total_required_skills > 0:
            skill_match_percentage = (
                                             matched_skill_count / total_required_skills
                                     ) * 100
        else:
            skill_match_percentage = 0
        # Display matching skills
        st.subheader("✅ Matching Skills")

        if matching_skills:
            for skill in matching_skills:
                st.write("✔️", skill.title())
        else:
            st.write("No matching skills found.")

        # Display missing skills
        st.subheader("❌ Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.write("🔴", skill.title())
        else:
            st.write("No missing skills found.")

        # Resume Strengths
        st.subheader("💪 Resume Strengths")

        if matching_skills:
            st.write("Your resume matches these required skills:")
            for skill in matching_skills:
                st.write("✅", skill.title())
        else:
            st.write("No strong skill matches found yet.")

        # Resume Weaknesses
        st.subheader("⚠️ Resume Weaknesses")

        if missing_skills:
            st.write("These skills are required by the job but are missing from your resume:")
            for skill in missing_skills:
                st.write("❌", skill.title())
        else:
            st.success("No major skill gaps detected!")

        # Learning Recommendations
        st.subheader("💡 Recommended Actions")

        if missing_skills:
            st.write("To improve your chances for this job, focus on:")

            for skill in missing_skills:
                if skill == "scikit-learn":
                    st.write("📚 Learn Scikit-learn and practice classification/regression models.")
                elif skill == "machine learning":
                    st.write("📚 Strengthen Machine Learning concepts and model evaluation.")
                elif skill == "sql":
                    st.write("📚 Practice SQL queries, JOINs, GROUP BY and subqueries.")
                elif skill == "python":
                    st.write("📚 Strengthen Python programming and problem-solving.")
                elif skill == "pandas":
                    st.write("📚 Practice Pandas for data cleaning and analysis.")
                elif skill == "numpy":
                    st.write("📚 Practice NumPy arrays and numerical operations.")
                elif skill == "deep learning":
                    st.write("📚 Learn neural networks and deep learning fundamentals.")
                elif skill == "nlp":
                    st.write("📚 Learn NLP preprocessing and text classification.")
                elif skill == "generative ai":
                    st.write("📚 Learn LLMs, prompt engineering and Generative AI concepts.")
                elif skill == "llm":
                    st.write("📚 Learn LLM APIs, embeddings and basic RAG concepts.")
                elif skill == "computer vision":
                    st.write("📚 Practice OpenCV and computer vision fundamentals.")
                else:
                    st.write("📚 Learn:", skill.title())

        else:
            st.success("🎉 Your skills match the job requirements!")

        # Resume Quality Analysis
        st.subheader("📝 Resume Quality Analysis")

        resume_checks = {
            "📧 Email": "@" in resume_text,
            "📱 Phone Number": any(char.isdigit() for char in resume_text) and len(
                "".join(filter(str.isdigit, resume_text))
            ) >= 10,
            "🔗 LinkedIn": "linkedin" in resume_lower,
            "💻 GitHub": "github" in resume_lower,
            "🎓 Education": "education" in resume_lower or "university" in resume_lower,
            "🛠️ Skills": "skills" in resume_lower or "technical skills" in resume_lower,
            "🚀 Projects": "projects" in resume_lower or "project" in resume_lower,
            "💼 Experience": "experience" in resume_lower or "internship" in resume_lower
        }

        for check, passed in resume_checks.items():
            if passed:
                st.success(f"✅ {check} — Found")
            else:
                st.warning(f"⚠️ {check} — Not Found")

        # Project & Experience Analysis
        st.subheader("🚀 Project & Experience Analysis")

        project_keywords = [
            "project",
            "projects",
            "developed",
            "built",
            "created",
            "implemented"
        ]

        experience_keywords = [
            "experience",
            "internship",
            "intern",
            "worked",
            "company"
        ]

        project_found = any(
            keyword in resume_lower
            for keyword in project_keywords
        )

        experience_found = any(
            keyword in resume_lower
            for keyword in experience_keywords
        )

        col1, col2 = st.columns(2)

        with col1:
            if project_found:
                st.success("🚀 Project experience detected")
            else:
                st.warning("⚠️ No project experience detected")

        with col2:
            if experience_found:
                st.success("💼 Experience/Internship detected")
            else:
                st.info("ℹ️ No formal experience detected")

        # Project Quality Analysis
        st.subheader("🔍 Project Quality Analysis")

        action_words = [
            "developed",
            "built",
            "created",
            "implemented",
            "designed",
            "developed",
            "analyzed",
            "trained",
            "predicted",
            "automated"
        ]

        action_word_count = 0

        for word in action_words:
            if word in resume_lower:
                action_word_count += 1

        if action_word_count >= 4:
            st.success("🔥 Strong project language detected!")
        elif action_word_count >= 2:
            st.info("👍 Your project descriptions are decent.")
        else:
            st.warning("⚠️ Add stronger technical action words to your project descriptions.")

        st.metric(
            "Technical Action Words",
            action_word_count
        )

        # Keyword Analysis
        st.subheader("🔑 Keyword Analysis")

        job_words = job_lower.split()

        resume_keyword_matches = []

        for word in job_words:
            clean_word = word.strip(".,!?():;\"'")

            if len(clean_word) > 3 and clean_word in resume_lower:
                if clean_word not in resume_keyword_matches:
                    resume_keyword_matches.append(clean_word)

        st.write(
            f"Found **{len(resume_keyword_matches)}** relevant job-description keywords in your resume."
        )

        if resume_keyword_matches:
            for keyword in resume_keyword_matches[:20]:
                st.write("🔹", keyword.title())
        else:
            st.warning("No important keywords were detected.")

        # Resume Readiness Score
        st.subheader("🏆 Resume Readiness Score")

        skill_score = skill_match_percentage

        quality_score = (
                                sum(resume_checks.values()) / len(resume_checks)
                        ) * 100

        project_score = 100 if project_found else 0

        keyword_score = min(
            (len(resume_keyword_matches) / max(len(job_words), 1)) * 100,
            100
        )

        readiness_score = (
                (score * 0.40)
                + (skill_score * 0.30)
                + (quality_score * 0.15)
                + (project_score * 0.10)
                + (keyword_score * 0.05)
        )

        st.metric(
            "Overall Resume Readiness",
            f"{readiness_score:.1f}%"
        )

        if readiness_score >= 80:
            st.success("🟢 Your resume is highly job-ready!")
        elif readiness_score >= 60:
            st.info("🟡 Your resume is fairly job-ready. A few improvements can help.")
        elif readiness_score >= 40:
            st.warning("🟠 Your resume needs some improvement before applying.")
        else:
            st.error("🔴 Your resume needs significant improvement for this job.")

        # Visual Resume Readiness
        st.subheader("📈 Resume Readiness Visualization")

        st.progress(
            int(readiness_score)
        )

        st.write(
            f"Your resume readiness is **{readiness_score:.1f}%**"
        )

        # Download Analysis Report
        st.subheader("📥 Download Analysis Report")

        report = f"""
        AI RESUME ANALYZER REPORT
        =========================

        Resume Match Score: {score:.2f}%
        Skill Match: {skill_match_percentage:.2f}%
        Resume Readiness: {readiness_score:.2f}%

        Required Skills: {total_required_skills}
        Matched Skills: {matched_skill_count}

        MATCHING SKILLS
        ---------------
        {", ".join(matching_skills) if matching_skills else "None"}

        MISSING SKILLS
        --------------
        {", ".join(missing_skills) if missing_skills else "None"}

        RESUME QUALITY
        --------------
        """

        for check, passed in resume_checks.items():
            status = "Found" if passed else "Not Found"
            report += f"{check}: {status}\n"

        report += f"""
        PROJECT EXPERIENCE
        ------------------
        {"Detected" if project_found else "Not Detected"}

        EXPERIENCE / INTERNSHIP
        -----------------------
        {"Detected" if experience_found else "Not Detected"}

        TECHNICAL ACTION WORDS
        ----------------------
        {action_word_count}

        JOB KEYWORDS FOUND
        ------------------
        {", ".join(resume_keyword_matches[:20]) if resume_keyword_matches else "None"}
        """

        st.download_button(
            label="📥 Download Analysis Report",
            data=report,
            file_name="resume_analysis_report.txt",
            mime="text/plain"
        )

        # Resume text
        st.subheader("📄 Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )