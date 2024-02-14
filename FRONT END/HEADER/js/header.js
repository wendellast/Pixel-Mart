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
