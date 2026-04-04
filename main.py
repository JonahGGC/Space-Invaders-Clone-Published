from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

BUILD_PATH = os.path.join(os.path.dirname(__file__), "WebGame")

# add this temporarily to main.py
import os
print("BUILD_PATH:", os.path.join(os.path.dirname(__file__), "WebGame"))
print("Build exists:", os.path.exists(os.path.join(os.path.dirname(__file__), "WebGame", "Build")))
print("TemplateData exists:", os.path.exists(os.path.join(os.path.dirname(__file__), "WebGame", "TemplateData")))

# mount each subfolder separately
app.mount("/Build", StaticFiles(directory=os.path.join(BUILD_PATH, "Build")), name="build")
app.mount("/TemplateData", StaticFiles(directory=os.path.join(BUILD_PATH, "TemplateData")), name="template")

@app.get("/")
def read_root():
    return FileResponse(os.path.join(BUILD_PATH, "index.html"))