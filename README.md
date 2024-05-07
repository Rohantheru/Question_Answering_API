# Webpage Question Answer API

This FastAPI-based API allows you to retrieve answers to questions from a given webpage using OpenAI's GPT-3.5 language model. It utilizes BeautifulSoup for web scraping and interacts with OpenAI's API for question answering.

## Setup

1. Clone the repository:

```bash
git clone git@github.com:Rohantheru/Question_Answering_API.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. For running the api:
```bash
uvicorn main:app --reload
```
You can access the swagger from (http://127.0.0.1:8000/docs)

