from langchain_community.tools import Tool
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.vectorstores import DistanceStrategy

from constants.model_constants import CHAT_MODEL
from methods.database_methods import get_db_connection
from methods.embedding_methods import OPENAI_EMBEDDINGS


def search_question_in_vector_store(question: str) -> str:
    db = get_db_connection(
        OPENAI_EMBEDDINGS,
        distance_strategy=DistanceStrategy.COSINE,
        collection_name="fighters",
    )

    chain = RetrievalQA.from_chain_type(
        retriever=db.as_retriever(),
        llm=CHAT_MODEL,
        chain_type="map_rerank",
    )
    result = chain.invoke(question)
    return result


search_question_in_vector_store_tool = Tool(
    name="knowledge_base_search",
    func=search_question_in_vector_store,
    description="Search the knowledge base for a question",
)


def get_user_context(*args, **kwargs) -> dict:
    return {"name": "Juan Trujillo", "age": 25, "job": "Software Engineer"}


get_user_context_tool = Tool(
    name="get_user_context",
    func=get_user_context,
    description="Get the user context",
)
