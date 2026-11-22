import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Get the API key
api_key = os.getenv("GEMINI_API_KEY")

# Check whether the API key was loaded
if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in the .env file.")

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_summary(text):
    """
    Generate a concise study summary using Gemini.
    """

    prompt = f"""
You are an expert AI study assistant.

Summarize the following study material into clear and concise study notes.

Requirements:
- Use simple English.
- Keep the important concepts.
- Organize the information using headings and bullet points.
- Do not remove important definitions or key facts.

Study Material:
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


def generate_smart_notes(text):
    """
    Generate structured study notes using Gemini.
    """

    prompt = f"""
You are an expert AI study assistant.

Convert the following study material into well-organized smart study notes.

Requirements:
- Use clear headings and subheadings.
- Explain important concepts in simple English.
- Use bullet points wherever appropriate.
- Include important definitions.
- Include key concepts and facts.
- Include examples when they are present in the material.
- Avoid unnecessary repetition.
- Do not add information that is not supported by the study material.
- Make the notes useful for a college student preparing for an exam.

Study Material:
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


def generate_mcqs(text):
    """
    Generate 5 structured multiple-choice questions using Gemini.
    """

    prompt = f"""
You are an expert AI study assistant.

Create exactly 5 multiple-choice questions from the study material below.

Requirements:
- Questions must be based ONLY on the provided material.
- Each question must have exactly 4 options.
- There must be exactly one correct answer.
- Include a short explanation for the correct answer.
- Questions should test important concepts and facts.
- Avoid duplicate questions.
- Keep the language simple and suitable for a college student.

IMPORTANT:
Return ONLY the questions.
Do not add any introduction or conclusion.

Use EXACTLY this format:

MCQ 1
Question: ...
A: ...
B: ...
C: ...
D: ...
Correct Answer: A
Explanation: ...

MCQ 2
Question: ...
A: ...
B: ...
C: ...
D: ...
Correct Answer: B
Explanation: ...

Continue until MCQ 5.

Study Material:
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text
def generate_keywords(text):
    """
    Extract important keywords and concepts using Gemini.
    """

    prompt = f"""
You are an expert AI study assistant.

Identify the most important keywords and concepts from the following study material.

Requirements:
- Extract 10 to 15 important keywords or concepts.
- Give a short and simple explanation for each keyword.
- Focus on concepts that are useful for exam preparation.
- Do not include unnecessary or very common words.
- Use only information from the provided study material.
- Do not invent information.

Use this format:

# 🔑 Important Keywords

### 1. Keyword
Short explanation.

### 2. Keyword
Short explanation.

Continue for all important keywords.

Study Material:
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text
def generate_flashcards(text):
    """
    Generate 10 structured study flashcards using Gemini.
    """

    prompt = f"""
You are an expert AI study assistant.

Create exactly 10 study flashcards from the following study material.

Requirements:
- Each flashcard must have one question and one answer.
- Focus on important concepts, definitions, and facts.
- Keep questions clear and suitable for a college student.
- Keep answers concise but informative.
- Use only information from the study material.
- Do not invent information.
- Avoid duplicate questions.

IMPORTANT:
Return ONLY the flashcards.
Do not add an introduction or conclusion.

Use EXACTLY this format:

FLASHCARD 1
Question: ...
Answer: ...

FLASHCARD 2
Question: ...
Answer: ...

FLASHCARD 3
Question: ...
Answer: ...

Continue until FLASHCARD 10.

Study Material:
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text