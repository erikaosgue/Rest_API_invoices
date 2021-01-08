

"""Module that create the tables and content of the database """

from models import storage
from models.client import Client
from models.invoice import Invoice
from models.item import Item
from models.product import Product
from models.user import User
from datetime import date

print(" Creating tables Client and Product...")

client_1 = Client(name="Ulter")
client_1.save() 


client_2 = Client(name="Somantich")
client_2.save() 

client_3 = Client(name="KP")
client_3.save() 

client_4 = Client(name="Twilio")
client_4.save() 

product_1 = Product(description="Iphone", product_code=1234)
product_1.save()

product_2 = Product(description="Mackbook", product_code=4567)
product_2.save()

product_3 = Product(description="Airpods", product_code=7890)
product_3.save()

product_4 = Product(description="Ipad", product_code=1234)
product_4.save()

user_1 = User(name="Erika", lastInvoiceCode=1, lastItemCode=1)
user_1.save()

# print(user_1.lastInvoiceCode)
# print(user_1.lastItemCode)
# invoiceNum = '{0:04}'.format(user_1.lastInvoiceCode + 1)
# user_1.save()

# invoice_1 = Invoice(invoice_number=invoiceNum, date=date(2020, 10, 16), client_id=client_1.id, discount=2, client_name=client_1.name)
# invoice_1.save()


# item_1 = Item(item_number='0001', name=product_1.description, quantity=2, price=130000, product_id=product_1.id, invoice_id=invoice_1.id)
# item_1.total = item_1.quantity * item_1.price


# # Actualizando invoice_1 (Simulando el Post)
# invoice_1.subtotal += item_1.total
# invoice_1.total = int(invoice_1.subtotal * (1 - invoice_1.discount / 100))
# invoice_1.num_items += 1

# item_1.save()
# invoice_1.save()


# # -------- item 2 with the same invoice ------

# item_2 = Item(item_number='0002', name=product_2.description, quantity=1, price=130000, product_id=product_2.id, invoice_id=invoice_1.id)
# item_2.total = item_2.quantity * item_2.price


# # Actualizando invoice_1 (Simulando el Post)
# invoice_1.subtotal += item_2.total
# invoice_1.total = int(invoice_1.subtotal * (1 - invoice_1.discount / 100))
# invoice_1.num_items += 1

# item_2.save()
# invoice_1.save()


print("Tables created succesfully!")