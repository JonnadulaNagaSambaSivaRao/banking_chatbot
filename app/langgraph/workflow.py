from langgraph.graph import StateGraph


from typing import TypedDict


class ChatState(TypedDict):

    question:str

    answer:str



def chatbot(state):

    from app.langchain.llm import llm

    response=llm.invoke(
        state["question"]
    )

    return {
        "answer":response.content
    }



graph=StateGraph(ChatState)


graph.add_node(
    "chatbot",
    chatbot
)


graph.set_entry_point(
    "chatbot"
)


graph.set_finish_point(
    "chatbot"
)


workflow=graph.compile()