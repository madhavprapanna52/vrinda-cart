# Vrinda-cart
Goal : An E-commerce platform for customers and sellers to list product and get end to end support for thier buisness to grow,
vrinda-cart currently serves vrindavan local market and provides online platform for local market via our awesome service and platform

## Project Overview

user --> selects a product --> proceeds payment --> completes transactions

Technical overview
+ Used Multiple layers of abstractions and usefull reusable code at low level of DB endpoint to understand about CRUDE operations
+ tried to make generalised DB end point for future expansion of code for upgrade
+ Made foundational mechanism which is working on surface level testing

Details of Project working

1. Custom DB-endpoint made using sqlite3 DB, Handles basic DB-operations
2. Made general DB object which is abstracted to handle objects data flow at DB-endpoint level
3. Made 2 custom objects on top of general db-object to resemble basic user and product a lot to build on top
4. user and product are classes which initialise and inherit from general db to make good data flow and operations
5. Tried to Make crafted abstract and easy to implement front-end friendly basic backend design

Scope of project and potential
=> Project could be upgraded due to its abstract and simple nature thus have potential to turn into B2C buisness
=> Transactions and user history is traced to build ML units such as recommendation system to deploy and test on such senarios
=> Could be used to study real buisness with some testing to deploy on real world

Future Targets
1. Refactor code for more robust and optimized code for more reliable backend system
2. Implement seamless , real world payment gateway and advanced security to inhance its responsibility in real world.
3. Introduce custom sales man tailoured to user to recommend user items and drives sales via using smart models.
4. Deploying project to real users and understand real buisness via local full scale driving model

Final Note
- Project is under development and their are many things to complete test and refactor, do fork it and contribute if you feel like :)


Targets
1. Implement final touch for transactions storage system
2. Make basic frontend ready api systems
3. wraping code into flask for final backend working
4. Implement basic frontend using compoenent based development with js power +U+
