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
