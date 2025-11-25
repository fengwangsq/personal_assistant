from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END, START
from langgraph.prebuilt import ToolNode
from app.tools.filesystem import list_files, read_file, write_file, make_directory

# Define the state
class AgentState(TypedDict):
    messages: Sequence[BaseMessage]

# Initialize the model
llm = ChatOllama(model="llama3.2:3b-instruct-q4_K_M", temperature=0)

# Define tools
tools = [list_files, read_file, write_file, make_directory]
llm_with_tools = llm.bind_tools(tools)

# System prompt
SYSTEM_PROMPT = """You are a helpful personal assistant running locally on the user's computer. 

Your capabilities:
- list_files: List files in a directory
- read_file: Read the content of a file
- write_file: Write content to a file
- make_directory: Create a new directory

IMPORTANT INSTRUCTIONS:
- When the user asks you to DO something with files (list, read, write, create), USE THE TOOLS immediately
- Do NOT just explain what you could do - actually do it by calling the appropriate tool
- After using a tool, explain the results in a friendly way
- For general questions (like "what can you do"), answer conversationally without using tools

Examples:
- "list files in current directory" → Use list_files tool immediately
- "read README.md" → Use read_file tool immediately
- "what can you do?" → Just answer conversationally

Be concise, helpful, and action-oriented."""

# Define the agent node
def agent(state: AgentState):
    messages = state["messages"]
    # Add system prompt as the first message if not already present
    if not messages or not isinstance(messages[0], type(messages[0])) or messages[0].content != SYSTEM_PROMPT:
        from langchain_core.messages import SystemMessage
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + list(messages)
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

# Define the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("agent", agent)
workflow.add_node("tools", ToolNode(tools))

# Add edges
workflow.add_edge(START, "agent")

def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END

workflow.add_conditional_edges("agent", should_continue)
workflow.add_edge("tools", "agent")

# Compile the graph
app_agent = workflow.compile()
