// Simple Authentication Flow

const form = document.getElementById("loginForm");
const error = document.getElementById("error");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  try{
    const response = await fetch("http://127.0.0.1:5000/login/",{
      method : "POST",
      headers : {
        "Content-Type" : "application/json"
      },
      body : JSON.stringify({username : username, password : password})
    });

    if (!response.ok){
      throw new Error("Invalid Credentials");
    }
    const data = await response.json();

    // store token
    localStorage.setItem("access_token", data.access_token);

    // TODO : Make authentication pipeline via using this access tokenn 

    window.location.href = "/products";
  } catch (error) {
      error.innerText = error.message;
  }
});
