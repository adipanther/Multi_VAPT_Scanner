import requests

def credential_test(target, username, password):
    try:
        r = requests.post(target, data={"username": username, "password": password}, timeout=5)
        if "invalid" in r.text.lower() or r.status_code == 401:
            return {"status": "failed", "message": "Invalid credentials"}
        return {"status": "success", "message": "Credentials might be valid"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
