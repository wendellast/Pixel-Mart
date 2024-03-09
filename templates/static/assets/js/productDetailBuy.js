const mais = document.getElementById("mais");
const menos = document.getElementById("menos");
const visor = document.getElementById("infoQuantidade");

mais.addEventListener("click", () => {
    let currentValue = parseInt(visor.textContent);
    visor.textContent = currentValue + 1;
});

menos.addEventListener("click", () => {
    let currentValue = parseInt(visor.textContent);
    if (currentValue > 0) {
        visor.textContent = currentValue - 1;
    }
});

const x = document.getElementById("x");
const tela = document.getElementById("verMais");
const verMais = document.getElementById("abrirVerMais");

verMais.addEventListener("click", function () {
    tela.style.display = "flex";
});
x.addEventListener("click", function () {
    tela.style.display = "none";
});
