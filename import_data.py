from methods.data_loading_methods import load_documents_to_db, load_txt_file
from methods.database_methods import get_db_connection
from methods.embedding_methods import OPENAI_EMBEDDINGS


db = get_db_connection(OPENAI_EMBEDDINGS)

# Load Fighter stats
documents = load_txt_file("data/fighters_cleaned.txt")
print(documents)

load_documents_to_db("fighters", db.embeddings, documents)
print("Fighter stats loaded")
