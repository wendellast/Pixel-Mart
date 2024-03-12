const adicionar = document.querySelector(`#adicionar`);
const cartList = document.querySelector ('#itensDoCart');
const indicadorQuantidade = document.querySelector('#quantidade-no-carrinho');
const selectScreenP = document.getElementsByClassName("SelectVariation")[0];


const mais = document.getElementById("mais");
const menos = document.getElementById("menos");
const visor = document.getElementById("infoQuantidade");

mais.addEventListener("click", () => {
    let currentValue = parseInt(visor.textContent);
    visor.textContent = currentValue + 1;
});

menos.addEventListener("click", () => {
    let currentValue = parseInt(visor.textContent);
    if (currentValue > 1) {
        visor.textContent = currentValue - 1;
    }
});

adicionar.addEventListener('click', () => {
    let currentQuantity = parseInt(indicadorQuantidade.textContent);
    let currentValue = parseInt(visor.textContent);

    if (currentValue > 0) {
        indicadorQuantidade.textContent = currentQuantity + currentValue;
        selectScreenP.style.display = "none";
    }
});

const maisC = document.getElementById("maisC");
const menosC = document.getElementById("menosC");
const visorC = document.getElementById("infoQuantidadeC");

maisC.addEventListener("click", () => {
    let currentValueC = parseInt(visorC.textContent);
    visorC.textContent = currentValueC + 1;
});

menosC.addEventListener("click", () => {
    let currentValueC = parseInt(visorC.textContent);
    if (currentValueC > 1) {
        visorC.textContent = currentValueC - 1;
    }
});