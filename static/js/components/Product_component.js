/* Product component
 
functions 
  1. fetches product details and displays the product
  2. add to cart, show details options with simple image rendering thing
*/ 
class ProductComponent extends HTMLElement {
  constructor() {
    super();
    const shadow = this.attachShadow({ mode: 'open'});

    // load prebuilt template
    const template = document.getElementById('product-template').content;
    shadow.appendChild(template.cloneNode(true));
  }

  // Page update
  connectedCallback() {
    // Edit template based on tags attributes
    const name = this.getAttribute('name') || "Product";
    const price = this.getAttribute('price') || "0.00";
    // we can also add image and discription later

    this.shadowRoot.getElementById('title').textContent = name;
    this.shadowRoot.getElementById('price').textContent = price;

    const button = this.shadowRoot.getElementById("add-to-cart");
    button.addEventListener('click', () => this.addToCart(name));
  }

  async addToCart(name){
    console.log("Add to cart innitiated :)");
    // with name we would make api -request for adding prduct
    const token = localStorage.getItem("access_token");
    console.log(token);
    if (!token){
      alert("Login first");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/user/cart/add",{
        method : "POST",
        headers : {
          "Content-Type":"application/json",
          "Authorization" : `Bearer ${token}`
        },
        body : JSON.stringify(
          {name:name, quantity:1}
        )
      });

      console.log(response);

      if (!response.ok){
        throw new Error("Unautherised");
      }

      const data = await response.json();
      alert(data.message);
    } catch (error){
      console.log("Hiting Endpoint presented Errro");
      alert("Session expired or Login Required");
    }
  }
}

customElements.define('product-card', ProductComponent);
