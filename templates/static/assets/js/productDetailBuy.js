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

const xClose = document.getElementById("x");
const tela = document.getElementsByClassName("verMais")[0];
const verMais = document.getElementById("abrirVerMais");

verMais.addEventListener("click", function () {
    tela.style.display = "flex";
});
xClose.addEventListener("click", function () {
    tela.style.display = "none";
});

const mainImage = document.getElementsByClassName("mainImg")[0];
const smallerImages = document.querySelectorAll(".menores .imgMenor img");

smallerImages.forEach((smallerImage) => {

  smallerImage.addEventListener("click", () => {

    mainImage.src = smallerImage.src;

  });

});

const closeVar = document.getElementById("closeVar");
const selectScreen = document.getElementsByClassName("SelectVariation")[0];
const openSelect = document.getElementsByClassName("add")[0];

openSelect.addEventListener("click", function () {
    selectScreen.style.display = "flex";
});
closeVar.addEventListener("click", function () {
    selectScreen.style.display = "none";
});