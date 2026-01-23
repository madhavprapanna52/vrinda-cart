/*
 Make Request to the endpoint and load the user information
As the DOM is loaded make the user info load via api request
*/ 

document.addEventListener("DOMContentLoaded", loadAccountInfo);

async function loadAccountInfo(){

  const token = localStorage.getItem("access_token");

  if (!token){
    window.location.href = "/login";
    return;
  }
  try {
    const response = await fetch(
      "http://127.0.0.1:5000/user/info",
      {
        method : "GET",
        headers : {
          "Authorization" : `Bearer ${token}`
        }
      }
    );
    if (!response.ok){
      throw new Error("Unauthorised or token expired");
      window.location.href = "/login";
    }
    const data = await response.json();

    updateAccountPage(data);
  } catch(error){
    console.log(error)
    console.log("I am DOne with JS :)");
  }
}

function updateAccountPage(data) {
  const name = data.name;
  document.getElementById("account-info").textContent = `Hello, ${name}`;
  // Cart Update
  const cartList = document.getElementById("product-list");
  cartList.innerHTML = "";

  data.cart.forEach(item =>{
    const li = document.createElement("li");
    li.textContent = item;
    cartList.appendChild(li);
  });

  // Orders
  const orderList = document.getElementById("order-list");
  orderList.innerHtml = "";

  data.order.forEach(order => {
    const li = document.createElement("li");
    li.textContent = order;
    orderList.appendChild(li);
  });
}
