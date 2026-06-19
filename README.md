# AI Image Generator Chatbot

## Features

- Streamlit Frontend
- Hugging Face FLUX.1-schnell
- Style Conditioned Prompts
- Prompt History
- Gallery View
- Download Image
- Multiple Image Generation
- Negative Prompt
- Random Prompt Generator
- Favorite Prompts
- Regenerate Last Image
- Dark/Light Mode
- Save Images Locally
- Progress Bar
- Error Handling

---

## Installation

```bash
git clone <repo-link>

cd image-generator-chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env`

```env
HF_TOKEN=your_token_here
```

Run:

```bash
streamlit run app.py
```

---

## Deployment

Deploy using:

- Streamlit Community Cloud

Add:

```text
HF_TOKEN = your_token
```

inside Streamlit Secrets.

---

## Known Limitation

Free Hugging Face inference endpoints can sometimes be slow or rate limited.

---

## Screenshot

Add a screenshot named:

```text
screenshot.png
```

to the root folder.