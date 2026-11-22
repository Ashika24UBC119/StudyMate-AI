# StudyMate AI 📚

**An AI-powered study assistant that transforms PDF study materials into structured, easy-to-understand learning resources.**

StudyMate AI helps students study smarter by using Generative AI to extract useful information from uploaded PDF documents and generate personalized learning materials.

## ✨ Features

- **Chapter Summary:** Generate concise summaries from study materials.
- **Smart Notes:** Convert lengthy content into structured notes.
- **Practice MCQs:** Generate multiple-choice questions for self-assessment.
- **Important Keywords:** Extract important terms and concepts.
- **Flashcards:** Create question-and-answer cards for active recall.

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- PyMuPDF
- python-dotenv

## 📂 Project Structure

```text
AI-Study-Notes-Generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── utils/
    ├── pdf_reader.py
    └── summarizer.py
```

## 🚀 Run Locally

1. Clone this repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd AI-Study-Notes-Generator
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

5. Run the application:

```bash
streamlit run app.py
```

## 🔐 Security

API credentials are stored in environment variables and must never be committed to the public repository.

## 🎯 Project Goal

To make learning more interactive and efficient by transforming static study materials into AI-generated summaries, notes, quizzes, keywords, and flashcards.

---

**Built with Python, Streamlit, and Generative AI.**