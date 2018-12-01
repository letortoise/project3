
// Compile template for cart item
const item_template = Handlebars.compile(document.querySelector('#cart-item').innerHTML);

// Get cart info from localStorage
const cart = JSON.parse(localStorage.getItem('cart'));
console.log(cart);

document.addEventListener('DOMContentLoaded', () => {
    const itemsElement = document.querySelector('#items');

    if (!cart) {
        itemsElement.innerHTML = "Your Cart Is Empty";
    }
    else {
        for (let item of cart) {
            itemsElement.innerHTML += item_template({'item': item.name});
        }
    }

});

function add_item() {
    // Render the item template and display it
    const item = item_template();
    document.querySelector('#items').innerHTML += item;
}
