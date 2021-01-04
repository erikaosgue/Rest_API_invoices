# Rest API invoices

REST APi invoices Provides Information of the invoices and items that exist in the database, as well as creating them.

### Get list of Invoices

    curl -i -H 'Accept: application/json' http://localhost:8084/api/v1/invoices

### Response

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 3
    Access-Control-Allow-Origin: *
    Server: Werkzeug/1.0.1 Python/3.8.5
    Date: Mon, 04 Jan 2021 09:44:14 GMT

    []


### Get list of Items

    curl -i -H 'Accept: application/json' http://localhost:8084/api/v1/items

### Response

    HTTP/1.0 201 CREATED
    Content-Type: application/json
    Content-Length: 3
    Access-Control-Allow-Origin: *
    Server: Werkzeug/1.0.1 Python/3.8.5
    Date: Mon, 04 Jan 2021 09:45:49 GMT

    []

## Create a new Thing

### Request

    curl -i localhost:8084/api/v1/invoices -H 'Accept: application/json' -d '{"invoice_number": 12211, "date": "2012-04-23", "client_id": "16d5dbf0-1681-4792-802e-9d50f45913ca", "discount": 0}'



### Get a non-existent Object



