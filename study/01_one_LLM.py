from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

response = llm.invoke("What is the capital of France?")
print(response.content)
