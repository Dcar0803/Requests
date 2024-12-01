import requests
import pytest

def test_http_get():
    url = "https://httpbin.org/get"
    response = send_http_get_request(url)
    assert isinstance(response, tuple)
    assert response[0] == 200 # 200 :Request from a client to a server was successful