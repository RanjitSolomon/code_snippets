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

# Class to store messages
class State(TypedDict):
    messages: Annotated[list, add_messages]

#define a graph builder 
graph_builder = StateGraph(State) 

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

# Register Graph
graph_builder.add_node("chatbot", chatbot)

# Start Node 
graph_builder.add_edge(START, "chatbot")
# End Node
graph_builder.add_edge("chatbot", END)
# Syntax error : graph_builder.add_edge(START, end_key:"chatbot")

### Another method
# Set entry and finish points
# graph_builder.set_entry_point("chatbot")
# graph_builder.set_finish_point("chatbot")

graph = graph_builder.compile() 

user_input = input("Enter a message: ")
state = graph.invoke({"messages":[{"role": "user", "content": user_input}]})

print(state["messages"][-1].content)


# Print Graph - Within Jupyter Notebook
from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass


# uv run main.py

# Hello There!
## response: Hi! How can I help you today?

# Solve for x,  (25/9)^(x^2-12) = (27/125)^3
