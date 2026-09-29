from google.adk.agents import LlmAgent


def run_coordination(ctx):
    llm_agent = LlmAgent(name="coordinator", model="gemini-2.0-flash")
    result = llm_agent.run(ctx)
    print(f"LLM response: {result}")
    print("Coordination complete")
    return result
