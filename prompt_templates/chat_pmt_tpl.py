from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

# Initialize the Ollama model
llm = ChatOllama(model="qwen3:8b")
prompt_template = ChatPromptTemplate([
    ("system", "You are a philosopher who has enlightened the philosophy of the whole world."),
    ("user", "What is the meaning of {topic}")    
])

message = prompt_template.format_messages(topic="life")

# Pass the message to the LLM
response = llm.invoke(message)
print("Response:", response.content)