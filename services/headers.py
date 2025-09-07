import requests

def check_headers(target):
    try:
        r = requests.get(target, timeout=5)
        headers = r.headers
        important = [
            "Content-Security-Policy", "X-Frame-Options",
            "Strict-Transport-Security", "X-Content-Type-Options",
            "Referrer-Policy", "Server"
        ]
        return {h: headers.get(h, "❌ Missing") for h in important}
    except Exception as e:
        return {"error": str(e)}
