# WhoWrites

**WhoWrites** is a playful and powerful AI rewriting platform that allows users to craft content in the voice of a fully customized persona.

## 🔥 What It Does

The platform features a creative interface called **"Build Your Voice"**, where users can define:

- **Name**
- **Age**
- **Profession**
- **Cultural Background**
- **Tone**
- **Signature Emoji**

This flexibility allows users to go beyond generic tones like *formal* or *informal* — and instead imagine their content written by, say, an **8-year-old girl from Japan who’s lighthearted** or a **60-year-old Indian man who’s a retired lawyer with a serious tone**.

This feature makes **WhoWrites** great for:

- ✨ Storytelling  
- 📚 Teaching  
- 🧠 Creative writing  
- 📝 Personalizing communication  
- 💬 Adding personality to any content

Users can even **save their persona for later reuse**, making the process seamless and fun.

---

## 🛠️ Tech Stack

| Frontend         | Backend        | AI / Infra           | Other Tools       |
|------------------|----------------|-----------------------|-------------------|
| HTML, CSS        | Python         | Together.ai (Mistral) | Figma (UI Design) |
| JavaScript       | FastAPI        | Supabase (if used)    | Netlify (Hosting) |
| React (optional) |                |                       |                   |

---

## 📦 How It Works

1. **Frontend** collects persona input + user text via a sleek UI.
2. On clicking **Transform Text**, a request is sent to the FastAPI backend.
3. The backend constructs a persona-specific prompt and forwards it to **Together.ai’s Mistral model**.
4. The model responds with rewritten content in the desired style.
5. The rewritten text is displayed back to the user.

---

## ⚠️ API Key Notice

This project uses an `.env` file to store the `TOGETHER_API_KEY`.  
Please **do not commit this file** to public repositories.

Instead, include a sample `.env.example` like:

```env
TOGETHER_API_KEY=your_api_key_here
