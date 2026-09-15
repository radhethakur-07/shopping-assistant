/**
 * SmartCart AI Assistant Suite:
 * 1. Floating AI Grocery Chatbot ("SmartBot")
 * 2. Recipe-to-Cart Meal Kit Studio
 * 3. Cart Health & Nutrition Score Radar
 * 4. Predictive 'Did You Forget?' Reminders
 */

const SmartAssistant = (function () {
  /**
   * Initialize Floating SmartBot Chatbot in the bottom right corner of the page.
   */
  function initChatbot() {
    if (document.getElementById("smartbot-widget")) return;

    const widget = document.createElement("div");
    widget.id = "smartbot-widget";
    widget.innerHTML = `
      <!-- Trigger Button -->
      <button id="smartbot-toggle-btn" class="smartbot-toggle-btn" title="Ask AI Grocery Assistant">
        <i class="fa-solid fa-robot"></i>
        <span class="smartbot-pill-label">Ask SmartBot</span>
      </button>

      <!-- Chat Window -->
      <div id="smartbot-window" class="smartbot-window hidden">
        <div class="smartbot-header">
          <div class="smartbot-header-left">
            <div class="smartbot-avatar"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
            <div>
              <h4>SmartCart AI</h4>
              <span>Intelligent Grocery Assistant</span>
            </div>
          </div>
          <button id="smartbot-close-btn" class="smartbot-close-btn"><i class="fa-solid fa-xmark"></i></button>
        </div>

        <div class="smartbot-messages" id="smartbot-messages">
          <div class="smartbot-msg bot">
            👋 Hi! I'm your SmartCart AI Assistant. Ask me anything like:
            <div class="smartbot-chips">
              <button class="smartbot-chip" onclick="SmartAssistant.sendQuickPrompt('Healthy breakfast under $10')">🍳 Breakfast under $10</button>
              <button class="smartbot-chip" onclick="SmartAssistant.sendQuickPrompt('High protein diet staples')">💪 High Protein</button>
              <button class="smartbot-chip" onclick="SmartAssistant.sendQuickPrompt('Easy pasta dinner ingredients')">🍝 Pasta Dinner</button>
            </div>
          </div>
        </div>

        <form class="smartbot-input-form" id="smartbot-input-form">
          <input type="text" id="smartbot-input" placeholder="Ask for recipes, budget bundles, diet tips..." autocomplete="off" required />
          <button type="submit"><i class="fa-solid fa-paper-plane"></i></button>
        </form>
      </div>
    `;

    document.body.appendChild(widget);

    const toggleBtn = document.getElementById("smartbot-toggle-btn");
    const closeBtn = document.getElementById("smartbot-close-btn");
    const windowEl = document.getElementById("smartbot-window");
    const form = document.getElementById("smartbot-input-form");

    toggleBtn.addEventListener("click", () => {
      windowEl.classList.toggle("hidden");
    });

    closeBtn.addEventListener("click", () => {
      windowEl.classList.add("hidden");
    });

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const input = document.getElementById("smartbot-input");
      const userText = input.value.trim();
      if (!userText) return;
      input.value = "";
      await handleUserMessage(userText);
    });
  }

  async function handleUserMessage(text) {
    const msgContainer = document.getElementById("smartbot-messages");
    if (!msgContainer) return;

    // Append user message
    const userBubble = document.createElement("div");
    userBubble.className = "smartbot-msg user";
    userBubble.textContent = text;
    msgContainer.appendChild(userBubble);
    msgContainer.scrollTop = msgContainer.scrollHeight;

    // Typing indicator
    const typingBubble = document.createElement("div");
    typingBubble.className = "smartbot-msg bot typing";
    typingBubble.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Thinking...`;
    msgContainer.appendChild(typingBubble);
    msgContainer.scrollTop = msgContainer.scrollHeight;

    try {
      const data = await API.sendChatMessage(text);
      typingBubble.remove();

      const botBubble = document.createElement("div");
      botBubble.className = "smartbot-msg bot";

      let productsHtml = "";
      if (data.products && data.products.length > 0) {
        productsHtml = `<div class="smartbot-product-list">`;
        data.products.forEach((p) => {
          productsHtml += `
            <div class="smartbot-product-item">
              <img src="${p.image_url || 'https://images.unsplash.com/photo-1542838132-92c53300491e?w=600'}" alt="${p.name}" />
              <div class="smartbot-product-info">
                <strong>${p.name}</strong>
                <span>${formatCurrency(p.price)} • ${p.unit}</span>
              </div>
              <button class="btn-icon btn-add-cart" onclick="handleQuickAddToCart(${p.id}, '${p.name.replace(/'/g, "\\'")}')" title="Add to Cart">
                <i class="fa-solid fa-plus"></i>
              </button>
            </div>
          `;
        });
        productsHtml += `</div>`;
      }

      botBubble.innerHTML = `
        <div>${data.reply}</div>
        ${productsHtml}
      `;
      msgContainer.appendChild(botBubble);
      msgContainer.scrollTop = msgContainer.scrollHeight;
    } catch (err) {
      typingBubble.remove();
      const errBubble = document.createElement("div");
      errBubble.className = "smartbot-msg bot error";
      errBubble.textContent = "Sorry, I couldn't reach the grocery intelligence engine. Please try again.";
      msgContainer.appendChild(errBubble);
    }
  }

  /**
   * Load Recipe-to-Cart Studio into a target container.
   */
  async function loadRecipeStudio(containerId = "recipe-studio-grid") {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
      <div class="skeleton-card"></div>
      <div class="skeleton-card"></div>
    `;

    try {
      const data = await API.getSmartRecipes();
      const recipes = data.recipes || [];
      container.innerHTML = "";

      recipes.forEach((rec) => {
        const card = document.createElement("div");
        card.className = "recipe-card";

        let badgeStyle = "background: #dbeafe; color: #1e40af;";
        if (rec.is_complete) badgeStyle = "background: #dcfce7; color: #166534;";

        card.innerHTML = `
          <div class="recipe-img-wrap">
            <img src="${rec.image_url}" alt="${rec.name}" />
            <span class="recipe-cat-badge">${rec.category}</span>
          </div>
          <div class="recipe-body">
            <div class="recipe-meta-row">
              <span><i class="fa-regular fa-clock"></i> ${rec.prep_time}</span>
              <span><i class="fa-solid fa-gauge-high"></i> ${rec.difficulty}</span>
              <span class="recipe-status-pill" style="${badgeStyle}">
                ${rec.is_complete ? 'All in Cart' : `${rec.in_cart_count}/${rec.total_ingredients_count} Ingredients in Cart`}
              </span>
            </div>
            <h3 class="recipe-title">${rec.name}</h3>
            <p class="recipe-desc">${rec.description}</p>
            
            <div class="recipe-bottom">
              <div>
                <span style="font-size: 0.75rem; color: var(--gray-500); display: block;">Missing Items Bundle</span>
                <strong style="font-size: 1.15rem; color: var(--primary-dark);">${formatCurrency(rec.missing_bundle_price)}</strong>
              </div>
              <button class="btn-primary" style="width: auto; padding: 0.6rem 1.1rem; font-size: 0.9rem;" onclick="SmartAssistant.addRecipeBundle('${rec.id}')">
                <i class="fa-solid fa-cart-plus"></i> ${rec.is_complete ? 'Re-add Bundle' : '1-Click Add Missing'}
              </button>
            </div>
          </div>
        `;

        container.appendChild(card);
      });
    } catch (err) {
      container.innerHTML = `<p style="grid-column: 1 / -1; text-align: center; color: var(--gray-500);">Unable to load recipes right now.</p>`;
    }
  }

  async function addRecipeBundle(recipeId) {
    try {
      const res = await API.addRecipeToCart(recipeId);
      showToast(res.message || "Recipe ingredients added to cart!", "success");
      updateHeaderBadges();
      window.dispatchEvent(new CustomEvent("cart-updated"));
    } catch (err) {
      showToast(err.message || "Failed to add recipe bundle.", "error");
    }
  }

  /**
   * Load Cart Health & Nutrition Score Radar into a target element.
   */
  async function loadCartHealthRadar(containerId = "cart-health-radar") {
    const container = document.getElementById(containerId);
    if (!container) return;

    try {
      const data = await API.getCartHealth();
      if (!data || data.health_score === 0) {
        container.innerHTML = "";
        return;
      }

      let scoreColor = "var(--primary)";
      if (data.health_score < 50) scoreColor = "var(--accent)";
      if (data.health_score < 35) scoreColor = "var(--danger)";

      container.innerHTML = `
        <div class="health-radar-card">
          <div class="health-radar-left">
            <div class="health-score-circle" style="border-color: ${scoreColor};">
              <span class="health-score-num" style="color: ${scoreColor};">${data.health_score}</span>
              <span class="health-score-label">/ 100</span>
            </div>
            <div>
              <h4 style="font-size: 1.1rem; font-weight: 700; color: var(--gray-900); display: flex; align-items: center; gap: 0.4rem;">
                <i class="fa-solid fa-heart-pulse" style="color: var(--danger);"></i> Cart Health Radar
              </h4>
              <span style="font-size: 0.85rem; font-weight: 600; color: ${scoreColor};">${data.status_label}</span>
              <div style="font-size: 0.8rem; color: var(--gray-500); margin-top: 0.25rem;">${data.summary}</div>
            </div>
          </div>

          <div class="health-radar-bars">
            <div class="health-bar-item">
              <div class="health-bar-label"><span>🥦 Fresh Produce</span><strong>${data.produce_pct}%</strong></div>
              <div class="health-bar-track"><div class="health-bar-fill" style="width: ${data.produce_pct}%; background: #16a34a;"></div></div>
            </div>
            <div class="health-bar-item">
              <div class="health-bar-label"><span>🥩 Protein & Grains</span><strong>${data.protein_pct}%</strong></div>
              <div class="health-bar-track"><div class="health-bar-fill" style="width: ${data.protein_pct}%; background: #0284c7;"></div></div>
            </div>
            <div class="health-bar-item">
              <div class="health-bar-label"><span>🍪 Snacks / Processed</span><strong>${data.snack_pct}%</strong></div>
              <div class="health-bar-track"><div class="health-bar-fill" style="width: ${data.snack_pct}%; background: #eab308;"></div></div>
            </div>
          </div>

          <div class="health-radar-tip">
            <i class="fa-solid fa-lightbulb" style="color: var(--accent);"></i>
            <span>${data.tips[0] || 'Good nutritional balance.'}</span>
          </div>
        </div>
      `;
    } catch (err) {
      console.debug("[Cart Health] Could not load health radar:", err);
    }
  }

  /**
   * Load Predictive 'Did You Forget?' alerts in the Cart.
   */
  async function loadDidYouForget(containerId = "did-you-forget-container") {
    const container = document.getElementById(containerId);
    if (!container) return;

    try {
      const data = await API.getDidYouForget();
      const reminders = data.reminders || [];
      if (reminders.length === 0) {
        container.innerHTML = "";
        return;
      }

      container.innerHTML = "";
      reminders.forEach((rem) => {
        const p = rem.suggested_product;
        const alertEl = document.createElement("div");
        alertEl.className = "did-you-forget-banner";
        alertEl.innerHTML = `
          <div class="forget-left">
            <div class="forget-icon"><i class="fa-solid fa-bell"></i></div>
            <div>
              <strong>Did You Forget?</strong>
              <p>${rem.message}</p>
            </div>
          </div>
          <button class="btn-primary forget-add-btn" onclick="handleQuickAddToCart(${p.id}, '${p.name.replace(/'/g, "\\'")}')">
            <i class="fa-solid fa-plus"></i> Add ${p.name} (${formatCurrency(p.price)})
          </button>
        `;
        container.appendChild(alertEl);
      });
    } catch (err) {
      console.debug("[Did You Forget] Failed to fetch reminders:", err);
    }
  }

  return {
    initChatbot,
    loadRecipeStudio,
    addRecipeBundle,
    loadCartHealthRadar,
    loadDidYouForget,
    sendQuickPrompt(prompt) {
      const input = document.getElementById("smartbot-input");
      if (input) {
        input.value = prompt;
        const form = document.getElementById("smartbot-input-form");
        if (form) form.dispatchEvent(new Event("submit"));
      }
    }
  };
})();

// Auto-initialize chatbot on any page
document.addEventListener("DOMContentLoaded", () => {
  SmartAssistant.initChatbot();
});
