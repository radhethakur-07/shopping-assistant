/**
 * SmartCart Shopping List Controller
 */

(function () {
  let allCatalogProducts = [];

  async function loadShoppingList() {
    const container = document.getElementById("shopping-list-items");
    const progressCountEl = document.getElementById("list-progress-count");
    const progressPctEl = document.getElementById("list-progress-percentage");
    const progressBarFill = document.getElementById("list-progress-fill");

    if (!container) return;

    try {
      const data = await API.getShoppingList();
      const items = data.items || [];

      // Update Progress
      const total = items.length;
      const purchased = items.filter((i) => i.purchased).length;
      const pct = total > 0 ? Math.round((purchased / total) * 100) : 0;

      if (progressCountEl) progressCountEl.textContent = `${purchased} of ${total} items checked off`;
      if (progressPctEl) progressPctEl.textContent = `${pct}%`;
      if (progressBarFill) progressBarFill.style.width = `${pct}%`;

      if (items.length === 0) {
        container.innerHTML = `
          <div class="empty-state">
            <div class="empty-state-icon"><i class="fa-solid fa-clipboard-list"></i></div>
            <h3>Your Shopping List is Empty</h3>
            <p>Plan your grocery trip efficiently by adding items you need.</p>
            <a href="products.html" class="btn-primary" style="display: inline-flex; max-width: 220px; margin: 0 auto;">
              <i class="fa-solid fa-plus"></i> Browse Products
            </a>
          </div>
        `;

        Recommendations.load({
          containerId: "list-recommendations-grid",
          shoppingListId: 1,
          limit: 4,
          titleId: "list-rec-title",
        });
        return;
      }

      container.innerHTML = "";
      items.forEach((item) => {
        const row = createListItemRow(item);
        container.appendChild(row);
      });

      updateHeaderBadges();

      // Load List-based Recommendations
      Recommendations.load({
        containerId: "list-recommendations-grid",
        shoppingListId: 1,
        limit: 4,
        titleId: "list-rec-title",
      });
    } catch (err) {
      console.error("[Shopping List] Error loading list:", err);
      container.innerHTML = `
        <div class="empty-state">
          <div class="empty-state-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
          <h3>Failed to load shopping list</h3>
          <p>${err.message || 'Please check your connection and try again.'}</p>
        </div>
      `;
    }
  }

  function createListItemRow(item) {
    const p = item.product;
    const row = document.createElement("div");
    row.className = "list-item-row";

    row.innerHTML = `
      <div class="list-item-left">
        <div class="custom-checkbox ${item.purchased ? 'checked' : ''}" onclick="ShoppingListController.toggleItem(${item.id}, ${!item.purchased})" title="Mark purchased">
          <i class="fa-solid fa-check"></i>
        </div>
        <img src="${p.image_url || 'https://images.unsplash.com/photo-1542838132-92c53300491e?w=600'}" alt="${p.name}" style="width: 48px; height: 48px; border-radius: 8px; object-fit: cover;" />
        <div>
          <div class="list-item-title ${item.purchased ? 'purchased' : ''}">${p.name}</div>
          <div style="font-size: 0.8rem; color: var(--gray-500);">${p.brand || 'Groceries'} • ${p.unit} • ${formatCurrency(p.price)}</div>
        </div>
      </div>
      <div class="list-item-right">
        <span style="font-weight: 700; font-size: 0.9rem; background: var(--gray-100); padding: 0.25rem 0.6rem; border-radius: 6px;">
          Qty: ${item.quantity}
        </span>
        <button class="btn-icon btn-add-cart" title="Move to Cart" onclick="ShoppingListController.moveToCart(${item.id}, ${p.id}, '${p.name.replace(/'/g, "\\'")}')">
          <i class="fa-solid fa-cart-arrow-down"></i>
        </button>
        <button class="cart-remove-btn" title="Remove item" onclick="ShoppingListController.removeItem(${item.id}, '${p.name.replace(/'/g, "\\'")}')">
          <i class="fa-solid fa-trash-can"></i>
        </button>
      </div>
    `;

    return row;
  }

  async function populateQuickAddDropdown() {
    const select = document.getElementById("quick-add-product-select");
    if (!select) return;

    try {
      allCatalogProducts = await API.getProducts({ limit: 100 });
      select.innerHTML = '<option value="">-- Choose a product to add --</option>';
      allCatalogProducts.forEach((prod) => {
        const opt = document.createElement("option");
        opt.value = prod.id;
        opt.textContent = `${prod.name} (${prod.category}) - ${formatCurrency(prod.price)}`;
        select.appendChild(opt);
      });
    } catch (err) {
      console.debug("[Shopping List] Quick-add dropdown fetch failed:", err);
    }
  }

  window.ShoppingListController = {
    async toggleItem(itemId, newStatus) {
      try {
        await API.togglePurchased(itemId, newStatus);
        loadShoppingList();
      } catch (err) {
        showToast(err.message || "Failed to update item status.", "error");
      }
    },

    async removeItem(itemId, productName) {
      try {
        await API.removeShoppingListItem(itemId);
        showToast(`Removed "${productName}" from shopping list.`, "info");
        loadShoppingList();
      } catch (err) {
        showToast(err.message || "Failed to remove item.", "error");
      }
    },

    async clearAll() {
      if (!confirm("Are you sure you want to clear your entire shopping list?")) return;
      try {
        await API.clearShoppingList();
        showToast("Shopping list cleared.", "info");
        loadShoppingList();
      } catch (err) {
        showToast(err.message || "Failed to clear list.", "error");
      }
    },

    async moveToCart(listItemId, productId, productName) {
      try {
        await API.addToCart(productId, 1);
        await API.togglePurchased(listItemId, true);
        showToast(`Moved "${productName}" to cart!`, "success");
        loadShoppingList();
      } catch (err) {
        showToast(err.message || "Failed to transfer item to cart.", "error");
      }
    },

    async handleQuickAddForm(e) {
      e.preventDefault();
      const select = document.getElementById("quick-add-product-select");
      const qtyInput = document.getElementById("quick-add-qty-input");
      const prodId = parseInt(select.value, 10);
      const qty = parseInt(qtyInput.value, 10) || 1;

      if (!prodId) {
        showToast("Please select a product to add.", "error");
        return;
      }

      try {
        await API.addToShoppingList(prodId, qty);
        showToast("Product added to shopping list!", "success");
        select.value = "";
        qtyInput.value = "1";
        loadShoppingList();
      } catch (err) {
        showToast(err.message || "Failed to add item.", "error");
      }
    },
  };

  document.addEventListener("DOMContentLoaded", () => {
    loadShoppingList();
    populateQuickAddDropdown();
    window.addEventListener("list-updated", loadShoppingList);

    const form = document.getElementById("quick-add-form");
    if (form) {
      form.addEventListener("submit", ShoppingListController.handleQuickAddForm);
    }
  });
})();
