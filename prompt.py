from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings,
)