# Making routing system
Implementing simple authentication routing system using JS-fetch calls and flask api points and implementing localStorage based authentication and access_token system

# Ultimate Idea of Authentication and Authorization
User login -> Access granted with token --> Locally stored

Api-hit --> JS calls api for adding to cart and user page fetches DB when refreshed to fetch user details only after JS hits with access token

Way to do
1. Make sure login.html is loading and calling the js script
2. Ensure authentication flow is working for user credentials
3. Call for access token generation for user and store into the storage
4. Make the flow for further requests to the application for making critical back-end calls
