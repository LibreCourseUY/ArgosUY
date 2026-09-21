from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.get("/")
async def root_redirect():
    return RedirectResponse("/docs")