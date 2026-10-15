from fastapi import FastAPI, status

app =FastAPI()

@app.get("/", status_code=status.HTTP_204_NO_CONTENT)
def test():
    return ("text")