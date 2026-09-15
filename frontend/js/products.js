/**
 * SmartCart Products Catalog Controller
 */

(function () {
  let allProducts = [];
  let currentCategory = "All";
  let searchQuery = "";
  let currentSort = "default";

  const CATEGORIES = [
    "All",
    "Fruits",
    "Vegetables",
    "Dairy",
    "Bakery",
    "Beverages",
    "Snacks",
    "Grains",
    "Personal Care",
    "Household",
    "Frozen Food",
  ];

  function init() {
    renderCategoryFilters();
    bindEvents();
    parseUrlParams();
    fetchAndDisplayProducts();
  }

  function parseUrlParams() {
    const urlParams = new URLSearchParams(window.location.search);
    const cat = urlParams.get("category");
    const q = urlParams.get("q");

    if (cat && CATEGORIES.includes(cat)) {
      currentCategory = cat;
    }
    if (q) {
      searchQuery = q;
      const searchInput = document.getElementById("product-search-input");
      if (searchInput) searchInput.value = q;
    }
  }

  function renderCategoryFilters() {
    const filterContainer = document.getElementById("category-filter-bar");
    if (!filterContainer) return;

    filterContainer.innerHTML = "";
    CATEGORIES.forEach((cat) => {
      const pill = document.createElement("button");
      pill.className = `category-filter-pill ${cat === currentCategory ? "active" : ""}`;

      let iconHtml = "";
      if (cat !== "All" && CATEGORY_META[cat]) {
        iconHtml = `<i class="${CATEGORY_META[cat].icon}"></i> `;
      } else if (cat === "All") {
        iconHtml = `<i class="fa-solid fa-border-all"></i> `;
      }

      pill.innerHTML = `${iconHtml}${cat}`;
      pill.addEventListener("click", () => {
        document.querySelectorAll(".category-filter-pill").forEach((el) => el.classList.remove("active"));
        pill.classList.add("active");
        currentCategory = cat;
        fetchAndDisplayProducts();
      });
      filterContainer.appendChild(pill);
    });
  }

  function bindEvents() {
    const searchInput = document.getElementById("product-search-input");
    if (searchInput) {
      searchInput.addEventListener(
        "input",
        debounce((e) => {
          searchQuery = e.target.value.trim();
          fetchAndDisplayProducts();
        }, 300)
      );
    }

    const sortSelect = document.getElementById("product-sort-select");
    if (sortSelect) {
      sortSelect.addEventListener("change", (e) => {
        currentSort = e.target.value;
        sortAndRenderProducts();
      });
    }
  }

  async function fetchAndDisplayProducts() {
    const grid = document.getElementById("products-grid");
    const countEl = document.getElementById("product-count-display");
    if (!grid) return;

    grid.innerHTML = `
      <div class="skeleton-card"></div>
      <div class="skeleton-card"></div>
      <div class="skeleton-card"></div>
      <div class="skeleton-card"></div>
    `;

    try {
      if (searchQuery) {
        allProducts = await API.searchProducts(searchQuery);
        if (currentCategory !== "All") {
          allProducts = allProducts.filter(
            (p) => p.category.toLowerCase() === currentCategory.toLowerCase()
          );
        }
      } else if (currentCategory !== "All") {
        allProducts = await API.getProductsByCategory(currentCategory);
      } else {
        allProducts = await API.getProducts();
      }

      if (countEl) {
        countEl.textContent = `Showing ${allProducts.length} ${allProducts.length === 1 ? "product" : "products"}`;
      }

      sortAndRenderProducts();
    } catch (err) {
      console.error("[Products] Error fetching products:", err);
      grid.innerHTML = `
        <div class="empty-state" style="grid-column: 1 / -1;">
          <div class="empty-state-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
          <h3>Unable to Load Products</h3>
          <p>Please ensure the backend service is running and accessible.</p>
          <button class="btn-primary" style="max-width: 200px; margin: 0 auto;" onclick="window.location.reload()">
            <i class="fa-solid fa-rotate"></i> Retry
          </button>
        </div>
      `;
    }
  }

  function sortAndRenderProducts() {
    const grid = document.getElementById("products-grid");
    if (!grid) return;

    let sorted = [...allProducts];

    if (currentSort === "price-asc") {
      sorted.sort((a, b) => a.price - b.price);
    } else if (currentSort === "price-desc") {
      sorted.sort((a, b) => b.price - a.price);
    } else if (currentSort === "rating-desc") {
      sorted.sort((a, b) => b.rating - a.rating);
    } else if (currentSort === "name-asc") {
      sorted.sort((a, b) => a.name.localeCompare(b.name));
    }

    grid.innerHTML = "";

    if (sorted.length === 0) {
      grid.innerHTML = `
        <div class="empty-state" style="grid-column: 1 / -1;">
          <div class="empty-state-icon"><i class="fa-solid fa-magnifying-glass"></i></div>
          <h3>No matching products found</h3>
          <p>Try clearing your search or switching categories.</p>
          <button class="btn-primary" style="max-width: 220px; margin: 0 auto;" onclick="window.location.href='products.html'">
            <i class="fa-solid fa-border-all"></i> View All Products
          </button>
        </div>
      `;
      return;
    }

    sorted.forEach((product) => {
      const card = createProductCard(product);
      grid.appendChild(card);
    });
  }

  function createProductCard(product) {
    const card = document.createElement("div");
    card.className = "product-card";

    const isOutOfStock = product.stock_quantity <= 0;
    const stockBadge = isOutOfStock
      ? `<span style="color: var(--danger); font-size: 0.75rem; font-weight: 700;">Out of Stock</span>`
      : `<span style="color: var(--gray-500); font-size: 0.75rem;">${product.stock_quantity} available</span>`;

    card.innerHTML = `
      <div class="product-img-wrap">
        <img src="${product.image_url || 'https://images.unsplash.com/photo-1542838132-92c53300491e?w=600'}" alt="${product.name}" loading="lazy" />
        <span class="product-cat-tag">${product.category}</span>
      </div>
      <div class="product-body">
        <div class="product-brand">${product.brand || 'Groceries'}</div>
        <h3 class="product-title" title="${product.name}">${product.name}</h3>
        <div class="product-unit">${product.unit}</div>
        
        <div class="product-rating">
          <i class="fa-solid fa-star"></i>
          <span class="rating-num">${product.rating.toFixed(1)}</span>
          <span style="margin-left: auto;">${stockBadge}</span>
        </div>

        <p style="font-size: 0.8rem; color: var(--gray-600); margin-bottom: 0.75rem; line-height: 1.4; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
          ${product.description || ''}
        </p>

        <div class="product-bottom">
          <div class="product-price">${formatCurrency(product.price)}</div>
          <div class="product-actions">
            <button class="btn-icon" title="Add to Shopping List" onclick="handleQuickAddToList(${product.id}, '${product.name.replace(/'/g, "\\'")}')">
              <i class="fa-solid fa-list-check"></i>
            </button>
            <button class="btn-icon btn-add-cart" ${isOutOfStock ? 'disabled style="opacity: 0.5; cursor: not-allowed;"' : ''} title="Add to Cart" onclick="handleQuickAddToCart(${product.id}, '${product.name.replace(/'/g, "\\'")}')">
              <i class="fa-solid fa-cart-plus"></i>
            </button>
          </div>
        </div>
      </div>
    `;

    return card;
  }

  document.addEventListener("DOMContentLoaded", init);
})();
