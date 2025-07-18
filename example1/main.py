from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    sample = ["adnan","ziya"]
    return {"data": sample}

@app.get("/sample")
async def sample():
    sample = ["adnan","mert"]
    return {"data": sample}