import requests

import json 

req = {
    "cve_id": "CVE-2021-34527",
    "package_name": "httpd",
    "package_version": "2.4.46",
    "source_path": "./test_package",
    "language": "python",
}


res = requests.post(
    "http://localhost:8000/reachability",
    json=req)


print(res.status_code)
print(json.dumps(res.json(), indent=2))
