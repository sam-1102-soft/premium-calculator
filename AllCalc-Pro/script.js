const state = { theme: localStorage.getItem('allcalc-theme') || 'light', favorites: JSON.parse(localStorage.getItem('allcalc-favorites') || '[]'), history: JSON.parse(localStorage.getItem('allcalc-history') || '[]') };
function showToast(message) { const container = document.getElementById('toast-container'); if (!container) return; const toast = document.createElement('div'); toast.className = 'toast'; toast.textContent = message; container.appendChild(toast); setTimeout(() => toast.remove(), 2200); }
function applyTheme(theme) { document.documentElement.setAttribute('data-theme', theme); const button = document.getElementById('theme-toggle'); if (button) button.textContent = theme === 'dark' ? '☀️' : '🌙'; }
function toggleTheme() { state.theme = state.theme === 'dark' ? 'light' : 'dark'; localStorage.setItem('allcalc-theme', state.theme); applyTheme(state.theme); showToast(state.theme === 'dark' ? 'Dark mode enabled' : 'Light mode enabled'); }
function handleRipple(event) { const button = event.currentTarget; const rect = button.getBoundingClientRect(); const ripple = document.createElement('span'); ripple.className = 'ripple'; ripple.style.left = `${event.clientX - rect.left}px`; ripple.style.top = `${event.clientY - rect.top}px`; button.appendChild(ripple); setTimeout(() => ripple.remove(), 600); }
function animateCounters() { document.querySelectorAll('.counter').forEach((counter) => { const target = Number(counter.dataset.target || 0); const duration = 1200; const start = performance.now(); const step = (now) => { const progress = Math.min((now - start) / duration, 1); counter.textContent = Math.floor(progress * target).toString(); if (progress < 1) requestAnimationFrame(step); }; requestAnimationFrame(step); }); }
function filterCalculators(term) { document.querySelectorAll('.calculator-card').forEach((card) => { const text = `${card.dataset.name} ${card.dataset.category}`.toLowerCase(); card.style.display = text.includes(term.toLowerCase()) ? 'grid' : 'none'; }); }
function renderFavorites() { const container = document.getElementById('favorites-list'); if (!container) return; if (!state.favorites.length) { container.innerHTML = '<li>No favorites yet.</li>'; return; } container.innerHTML = state.favorites.map((item) => `<li>${item}</li>`).join(''); }
function renderHistory() { const container = document.getElementById('recent-list'); if (!container) return; if (!state.history.length) { container.innerHTML = '<li>No recent calculations yet.</li>'; return; } container.innerHTML = state.history.slice(0, 5).map((item) => `<li>${item.title}: ${item.result}</li>`).join(''); }
function addHistory(title, result) { state.history.unshift({ title, result, time: new Date().toLocaleString() }); state.history = state.history.slice(0, 8); localStorage.setItem('allcalc-history', JSON.stringify(state.history)); renderHistory(); }
function toggleFavorite(id) { const index = state.favorites.indexOf(id); if (index >= 0) { state.favorites.splice(index, 1); showToast('Removed from favorites'); } else { state.favorites.push(id); showToast('Added to favorites'); } localStorage.setItem('allcalc-favorites', JSON.stringify(state.favorites)); renderFavorites(); }
function initHomePage() { 
    applyTheme(state.theme);
    renderFavorites();
    renderHistory();
    animateCounters();

    const search = document.getElementById('search');
    if (search) {
        search.addEventListener('input', (event) => filterCalculators(event.target.value));
    }

    document.querySelectorAll('.chip').forEach((chip) => {
        chip.addEventListener('click', () => {
            document.querySelectorAll('.chip').forEach((item) => item.classList.remove('is-active'));
            chip.classList.add('is-active');
            const filter = chip.dataset.filter;
            document.querySelectorAll('.calculator-card').forEach((card) => {
                const matches = filter === 'all' || card.dataset.category === filter;
                card.style.display = matches ? 'grid' : 'none';
            });
        });
    });

    document.querySelectorAll('.favorite-btn').forEach((button) => {
        button.addEventListener('click', (event) => {
            event.preventDefault();
            const id = button.dataset.fav || button.closest('.calculator-card').dataset.name;
            toggleFavorite(id);
            button.textContent = state.favorites.includes(id) ? '★' : '☆';
        });
    });

    document.querySelectorAll('.btn').forEach((button) => button.addEventListener('click', handleRipple));

    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach((item) => {
        item.addEventListener('toggle', () => {
            if (item.open) {
                faqItems.forEach((other) => {
                    if (other !== item) other.open = false;
                });
            }
        });
    });

    const backToTop = document.querySelector('.back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', () => backToTop.classList.toggle('show', window.scrollY > 300));
        backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    }

    document.addEventListener('keydown', (event) => {
        if (event.key === '/') {
            event.preventDefault();
            const search = document.getElementById('search');
            if (search) search.focus();
        }
        if (event.key.toLowerCase() === 't') toggleTheme();
    });

    document.querySelector('.fab')?.addEventListener('click', () => showToast('Quick actions ready.'));
}

window.addEventListener('DOMContentLoaded', () => {
	if (document.body.dataset.page) {
		if (typeof window.initCalculatorPage === 'function') window.initCalculatorPage();
	} else {
		initHomePage();
	}
});