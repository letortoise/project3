document.addEventListener('DOMContentLoaded', () => {

    // Add item to cart when user clicks 'add' button
    buttons = document.querySelectorAll('.add');
    buttons.forEach(button => {
        button.onclick = function() {
            // Get item info
            const parent = this.parentElement;
            const name = parent.dataset.name;
            const id = parent.dataset.value;

            // Add item to the cart
            if (!localStorage.getItem('cart')) {
                const cart = JSON.stringify([new CartItem(id, name)]);
                console.log(cart);
                localStorage.setItem('cart', cart);
            }
            else {
                const cart = JSON.parse(localStorage.getItem('cart'));
                cart.push(new CartItem(id, name));
                localStorage.setItem('cart', JSON.stringify(cart));
                console.log(localStorage.getItem('cart'));
            }

        };
    });

});

function CartItem(id, name, extras) {
    this.id = id;
    this.name = name;
    this.extras = extras;
}

// document.addEventListener('click', e => {
//     const element = e.target;
//     console.log(element.className);
//     if (element.className === 'add') {
//         // Get info about parent element
//         parent = element.parentElement;
//         pk = parent.data.pk;
//         console.log(pk);
//     }
// });
