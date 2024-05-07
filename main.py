from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
import openai

app = FastAPI()

# Set your OpenAI API key here
openai.api_key = 'YOUR_API_KEY_HERE'

class QuestionAnswerInput(BaseModel):
    url: str
    question: str

class QuestionAnswerOutput(BaseModel):
    answer: str

@app.post("/get_answer", response_model=QuestionAnswerOutput)
async def get_answer(data: QuestionAnswerInput):
    url = data.url
    question = data.question

    # Fetch webpage content
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="URL not found")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract text from webpage
    paragraphs = soup.find_all('p')
    text = ' '.join([p.get_text() for p in paragraphs])

    # Choose a different OpenAI model (replace with your desired model)
    engine = "davinci-002"  # Example - You can choose another model here

    prompt = f"Context: {text}\nQuestion: {question}\nAnswer:"

    completion = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=0.5,
        max_tokens=50
    )

    answer = completion.choices[0].text.strip()

    return {"answer": answer}
    