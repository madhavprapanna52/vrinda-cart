# Endpoint

DB Endpoint
* core CRUDE operation
* handle single thread execution
* table based handles - parallel processing

Endpoint
  Low level DB communication endpoint,consists of all DB level things to handle
  with fail steps, Executes and Logs query and outputs

* CORE features
  + Flexible endpoint for more data needs as we need to store images and adjust the schema for security and modularity, storing product , description, images, reviews, price, required for scaling and real deployment
  + Require to handle multiple join and automated DB calls for seamless communication system

## ENDPOINT

  1. execute
    > query, option
    Executes query via connection and returns output based on option 
  2. search
    > anchor_information, fetch_target
    search DB table for given target
  3. fetch_instance
    > DB table state fetch
  4. create
    > information : Dictionary with given information about table feilds
    Makes the creation request
  5. edit
    > target_information, edit_information
    Makes changes into the target information columns with given edit information
  5. delete
    > target
    Deletes the given Target

## General_Object
Needs improvement to handle good level of needs and be robust for single thread execution
for transaction endpoints being clean to execute
