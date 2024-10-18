# python vue application example

This is example of python Flask app serving Vue frontend.

## Directory Structure

```
projectRoot/
    +-- frontend/
        +-- dist/
            +-- index.html
        +-- src/
            +-- main.ts
        +-- vite.config.ts
    +-- backend/
        +-- main.py
```

## Vue frontend setup

```sh
mkdir my-app
cd my-app
npx create-vite frontend
cd frontend
yarn && yarn build
```

## Python backend setup

```sh
cd ..
mkdir backend
cd backend
```

**Create Python virtual environment**:

```sh
python -m venv .venv
source .venv/Scripts/activate
```

**Install**:

```sh
python -m pip install fastapi uvicorn
```

### backend/main.py:

```python
# backend/main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/", StaticFiles(directory="../frontend/dist", html = True), name="static")

@app.get('/')
async def home():
    return app.staticfiles('/index.html')
```

## Running Web server:

```sh
uvicorn main:app --reload --port 5000
```
