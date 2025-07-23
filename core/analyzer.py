from api.models import ReachabilityRequest, ReachabilityResponse
from utils.cve_mapper import map_cve_function
from utils.vex_generator import generate_vex_report


def mock_find_path_to_function(source_path, vuln_func):
    # Stubs 
    return ["main()", "processRequest()", vuln_func] if vuln_func else []


def analyze_reachability(request: ReachabilityRequest) -> ReachabilityResponse:
    # map cve to known vulnerabilities function mock
    vuln_func = map_cve_function(request.cve_id)
    call_path = mock_find_path_to_function(request.source_path, vuln_func)
    
    reachable = bool(call_path)
    confidence = "high" if reachable else "low"
    
    vex_report = generate_vex_report(
        package_name=request.package_name,
        package_version=request.package_version,
        cve_id=request.cve_id,
        reachable=reachable
    )
    
    print(vex_report)
    
    return ReachabilityResponse(
        reachable=bool(call_path),
        call_stack=call_path,
        exploit_possible=reachable,
        confidence=confidence
    )