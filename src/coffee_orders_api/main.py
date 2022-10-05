from flask import Flask
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)
# Fake orders
orders = [{"id":1,
           "name": "John Doe",
           "coffeeName":"Hot Coffee",
           "total": 4.50,
           "coffeeSize": "Medium"}]

def abort_if_order_exisnt(order_id: int):
    beginning = 0
    end = len(orders) - 1

    while beginning <= end:
        mid = int(beginning + end / 2)
        if orders[mid]['id'] == order_id:
            return orders[mid]
        elif orders[mid]['id'] < order_id:
            beginning = mid+1
        elif orders[mid]['id'] > order_id:
            end = mid-1
        abort(404, message=(f"Order with id {order_id} doesn't exist."))


class Order(Resource):
    def get(self, order_id):
        return orders

class AllOrders(Resource):
    def get(self):
        return orders

api.add_resource(Order, "/orders/<order_id>")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

