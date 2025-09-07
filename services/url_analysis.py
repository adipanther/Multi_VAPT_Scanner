import requests
from urllib.parse import urlparse

def url_analysis(target):
    try:
        parsed = urlparse(target)
        r = requests.get(target, timeout=5)

        return {
            "status": "success",
            "url": target,
            "scheme": parsed.scheme,
            "domain": parsed.netloc,
            "path": parsed.path,
            "status_code": r.status_code,
            "content_type": r.headers.get("Content-Type", "unknown"),
            "server": r.headers.get("Server", "unknown")
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
