from fastapi import FastAPI
from api import reachability

app = FastAPI(title="ReachMCP Server")

app.include_router(reachability.router, prefix="/reachability", tags=["Reachability"])
