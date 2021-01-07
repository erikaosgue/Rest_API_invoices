""" objects that handles all default RestFul API actions for Clients """

from models.invoice import Invoice
from models.client import Client
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from datetime import date
from random import randint

@app_views.route('/clients', methods=['GET'], strict_slashes=False)
def get_clients():
    """
    Retrieves the list of all clients objects
    """
    all_clients = storage.all(Client).values()
    list_clients = []
    for client in all_clients:
        list_clients.append(client.to_dict())
    return jsonify(list_clients)

@app_views.route('/clients/<client_id>', methods=['GET'],
                 strict_slashes=False)
def get_client(client_id):
    """
    Retrieves the object invoice base on client_id
    """
    client = storage.get(Client, client_id)
    if not client:
        abort(404)

    return jsonify(client.to_dict())