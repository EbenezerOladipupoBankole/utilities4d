document.addEventListener("DOMContentLoaded", function () {
  const container = document.getElementById('products-container');
  if (!container || !window.products) return;

  const maxVisible = 6;
  let showingAll = false;

  function renderProducts() {
    let html = "";
    const toShow = showingAll ? products : products.slice(0, maxVisible);
    toShow.forEach(product => {
      html += `
        <div class="bg-white rounded-lg shadow-lg overflow-hidden hover:shadow-xl transition">
          <img src="${product.image}" alt="${product.name} interface for Dragon speech recognition" class="w-full h-48 object-cover" />
          <div class="p-6">
            <h3 class="text-xl font-semibold mb-2">${product.name}</h3>
            <p class="text-gray-700 mb-2">Price: <strong>${product.price}</strong></p>
            <p class="text-gray-700 mb-4">${product.description}</p>
            <a href="${product.url}" class="text-blue-600 hover:underline font-semibold">Explore now</a>
          </div>
        </div>
      `;
    });

    // Add See More button if needed
    if (!showingAll && products.length > maxVisible) {
      html += `
        <div class="flex justify-center items-center col-span-full mt-6">
          <button id="seeMoreBtn" class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition font-semibold focus:outline-none focus:ring-2 focus:ring-blue-500">
            See More
          </button>
        </div>
      `;
    }

    container.innerHTML = html;

    // Add event listener for See More button
    const seeMoreBtn = document.getElementById('seeMoreBtn');
    if (seeMoreBtn) {
      seeMoreBtn.addEventListener('click', function () {
        showingAll = true;
        renderProducts();
      });
    }
  }

  renderProducts();
}); 