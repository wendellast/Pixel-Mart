const limiteDePalavrasD = 50;
const descricao = document.getElementById("descricao");
const palavrasD = descricao.innerText.split(" ");
if (palavrasD.length > limiteDePalavrasD) {
    let cortadaDescricao =
        palavrasD.slice(0, limiteDePalavrasD).join(" ") + "...";
    descricao.innerText = cortadaDescricao;
}