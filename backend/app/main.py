from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Personal Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from pydantic import BaseModel
from app.agents.core import app_agent
from langchain_core.messages import HumanMessage

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"message": "Personal Assistant API is running"}

@app.post("/chat")
async def chat(request: ChatRequest):
    response = app_agent.invoke({"messages": [HumanMessage(content=request.message)]})
    return {"response": response["messages"][-1].content}
