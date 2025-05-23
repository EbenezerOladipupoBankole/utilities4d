document.addEventListener("DOMContentLoaded", () => {
  if (getCookie("cookie_consent") === "accepted") {
    initializeAnalytics();
    return;
  }
  if (getCookie("cookie_consent")) return;

  const banner = document.createElement("div");
  banner.className = "cookie-banner fade-in";
  banner.setAttribute("role", "dialog");
  banner.setAttribute("aria-labelledby", "cookie-banner-title");
  banner.innerHTML = `
      <div class="cookie-content">
        <div>
          <h3 id="cookie-banner-title">We use cookies</h3>
          <p>We use cookies for analytics. See our <a href="./privacy-policy.html" class="text-blue-400 hover:underline">cookie policy</a>.</p>
        </div>
        <div class="flex gap-4">
          <button class="cookie-accept">Accept</button>
          <button class="cookie-decline">Decline</button>
        </div>
      </div>`;

  document.body.appendChild(banner);

  banner.querySelector(".cookie-accept").addEventListener("click", () => {
    setCookie("cookie_consent", "accepted", 365);
    fadeOutBanner(banner);
    initializeAnalytics();
  });

  banner.querySelector(".cookie-decline").addEventListener("click", () => {
    setCookie("cookie_consent", "declined", 365);
    fadeOutBanner(banner);
  });
});

function fadeOutBanner(el) {
  el.classList.replace("fade-in", "fade-out");
  setTimeout(() => el.remove(), 500);
}

function setCookie(name, value, days) {
  const expires = new Date(Date.now() + days * 864e5).toUTCString();
  document.cookie = `${name}=${value}; expires=${expires}; path=/; SameSite=Lax`;
}

function getCookie(name) {
  return document.cookie
    .split("; ")
    .find((row) => row.startsWith(name + "="))
    ?.split("=")[1];
}

function initializeAnalytics() {
  window.dataLayer = window.dataLayer || [];
  function gtag() {
    dataLayer.push(arguments);
  }
  gtag("js", new Date());
  gtag("config", "YOUR_TRACKING_ID", { anonymize_ip: true });
}