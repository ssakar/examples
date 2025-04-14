from agents import (
    Agent,
    InputGuardrail,
    GuardrailFunctionOutput,
    Runner,
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    InputGuardrailTripwireTriggered,
    set_tracing_disabled,
    enable_verbose_stdout_logging,
)

from pydantic import BaseModel
import asyncio

set_tracing_disabled(disabled=True)
enable_verbose_stdout_logging()

BASE_URL = "http://blackwell.lan:8000/v1"
API_KEY = "dummy"
MODEL_NAME = "Qwen/QwQ-32B-AWQ"

client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)



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
    handoffs=["system_architect"],
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
    handoffs=["senior_software_engineer"],
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
)

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
    handoffs=["code_reviewer"],
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
)

# Code Reviewer Agent
code_reviewer = Agent(
    name="Code Reviewer",
    handoff_description="Reviews code and design for quality and correctness; on rejection, returns feedback to the Senior Software Engineer.",
    instructions="""
    Your job is to review the code and documentation for correctness and quality.
    
    Step-by-step instructions:
    1. Compare the implementation to the requirements and architecture.
    2. Identify any bugs, code smells, or missing documentation.
    3. Write a clear review report listing issues and suggestions.
    4. Approve or reject the implementation for QA.
       - If approved: hand off to the QA Engineer.
       - If rejected: hand off feedback and required changes to the Senior Software Engineer for revision.
    5. Output:
       - Review Summary (approved/rejected)
       - List of Issues (with severity and suggestions)
    6. When complete, hand off your output to the appropriate agent.
    """,
    handoffs=["qa_engineer", "senior_software_engineer"],
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
)

# QA Engineer Agent
qa_engineer = Agent(
    name="QA Engineer",
    handoff_description="Performs quality assurance and testing",
    instructions="""
    Your job is to test the software for correctness and quality.
    
    Step-by-step instructions:
    1. Read the requirements and review report.
    2. Write test cases covering all acceptance criteria and main features.
    3. Execute the tests (manual or automated).
    4. Log any defects with steps to reproduce and severity.
    5. Output:
       - Test Plan (test cases)
       - Test Results (pass/fail, defects found)
       - Defect Reports (if any)
    6. Provide results and defects back to the team for fixes or closure.
    """,
    handoffs=[],
    model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
)

# Map agent names to agent objects for handoff resolution
agent_registry = {
    "requirements_engineer": requirements_engineer,
    "system_architect": system_architect,
    "senior_software_engineer": senior_software_engineer,
    "code_reviewer": code_reviewer,
    "qa_engineer": qa_engineer,
}

# Resolve string handoffs to agent objects
for agent in agent_registry.values():
    resolved_handoffs = []
    for handoff in agent.handoffs:
        if isinstance(handoff, str):
            resolved_handoffs.append(agent_registry[handoff])
        else:
            resolved_handoffs.append(handoff)
    agent.handoffs = resolved_handoffs

# Print out the handoff structure for all agents
print("Agent Handoff Structure:")
for name, agent in agent_registry.items():
    handoff_names = [h.name for h in agent.handoffs]
    print(f"- {agent.name} hands off to: {', '.join(handoff_names) if handoff_names else 'None'}")


def main():
    # Multi-line input for requirements
    print("Enter the main software requirement (multi-line supported). Press ENTER on an empty line to finish:")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    requirement = "\n".join(lines)
    
    try:
        result = Runner.run_sync(requirements_engineer, requirement)
        print(result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print("Requirement validation failed:", e)


if __name__ == "__main__":
    main()
