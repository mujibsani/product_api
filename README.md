# product_api
This repository for build api for products

Environment Setup and run:

1. pip install django
2. pip install djangorestframework
3. products > settings > INSTALLED_APPS [.....  'rest_framework','products']
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver

Then go to browser

1. Total Product List - http://127.0.0.1:8000/product/
2. Update or single product view - http://127.0.0.1:8000/product/product_id
3. Add product attribute - http://127.0.0.1:8000/product/product_id/attribute
4. Update product attribute - http://127.0.0.1:8000/product/product_id/attribute/attribute_id
5. Price List or Add product price - http://127.0.0.1:8000/product/product_id/price
4. Update product price - http://127.0.0.1:8000/product/product_id/attribute/price_id
