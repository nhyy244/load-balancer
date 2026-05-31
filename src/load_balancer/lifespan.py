from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from load_balancer.loadBalancer import LoadBalancer, Server


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    app.state.lb = LoadBalancer(
        [
            Server(base_url="http://localhost:8001"),
            Server(base_url="http://localhost:8002"),
        ]
    )
    yield
