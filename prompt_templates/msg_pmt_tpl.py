from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

# Initialize the Ollama model
llm = ChatOllama(model="qwen3:8b")

# Define the prompt template with a MessagesPlaceholder
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a philosopher who has enlightened the philosophy of the whole world. What is the meaning of {question}"),
    MessagesPlaceholder(variable_name="msgs")
])

# Define the messages to pass
message_to_pass = [
    HumanMessage(content="What is the meaning of life?"),
    AIMessage(content="The meaning of life is a profound philosophical question that has been debated for centuries. It often revolves around the pursuit of happiness, fulfillment, and understanding one's purpose in the universe."),
    HumanMessage(content="Then why we are here?")
]

# Format the prompt with the question and messages
formatted_prompt = prompt_template.format(question="life", msgs=message_to_pass)

# Pass the formatted prompt to the LLM
response = llm.invoke([formatted_prompt])

# Print the response
print("Response:", response.content)