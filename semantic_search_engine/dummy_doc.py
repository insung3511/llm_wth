from langchain_core.documents import Document
from langchain_community.chat_models import ChatOllama

# Documents to be used in the semantic search engine. 
# In practice, these would be loaded from a database or file system. Here we define some dummy documents. 
# These documents are just examples and can be replaced with any text data.
document = [
    Document(
        page_content="To make a sweet pancake, you need flour, eggs, milk, sugar, and a pinch of salt. Mix the ingredients together and cook on a hot griddle until golden brown on both sides.", 
        metadata={"source": "cooking_recipes.txt"}
    ),
    Document(
        page_content="The capital of France is Paris. It is known for its art, fashion, gastronomy, and culture.", 
        metadata={"source": "geography_facts.txt"}
    ),
]

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

question = "How to make a sweet pancake?"
answer = answer_question(question)
print("Answer:", answer)