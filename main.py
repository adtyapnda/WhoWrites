from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Hello Judges
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RewriteRequest(BaseModel):
    name: str
    age: str
    profession: str
    culture: str
    tone: str
    emoji: str
    userText: str

@app.post("/rewrite")
async def rewrite_text(payload: RewriteRequest):
    prompt = f"""You are an AI for a rewriting tool called WhoWrites.
Here is the persona:
- Name: {payload.name}
- Age: {payload.age}
- Profession: {payload.profession}
- Cultural Background: {payload.culture}
- Tone: {payload.tone}
- Emoji: {payload.emoji}

Rewrite the following text in that style:
"{payload.userText}"

Return only the rewritten version."""

    response = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
            "max_tokens": 500,
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    if response.status_code == 200:
        result = response.json()
        rewritten_text = result["choices"][0]["message"]["content"]
        return {"rewrittenText": rewritten_text}
    else:
        return {"error": "API call failed", "status": response.status_code}
