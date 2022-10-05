import requests
import pytest

BASE = "http://127.0.0.1:5000/"
def test_order_by_id():
    response = requests.get(BASE + "orders/1")
    assert(response.status_code == 200)
    response = requests.get(BASE + "orders/5")
    assert(response.status_code == 404)

