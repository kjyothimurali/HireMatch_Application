
# 🚀 HireMatch – Intelligent Resume & Job Description Evaluation System

## 📌 Introduction

HireMatch is an AI-based recruitment assistance platform designed to help candidates and recruiters evaluate job descriptions and resumes efficiently. By combining Machine Learning, Natural Language Processing (NLP), and modern AI models, the platform predicts suitable job sectors and roles while analyzing resumes for skill alignment.

Using **BERT**, **TF-IDF**, **Cosine Similarity**, and **Streamlit**, HireMatch delivers an interactive solution for career guidance and recruitment support.

---

## ✨ Key Features

### 📄 Job Description Evaluation

Users can upload a Job Description PDF or enter the content manually.

The platform automatically:

* Classifies the job into the most relevant industry sector
* Predicts the best-matching job role
* Displays prediction confidence levels
* Provides role-matching insights and recommendations

### 📑 Resume Assessment

Upload a resume and choose a desired sector and role.

The system will:

* Extract resume content automatically
* Identify skills present in the resume
* Detect missing industry-relevant skills
* Compute a Resume Match Percentage
* Suggest personalized improvements

### 📊 Analytics Dashboard

A dedicated dashboard provides:

* Total number of analyses performed
* Average resume match percentage
* Sector-wise distribution statistics
* Historical analysis records
* Performance visualization and insights

---

## 🧠 AI & Machine Learning Workflow

### Stage 1: Sector Identification

A fine-tuned BERT model categorizes job descriptions into sectors such as:

* Information Technology
* Finance
* Healthcare
* Sales & Marketing

### Stage 2: Role Recommendation

After determining the sector:

1. Sector-specific records are filtered
2. TF-IDF features are generated
3. Cosine Similarity scores are calculated
4. The most relevant role is predicted

### Resume Skill Evaluation

Resume content is compared with predefined skill sets to:

* Detect matching skills
* Highlight missing competencies
* Generate a skill match score
* Provide enhancement suggestions

---

## 🏗️ System Architecture

```text
HireMatch_Streamlit
│
├── app.py
│
├── pages/
│   ├── 1_Job_Analysis.py
│   ├── 2_Resume_Analysis.py
│   └── 3_Dashboard.py
│
├── utils/
│   ├── predictor.py
│   ├── role_predictor.py
│   ├── pdf_reader.py
│   ├── skill_matcher.py
│   └── history.py
│
├── data/
│   ├── final_dataset.csv
│   └── analysis_history.csv
│
├── models/
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   └── tokenizer_config.json
│
├── requirements.txt
│
└── .streamlit/
    └── config.toml
```

---

## ⚙️ Technology Stack

### User Interface

* Streamlit
* Custom Styling (CSS)
* Interactive Dashboard Components

### Artificial Intelligence & ML

* BERT Transformer Model
* PyTorch
* TF-IDF Vectorization
* Cosine Similarity

### Data Processing Tools

* Pandas
* NumPy
* PDFPlumber

### Deployment & Version Control

* GitHub
* Streamlit Community Cloud

---

## 📂 Dataset Information

The platform utilizes a structured dataset containing job-related information.

| Column Name    | Description                   |
| -------------- | ----------------------------- |
| Title          | Job Role Name                 |
| JobDescription | Original Job Description      |
| text           | Processed Text Representation |
| sector         | Industry Sector Label         |

### Dataset Usage

The dataset supports:

* Job Role Prediction
* Similarity-Based Matching
* Sector Filtering
* Training and Evaluation

---

## 🚀 Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/kjyothimurali/HireMatch_Application.git
cd HireMatch_Application
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Launching the Application

Run the following command:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📖 Application Usage

### Job Description Analysis

1. Navigate to the Job Analysis page.
2. Upload a PDF or paste a Job Description.
3. Click **Analyze**.
4. Review:

   * Predicted Sector
   * Confidence Score
   * Recommended Role
   * Similarity Percentage

### Resume Analysis

1. Open the Resume Analysis page.
2. Upload your resume.
3. Select the target sector.
4. Select the target role.
5. Click **Analyze Resume**.
6. Review:

   * Resume Match Percentage
   * Matching Skills
   * Missing Skills
   * Improvement Suggestions

### Dashboard Analytics

1. Open the Dashboard page.
2. Explore:

   * Analysis History
   * Sector Statistics
   * Match Score Trends
   * Performance Metrics

---

## 🎯 Planned Enhancements

Future versions may include:

* Multi-label Sector Classification
* ATS Compatibility Analysis
* Resume Ranking System
* AI-Based Interview Question Generator
* Personalized Career Recommendations
* Learning Roadmaps for Missing Skills
* Cloud Database Integration
* Secure User Authentication

---

## 👨‍💻 Project Team

### Jyothi Murali

* Development of Machine Learning Modules
* BERT-Based Sector Classification
* Streamlit Application Design
* Resume Evaluation Features

### Jayanth Jakkula

* Data Collection and Preparation
* Model Training and Testing
* Role Prediction Development
* Validation and Performance Analysis

---

**Institution:** CVR College of Engineering

**Program:** Bachelor of Technology (Computer Science & Engineering)

**Project Title:** HireMatch – Intelligent Resume & Job Description Evaluation System

---

## 📜 License

This project has been developed for academic learning and research purposes.

Users are welcome to explore, modify, and extend the project for educational use while providing appropriate attribution.
