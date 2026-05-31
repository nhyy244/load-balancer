import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def catch_all(path: str, request: Request):
    return {"server": "localhost:8002", "path": f"/{path}", "method": request.method}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8002)
