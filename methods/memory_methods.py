import psycopg
from langchain.memory import ConversationBufferWindowMemory
from langchain_postgres import PostgresChatMessageHistory

import settings
from constants.model_constants import CHAT_MODEL


CONNECTION_INFO = "postgresql://{}:{}@{}:{}/{}".format(
    settings.DATABASE_USER,
    settings.DATABASE_PASSWD,
    settings.DATABASE_HOST,
    settings.DATABASE_PORT,
    settings.DATABASE_NAME
)

SYNC_CONNECTION = psycopg.connect(CONNECTION_INFO)

def get_or_create_postgres_chat_message_history(session_id):
    return PostgresChatMessageHistory(
        "chat_history",
        str(session_id),
        sync_connection=SYNC_CONNECTION,
    )


def get_conversation_summary_memory(session_id):
    return ConversationBufferWindowMemory(
        session_id=session_id,
        llm=CHAT_MODEL,
        memory_key="messages",
        return_messages=True,
        chat_memory=get_or_create_postgres_chat_message_history(session_id),
    )
