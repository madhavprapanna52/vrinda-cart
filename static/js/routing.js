// Simple User information loading script
document.addEventListener("DOMContentLoaded", () => {
  loadUserInfo();
});

async function loadUserInfo() {
  const token = localStorage.getItem("access_token");
  console.log(token);

  if (!token) {
    alert("login required");
    window.location.href = "/login";
    return;
  }

  try{
    const response = await fetch("http://127.0.0.1:5000/user/info",
      {
        method : "GET",
        headers : {
          "Authorization" : `Bearer ${token}`
        }
      }
    );

    if (response.status == 401) {
      localStorage.removeItem("access_token");
      console.log("Make endpoint please");
      // window.location.href = "/login";
      return;
    }

    if (!response.ok){
      throw new Error("Failed to Fetch user info :(");
    }

    const data = await response.json();
    // fetch all DOM Elements
    const info = document.getElementById("account-info");

    info.innerText = data.name;

  } catch(error){
    console.error(error);
    console.log("error");
    // window.location.href = "/login";
  }
}
