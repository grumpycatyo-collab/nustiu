from pydantic import BaseModel, Field
from typing import Optional

class ChatRequest(BaseModel):
    message: str
    model_name: Optional[str] = Field(default="claude-3-sonnet-20240229", description="The Claude model to use")
    max_tokens: Optional[int] = Field(default=3000, ge=1, le=4096, description="Maximum number of tokens to generate")

class ChatResponse(BaseModel):
    response: str 