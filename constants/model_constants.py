from langchain_openai.chat_models import ChatOpenAI

import settings

CHAT_MODEL = ChatOpenAI(
    openai_api_key=settings.OPENAI_KEY,
    model_name="gpt-4o",
    temperature=0.0
)
