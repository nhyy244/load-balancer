import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

import uvicorn
from fastapi import FastAPI

from load_balancer.lifespan import lifespan
from load_balancer.api.routes import router

app = FastAPI(title="load-balancer", lifespan=lifespan)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
