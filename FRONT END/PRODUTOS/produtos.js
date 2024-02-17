const limiteDePalavrasD = 8;
const limiteDePalavrasT = 5;
const descricao = document.getElementById("descricao");
const titulo = document.getElementById("titulo");
const palavrasD = descricao.innerText.split(" ");
const palavrasT = titulo.innerText.split(" ");
if (palavrasD.length > limiteDePalavrasD) {
    let cortadaDescricao =
        palavrasD.slice(0, limiteDePalavrasD).join(" ") + "...";
    descricao.innerText = cortadaDescricao;
}
if (palavrasT.length > limiteDePalavrasT) {
    let cortadoTitulo =
        palavrasT.slice(0, limiteDePalavrasT).join(" ") + "...";
    titulo.innerText = cortadoTitulo;
}