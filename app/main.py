from fastapi import FastAPI

app = FastAPI()





@app.on_event("startup")
async def on_startup():
    print("starting up init Db Connection")

@app.get("/")
async def root():
    return {"message": "Hello World"}