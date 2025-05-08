# uv init . 
# uv add 
# create .env file 
# add ANTHROPIC_API_KEY=""


from dotenv import load_dotenv
from typing import Annotated, Literal 
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages 
from langchain.chat_models import init_chat_model 
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

load_dotenv()

llm = init_chat_model("anthropic:claude-3-5-sonnet-latest")

# Pydantic
class MessageClassifier(BaseModel): 
    message_type: Literal["emotional", "logical"] = Field(
        ..., 
        description="Classify if the message requires an emotional (therapist) or logical response."
    )


# Class to store messages
class State(TypedDict):
    messages: Annotated[list, add_messages]
    message_type: str | None

def classify_message(state: State):
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)

    result = classifier_llm.invoke([
         {
            "role": "system",
            "content": """Classify the user message as either:
            - 'emotional': if it asks for emotional support, therapy, deals with feelings, or personal problems
            - 'logical': if it asks for facts, information, logical analysis, or practical solutions
            """
        },
        {"role": "user", "content": last_message.content}
    ])
    return {"message_type": result.message_type}


def router(state: State):
    message_type = state.get("message_type", "logical")
    if message_type == "emotional":
        return {"next": "therapist"}

    return {"next": "logical"}

def therapist_agent(state: State):
    last_message = state["messages"][-1]

    messages = [
        {"role": "system",
         "content": """You are a compassionate therapist. Focus on the emotional aspects of the user's message.
                        Show empathy, validate their feelings, and help them process their emotions.
                        Ask thoughtful questions to help them explore their feelings more deeply.
                        Avoid giving logical solutions unless explicitly asked."""
         },
        {
            "role": "user",
            "content": last_message.content
        }
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}

def logical_agent(state: State):
    last_message = state["messages"][-1]

    messages = [
        {"role": "system",
         "content": """You are a purely logical assistant. Focus only on facts and information.
            Provide clear, concise answers based on logic and evidence.
            Do not address emotions or provide emotional support.
            Be direct and straightforward in your responses."""
         },
        {
            "role": "user",
            "content": last_message.content
        }
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}




#define a graph builder 
graph_builder = StateGraph(State) 

graph_builder.add_node("classifier", classify_message)
graph_builder.add_node("router", router)
graph_builder.add_node("therapist", therapist_agent)
graph_builder.add_node("logical", logical_agent)

graph_builder.add_edge(START, "classifier")
graph_builder.add_edge("classifier", "router")

graph_builder.add_conditional_edges(
    "router",
    lambda state: state.get("next"),
    {"therapist": "therapist", "logical": "logical"}
)

graph_builder.add_edge("therapist", END)
graph_builder.add_edge("logical", END)

graph = graph_builder.compile() 




def run_chatbot():
    state = {"messages": [], "message_type": None}

    while True:
        user_input = input("Message: ")
        if user_input == "exit":
            print("Bye")
            break

        state["messages"] = state.get("messages", []) + [
            {"role": "user", "content": user_input}
        ]

        state = graph.invoke(state)

        if state.get("messages") and len(state["messages"]) > 0:
            last_message = state["messages"][-1]
            print(f"Assistant: {last_message.content}")


if __name__ == "__main__":
    run_chatbot()

# Message: Hey, I'm really sad right now
# Assistant: I hear that you're feeling really sad, and I want you to know that I'm here to listen. It can be really hard to sit with these heavy feelings. Would you like to share more about what's bringing up this sadness for you? Sometimes putting our feelings into words can help us understand them better, but it's also okay if you're not ready to dive deeper yet. I'm here to support you either way.
# Message: I need some hard solid advice about buying a house
# 
# Key Financial Factors:
# 1. Purchase price should not exceed 3-4x your annual income
# 2. Down payment of 20% ideal to avoid PMI
# 3. Monthly payment (including taxes/insurance) should not exceed 28% of gross monthly income

# Critical Steps:
# 1. Check credit score - aim for 740+ for best rates
# 2. Calculate total costs:
#    - Down payment
#    - Closing costs (2-5% of purchase price)
#    - Monthly mortgage
#    - Property taxes
#    - Insurance
#    - Maintenance (1% of home value annually)

# Due Diligence:
# 1. Inspect:
#    - Foundation
#    - Roof condition
#    - Electrical systems
#    - Plumbing
#    - HVAC age/condition

# 2. Research:
#    - Neighborhood comps
#    - Property tax history
#    - Flood zones
#    - Crime rates
#    - School ratings

# Would you like specific details about any of these points?
# Message: exit
