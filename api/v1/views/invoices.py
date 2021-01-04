
""" objects that handles all default RestFul API actions for invoices """

from models.invoice import Invoice
from models.client import Client
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from datetime import date

@app_views.route('/invoices', methods=['GET'], strict_slashes=False)
def get_invoices():
    """
    Retrieves the list of all Invoices objects
    """
    all_invoices = storage.all(Invoice).values()
    list_invoices = []
    for invoice in all_invoices:
        list_invoices.append(invoice.to_dict())
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

    return jsonify(invoice.to_dict())

@app_views.route('/invoices', methods=['POST'], strict_slashes=False)
def post_invoice():
    """
    Creates a Invoice Object
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()


    if 'invoice_number' not in data:
        abort(400, description="Missing invoice number")
    
    if 'date' not in data:
        abort(400, description="Missing date")

    if 'client_id' not in data:
        abort(400, description="Missing client")
    
    if 'discount' not in data:
        abort(400, description="Missing discount")

    client = storage.get(Client, data['client_id'])
    if not client:
        abort(404, description="Client doesn't exist")

    # Changing
    data['date'] = date(2020, 10, 16)

    new_invoice = Invoice(**data)

    new_invoice.save()
    return make_response(jsonify(new_invoice.to_dict()), 201)
