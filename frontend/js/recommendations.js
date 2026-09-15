/**
 * SmartCart Recommendation Component Renderer
 */

const Recommendations = (function () {
  /**
   * Render recommendation card HTML element.
   */
  function createCardElement(recItem) {
    const { product, score, reason, recommendation_type } = recItem;
    const card = document.createElement("div");
    card.className = "product-card rec-card";

    const matchPercent = Math.round(score * 100);

    let typeBadgeIcon = "fa-solid fa-sparkles";
    if (recommendation_type === "complementary") typeBadgeIcon = "fa-solid fa-link";
    if (recommendation_type === "category_affinity") typeBadgeIcon = "fa-solid fa-layer-group";
    if (recommendation_type === "popular") typeBadgeIcon = "fa-solid fa-fire";

    card.innerHTML = `
      <div class="product-img-wrap">
        <img src="${product.image_url || 'https://images.unsplash.com/photo-1542838132-92c53300491e?w=600'}" alt="${product.name}" loading="lazy" />
        <span class="product-cat-tag">${product.category}</span>
      </div>
      <div class="product-body">
        <div class="rec-badge">
          <i class="${typeBadgeIcon}"></i>
          <span>${matchPercent}% Match</span>
        </div>
        <div class="rec-reason">
          ${reason}
        </div>
        <div class="product-brand">${product.brand || 'Groceries'}</div>
        <h3 class="product-title" title="${product.name}">${product.name}</h3>
        <div class="product-unit">${product.unit}</div>
        
        <div class="product-rating">
          <i class="fa-solid fa-star"></i>
          <span class="rating-num">${product.rating.toFixed(1)}</span>
          <span style="color: var(--gray-400); margin-left: auto; font-size: 0.75rem;">
            ${product.stock_quantity > 0 ? `${product.stock_quantity} in stock` : 'Out of Stock'}
          </span>
        </div>

        <div class="product-bottom">
          <div class="product-price">${formatCurrency(product.price)}</div>
          <div class="product-actions">
            <button class="btn-icon" title="Add to Shopping List" onclick="handleQuickAddToList(${product.id}, '${product.name.replace(/'/g, "\\'")}')">
              <i class="fa-solid fa-list-check"></i>
            </button>
            <button class="btn-icon btn-add-cart" title="Add to Cart" onclick="handleQuickAddToCart(${product.id}, '${product.name.replace(/'/g, "\\'")}')">
              <i class="fa-solid fa-cart-plus"></i>
            </button>
          </div>
        </div>
      </div>
    `;

    return card;
  }

  /**
   * Load and render smart recommendations into a target container.
   */
  async function load({ containerId, cartId = 1, shoppingListId = null, limit = 4, titleId = null }) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
      <div class="skeleton-card"></div>
      <div class="skeleton-card"></div>
      <div class="skeleton-card"></div>
      <div class="skeleton-card"></div>
    `;

    try {
      const data = await API.getRecommendations({ cartId, shoppingListId, limit });
      container.innerHTML = "";

      if (!data.recommendations || data.recommendations.length === 0) {
        container.innerHTML = `
          <div style="grid-column: 1 / -1; text-align: center; color: var(--gray-500); padding: 1.5rem;">
            No recommendations currently available. Add more items to your cart or list!
          </div>
        `;
        return;
      }

      if (titleId) {
        const titleEl = document.getElementById(titleId);
        if (titleEl) {
          if (data.context_source === "cart") {
            titleEl.textContent = "Frequently Paired with Your Cart Items";
          } else if (data.context_source === "shopping_list") {
            titleEl.textContent = "Recommended for Your Shopping List";
          } else {
            titleEl.textContent = "AI Smart Suggestions For You";
          }
        }
      }

      data.recommendations.forEach((rec) => {
        const card = createCardElement(rec);
        container.appendChild(card);
      });
    } catch (err) {
      console.error("[Recommendations] Failed to load recommendations:", err);
      container.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; color: var(--gray-500); padding: 1rem;">
          Suggestions will appear once items are added.
        </div>
      `;
    }
  }

  return {
    load,
    createCardElement,
  };
})();
