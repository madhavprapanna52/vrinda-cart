async function loginUser(username, password) {

  const response = await fetch('/login', {
    'Content-type' : 'application/json' },
    body:
    JSON.stringify({"username": username, "password" : password})
  });

  if (response.ok) {
    const data = await response.json();
    // Save the token for future responses
    localStorage.setItem('access_token', data.access_token);
    console.log("Login Successfull");
  } else{
    alert("Login Failed")
  }
  
}

// TODO : Broken login routing and js urgent fix required :)

const loginFrom = document.querySelector('#login-form');

loginForm.addEventListener('submit', aysync (e) => {
  preventDefault(); // Stop refresh

  alert("Working Button with js");
  
  const username = document.querySelector('#username').value;
  const password = docuemnt.querySelector('#password').value;

  // using login function
  await loginUser(username, password);
  console.log("Something working he he ");

})
