import os
from .fallback import fallback_translate

def translate_error(text, lang="auto"):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return fallback_translate(text, lang)

    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
You are an error translator.
Translate the following Python error message into {lang}.
Do NOT include English.
Keep it short and clear.

Error:
{text}
"""
        res = model.generate_content(prompt)
        return res.text.strip()

    except Exception:
        return fallback_translate(text, lang)
