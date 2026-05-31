import httpx
from fastapi import APIRouter, Request

router = APIRouter()


@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def forward(path: str, request: Request):
    lb = request.app.state.lb
    server_base_url = lb.roundRobin()
    target_url = f"{server_base_url}/{path}"

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=target_url,
            headers=dict(request.headers),
            content=await request.body(),
            params=dict(request.query_params),
        )

    stats = {server.url: server.received_requests for server in lb.server_list}

    return {
        "status_code": response.status_code,
        "body": response.json() if response.headers.get("content-type", "").startswith("application/json") else response.text,
        "server_stats": stats,
    }
