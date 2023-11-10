from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def say_hello():
    return {"message": "Hello World!"}


@app.get("/born/")
async def say_hello_to_world():
    return {"message": "Hello World, I was born "}

@app.get("/talantino/")
async def sent_message():
    return {"message": "This is done by Talantino"}
