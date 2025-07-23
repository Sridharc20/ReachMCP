import uuid

from datetime import datetime


def generate_vex_report(package_name: str, package_version: str, cve_id: str, reachable: bool) -> dict:
    """
    Generate a VEX report for a given package and CVE.
    
    Args:
        package_name (str): Name of the package.
        package_version (str): Version of the package.
        cve_id (str): CVE identifier.
        source_path (str): Path to the source code.
        language (str): Programming language of the source code.
    
    Returns:
        dict: A dictionary containing the VEX report.
    """
    return {
        "report_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "package_name": package_name,
        "package_version": package_version,
        "cve_id": cve_id,
        "reachable": reachable,
        "status": "vulnerable",
        "details": f"Vulnerability {cve_id} found in {package_name} version {package_version}."
    }