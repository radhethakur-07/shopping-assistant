/**
 * SmartCart REST API Client Wrapper
 * Handles all network requests via Fetch API with unified error handling.
 */

const API = (function () {
  const getBaseUrl = () => {
    return (window.APP_CONFIG && window.APP_CONFIG.API_BASE_URL) || "http://127.0.0.1:8000";
  };

  /**
   * Generic Fetch wrapper with JSON parsing and standardized error handling.
   */
  async function request(endpoint, options = {}) {
    const baseUrl = getBaseUrl().replace(/\/$/, "");
    const url = `${baseUrl}${endpoint}`;

    const defaultHeaders = {
      "Content-Type": "application/json",
      Accept: "application/json",
    };

    const config = {
      ...options,
      headers: {
        ...defaultHeaders,
        ...options.headers,
      },
    };

    try {
      const response = await fetch(url, config);

      // Handle non-JSON responses gracefully
      const contentType = response.headers.get("content-type");
      const isJson = contentType && contentType.includes("application/json");
      const data = isJson ? await response.json() : await response.text();

      if (!response.ok) {
        const errorMsg =
          (data && (data.detail || data.message || data.error)) ||
          `Request failed with status ${response.status}`;
        throw new Error(errorMsg);
      }

      return data;
    } catch (error) {
      console.error(`[API Error] ${options.method || "GET"} ${url}:`, error);
      throw error;
    }
  }

  return {
    // ------------------------------------------------------------------------
    // Product Endpoints
    // ------------------------------------------------------------------------
    async getProducts({ skip = 0, limit = 100, category = null } = {}) {
      let query = `?skip=${skip}&limit=${limit}`;
      if (category && category !== "All") {
        query += `&category=${encodeURIComponent(category)}`;
      }
      return request(`/api/products${query}`);
    },

    async getProduct(id) {
      return request(`/api/products/${id}`);
    },

    async searchProducts(searchTerm) {
      return request(`/api/products/search?q=${encodeURIComponent(searchTerm)}`);
    },

    async getProductsByCategory(category) {
      return request(`/api/products/category/${encodeURIComponent(category)}`);
    },

    // ------------------------------------------------------------------------
    // Cart Endpoints
    // ------------------------------------------------------------------------
    async getCart(cartId = 1) {
      return request(`/api/cart?cart_id=${cartId}`);
    },

    async addToCart(productId, quantity = 1, cartId = 1) {
      return request(`/api/cart/items?cart_id=${cartId}`, {
        method: "POST",
        body: JSON.stringify({ product_id: productId, quantity }),
      });
    },

    async updateCartItem(itemId, quantity, cartId = 1) {
      return request(`/api/cart/items/${itemId}?cart_id=${cartId}`, {
        method: "PUT",
        body: JSON.stringify({ quantity }),
      });
    },

    async removeCartItem(itemId, cartId = 1) {
      return request(`/api/cart/items/${itemId}?cart_id=${cartId}`, {
        method: "DELETE",
      });
    },

    async clearCart(cartId = 1) {
      return request(`/api/cart?cart_id=${cartId}`, {
        method: "DELETE",
      });
    },

    // ------------------------------------------------------------------------
    // Shopping List Endpoints
    // ------------------------------------------------------------------------
    async getShoppingList(listId = 1) {
      return request(`/api/shopping-list?list_id=${listId}`);
    },

    async addToShoppingList(productId, quantity = 1, listId = 1) {
      return request(`/api/shopping-list/items?list_id=${listId}`, {
        method: "POST",
        body: JSON.stringify({ product_id: productId, quantity }),
      });
    },

    async updateShoppingListItem(itemId, quantity, purchased = null, listId = 1) {
      const body = {};
      if (quantity !== null) body.quantity = quantity;
      if (purchased !== null) body.purchased = purchased;

      return request(`/api/shopping-list/items/${itemId}?list_id=${listId}`, {
        method: "PUT",
        body: JSON.stringify(body),
      });
    },

    async togglePurchased(itemId, purchased, listId = 1) {
      return request(`/api/shopping-list/items/${itemId}/purchased?list_id=${listId}`, {
        method: "PATCH",
        body: JSON.stringify({ purchased }),
      });
    },

    async removeShoppingListItem(itemId, listId = 1) {
      return request(`/api/shopping-list/items/${itemId}?list_id=${listId}`, {
        method: "DELETE",
      });
    },

    async clearShoppingList(listId = 1) {
      return request(`/api/shopping-list?list_id=${listId}`, {
        method: "DELETE",
      });
    },

    // ------------------------------------------------------------------------
    // Recommendations Endpoint
    // ------------------------------------------------------------------------
    async getRecommendations({ cartId = 1, shoppingListId = null, limit = 8 } = {}) {
      let query = `?limit=${limit}`;
      if (cartId) query += `&cart_id=${cartId}`;
      if (shoppingListId) query += `&shopping_list_id=${shoppingListId}`;
      return request(`/api/recommendations${query}`);
    },

    // ------------------------------------------------------------------------
    // System Health Endpoint
    // ------------------------------------------------------------------------
    async getHealth() {
      return request("/health");
    },
  };
})();
