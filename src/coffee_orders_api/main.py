from flask import Flask, jsonify
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

# Fake orders
'''
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
'''
orders = []
#request parser
order_post_args = reqparse.RequestParser()
order_post_args.add_argument("id", type=int, help="Entity of ID")
order_post_args.add_argument("name", type=str, help="Name of customer")
order_post_args.add_argument("coffeeName", type=str, help="Name of drink type")
order_post_args.add_argument("total", type=float, help="Price of drink")
order_post_args.add_argument("coffeeSize", type=str, help="Size of drink")

def wipe_orders():
    # recursivly remove all orders
    if len(orders) < 1:
        return
    orders.pop()
    wipe_orders()

def get_abort_if_order_existnt(order_id: int):
    # binary search thru orders call abort and return 404 code
    # if not found
    beginning = 0
    end = len(orders) - 1

    while beginning <= end:
        mid = (beginning + end) // 2
        print(f"LOC:{mid}, B:{beginning}, E:{end}")
        if orders[mid]['id'] == order_id:
            return orders[mid]
        elif orders[mid]['id'] < order_id:
            beginning = mid+1
        elif orders[mid]['id'] > order_id:
            end = mid-1
    abort(404, message=(f"Order with id {order_id} doesn't exist."))


def pop_abort_if_order_existnt(order_id: int):
    # binary search thru orders call abort and return 404 code
    # if not found
    beginning = 0
    end = len(orders) - 1

    while beginning <= end:
        mid = (beginning + end) // 2
        print(f"LOC:{mid}, B:{beginning}, E:{end}")
        if orders[mid]['id'] == order_id:
            order = orders.pop(mid)
            return order
        elif orders[mid]['id'] < order_id:
            beginning = mid+1
        elif orders[mid]['id'] > order_id:
            end = mid-1
    abort(404, message=(f"Order with id {order_id} doesn't exist."))

class Order(Resource):
    def get(self, order_id):
        o_id = int(order_id)
        return get_abort_if_order_existnt(o_id)

    def delete(self, order_id):
        o_id = int(order_id)
        order = get_abort_if_order_existnt(o_id)
        return pop_abort_if_order_existnt(o_id)

class PlaceOrder(Resource):
    def post(self):
       args = order_post_args.parse_args()
       if len(orders) < 1:
           order_id = 1
       else:
           order_id = orders[len(orders)-1]['id'] + 1

       args['id'] = order_id
       orders.append(args)
       return get_abort_if_order_existnt(order_id)

class AllOrders(Resource):
    def get(self):
        return orders

class ClearOrders(Resource):
    def get(self):
        wipe_orders()
        return orders

api.add_resource(Order, "/orders/<order_id>")
api.add_resource(AllOrders, "/orders")
api.add_resource(PlaceOrder, "/place-order")
api.add_resource(ClearOrders, "/clear-orders")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

