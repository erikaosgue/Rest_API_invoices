#!/bin/bash

echo ""
echo " -------------- TABLE USERS ----------------"
echo "select * from users\G;" | sudo mysql invoices_db

echo ""
echo " -------------- TABLE PRODUCTS ----------------"
echo "select * from products\G;" | sudo mysql invoices_db

echo ""

echo "------------------- TABLE ITEMS ----------------"
echo "select * from items\G;" | sudo mysql invoices_db

echo ""

echo " -------------------- TABLE CLIENTS ---------------"
echo "select * from clients\G;" | sudo mysql invoices_db
echo ""

echo " -------------------- TABLE INVOICES ---------------"
echo "select * from invoices\G;" | sudo mysql invoices_db
echo ""