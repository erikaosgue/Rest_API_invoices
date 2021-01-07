
""" objects that handles all default RestFul API actions for invoices """

from models.invoice import Invoice
from models.client import Client
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from datetime import date
from random import randint
from datetime import datetime
import json

@app_views.route('/invoices', methods=['GET'], strict_slashes=False)
def get_invoices():
    """
    Retrieves the list of all Invoices objects
    """
    all_invoices = storage.all(Invoice).values()
    list_invoices = []
    for invoice in all_invoices:
        list_invoices.append(invoice.to_dict())
        print(invoice.items)
        for item in invoice.items:
            print(item.to_dict())

    return jsonify(list_invoices)


@app_views.route('/invoices/<invoice_id>', methods=['GET'],
                 strict_slashes=False)
def get_invoice(invoice_id):
    """
    Retrieves the object invoice base on invoice_id
    """
    invoice = storage.get(Invoice, invoice_id)
    if not invoice:
        abort(404)

    print(invoice.items)

    return jsonify(invoice.to_dict())

@app_views.route('/invoices/<invoice_id>/items', methods=['GET'],
                 strict_slashes=False)
def get_invoiceItems(invoice_id):
    """
    Retrieves the object items contain on invoice
    """
    invoice = storage.get(Invoice, invoice_id)
    if not invoice:
        abort(404)
    list_items = []
    print("@@@@ ", invoice.items)
    for items in invoice.items:
        print("==> ", items)
        list_items.append(items.to_dict())

    print(list_items)

    return jsonify(list_items)

@app_views.route('/invoices', methods=['POST'], strict_slashes=False)
def post_invoice():
    """
    Creates a Invoice Object
    """

    if not request.get_json():
        abort(400, description="Not a JSON")

    # ---Using POSTMAN
    # data = request.get_json()
    # --- Using vue
    data = request.get_json()['jsonData']
    data = json.loads(data)


    if 'client_id' not in data:
        abort(400, description="Missing client_id")
    
    if 'date' not in data:
        abort(400, description="Missing date")
    
    if 'discount' not in data:
        abort(400, description="Missing discount")

    client = storage.get(Client, data['client_id'])
    if not client:
        abort(404, description="Client doesn't exist")

    
    data['client_name'] = client.name
    
    data['discount'] = int(data['discount'])

    # Changing
    data['date'] = datetime.strptime(data['date'], '%Y-%m-%d').date()

    
    # Is better to pass in the Json the Id of the user, this is
    # just for facilitate the things
    users = storage.all(User).values()
    for user in users:
        if not user.lastInvoiceCode:
            user.lastInvoiceCode = 0
        data['invoice_number'] = '{0:04}'.format(user.lastInvoiceCode + 1)
        user.lastInvoiceCode += 1
        user.save()
    
    

    new_invoice = Invoice(**data)
    print(new_invoice.items)

    new_invoice.save()
    return make_response(jsonify(new_invoice.to_dict()), 201)