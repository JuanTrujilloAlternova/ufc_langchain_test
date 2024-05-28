from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_postgres import PostgresChatMessageHistory

from constants.model_constants import CHAT_MODEL
from constants.prompts_constants import custom_system_prompt
from methods.agent_methods import initialize_openai_agent
from methods.memory_methods import get_conversation_summary_memory, SYNC_CONNECTION
from methods.tools_methods import get_user_context_tool, search_question_in_vector_store_tool

chat_prompt = ChatPromptTemplate(
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

tools = [search_question_in_vector_store_tool, get_user_context_tool]

table_name = "chat_history"
PostgresChatMessageHistory.create_tables(SYNC_CONNECTION, table_name)

chat_id = "35d0bb55-6cf7-46e0-9184-c85edb7c3202"
agent_executor = initialize_openai_agent(
    llm=CHAT_MODEL,
    prompt=chat_prompt,
    tools=tools,
    memory=get_conversation_summary_memory(session_id=chat_id)
)

while True:
    message = input("Ask me a question: ")
    print(
        agent_executor.invoke(
            {
                "content": message,
            },
        )["output"]
    )
