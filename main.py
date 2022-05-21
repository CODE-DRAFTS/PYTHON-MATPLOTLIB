from fastapi import FastAPI



app = FastAPI()


app.get("/")
def root():
    return { "hello api its working"}
