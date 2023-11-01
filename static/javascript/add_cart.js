
// Define a function to handle the hover effect
function handleHoverEffect() {
    // Get all items on the page
    var items = document.querySelectorAll(".item");

    items.forEach(function (item) {
        item.addEventListener("mouseover", function () {
            // Create the "Add to Cart" element
            var addToCartElement = document.createElement("p");
            addToCartElement.textContent = "Add to Cart";
            addToCartElement.classList.add("add-to-cart");

            // Append the "Add to Cart" element below the description
            var description = this.querySelector(".description");
            description.insertAdjacentElement("afterend", addToCartElement);
        });

        item.addEventListener("mouseout", function () {
            // Remove the "Add to Cart" element when the mouse leaves the item
            var addToCartElement = this.querySelector(".add-to-cart");
            if (addToCartElement) {
                addToCartElement.remove();
            }
        });
    });
}



