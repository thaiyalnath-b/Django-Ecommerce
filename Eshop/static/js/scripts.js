// Cart Handling

// Add to cart

const products_container = document.getElementById('products-container');
const cart_count = document.getElementById('cart-count');

// Load current Value
async function loadCartCount() {
    const countUrl = cart_count.dataset.countUrl;
    try {
        const result = await fetch(countUrl);
        const data = await result.json();
        cart_count.innerText = data.cart_count;

    }
    catch (error) {
        console.error(`Cart count fetch error: ${error}`)
    }
}
if (cart_count) {
    loadCartCount();
}

const csrfToken = document.querySelector("[name = csrfmiddlewaretoken]").value

// Adding event listener onto product cards through their parent container

if (products_container) {
    // Add to cart url
    const addUrl = products_container.dataset.addUrl;

    products_container.addEventListener('click', async function (event) {
        if (!event.target.classList.contains('add-to-cart')) {
            return;
        }


        const btn = event.target;
        const product_card = btn.closest(".product-card");
        const productId = product_card.dataset.productId;

        btn.disabled = true;
        btn.innerText = 'Adding...'

        // try to make a POST request
        try {
            const response = await fetch(addUrl, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    'Content-type': "application/x-www-form-urlencoded"
                },

                body: `product_id=${productId}`
            })

            const data = await response.json();

            // if the backend returns 401 status,
            if (response.status === 401 && data.redirect_url) {
                window.location.href = data.redirect_url;
                return;
            }

            if (data.cart_count !== undefined) {
                cart_count.innerText = data.cart_count;
            }

        }
        catch (error) {
            console.error("Cart error:", error);
        }
        finally {
            btn.disabled = false;
            btn.innerText = 'Add to Cart';
        }
    });
}

// Increase and Decrease Functions
const cartContainer = document.querySelector('.cart-container');

if (cartContainer) {
    cartContainer.addEventListener('click', async function (e) {
        const productId = e.target.dataset.productId;
        if (!productId) return;

        let url = '';

        if (e.target.classList.contains('increase')) {
            url = '/cart/increase/';
        } else if (e.target.classList.contains('decrease')) {
            url = '/cart/decrease/';
        } else if (e.target.classList.contains('remove-btn')) {
            url = '/cart/remove/';
        } else {
            return;
        }

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `product_id=${productId}`
        });

        if (response.ok) {
            location.reload();
        }
    });
}





