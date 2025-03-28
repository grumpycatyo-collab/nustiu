from anthropic import Anthropic
from app.core.config import settings
from app.prompts.templates import DEFAULT_PROMPT_TEMPLATE

class ClaudeService:
    def __init__(self):
        self.client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        self.model = settings.MODEL_NAME

    def get_completion(self, user_input: str) -> str:
        prompt = DEFAULT_PROMPT_TEMPLATE.format(user_input=user_input)
        
        message = self.client.messages.create(
            model=self.model,
            max_tokens=3000,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        return message.content[0].text 