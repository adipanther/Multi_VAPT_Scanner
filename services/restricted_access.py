import requests

restricted_paths = ["/admin", "/login", "/dashboard", "/config"]

def restricted_access_check(target):
    results = []
    for path in restricted_paths:
        try:
            url = target.rstrip("/") + path
            r = requests.get(url, timeout=5)
            results.append({"path": url, "status": r.status_code})
        except:
            pass
    return {"results": results}
