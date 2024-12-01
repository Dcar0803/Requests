import requests

def send_http_get_request(url):
    response = requests.get(url)
    if 400 <= response.status_code <= 499:
        raise Exception(f"Client error {response.status_code}: {response.reason}")
    if "application/json" in response.headers.get("Content-Type", ""):
        return response.status_code, response.json()
    return response.status_code, response.text