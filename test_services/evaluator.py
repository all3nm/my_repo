import vertexai.generative_models as genai

model = genai.GenerativeModel("gemini-2.5-pro")


def build_prompt(ctx: dict) -> str:
    return f"Evaluate the following: {ctx.get('input', '')}"


def run_evaluation(ctx: dict) -> str:
    response = model.generate_content(build_prompt(ctx))
    return response.text
