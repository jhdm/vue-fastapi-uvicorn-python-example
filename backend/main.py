from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/", StaticFiles(directory="../frontend/dist", html = True), name="static")

@app.get('/')
async def home():
    return app.staticfiles('/index.html')
