from langchain_core.messages import SystemMessage
from langchain_core.prompts import (
    ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
)

from constants.prompts_constants import custom_system_prompt


def create_chat_prompt_template():
    return ChatPromptTemplate(
        messages=[
            SystemMessage(content=custom_system_prompt),
            MessagesPlaceholder(variable_name="messages"),
            HumanMessagePromptTemplate.from_template(
                "{content}"
            ),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ],
        input_variables=["content", "messages", "agent_scratchpad", "user_context"],
    )
