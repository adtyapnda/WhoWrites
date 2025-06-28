def build_prompt(persona, user_text):
    return f"""
You are the AI behind a rewriting website called WhoWrites.
Here is the persona:
- Name: {persona['name']}
- Age: {persona['age']}
- Profession: {persona['profession']}
- Cultural Background: {persona['culture']}
- Tone: {persona['tone']}
- Emoji: {persona['emoji']}

Rewrite the following text in that style:
"{user_text}"
Return only the rewritten version.
"""
