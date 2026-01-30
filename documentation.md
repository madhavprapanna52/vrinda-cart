# DB-Endpoint
Data flow through application model

```
Executor [db-requests] -> Data base
   | handle desision and validation with fetch handle
General_Object [Data flow handle] -> Modles data flow

```
Front-end read requests --> Search_Handle [read requests, filters, search outputs] ~ filteration/validation

Data base unit refinement
  + search Handle -> All read requests
  + Executor handles all writes to the DB
  + General Object handles unit data flow into DB and their edits , validates via targeted search requests 
  + Models have their whole data flow made via general objects

----- 
```
