class ProductInfo extends HTMLElement {
	constructor(){
		super();
		// open shadow root | isolation from global
		this.attachShadow({mode: 'open'});
	}

	// observers for behaviour change
	static get observedAttributes() {
		return ['name', 'prize']; // extend with image and discription
	}
	
	// runs while added to dom
	connectedCallback() {
		this.render();
	}

	// attribute update
	attributeChangedCallback() {
		this.render();
	}

	render() {
		const name = this.getAttribute('name');
		const prize = this.getAttribute('prize');
		
		this.shadowRoot.innerHTML = `
		<h3> ${name} </h3>
		<div class="prize">${prize}</div>
		`;
	}
}

customElements.define('product-info', ProductInfo);
