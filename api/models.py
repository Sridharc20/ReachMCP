from pydantic import BaseModel, Field

from typing import Optional, List

class ReachabilityRequest(BaseModel):
    cve_id: str
    package_name:str
    package_version: str
    source_path:str
    language: str

class ReachabilityResponse(BaseModel):
    reachable: bool
    call_stack: Optional[List[str]]
    exploit_possible: bool
    confidence: str