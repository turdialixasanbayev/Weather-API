import requests

def get_client_ip(request):
    """Extract client IP address."""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_ip_location(ip):
    """Get IP info from ipapi.co (free)."""
    try:
        resp = requests.get(f"https://ipapi.co/{ip}/json/").json()
        return {
            "ip": ip,
            "city": resp.get("city"),
            "region": resp.get("region"),
            "country": resp.get("country_name"),
            "latitude": resp.get("latitude"),
            "longitude": resp.get("longitude"),
            "org": resp.get("org"),
        }
    except:
        return {"ip": ip}
