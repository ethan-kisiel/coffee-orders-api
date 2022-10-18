import requests
import pytest

FAKE_ORDERS = [{"id": 1, "name": "Ethan Kisiel",
                "coffeeName": "Hot Coffee",
                "total": 0.01,
                "coffeeSize": "Large"},
               {"id": 2, "name": "John Doe",
                "coffeeName": "Iced Coffee",
                "total": 0.02,
                "coffeeSize": "Medium"},
               {"id": 3, "name": "Jane Doe",
                "coffeeName": "Hot Coffee",
                "total": 0.03,
                "coffeeSize": "Small"}]

BASE = "http://127.0.0.1:5000/"
print(FAKE_ORDERS[0])
def place_order(order: dict) -> requests.Response:
    r = requests.post(BASE + "/place-order", order)
    return r

def clear_orders() -> int:
    r = requests.get(BASE + "clear-orders")
    return r.status_code

def test_order_by_id():
    order = FAKE_ORDERS[0]

    clear_response = clear_orders()
    assert(clear_response == 200)

    response = place_order(order)
    assert(response.status_code == 200)

    # test if existing order returns 200 response code
    response = requests.get(BASE + "orders/1")
    assert(response.status_code == 200)
    # test if nonexistent order returns 404 response code
    response = requests.get(BASE + "orders/5")
    assert(response.status_code == 404)

def test_all_orders():
    clear_response = clear_orders()

    for order in FAKE_ORDERS:
        response = place_order(order)
        assert(response.status_code == 200)

    response = requests.get(BASE + "/orders")
    assert(response.status_code == 200)
    assert(len(response.json()) == 3)

def test_add_order():
    order = FAKE_ORDERS[0]
    response = requests.post(BASE + "/place-order", order)
    assert(response.status_code == 200)
    assert(response.json()['name'] == "Ethan Kisiel")

def test_update_order():
    clear_response = clear_orders()
    order = FAKE_ORDERS[0]
    response = place_order(order)
    order_id = response.json()['id']
    assert(response.status_code == 200 and response.json()['name'] == "Ethan Kisiel")

    order_to_put = FAKE_ORDERS[1]
    response = requests.put(BASE + f"/orders/{order_id}", order_to_put)
    assert(response.status_code == 200)

    response = requests.get(BASE + f"/orders/{order_id}")
    assert(response.status_code == 200 and response.json()['name'] == "John Doe")



def test_delete_order():
    clear_response = clear_orders()
    order = FAKE_ORDERS[0]
    response = place_order(order)
    assert(response.status_code == 200)

    order_id = response.json()["id"]
    response = requests.delete(BASE + f"/orders/{order_id}")
    assert(response.status_code == 200)
    order = response.json()
    assert(order["id"] == order_id)
