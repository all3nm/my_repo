from google.adk.agents import LlmAgent

llm_agent = LlmAgent(name="decision", model="gemini-2.0-flash")


def process_decision(ctx):
    raw = llm_agent.run(ctx).text
    db.save_decision(raw)
    return raw
