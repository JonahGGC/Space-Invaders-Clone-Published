from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

BUILD_PATH = os.path.join(os.path.dirname(__file__), "WebGame")

app.mount("/Build", StaticFiles(directory=os.path.join(BUILD_PATH, "Build")), name="build")
app.mount("/TemplateData", StaticFiles(directory=os.path.join(BUILD_PATH, "TemplateData")), name="template")

@app.get("/")
def read_root():
    return FileResponse(os.path.join(BUILD_PATH, "index.html"))