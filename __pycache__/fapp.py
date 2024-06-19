from fastapi import FastAPI

app = FastAPI()

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.get("/")
async def check_prime(number1):
    number = int(number1)
    if number is None:
        print("Number is null")
    result = is_prime(number)
    return {"number": number, "is_prime": result}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
