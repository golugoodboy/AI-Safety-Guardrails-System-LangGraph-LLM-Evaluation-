from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from main import run_pipeline

class State(TypedDict):
    question: str
    result: dict
    retry_count: int

def process_query(state: State):
    result = run_pipeline(state["question"])
    return {"result": result, "retry_count": state.get("retry_count", 0)}

def decide(state: State):
    status = state["result"]["status"]
    
    if "Unsafe" in status:
        if state.get("retry_count", 0) >= 3:
            return "end" 
        else:
            return "retry"
    else:
        return "end"

def retry(state: State):
    new_query = state["question"] + " Please answer in a safe and appropriate manner."
    current_retries = state.get("retry_count", 0)
    
    return {"question": new_query, "retry_count": current_retries + 1}

builder = StateGraph(State)

builder.add_node("process_query", process_query)
builder.add_node("retry", retry)

builder.add_edge(START, "process_query")

builder.add_conditional_edges(
    "process_query", 
    decide, 
    {"retry": "retry", "end": END}
)

builder.add_edge("retry", "process_query")

workflow = builder.compile()

if __name__ == "__main__":
    result = workflow.invoke({
        "question": "What is the capital of Germany?"
    })

    print(result)
