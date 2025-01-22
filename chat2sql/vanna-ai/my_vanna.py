from vanna.ollama import Ollama
from vanna.chromadb import ChromaDB_VectorStore


class MyVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)


vn = MyVanna(config={"model": "llama3"})  # mixtral:8x7b,llama3,qwq:latest

# vn.connect_to_postgres(host='localhost', port=5432, user='hollysys', password='hollysys', database='hollysys')
vn.connect_to_postgres(
    host="127.0.0.1",
    dbname="hollysys",
    user="hollysys",
    password="hollysys",
    port="5432",
)
