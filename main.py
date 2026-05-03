from fastapi import FastAPI
from google import genai

app = FastAPI()
client = genai.Client()


@app.get("/")
def root():
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents="you are an AI model running on a live server that was just deployed, welcome the user with a short excited message letting him know this is new to production server",
    )
    
    response_text = response.text.replace("n", '</br>') # type: ignore
    
    return (
        f"""
        <html>
            <body>
                <h1>Welcome to this app!</h1>
                <p>{response_text}</p>
            </body>
        </html>
        """
    )
    
