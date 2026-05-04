from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from google import genai
from dotenv import load_dotenv
import os

load_dotenv('.env.local')

app = FastAPI()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.get("/")
def root():
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents="""
        you are an AI model running on a live server that was just deployed, welcome the user with a short excited message letting him know this is new to production server, keep response in html format cuz it will be directly injected to the user end, include nice css styles to make it beautiful, your html should be the full page from the opening <html> to the closing </html>, don't write it as code block (dont' include the ```html at the beginning cuz this breaks rendering), your text response will be used immediatly in return HTMLResponse(what_you_give_me_directly)
        
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview",
            contents=this prompt.. you are seeing..,
        )
    
        return HTMLResponse(response.text)
        """,
    )
    
    return HTMLResponse(response.text)
    

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)