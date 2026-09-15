/**
 * SmartCart Global Application Utilities & State
 */

// Category icons mapping
const CATEGORY_META = {
  "Fruits": { icon: "fa-solid fa-apple-whole", color: "#ef4444" },
  "Vegetables": { icon: "fa-solid fa-carrot", color: "#f97316" },
  "Dairy": { icon: "fa-solid fa-cheese", color: "#eab308" },
  "Bakery": { icon: "fa-solid fa-bread-slice", color: "#854d0e" },
  "Beverages": { icon: "fa-solid fa-mug-hot", color: "#0284c7" },
  "Snacks": { icon: "fa-solid fa-cookie-bite", color: "#d97706" },
  "Grains": { icon: "fa-solid fa-wheat-awn", color: "#65a30d" },
  "Personal Care": { icon: "fa-solid fa-pump-soap", color: "#06b6d4" },
  "Household": { icon: "fa-solid fa-spray-can-sparkles", color: "#6366f1" },
  "Frozen Food": { icon: "fa-solid fa-snowflake", color: "#38bdf8" },
};

/**
 * Format numeric value as currency.
 */
function formatCurrency(amount) {
  const sym = (window.APP_CONFIG && window.APP_CONFIG.CURRENCY_SYMBOL) || "$";
  return `${sym}${Number(amount || 0).toFixed(2)}`;
}

/**
 * Create debounce wrapper for input handlers.
 */
function debounce(func, delay = 350) {
  let timeoutId;
  return function (...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func.apply(this, args), delay);
  };
}

/**
 * Toast Notification System
 */
function showToast(message, type = "info") {
  let container = document.getElementById("toast-container");
  if (!container) {
    container = document.createElement("div");
    container.id = "toast-container";
    document.body.appendChild(container);
  }

  const toast = document.createElement("div");
  toast.className = `toast ${type}`;

  let iconClass = "fa-solid fa-circle-info";
  if (type === "success") iconClass = "fa-solid fa-circle-check";
  if (type === "error") iconClass = "fa-solid fa-circle-exclamation";

  toast.innerHTML = `
    <i class="${iconClass}"></i>
    <span>${message}</span>
  `;

  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateX(100%)";
    setTimeout(() => {
      if (toast.parentNode) {
        toast.parentNode.removeChild(toast);
      }
    }, 300);
  }, 3500);
}

/**
 * Update Header Badge Counts for Cart and Shopping List.
 */
async function updateHeaderBadges() {
  try {
    const [cartData, listData] = await Promise.allSettled([
      API.getCart(),
      API.getShoppingList(),
    ]);

    if (cartData.status === "fulfilled" && cartData.value) {
      const cartBadge = document.getElementById("header-cart-count");
      if (cartBadge) {
        cartBadge.textContent = cartData.value.total_quantity || 0;
      }
    }

    if (listData.status === "fulfilled" && listData.value) {
      const listBadge = document.getElementById("header-list-count");
      if (listBadge) {
        const pending = listData.value.pending_items !== undefined
          ? listData.value.pending_items
          : (listData.value.items || []).filter((i) => !i.purchased).length;
        listBadge.textContent = pending || 0;
      }
    }
  } catch (err) {
    // Fail silently on header badge refresh
    console.debug("[Header Badges] Could not sync counts:", err);
  }
}

/**
 * Quick Add to Cart with Toast
 */
async function handleQuickAddToCart(productId, productName) {
  try {
    await API.addToCart(productId, 1);
    showToast(`Added "${productName}" to cart!`, "success");
    updateHeaderBadges();
    // Dispatch custom event so active pages can update if needed
    window.dispatchEvent(new CustomEvent("cart-updated"));
  } catch (err) {
    showToast(err.message || "Failed to add item to cart.", "error");
  }
}

/**
 * Quick Add to Shopping List with Toast
 */
async function handleQuickAddToList(productId, productName) {
  try {
    await API.addToShoppingList(productId, 1);
    showToast(`Added "${productName}" to your shopping list!`, "success");
    updateHeaderBadges();
    window.dispatchEvent(new CustomEvent("list-updated"));
  } catch (err) {
    showToast(err.message || "Failed to add to shopping list.", "error");
  }
}

// Global Image Error Fallback Handler to prevent any broken image display
document.addEventListener(
  "error",
  function (e) {
    if (e.target.tagName && e.target.tagName.toLowerCase() === "img") {
      e.target.onerror = null;
      e.target.src =
        "https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=600&q=80";
    }
  },
  true
);

// Global initialization
document.addEventListener("DOMContentLoaded", () => {
  // Mobile Nav Toggle
  const mobileToggle = document.getElementById("mobile-menu-toggle");
  const navLinks = document.getElementById("nav-links");
  if (mobileToggle && navLinks) {
    mobileToggle.addEventListener("click", () => {
      navLinks.classList.toggle("open");
    });
  }

  // Initial badge update
  updateHeaderBadges();
});
