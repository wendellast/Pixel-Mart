let contador = 1;
const totalSlides = document.querySelectorAll(
    '.slides input[type="radio"]'
).length;
document.getElementById("radio1").checked = true;

setInterval(function () {
    proximaImagem();
}, 5000);

function proximaImagem() {
    contador++;
    if (contador > totalSlides) {
        contador = 1;
    }

    document.getElementById("radio" + contador).checked = true;
}
