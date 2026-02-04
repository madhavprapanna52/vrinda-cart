# VRINDA - CART
A application which gives online platform for shops to sell their products
Features [Targeted]
1. Products listing page
2. User login system
3. Orders and stocks managers
4. Admin dashboard for sellers
5. custom sales man for individual customers
6. User Personalised Experience with ML

## Technical overview

Project structure
```
vrinda-cart
|--DB/
    |--/images
        |-- links.txt # image storage table
    |--/sql
        |-- schema.sql  # tables design
        |-- view.sql  # views fetch
        |-- trigger.sql # atomic triggers
    |-- Object.py  # custom mini ORM
    |-- QueryBuilder.py  # Query generator
    |-- Executor.py  # central executor unit
    |-- tools.py  # helper functions
|--Models/
    |-- User.py
    |-- Cart.py
    |-- Product.py
|--Auth/
    |-- Access.py  # sessions manager
    |-- Login.py  # Authentication unit
|--Routes/
    |-- Products_listing.py # listing routes
    |-- Account.py
|--API/
    |--routing.py  # central routing gateway for request
    |-- user.py
    |-- product.py
    |-- cart.py
|--Tests/
    |-- db_test.py  # db testing
    |-- models_flow.py  # models testing
    |-- integration_test.py
|--static/
    |--js/
        |-- ProductComponent.js  # custom webcomponent for products card
        |-- Route.js  # central front-end request handler
        |-- UserInfo.js  # user information fetch
        |-- Cart.js  # cart requests and functions
    |--images/
        |-- logo.svg  # custom logo
        |-- shop.svg # custom shop icon design
        |-- cart.svg
        |-- icon.svg
    |--css/
        |-- main.css  # global styling 
        |--products.css
        |--login.css
        |--user.css 
|--templates/
    |-- index.html  # landing page layout
    |-- products.html  # products page
    |-- user.html  #user page 
    |-- login.html # login page
|-- run.py
|-- README.md
```

## Development Note
Project is under active development special features of ML and personalisations have not been implemented yet but scoped for future expansion currently a basic website foundation is to be laid and working and development is shared in linked in and explained on youtube

## Collaborations and Contributions
I am happy to collaborate with individual who would like to contribute and learn
DO mail me at : madhavprapanna@gmail.com