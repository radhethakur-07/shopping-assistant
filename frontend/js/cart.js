/**
 * SmartCart Shopping Cart Controller
 */

(function () {
  const FREE_SHIPPING_LIMIT = (window.APP_CONFIG && window.APP_CONFIG.FREE_SHIPPING_THRESHOLD) || 35.0;

  async function loadCart() {
    const listContainer = document.getElementById("cart-items-container");
    const summarySubtotal = document.getElementById("summary-subtotal");
    const summaryTax = document.getElementById("summary-tax");
    const summaryTotal = document.getElementById("summary-total");
    const shippingTracker = document.getElementById("shipping-tracker-fill");
    const shippingText = document.getElementById("shipping-tracker-text");

    if (!listContainer) return;

    try {
      const cart = await API.getCart();

      if (!cart.items || cart.items.length === 0) {
        listContainer.innerHTML = `
          <div class="empty-state">
            <div class="empty-state-icon"><i class="fa-solid fa-cart-shopping"></i></div>
            <h3>Your Shopping Cart is Empty</h3>
            <p>Looks like you haven't added any groceries to your cart yet.</p>
            <a href="products.html" class="btn-primary" style="display: inline-flex; max-width: 220px; margin: 0 auto;">
              <i class="fa-solid fa-store"></i> Start Shopping
            </a>
          </div>
        `;

        if (summarySubtotal) summarySubtotal.textContent = formatCurrency(0);
        if (summaryTax) summaryTax.textContent = formatCurrency(0);
        if (summaryTotal) summaryTotal.textContent = formatCurrency(0);
        if (shippingTracker) shippingTracker.style.width = "0%";
        if (shippingText) shippingText.textContent = `Add ${formatCurrency(FREE_SHIPPING_LIMIT)} more for FREE delivery`;

        // Load general popular recommendations
        Recommendations.load({
          containerId: "cart-recommendations-grid",
          cartId: 1,
          limit: 4,
          titleId: "cart-rec-title",
        });
        return;
      }

      // Render Items
      listContainer.innerHTML = "";
      cart.items.forEach((item) => {
        const row = createCartItemRow(item);
        listContainer.appendChild(row);
      });

      // Update Summaries
      if (summarySubtotal) summarySubtotal.textContent = formatCurrency(cart.subtotal);
      if (summaryTax) summaryTax.textContent = formatCurrency(cart.tax);
      if (summaryTotal) summaryTotal.textContent = formatCurrency(cart.total_price);

      // Shipping Progress
      if (shippingTracker && shippingText) {
        const diff = FREE_SHIPPING_LIMIT - cart.subtotal;
        if (diff <= 0) {
          shippingTracker.style.width = "100%";
          shippingTracker.style.backgroundColor = "var(--success)";
          shippingText.innerHTML = `<strong>🎉 You've unlocked FREE Delivery!</strong>`;
        } else {
          const pct = Math.min(100, Math.round((cart.subtotal / FREE_SHIPPING_LIMIT) * 100));
          shippingTracker.style.width = `${pct}%`;
          shippingTracker.style.backgroundColor = "var(--primary)";
          shippingText.innerHTML = `Add <strong>${formatCurrency(diff)}</strong> more for <strong>FREE Delivery</strong>`;
        }
      }

      // Update header badges
      updateHeaderBadges();

      // Load Contextual Recommendations based on cart items
      Recommendations.load({
        containerId: "cart-recommendations-grid",
        cartId: 1,
        limit: 4,
        titleId: "cart-rec-title",
      });
    } catch (err) {
      console.error("[Cart] Error loading cart:", err);
      listContainer.innerHTML = `
        <div class="empty-state">
          <div class="empty-state-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
          <h3>Failed to load cart</h3>
          <p>${err.message || 'Please check your connection and try again.'}</p>
        </div>
      `;
    }
  }

  function createCartItemRow(item) {
    const p = item.product;
    const row = document.createElement("div");
    row.className = "cart-item-row";

    row.innerHTML = `
      <img src="${p.image_url || 'https://images.unsplash.com/photo-1542838132-92c53300491e?w=600'}" alt="${p.name}" class="cart-item-img" />
      <div class="cart-item-info">
        <h4>${p.name}</h4>
        <div class="cart-item-meta">${p.brand || 'Groceries'} • ${p.unit} • ${formatCurrency(p.price)}/ea</div>
      </div>
      <div class="qty-stepper">
        <button class="qty-btn" onclick="CartController.changeQty(${item.id}, ${item.quantity - 1})" title="Decrease">
          <i class="fa-solid fa-minus"></i>
        </button>
        <span class="qty-val">${item.quantity}</span>
        <button class="qty-btn" onclick="CartController.changeQty(${item.id}, ${item.quantity + 1})" title="Increase">
          <i class="fa-solid fa-plus"></i>
        </button>
      </div>
      <div class="cart-item-subtotal">
        ${formatCurrency(item.subtotal)}
      </div>
      <button class="cart-remove-btn" onclick="CartController.removeItem(${item.id}, '${p.name.replace(/'/g, "\\'")}')" title="Remove item">
        <i class="fa-solid fa-trash-can"></i>
      </button>
    `;

    return row;
  }

  window.CartController = {
    async changeQty(itemId, newQty) {
      try {
        await API.updateCartItem(itemId, newQty);
        loadCart();
      } catch (err) {
        showToast(err.message || "Failed to update quantity.", "error");
      }
    },

    async removeItem(itemId, productName) {
      try {
        await API.removeCartItem(itemId);
        showToast(`Removed "${productName}" from cart.`, "info");
        loadCart();
      } catch (err) {
        showToast(err.message || "Failed to remove item.", "error");
      }
    },

    async clearAll() {
      if (!confirm("Are you sure you want to clear your entire cart?")) return;
      try {
        await API.clearCart();
        showToast("Your cart has been cleared.", "info");
        loadCart();
      } catch (err) {
        showToast(err.message || "Failed to clear cart.", "error");
      }
    },

    checkout() {
      showToast("🎉 Order placed successfully! Thank you for testing SmartCart.", "success");
      setTimeout(async () => {
        await API.clearCart();
        loadCart();
      }, 1200);
    },
  };

  document.addEventListener("DOMContentLoaded", () => {
    loadCart();
    window.addEventListener("cart-updated", loadCart);
  });
})();
