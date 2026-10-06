from typing import Optional
from typing import Dict
from fastapi import FastAPI 

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message" : "Hello World"}


@app.get('/greet')
async def greet(name: Optional[str] = "Barrack Obama", age:Optional[int] = 25) -> Dict:
    return {"message" : f"Hello {name} and you are {age} years old"}