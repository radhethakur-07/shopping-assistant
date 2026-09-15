/**
 * SmartCart Frontend Configuration
 * 
 * INSTRUCTIONS FOR DEPLOYMENT:
 * 1. When running on Render / GitHub Pages / Static Hosting, replace the RENDER_BACKEND_URL below
 *    with your deployed Render Backend URL (e.g. "https://smartcart-backend.onrender.com").
 * 2. When testing on localhost (127.0.0.1 or localhost), it automatically connects to "http://127.0.0.1:8000".
 */

(function () {
  // SET YOUR RENDER BACKEND URL HERE:
  const RENDER_BACKEND_URL = "https://shopping-assistant-14da.onrender.com";

  // Auto-detect local development vs deployed production environment
  const isLocal =
    window.location.hostname === "localhost" ||
    window.location.hostname === "127.0.0.1" ||
    window.location.protocol === "file:";

  const defaultApiUrl = isLocal ? "http://127.0.0.1:8000" : RENDER_BACKEND_URL;

  window.APP_CONFIG = {
    API_BASE_URL: window.APP_CONFIG?.API_BASE_URL || defaultApiUrl,
    APP_NAME: "SmartCart",
    CURRENCY_SYMBOL: "$",
    FREE_SHIPPING_THRESHOLD: 35.0,
  };
})();
