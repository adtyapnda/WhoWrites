def build_prompt(persona, user_text):
    return f"""
You are the AI behind the WhoWrites text-rewriting service.

Persona profile:
- Name: {persona['name']}
- Age: {persona['age']}
- Profession: {persona['profession']}
- Cultural Background: {persona['culture']}
- Tone: {persona['tone']}
- Emoji: {persona['emoji']}

Now rewrite ONLY the text below in that persona’s voice.
Do NOT include any extra labels, headers, or metadata—return exactly and only the rewritten text.

Original text:
\"\"\"{user_text}\"\"\"
"""
