from anthropic import Anthropic
from app.core.config import settings
from app.prompts.templates import DEFAULT_PROMPT_TEMPLATE
from typing import Optional

class ClaudeService:
    def __init__(self):
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        self.default_model = settings.MODEL_NAME
        self.default_max_tokens = 3000

    def get_completion(
        self, 
        user_input: str, 
        model_name: Optional[str] = None, 
        max_tokens: Optional[int] = None
    ) -> str:
        prompt = DEFAULT_PROMPT_TEMPLATE.format(user_input=user_input)
        
        message = self.client.messages.create(
            model=model_name or self.default_model,
            max_tokens=max_tokens or self.default_max_tokens,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        return message.content[0].text 