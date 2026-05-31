from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from load_balancer.serverOrchestrator import LoadBalancer, Server


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    app.state.lb = LoadBalancer(
        [Server(url="http://localhost:8001"), Server(url="http://localhost:8002")]
    )
    yield
