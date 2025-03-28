# Claude API Integration

A FastAPI backend that integrates with the Claude API, featuring a clean layered architecture and easy prompt engineering capabilities.

## Project Structure

```
app/
├── api/            # API routes and endpoints
├── core/           # Core configuration
├── models/         # Pydantic models
├── prompts/        # Prompt templates
└── services/       # Business logic and external service integration
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your Anthropic API key:
```
ANTHROPIC_API_KEY=your_api_key_here
```

## Running the Application

Start the server with:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### POST /api/chat

Send a message to Claude and get a response.

Request body:
```json
{
    "message": "Your message here"
}
```

Response:
```json
{
    "response": "Claude's response"
}
```

## Prompt Engineering

The prompt templates are located in `app/prompts/templates.py`. You can modify the `DEFAULT_PROMPT_TEMPLATE` to customize how user inputs are processed before being sent to Claude. 