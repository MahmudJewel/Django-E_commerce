## Licence
This web app is developed by : [Jewel Mahmud](https://mahmudjewel.herokuapp.com/
) under licence of [tech villain](https://www.youtube.com/channel/UCJCdq7lWqB7M5b16UatoTEw) youtube channel.

Start date of developing: Aug-2021
## Tools
#### Language
	Python (3.10)

### Back-end
	Django ==> 3.2.8

### Front-end
	Bootstrap ==> 5.1.3
	Fontawesome ==> 4.7.0
	HTML-5
	CSS-3

#### Other libraries / tools:
	asgiref==3.4.1
	django-active-link==0.1.8
	django-crispy-forms==1.13.0
	django-flatpickr==1.0.1
	django-tinymce==3.4.0
	django-widget-tweaks==1.4.9
	Pillow==8.4.0
	pytz==2021.3
	sqlparse==0.4.2
	whitenoise==5.3.0
### Database
	Sqlite

## Base
	Every page includes navebar & footer.

# Setup
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/MahmudJewel/Django-E_commerce
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ cd Django-E_commerce
$ python -m venv venv
$ source venv/bin/activate
```
Then install the dependencies:
```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
```

## Home page
Home page shows product category & products. It has a paginations of 12 products.
!![home page](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/1-home.png)

## Single product view
After clicking the product image, it will show the product’s descriptions.

![Single product view](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/2-single_product2.png)


## Category-wise view
After clicking catery title, products of these category will be shown.
![Category-wise view](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/3-product%20on%20categories.png)
## Cart Page
![Cart Page](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/4-cart_page.png)
## Checkout Page
![Checkout Page](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/5-checkout.png)
## Order History
![Order History](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/6-order%20history.png)
## Search Page
![Search Page](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/7-search%20page.png)
## Acount Page (Login, Sign up & Update)
###  Login page
![Login](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/login%20page.png)
###  Sign up
![Sign up](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/signup%20page.png)
###  Acount Update page
![Update](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/student%20update%20form.png)	

# Admin Page
## Admin Dashboard
![Admin Dashboard](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/admin/1-admin-dash.png)
## Admin-Order Dashboard
![Admin-Order Dashboard](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/admin/2.1-order-dash.png)
### Total Order List
![Total Order List](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/admin/2.2-order_total.png)
### Pending Order List
![Pending Order List](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/admin/2.3-order_pending.png)
### Processing Order List
![Processing Order List](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/admin/2.4-order_processing.png)
### Shipped Order List
![Shipped Order List](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/admin/2.5-order_shipped.png)
### Delivered Order List
![Delivered Order List](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/admin/2.6-order_delivered.png)
## Customer-List
![Customer-List](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/admin/3.0-customer.png)
## Product-Dashboard
![Product-Dashboard](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/admin/4.0-product-list.png)
## Update Status
![Update Status](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/admin/4.1-update-status.png)
## Admin-Category Dashboard
![Admin-Category Dashboard](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/admin/5.0-category-dash.png)
### Category update view
![Category update view](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/admin/5.1-category_update.png)
### Category List
![Category List](https://github.com/MahmudJewel/E_commerce-frontend/blob/main/screenshot%20of%20django%20project/admin/5.2-category_view.png)
The End


