
import gradio as gr
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

loader = DirectoryLoader("docs", glob="**/*.md")
docs = loader.load()

embedding = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embedding)
qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(), retriever=db.as_retriever())

def responder(pregunta):
    return qa.run(pregunta)

gr.ChatInterface(responder, title="Asistente IAG - Wiki Verticall").launch()
