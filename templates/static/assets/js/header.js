const cartIcon = document.querySelector("#cartIcon");
const cart = document.querySelector("#cart");
const cartContent = document.querySelector(".cart-content");
const x = document.querySelector("#closeCart");

cartIcon.addEventListener("click", function () {
    cart.style.display = "flex";
    cartContent.classList.remove("slideOutRight");
    cartContent.classList.add("slideInRight");
});

x.addEventListener("click", function () {
    cartContent.classList.remove("slideInRight");
    cartContent.classList.add("slideOutRight");
    setTimeout(() => {
        cart.style.display = "none";
    }, 500);
});

const menuIcon = document.querySelector("#menuIcon");
const menu = document.querySelector("#menu");
const menuContent = document.querySelector(".menu-content");
const x2 = document.querySelector("#closemenu");

menuIcon.addEventListener("click", function () {
    menu.style.display = "flex";
    menuContent.classList.remove("slideOutRight");
    menuContent.classList.add("slideInRight");
});

x2.addEventListener("click", function () {
    menuContent.classList.remove("slideInRight");
    menuContent.classList.add("slideOutRight");
    setTimeout(() => {
        menu.style.display = "none";
    }, 500);
});

const select = document.getElementById("cores");
select.addEventListener("change", () => {
    const theme = select.value;

    document.body.setAttribute("data-theme", theme);
});
select.dispatchEvent(new Event("change"));

const loginIcon = document.querySelector("#loginIcon");
const login = document.querySelector("#login");
const loginContent = document.querySelector(".login-content");
const x3 = document.querySelector("#closelogin");

loginIcon.addEventListener("click", function () {
    login.style.display = "flex";
    loginContent.classList.remove("slideOutRight");
    loginContent.classList.add("slideInRight");
});

x3.addEventListener("click", function () {
    loginContent.classList.remove("slideInRight");
    loginContent.classList.add("slideOutRight");
    setTimeout(() => {
        login.style.display = "none";
    }, 500);
});

// mover o titulo do input para fora

const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const emailLabel = document.querySelector(".email p");
const passwordLabel = document.querySelector(".password p");

emailInput.addEventListener("focus", () => {
    emailLabel.parentElement.classList.add("focus");
});

emailInput.addEventListener("blur", () => {
    if (emailInput.value === "") {
        emailLabel.parentElement.classList.remove("focus");
    }
});

passwordInput.addEventListener("focus", () => {
    passwordLabel.parentElement.classList.add("focus");
});

passwordInput.addEventListener("blur", () => {
    if (passwordInput.value === "") {
        passwordLabel.parentElement.classList.remove("focus");
    }
});

// senha visivel e inviaivel
const eyeOn = document.getElementById("eyeOn");
const eyeOf = document.getElementById("eyeOf");

function showPassword() {
    passwordInput.type = "text";
    eyeOn.style.display = "none";
    eyeOf.style.display = "flex";
}

function hidePassword() {
    passwordInput.type = "password";
    eyeOn.style.display = "flex";
    eyeOf.style.display = "none";
}

document.getElementById("irCadastro").addEventListener("click", function () {
    window.location.href = "/FRONT-END/LOGIN/login.html";
});

/*
document.querySelector(".logo").addEventListener("click", function () {
    location.reload();
});
*/
