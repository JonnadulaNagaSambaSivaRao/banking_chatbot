from langchain_core.prompts import ChatPromptTemplate


prompt=ChatPromptTemplate.from_template(
"""
You are a banking assistant.

Answer user questions clearly.

User Question:
{question}

Answer:
"""
)