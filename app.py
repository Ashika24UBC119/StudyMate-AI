import hashlib

import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.summarizer import (
    generate_summary,
    generate_smart_notes,
    generate_mcqs,
    generate_keywords,
    generate_flashcards,
)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide",
)


# =========================================================
# CUSTOM UI STYLING
# =========================================================

st.markdown(
    """
    <style>
    /* Global page */
    [data-testid="stAppViewContainer"] {
        background: #F8F8FF;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #F0EEFF;
    }

    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] li {
        color: #29245C !important;
    }

    /* Main headings and text */
    [data-testid="stMain"] h1,
    [data-testid="stMain"] h2,
    [data-testid="stMain"] h3 {
        color: #29245C !important;
    }

    [data-testid="stMain"] p,
    [data-testid="stMain"] label {
        color: #45416B;
    }

    /* Hero banner */
    .hero-banner {
        background: linear-gradient(120deg, #6554C0, #9585E8);
        padding: 35px;
        border-radius: 18px;
        margin-bottom: 28px;
        box-shadow: 0 8px 24px rgba(101, 84, 192, 0.14);
    }

    .hero-banner h1,
    .hero-banner p {
        color: #FFFFFF !important;
    }

    .hero-banner h1 {
        margin: 0 0 10px 0;
    }

    .hero-banner p {
        margin: 5px 0;
    }

    /* Buttons */
    .stButton > button,
    .stDownloadButton > button {
        background: #6554C0;
        color: #FFFFFF !important;
        border: 1px solid #6554C0;
        border-radius: 10px;
        padding: 10px 18px;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        background: #5140A5;
        border-color: #5140A5;
        color: #FFFFFF !important;
    }

    /* PDF uploader */
    [data-testid="stFileUploader"] {
        background: #FFFFFF;
        border: 1px solid #E5E0FF;
        border-radius: 15px;
        padding: 15px;
    }

    [data-testid="stFileUploaderDropzone"] {
        background: #FFFFFF !important;
        border: 1px dashed #9585E8 !important;
        border-radius: 12px !important;
    }

    [data-testid="stFileUploaderDropzone"] * {
        color: #45416B !important;
    }

    [data-testid="stFileUploader"] button {
        background: #6554C0 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px !important;
    }

    /* Radio options */
    [data-testid="stRadio"] label p {
        color: #29245C !important;
    }

    /* Content containers and expanders */
    [data-testid="stExpander"],
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 13px;
    }

    [data-testid="stExpander"] summary {
        color: #29245C !important;
    }

    /* Alerts and progress */
    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    [data-testid="stProgressBar"] > div > div {
        background-color: #7564D8;
    }

    /* Text areas */
    textarea {
        border-radius: 10px !important;
    }
    /* Download button - StudyMate AI */
.stDownloadButton button {
    background: linear-gradient(135deg, #6554C0, #8875DB) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 8px 20px !important;
    transition: 0.3s ease;
}

.stDownloadButton button:hover {
    background: #5140A5 !important;
    color: #FFFFFF !important;
    border: none !important;
}
/* Flashcard Show Answer button */
div[class*="st-key-show_answer_"] button {
    background-color: #E9E3FF !important;
    color: #5140A5 !important;
    border: 1px solid #C7B9F5 !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
}

div[class*="st-key-show_answer_"] button:hover {
    background-color: #DCD1FF !important;
    color: #40318F !important;
}

/* Learning tool selector */
[data-testid="stRadio"] [role="radiogroup"] {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}

[data-testid="stRadio"] [role="radiogroup"] label {
    background: #FFFFFF;
    border: 1px solid #E5E0FF;
    border-radius: 12px;
    padding: 10px 14px;
    transition: all 0.2s ease;
}

[data-testid="stRadio"] [role="radiogroup"] label:has(input:checked) {
    background: #EEE9FF;
    border: 1px solid #7564D8;
    box-shadow: 0 2px 8px rgba(101, 84, 192, 0.12);
}

[data-testid="stRadio"] [role="radiogroup"] label:hover {
    border-color: #9585E8;
}

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.title("📚 StudyMate AI")
    st.markdown("### Your AI Study Assistant")
    st.markdown(
        """
        Upload your study PDF and transform it into:

        📄 **Chapter Summaries**

        📝 **Smart Notes**

        ❓ **Practice Quizzes**

        🔑 **Important Keywords**

        🧠 **Interactive Flashcards**
        """
    )

    st.divider()
    st.markdown("### 💡 How it works")
    st.markdown(
        """
        **1.** Upload a PDF 📤

        **2.** Extract the study material 📖

        **3.** Choose an AI tool 🤖

        **4.** Study smarter! 🚀
        """
    )
    st.divider()
    st.caption("StudyMate AI • AI-powered learning")


# =========================================================
# MAIN TITLE
# =========================================================

st.markdown(
    """
    <div class="hero-banner">
        <h1>📚 StudyMate AI</h1>
        <p style="font-size:18px;">
            Your personal AI-powered study assistant.
        </p>
        <p style="font-size:14px;">
            Turn your study materials into summaries, smart notes,
            quizzes, keywords and flashcards.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# PDF UPLOAD SECTION
# =========================================================

st.subheader("📤 Upload Your Study Material")
st.write(
    "Upload a PDF containing your lecture notes, textbook material, "
    "or study resources."
)

uploaded_file = st.file_uploader(
    "📄 Drop your PDF here or click to browse",
    type=["pdf"],
    help="Only PDF files are supported.",
)


# =========================================================
# PROCESS UPLOADED PDF
# =========================================================

if uploaded_file is not None:
    file_bytes = uploaded_file.getvalue()
    file_hash = hashlib.md5(file_bytes).hexdigest()

    # Clear generated content when a different PDF is uploaded.
    if st.session_state.get("current_file_hash") != file_hash:
        keys_to_clear = [
            "summary",
            "smart_notes",
            "mcq_text",
            "mcq_index",
            "mcq_score",
            "mcq_answered",
            "mcq_selected",
            "keywords",
            "flashcards",
            "flashcard_index",
            "show_answer",
        ]
        for key in keys_to_clear:
            st.session_state.pop(key, None)

        st.session_state.current_file_hash = file_hash

    st.success("✅ PDF uploaded successfully!")

    st.subheader("📂 Uploaded File")
    file_col1, file_col2 = st.columns(2)

    with file_col1:
        st.info(f"📄 **File:** {uploaded_file.name}")

    with file_col2:
        file_size_kb = round(len(file_bytes) / 1024, 2)
        st.info(f"📦 **Size:** {file_size_kb} KB")

    # Extract text from the uploaded PDF.
    text = extract_text_from_pdf(uploaded_file)

    if not text or not text.strip():
        st.error(
            "We couldn't extract readable text from this PDF. "
            "Please try another PDF or check whether this file is scanned."
        )
    else:
        st.success("✅ Your study material is ready!")

        # =====================================================
        # EXTRACTED TEXT PREVIEW
        # =====================================================

        with st.expander("📖 Preview extracted text", expanded=False):
            st.text_area(
                "Extracted Text Preview",
                value=text[:3000],
                height=250,
                disabled=True,
            )

        # =====================================================
        # AI STUDY ASSISTANT
        # =====================================================

        st.markdown("---")
        st.subheader("🤖 AI Study Assistant")
        st.write("Choose what you would like to generate from your PDF.")

        option = st.radio(
            "Select a learning tool:",
            [
                "📄 Chapter Summary",
                "📝 Smart Notes",
                "❓ Practice MCQs",
                "🔑 Important Keywords",
                "🧠 Flashcards",
            ],
            horizontal=True,
            key="study_tool_option",
        )

        # =====================================================
        # CHAPTER SUMMARY
        # =====================================================

        if option == "📄 Chapter Summary":
            if "summary" not in st.session_state:
                with st.spinner("Generating chapter summary..."):
                    st.session_state.summary = generate_summary(text[:12000])

            summary = st.session_state.summary
            st.success("✅ Chapter Summary Generated!")

            with st.container(border=True):
                st.markdown("### 📖 Your Chapter Summary")
                st.markdown(
    f'<div style="color: #29243A; line-height: 1.7;">{summary}</div>',
    unsafe_allow_html=True
)

            st.download_button(
                label="📥 Download Chapter Summary",
                data=summary,
                file_name="chapter_summary.txt",
                mime="text/plain",
                key="download_summary",
            )

        # =====================================================
        # SMART NOTES
        # =====================================================

        elif option == "📝 Smart Notes":
            if "smart_notes" not in st.session_state:
                with st.spinner("Generating smart notes..."):
                    st.session_state.smart_notes = generate_smart_notes(text[:12000])

            notes = st.session_state.smart_notes
            st.success("✅ Smart Notes Generated!")

            with st.container(border=True):
                st.markdown("### 📝 Your Smart Notes")
                st.markdown(
    f'<div style="color: #29243A; line-height: 1.7;">{notes}</div>',
    unsafe_allow_html=True
)

            st.download_button(
                label="📥 Download Smart Notes",
                data=notes,
                file_name="smart_notes.txt",
                mime="text/plain",
                key="download_smart_notes",
            )

        # =====================================================
        # INTERACTIVE MCQ QUIZ
        # =====================================================

        elif option == "❓ Practice MCQs":
            if "mcq_text" not in st.session_state:
                with st.spinner("Generating practice MCQs..."):
                    st.session_state.mcq_text = generate_mcqs(text[:12000])

                st.session_state.mcq_index = 0
                st.session_state.mcq_score = 0
                st.session_state.mcq_answered = False
                st.session_state.mcq_selected = None

            mcq_text = st.session_state.mcq_text or ""
            questions = [
                question.strip()
                for question in mcq_text.split("MCQ ")
                if question.strip()
            ]

            if questions:
                current_index = st.session_state.get("mcq_index", 0)
                current_index = min(current_index, len(questions))
                st.session_state.mcq_index = current_index

                if current_index >= len(questions):
                    st.success("🎉 Quiz Completed!")
                    score = st.session_state.get("mcq_score", 0)
                    total = len(questions)
                    percentage = int((score / total) * 100) if total else 0

                    with st.container(border=True):
                        st.markdown("## 🏆 Your Final Score")
                        st.markdown(f"# {score} / {total}")
                        st.markdown(f"### {percentage}%")

                    if percentage >= 80:
                        st.balloons()
                        st.success("🌟 Excellent work! You really know this topic!")
                    elif percentage >= 50:
                        st.info("👍 Good job! A little more revision will help.")
                    else:
                        st.warning("📚 Keep studying! Try reviewing the notes once more.")

                    if st.button("🔄 Restart Quiz", key="restart_quiz"):
                        st.session_state.mcq_index = 0
                        st.session_state.mcq_score = 0
                        st.session_state.mcq_answered = False
                        st.session_state.mcq_selected = None
                        st.rerun()

                else:
                    current_question = questions[current_index]
                    question_lines = current_question.splitlines()
                    question = ""
                    options = {}
                    correct_answer = ""
                    explanation = ""

                    for line in question_lines:
                        line = line.strip()

                        if line.startswith("Question:"):
                            question = line.replace("Question:", "", 1).strip()
                        elif line.startswith("A:"):
                            options["A"] = line[2:].strip()
                        elif line.startswith("B:"):
                            options["B"] = line[2:].strip()
                        elif line.startswith("C:"):
                            options["C"] = line[2:].strip()
                        elif line.startswith("D:"):
                            options["D"] = line[2:].strip()
                        elif line.startswith("Correct Answer:"):
                            correct_answer = line.replace("Correct Answer:", "", 1).strip()
                        elif line.startswith("Explanation:"):
                            explanation = line.replace("Explanation:", "", 1).strip()

                    st.markdown(
                        f"**Question {current_index + 1} of {len(questions)}**"
                    )
                    st.progress((current_index + 1) / len(questions))

                    with st.container(border=True):
                        st.markdown(f"### {question or 'Please review this question.'}")

                        if options:
                            selected = st.radio(
                                "Choose your answer:",
                                list(options.keys()),
                                format_func=lambda choice: f"{choice}. {options[choice]}",
                                key=f"mcq_option_{current_index}",
                                disabled=st.session_state.get("mcq_answered", False),
                            )
                        else:
                            selected = None
                            st.warning("The generated question did not contain readable answer options.")

                        if not st.session_state.get("mcq_answered", False):
                            if st.button("✅ Submit Answer", key=f"submit_mcq_{current_index}", disabled=selected is None):
                                st.session_state.mcq_selected = selected
                                st.session_state.mcq_answered = True
                                if selected == correct_answer:
                                    st.session_state.mcq_score += 1
                                st.rerun()
                        else:
                            if st.session_state.mcq_selected == correct_answer:
                                st.success("🎉 Correct Answer!")
                            else:
                                st.error(f"❌ Incorrect! The correct answer is {correct_answer}.")

                            if explanation:
                                st.info(f"💡 **Explanation:** {explanation}")

                            if st.button("➡️ Next Question", key=f"next_mcq_{current_index}"):
                                st.session_state.mcq_index += 1
                                st.session_state.mcq_answered = False
                                st.session_state.mcq_selected = None
                                st.rerun()

                    st.caption(f"Current score: {st.session_state.get('mcq_score', 0)}")
            else:
                st.error("❌ Could not generate MCQs. Please try again.")

        # =====================================================
        # IMPORTANT KEYWORDS
        # =====================================================

        elif option == "🔑 Important Keywords":
            if "keywords" not in st.session_state:
                with st.spinner("Extracting important keywords..."):
                    st.session_state.keywords = generate_keywords(text[:12000])

            keywords = st.session_state.keywords
            st.success("✅ Important Keywords Generated!")

            
            with st.container(border=True):
                st.markdown("### 🔑 Important Keywords")
                st.markdown(
                    f'<div style="color: #29243A; line-height: 1.8;">{keywords}</div>',
                    unsafe_allow_html=True
                )


            st.download_button(
                label="📥 Download Keywords",
                data=keywords,
                file_name="important_keywords.txt",
                mime="text/plain",
                key="download_keywords",
            )

        # =====================================================
        # INTERACTIVE FLASHCARDS
        # =====================================================

        elif option == "🧠 Flashcards":
            if "flashcards" not in st.session_state:
                with st.spinner("Creating flashcards..."):
                    st.session_state.flashcards = generate_flashcards(text[:12000])

                st.session_state.flashcard_index = 0
                st.session_state.show_answer = False

            flashcard_text = st.session_state.flashcards or ""
            cards = [
                card.strip()
                for card in flashcard_text.split("FLASHCARD ")
                if card.strip()
            ]

            if cards:
                current_index = st.session_state.get("flashcard_index", 0)
                current_index = min(current_index, len(cards) - 1)
                st.session_state.flashcard_index = current_index
                current_card = cards[current_index]

                question = ""
                answer = ""

                if "Question:" in current_card:
                    question_part = current_card.split("Question:", 1)[1]
                    if "Answer:" in question_part:
                        question, answer = question_part.split("Answer:", 1)
                        question = question.strip()
                        answer = answer.strip()
                    else:
                        question = question_part.strip()
                else:
                    question = current_card.strip()

                
                st.markdown(
                    f"**Flashcard {current_index + 1} of {len(cards)}**"
                )
                st.progress((current_index + 1) / len(cards))

                with st.container(border=True):
                    st.markdown("### ❓ Question")
                    st.markdown(f"{question}")

                    if not st.session_state.get("show_answer", False):
                        if st.button("👀 Show Answer", key=f"show_answer_{current_index}"):
                            st.session_state.show_answer = True
                            st.rerun()
                    else:
                        st.markdown("### 💡 Answer")
                        st.markdown(
                            answer if answer else "No answer was generated for this card."
                        )

                previous_col, next_col = st.columns(2)

                with previous_col:
                    if st.button(
                        "⬅️ Previous",
                        key=f"previous_card_{current_index}",
                        disabled=current_index == 0,
                    ):
                        st.session_state.flashcard_index -= 1
                        st.session_state.show_answer = False
                        st.rerun()

                with next_col:
                    if st.button(
                        "➡️ Next",
                        key=f"next_card_{current_index}",
                        disabled=current_index >= len(cards) - 1,
                    ):
                        st.session_state.flashcard_index += 1
                        st.session_state.show_answer = False
                        st.rerun()
            else:
                st.error("❌ Could not generate flashcards. Please try again.")

else:
    st.markdown(
        """
        <div style="background:#FFFFFF; border:1px solid #E5E0FF;
                    border-radius:14px; padding:22px; margin-top:18px;">
            <h3 style="color:#29245C; margin-top:0;">✨ Ready to study smarter?</h3>
            <p style="color:#45416B; margin-bottom:0;">
                Upload a PDF above to create summaries, smart notes,
                practice quizzes, keywords and flashcards.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
