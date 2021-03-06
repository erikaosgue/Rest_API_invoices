
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.invoices import *
from api.v1.views.items import *
from api.v1.views.clients import *
from api.v1.views.products import *