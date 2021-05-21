# Book-Store

## Table of contents

- [Introduction](#introduction)
- [Demo](#demo)
- [Features](#features)
- [Technology](#technology)
- [Database Models](#database)
- [Run](#run)
- [License](#license)

## Introduction

A virtual BookStore website using Django,JavaScript and Ajax.

## Demo

![screenshot](screenshot.png)
The application is deployed to Heroku and can be accessed through the following link:

[BookStore on Heroku](https://bookstore4713.herokuapp.com/)

The website resembles a real store and you can add products to your cart and buy them.We have not integrated the payment options as one needs PayPal or any other account.

In order to access the admin panel on "/admin" you need to provide the admin email and password.

## Technology

The application is built with:

- asgiref==3.3.4
- Django==3.2.2
- Pillow==8.2.0
- pytz==2021.1
- sqlparse==0.4.1
- waitress==2.0.0
- whitenoise==5.2.0

## Features

The application displays a virtual Book store that contains virtual products and contact information.

Users can do the following:

- Create an account, login or logout
- Browse available products added by the admin
- Add products to the shopping cart
- Delete products from the shopping cart
- Display the shopping cart
- To checkout, a user must be logged in
- The profile contains all the informations about delivery address and user can add new address too
- User can see his/her past orders and its status
- Search bar allows user to search for his/her book and related results will be displayed

Admins can do the following:

- Login or logout to the admin panel
- View all the information stored in the database. They can view/add/edit/delete orders, users, products and categories. The cart model cannot be modified by an admin because a cart is either modified by the logged in user before the purchase or deleted after the purchase.

## Database

 - MySQL database is used to store products details
 - One can see the product fields in model file

 ### User Schema:

- username (String)
- email (String)
- password (String)

### Product Schema:

- ProductId(Number)
- title (String)
- imagePath (String)
- description (String)
- price (Number)
- category (ObjectId - a reference to the category schema)

### Cart Schema:

- items: an array of objects, each object contains: <br>
  ~ productId (ObjectId - a reference to the product schema) <br>
  ~ qty (Number) <br>
  ~ price (Number) <br>
  ~ title (String) <br>
- totalQty (Number)
- totalCost (Number)
- user (ObjectId - a reference to the user schema)
- createdAt

### Order Schema:

- user (ObjectId - a reference to the user schema)
- product (ObjectId - refrence to product schema)
- address (String)
- OrderDate (Date)
- Status (array of possible status)

## Run

To run this application
- you need to install requirements.txt items
- Set your SECRET_KEY
- Set your Database
- type <b>python manage.py runserver</b>

## License

[![License](https://img.shields.io/:License-MIT-blue.svg?style=flat-square)](http://badges.mit-license.org)

- MIT License
- Copyright 2021 © [Satyam Prakash](https://github.com/ruh-iziki-orz)
- Copyright 2021 © [Anurag Kumar](https://github.com/akgit4713)