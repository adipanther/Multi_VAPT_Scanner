import socket

def subdomain_enum(target):
    subs = ["www", "mail", "dev", "test", "api", "blog"]
    found = []
    for sub in subs:
        try:
            host = f"{sub}.{target}"
            ip = socket.gethostbyname(host)
            found.append({"subdomain": host, "ip": ip})
        except:
            pass
    return {"found": found or "No subdomains found"}
