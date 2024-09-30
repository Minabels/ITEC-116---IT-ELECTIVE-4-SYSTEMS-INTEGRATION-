from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/factorial/{value}")
def calculate_factorial(value: int):
    if value < 0:
        return {"The value must not be negative"}
    if value == 0:
        return {"result": False} 

    factorial = 1
    counter = 1


    while counter <= value:
            factorial *= counter
            counter += 1


    return {"result": factorial}