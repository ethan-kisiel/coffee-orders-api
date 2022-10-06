import requests
import pytest

BASE = "http://127.0.0.1:5000/"
def test_order_by_id():
    response = requests.get(BASE + "orders/1")
    assert(response.status_code == 200)
    response = requests.get(BASE + "orders/5")
    assert(response.status_code == 404)

def test_all_orders():
    return

def test_add_order():
    order_to_place = {"id": 1, "name": "Ethan Kisiel",
                      "coffeeName": "Hot Coffee", "total": 0.01,
                      "coffeeSize": "Large"}
    response = requests.post(BASE + "/place-order", order_to_place)
    assert(response.status_code == 200)
    assert(response.json()['name'] == "Ethan Kisiel")

def test_update_order():
    return

def test_delete_order():
    return

