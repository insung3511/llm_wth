from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

# Initialize the Ollama model
llm = ChatOllama(model="qwen3:8b")

question = "Testing... Testing... 잘 들리나요?"

# Invoke the model
response = llm.invoke([
    HumanMessage(
        content="Testing... Testing... 잘 들리나요?"
    )
])

# Print think. Think starting with <think> and ending with </think>
# response is string, so we should find the substring between <think> and </think>
start = response.content.find("<think>") + len("<think>")
end = response.content.find("</think>")
think = response.content[start:end].strip()
print("Think:", think)

# Print the full response
result = response.content[end + len("</think>"):].strip()
print("Result:", result)