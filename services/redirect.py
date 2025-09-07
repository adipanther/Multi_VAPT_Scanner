import requests

def redirect_check(target):
    try:
        r = requests.get(target, allow_redirects=True, timeout=5)
        return {
            "final_url": r.url,
            "redirects": [resp.url for resp in r.history]
        }
    except Exception as e:
        return {"error": str(e)}
