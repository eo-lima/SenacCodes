class MeuBotao extends HTMLElement {
    connectedCallback() {
        const texto = this.innerHTML || "Clique aqui";
 
        this.innerHTML = `<button class ="btn-customizado">${texto}</button>`;
    }
}
 
customElements.define('meu-botao', MeuBotao);