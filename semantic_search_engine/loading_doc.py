from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from langchain_community.chat_models import ChatOllama

FILE_PATH = "Rheology-of-Cats.pdf"
LOADER = PyPDFLoader(FILE_PATH)

document = LOADER.load()
print(len(document), "documents loaded.")
print("document content preview:", document[0].page_content[:500])  # Print
print("document metadata:", document[0].metadata)

# Initialize the Ollama model
llm = ChatOllama(model="qwen3:8b")

# Example function to demonstrate how the LLM can be used with the documents
def answer_question(question: str) -> str:
    # Here you would implement the logic to find the most relevant document(s) based on the question.
    # For simplicity, we will just concatenate all document contents.
    context = " ".join([doc.page_content for doc in document])
    
    # Create a prompt that includes the context and the question
    prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    
    # Invoke the model with the prompt
    response = llm.invoke([
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ])
    
    return response.content

question = "Read the context and explain why cats are so cute?"
answer = answer_question(question)
print("Answer:", answer)