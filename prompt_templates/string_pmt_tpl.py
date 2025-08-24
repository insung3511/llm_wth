from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

# Initialize the Ollama model
llm = ChatOllama(model="qwen3:8b")

prompt_template = PromptTemplate.from_template(
    "You are a philosopher who has enlightened the philosophy of the whole world. What is the meaning of {topic}?"
)

# Use the prompt template to create a HumanMessage
message = HumanMessage(content=prompt_template.format(question="life"))

# Pass the message to the LLM
response = llm.invoke([message])
print("Response:", response.content)
