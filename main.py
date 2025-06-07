from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI()
MOVIES_DIR = './Movies'

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use a specific origin in production
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static", html=True), name="static")
app.mount("/media", StaticFiles(directory=MOVIES_DIR), name="media")

@app.get("/")
async def root():
    return RedirectResponse(url="/static/")

@app.get("/movie_list")
async def get_movie_list():
    try:
        files = os.listdir(MOVIES_DIR)
        
        movie_files = [f for f in files if f.lower().endswith((".mp4",".mkv",".avi",".mov"))]
        
        return{"movies": movie_files}
    except Exception as e:
        return {"error": str(e)}
    




if __name__ == "__main__":
    uvicorn.run("main:app", host="192.168.1.57", port=8000, reload=True)
