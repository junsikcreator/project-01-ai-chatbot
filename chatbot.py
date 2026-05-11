import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_ai(user_input: str, history: list) -> str:
    """Send message to LLM while maintaining conversation history."""
    messages = [
        {"role": "system", "content": "You are a helpful, witty, and friendly AI assistant."}
    ]
    
    # Add conversation history
    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # fast & cheap, or use "gpt-4o" for better quality
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
    )
    
    return response.choices[0].message.content
