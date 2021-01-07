#!/bin/bash
echo "Droping tables ..."
echo "DROP Table items;" | sudo mysql invoices_db
echo "DROP Table products;" | sudo mysql invoices_db
echo "DROP Table invoices;" | sudo mysql invoices_db
echo "DROP Table clients;" | sudo mysql invoices_db
echo "DROP Table users;" | sudo mysql invoices_db
echo "--- Success! ---"