
""" objects that handles all default RestFul API actions for items """

from models.item import Item
from models.user import User
from models.product import Product
from models.invoice import Invoice
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from datetime import date
import json

@app_views.route('/items', methods=['GET'], strict_slashes=False)
def get_items():
    """
    Retrieves the list of all Items objects
    """
    all_items = storage.all(Item).values()
    list_items = []
    for item in all_items:
        list_items.append(item.to_dict())
    
    return make_response(jsonify(list_items), 201)


@app_views.route('/items/<item_id>', methods=['GET'],
                 strict_slashes=False)
def get_item(item_id):
    """
    Retrieves the object Item base on item_id
    """
    item = storage.get(Item, item_id)
    if not item:
        abort(404)

    return make_response(jsonify(item.to_dict()), 201)

@app_views.route('/items', methods=['POST'], strict_slashes=False)
def post_item():
    """
    Creates a Item Object
    """
    # if not request.get_json():
    #     abort(400, description="Not a JSON")
    # data = request.get_json()

    data = request.get_json()['jsonData']
    data = json.loads(data)
    print("here", data)


    if 'quantity' not in data:
        abort(400, description="Missing quantity")
    
    if 'price' not in data:
        abort(400, description="Missing price")
    ''
    if 'invoice_id' not in data:
        abort(400, description="Missing invoice_id")

    product = storage.get(Product, data['product_id'])
    if not product:
        abort(404, description="Product doesn't exist")
    
    data['name'] = product.description
    # Changing
    users = storage.all(User).values()
    for user in users:
        data['item_number'] = '{0:04}'.format((user.lastItemCode) + 1)
        user.lastItemCode += 1
        user.save()


    invoice_1 = storage.get(Invoice, data['invoice_id'])

    invoice_1.num_items += 1
    if invoice_1.num_items >= 3:
        return make_response(jsonify({'status': 'max_items'}))

    data['total'] = int(data['price']) * int(data['quantity'])

    new_item = Item(**data)
    
    invoice_1.subtotal += new_item.total
    subtotal = int(invoice_1.subtotal)
    discount = int(invoice_1.discount)
    invoice_1.total = int(subtotal - (subtotal * discount / 100))
    
    new_item.save()
    invoice_1.save()
    

    return make_response(jsonify(new_item.to_dict()), 201)
