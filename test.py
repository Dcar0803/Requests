import requests
import pytest
from main import send_http_get_request, get_beeceptor_data

def test_http_get():
    url = "https://httpbin.org/get"
    response = send_http_get_request(url)
    assert isinstance(response, tuple)
    assert response[0] == 200 # 200 :Request from a client to a server was successful


def test_get_beeceptor():
    response = get_beeceptor_data()
    assert isinstance(response, tuple)  # Need to return a tuple.
    assert len(response) == 2  # the tuple contains two elements.