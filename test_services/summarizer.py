import vertexai.generative_models as genai

model = genai.GenerativeModel("gemini-2.0-flash")


def summarize(text: str) -> str:
    return model.generate_content(text).text
