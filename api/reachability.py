from fastapi import APIRouter
from api.models import ReachabilityRequest, ReachabilityResponse
from core.analyzer import analyze_reachability

router= APIRouter()

@router.post("/", response_model=ReachabilityResponse)
def check_reachability(request: ReachabilityRequest):
    """
    Endpoint to check the reachability of a given target.
    """
    return analyze_reachability(request)