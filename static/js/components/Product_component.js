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
  }

}

customElements.define('product-card', ProductComponent);
