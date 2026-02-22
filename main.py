from fastapi import FastAPI from pydantic import BaseModel
app = FastAPI()
@app.get("/")

def root():

return {"status": "ok", "message": "Hello from CreativeU API"}

class Summary(BaseModel):

processed_files:

int = 0

creators_count:

int = 0
