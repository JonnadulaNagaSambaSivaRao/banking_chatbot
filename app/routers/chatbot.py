from fastapi import APIRouter

from app.langgraph.workflow import workflow


router=APIRouter()


@router.post("/chat")

def chat(message:str):

    result=workflow.invoke(
        {
            "question":message
        }
    )

    return {
        "response":
        result["answer"]
    }