from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    set_tracing_disabled,
    enable_verbose_stdout_logging,
)
import asyncio

set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()

BASE_URL = "http://blackwell.lan:8000/v1"
API_KEY = "dummy"
MODEL_NAME = "Qwen/QwQ-32B-AWQ"

client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)


# Senior Software Engineer Agent
senior_software_engineer = Agent(
    name="Senior Software Engineer",
    handoff_description="Implements features and components based on architecture and requirements",
    instructions="""
    Your job is to implement the system according to the architecture and requirements.
    
    Step-by-step instructions:
    1. Review the architecture and requirements.
    2. For each component, implement the code needed to fulfill its responsibilities.
    3. Write clear inline documentation and comments.
    4. Note any assumptions or deviations from the architecture.
    5. Output your work as:
       - Source code (with comments)
       - Implementation Notes (assumptions, deviations, rationale)
    6. When done, hand off your output to the Code Reviewer.
    """,
    handoffs=[],
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
)

# System Architect Agent
system_architect = Agent(
    name="System Architect",
    handoff_description="Designs the overall system architecture based on requirements",
    instructions="""
    Your job is to design a technical architecture that fulfills the documented requirements.
    
    Step-by-step instructions:
    1. Read all requirements and identify key system components and their responsibilities.
    2. Draw or describe the main system architecture (components, data flow, integrations).
    3. Select a technology stack and briefly justify each choice.
    4. Specify main APIs or interfaces, listing their endpoints and main data structures.
    5. Document any architectural decisions or trade-offs made.
    6. Output your work in a structured format:
       - Architecture Overview (diagram or description)
       - Technology Stack
       - API/Interface Summary
       - Key Decisions
    7. When complete, hand off your output to the Senior Software Engineer.
    """,
    handoffs=[senior_software_engineer],
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
)

# Requirements Engineer Agent
requirements_engineer = Agent(
    name="Requirements Engineer",
    handoff_description="Analyzes and documents software requirements",
    instructions="""
    Your job is to translate stakeholder needs into clear, actionable software requirements.
    
    Step-by-step instructions:
    1. List all functional requirements as concise user stories or bullet points.
    2. For each, specify clear acceptance criteria.
    3. Assign a priority (High, Medium, Low) to each requirement.
    4. If any requirement is unclear, come up with sensible assumptions.
    5. Output requirements in this format:
       - ID: REQ-001
       - Description: ...
       - Acceptance Criteria: ...
       - Priority: ...
    6. When all requirements are documented, hand off your output to the System Architect.
    """,
    handoffs=[system_architect],
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
)


async def main():
    # Multi-line input for requirements
    print(
        "Enter the main software requirement (multi-line supported)."
        "\nPress ENTER on an empty line to finish:"
    )
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    requirement = "\n".join(lines)

    try:
        result = await Runner.run(requirements_engineer, requirement)
        print(result.final_output)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
