from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    ANTHROPIC_API_KEY: str
    MODEL_NAME: str = "claude-3-sonnet-20240229"
    
    class Config:
        env_file = ".env"

settings = Settings() 