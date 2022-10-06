from coffee_orders_api import main
orders = [{"id":1,
           "name": "John Doe",
           "coffeeName":"Hot Coffee",
           "total": 4.50,
           "coffeeSize": "Medium"},
          {"id":2,
           "name": "Jane Doe",
           "coffeeName":"Iced Coffee",
           "total": 2.50,
           "coffeeSize": "Small"}]

print(main.abort_if_order_existnt(1))
print(main.abort_if_order_existnt(5))
