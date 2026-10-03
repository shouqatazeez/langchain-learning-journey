from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
     repo_id="Qwen/Qwen2.5-3B-Instruct",
     task="text-generation",
     provider="featherless-ai"
)

model = ChatHuggingFace(llm=llm)

messages = [
   SystemMessage(content="You are a helpful assistant"),
   HumanMessage(content="Tell me about the Langchain")
   
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)