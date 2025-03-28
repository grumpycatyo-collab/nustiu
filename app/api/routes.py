from fastapi import APIRouter, HTTPException
from app.models.chat import ChatRequest, ChatResponse
from app.services.claude_service import ClaudeService

router = APIRouter()
claude_service = ClaudeService()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        response = claude_service.get_completion(request.message)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 