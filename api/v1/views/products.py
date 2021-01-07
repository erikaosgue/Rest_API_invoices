""" objects that handles all default RestFul API actions for Products """

from models.invoice import Invoice
from models.product import Product
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from datetime import date
from random import randint

@app_views.route('/products', methods=['GET'], strict_slashes=False)
def get_products():
    """
    Retrieves the list of all products objects
    """
    print("Inside")
    all_products = storage.all(Product).values()
    list_products = []
    for product in all_products:
        list_products.append(product.to_dict())
    return jsonify(list_products)

# @app_views.route('/clients/<client_id>', methods=['GET'],
#                  strict_slashes=False)
# def get_client(client_id):
#     """
#     Retrieves the object invoice base on client_id
#     """
#     client = storage.get(Client, client_id)
#     if not client:
#         abort(404)

#     return jsonify(client.to_dict())