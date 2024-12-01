import requests

def send_http_get_request(url):

    """Sends an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to send the GET request to.

    Raises:
        Exception: If the status code is in the 4xx range (client errors).

    Returns:
        tuple: (status_code, response_text/dict).
            - If content type is JSON, response text is returned as a dictionary.
            - Otherwise, it is returned as a string.
    """
    response = requests.get(url)
    if 400 <= response.status_code <= 499:
        raise Exception(f"Client error {response.status_code}: {response.reason}")
    if "application/json" in response.headers.get("Content-Type", ""):
        return response.status_code, response.json()
    return response.status_code, response.text


def get_beeceptor_data():
    url = "https://echo.free.beeceptor.com"
    response = requests.get(url)
    headers = response.headers
    return headers.get("Postman-Token"), headers.get("X-Forwarded-For") #X-Forwarded-For is an HTTP header that identifies the IP address of a client that initiates an HTTP request
