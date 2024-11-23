from fastapi import FastAPI

app = FastAPI()

@app.get('/greet')
def greeting(greeting: str = "Hello", name: str = "Adela"):
    return {"message": f"{greeting}, {name}! This is my first FastAPI task"}