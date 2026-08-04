from autogen_agentchat.agents import AssistantAgent
from autogen_code_review.config import llm_client
from autogen_code_review.prompts import CODING_AGENT_PROMPT, REVIEWER_AGENT_PROMPT


coding_agent = AssistantAgent(
    name="coding_agent",
    model_client=llm_client,
    system_message=CODING_AGENT_PROMPT
)

reviewer_agent = AssistantAgent(
    name="reviewer_agent",
    model_client=llm_client,
    system_message=REVIEWER_AGENT_PROMPT,
)
