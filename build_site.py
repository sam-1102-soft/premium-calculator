from pathlib import Path

root = Path(r"c:\Users\User\Desktop\calculator")
(root / "assets" / "logo").mkdir(parents=True, exist_ok=True)
(root / "assets" / "backgrounds").mkdir(parents=True, exist_ok=True)
(root / "assets" / "icons").mkdir(parents=True, exist_ok=True)
(root / "calculators").mkdir(parents=True, exist_ok=True)
(root / "css").mkdir(parents=True, exist_ok=True)
(root / "js").mkdir(parents=True, exist_ok=True)


def write(path, content):
    path.write_text(content, encoding="utf-8")

index_html = '''<!DOCTYPE html>
<html lang="en" data-theme="light">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>AllCalc Pro | Premium Calculator Hub</title>
    <meta name="description" content="AllCalc Pro is a premium calculator portal with science, finance, health, and utility tools." />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="loading-screen"><div class="spinner"></div><p>Loading AllCalc Pro…</p></div>
    <button class="back-to-top" aria-label="Back to top">↑</button>
    <button class="fab" aria-label="Quick actions">⚡</button>
    <div class="toast-container" id="toast-container"></div>

    <header class="topbar">
      <a class="brand" href="#">
        <span class="brand-mark">A</span>
        <span><strong>AllCalc Pro</strong><small>Premium calculator suite</small></span>
      </a>
      <nav class="top-nav" aria-label="Primary navigation">
        <a href="#featured">Featured</a>
        <a href="#categories">Categories</a>
        <a href="#faq">FAQ</a>
        <button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">🌙</button>
      </nav>
    </header>

    <aside class="sidebar" id="sidebar">
      <div class="sidebar-card">
        <h3>Explore</h3>
        <a href="#featured" class="nav-link">Featured calculators</a>
        <a href="#categories" class="nav-link">By category</a>
        <a href="#stats" class="nav-link">Live stats</a>
        <a href="#recent" class="nav-link">Recently used</a>
      </div>
      <div class="sidebar-card">
        <h3>Quick Tools</h3>
        <a href="calculators/basic.html" class="nav-link">Basic</a>
        <a href="calculators/scientific.html" class="nav-link">Scientific</a>
        <a href="calculators/emi.html" class="nav-link">Finance</a>
        <a href="calculators/length.html" class="nav-link">Converters</a>
      </div>
    </aside>

    <main class="page-shell">
      <section class="hero card">
        <div>
          <p class="eyebrow">All-in-one • Smart • Fast</p>
          <h1>Calculate with clarity, speed, and sophistication.</h1>
          <p>From scientific math to finance, health, and utility tools, AllCalc Pro delivers a polished experience for daily decisions.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="calculators/basic.html">Start calculating</a>
            <a class="btn btn-secondary" href="#featured">Explore tools</a>
          </div>
          <div class="hero-tags"><span>Glassmorphism UI</span><span>Dark/Light mode</span><span>Offline ready</span></div>
        </div>
        <div class="hero-panel">
          <div class="metric-card"><strong class="counter" data-target="38">0</strong><span>Powerful tools</span></div>
          <div class="metric-card"><strong class="counter" data-target="99">0</strong><span>Accuracy score</span></div>
          <div class="metric-card"><strong class="counter" data-target="24">0</strong><span>On-demand calculators</span></div>
        </div>
      </section>

      <section class="search-panel card">
        <label class="search-box" for="search"><span>🔍</span><input id="search" type="search" placeholder="Search calculators by name or category" /></label>
        <div class="chip-row">
          <button class="chip is-active" data-filter="all">All</button>
          <button class="chip" data-filter="Basic">Basic</button>
          <button class="chip" data-filter="Scientific">Scientific</button>
          <button class="chip" data-filter="Finance">Finance</button>
          <button class="chip" data-filter="Health">Health</button>
          <button class="chip" data-filter="Utility">Utility</button>
        </div>
      </section>

      <section id="categories" class="section">
        <div class="section-heading"><h2>Calculator categories</h2><p>Choose the right tool for your next calculation.</p></div>
        <div class="grid categories-grid">
          <a class="category-card" href="calculators/basic.html"><h3>Basic</h3><p>Arithmetic with speed and clarity</p></a>
          <a class="category-card" href="calculators/scientific.html"><h3>Scientific</h3><p>Trig, logs, factorials, memory</p></a>
          <a class="category-card" href="calculators/bmi.html"><h3>Health</h3><p>BMI, BMR, calorie and water insights</p></a>
          <a class="category-card" href="calculators/emi.html"><h3>Finance</h3><p>EMI, GST, SIP, FD, and more</p></a>
          <a class="category-card" href="calculators/cgpa.html"><h3>Education</h3><p>CGPA, GPA, attendance, and marks</p></a>
          <a class="category-card" href="calculators/length.html"><h3>Converters</h3><p>Length, weight, temperature, area, and volume</p></a>
          <a class="category-card" href="calculators/age.html"><h3>Utility</h3><p>Age, password, fuel, electricity, tip</p></a>
          <a class="category-card" href="calculators/date.html"><h3>Date</h3><p>Difference, countdown, and time tools</p></a>
        </div>
      </section>

      <section id="featured" class="section">
        <div class="section-heading"><h2>Featured calculators</h2><p>Popular tools tuned for real-world use.</p></div>
        <div class="grid calculator-grid" id="calculator-grid">
          <article class="calculator-card" data-name="Basic Calculator" data-category="Basic" data-url="calculators/basic.html"><div class="card-head"><span>➕</span><button class="favorite-btn" data-fav="basic">☆</button></div><h3>Basic calculator</h3><p>Quick arithmetic for everyday tasks.</p><a href="calculators/basic.html" class="btn btn-mini">Open</a></article>
          <article class="calculator-card" data-name="Scientific Calculator" data-category="Scientific" data-url="calculators/scientific.html"><div class="card-head"><span>🧮</span><button class="favorite-btn" data-fav="scientific">☆</button></div><h3>Scientific calculator</h3><p>Advanced operations, logs, functions, and constants.</p><a href="calculators/scientific.html" class="btn btn-mini">Open</a></article>
          <article class="calculator-card" data-name="EMI Calculator" data-category="Finance" data-url="calculators/emi.html"><div class="card-head"><span>🏦</span><button class="favorite-btn" data-fav="emi">☆</button></div><h3>EMI calculator</h3><p>Estimate your monthly installments with confidence.</p><a href="calculators/emi.html" class="btn btn-mini">Open</a></article>
          <article class="calculator-card" data-name="BMI Calculator" data-category="Health" data-url="calculators/bmi.html"><div class="card-head"><span>⚖️</span><button class="favorite-btn" data-fav="bmi">☆</button></div><h3>BMI calculator</h3><p>Check body mass index instantly.</p><a href="calculators/bmi.html" class="btn btn-mini">Open</a></article>
          <article class="calculator-card" data-name="Currency Converter" data-category="Utility" data-url="calculators/currency.html"><div class="card-head"><span>💱</span><button class="favorite-btn" data-fav="currency">☆</button></div><h3>Currency converter</h3><p>Convert across currencies in seconds.</p><a href="calculators/currency.html" class="btn btn-mini">Open</a></article>
          <article class="calculator-card" data-name="Password Generator" data-category="Utility" data-url="calculators/password.html"><div class="card-head"><span>🔐</span><button class="favorite-btn" data-fav="password">☆</button></div><h3>Password generator</h3><p>Create strong passwords instantly.</p><a href="calculators/password.html" class="btn btn-mini">Open</a></article>
        </div>
      </section>

      <section id="stats" class="section stats-grid">
        <div class="card stat-card"><h3>Recently used</h3><ul id="recent-list"></ul></div>
        <div class="card stat-card"><h3>Favorites</h3><ul id="favorites-list"></ul></div>
        <div class="card stat-card"><h3>Usage snapshot</h3><p>Everything is stored locally so your preferences and history stay ready.</p></div>
      </section>

      <section class="section"><div class="section-heading"><h2>What users say</h2><p>Trusted by students, pros, and everyday planners.</p></div><div class="grid testimonials-grid"><article class="card quote-card"><p>“The interface feels premium and the calculations are instantly reliable.”</p><strong>— Aisha, student</strong></article><article class="card quote-card"><p>“I use it daily for EMI, GST, and quick conversions.”</p><strong>— Daniel, finance analyst</strong></article><article class="card quote-card"><p>“The dark mode and speed make it my favorite calculator hub.”</p><strong>— Maya, designer</strong></article></div></section>

      <section id="faq" class="section"><div class="section-heading"><h2>Frequently asked questions</h2></div><div class="faq-list"><details class="card faq-item" open><summary>Is AllCalc Pro fully responsive?</summary><p>Yes, the app adapts beautifully for phones, tablets, and desktops.</p></details><details class="card faq-item"><summary>Does it save my history?</summary><p>Yes, your calculations and favorites are preserved locally in your browser.</p></details><details class="card faq-item"><summary>Can I share results?</summary><p>Yes, you can copy, share, print, and export your history for easy use.</p></details></div></section>
    </main>

    <footer class="footer"><p>© 2026 AllCalc Pro. Built with HTML, CSS, and Vanilla JavaScript.</p></footer>
    <script src="script.js"></script>
  </body>
</html>
'''

style_css = ''' :root {
  color-scheme: light;
  --bg: linear-gradient(135deg, #f8fbff 0%, #eef4ff 100%);
  --surface: rgba(255,255,255,0.75);
  --surface-strong: rgba(255,255,255,0.95);
  --text: #0f172a;
  --muted: #64748b;
  --border: rgba(15, 23, 42, 0.08);
  --primary: #6c63ff;
  --secondary: #00d4ff;
  --accent: #00ffb2;
  --shadow: 0 20px 50px rgba(15, 23, 42, 0.12);
  --radius: 24px;
}
:root[data-theme="dark"] {
  color-scheme: dark;
  --bg: linear-gradient(135deg, #020617 0%, #111827 100%);
  --surface: rgba(15, 23, 42, 0.76);
  --surface-strong: rgba(15, 23, 42, 0.92);
  --text: #f8fafc;
  --muted: #94a3b8;
  --border: rgba(148, 163, 184, 0.15);
  --shadow: 0 20px 50px rgba(2, 6, 23, 0.46);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; font-family: 'Poppins', sans-serif; background: var(--bg); color: var(--text); min-height: 100vh; transition: background 0.25s ease, color 0.25s ease; }
a { color: inherit; text-decoration: none; }
button, input, select, textarea { font: inherit; }
img { max-width: 100%; display: block; }
.loading-screen { position: fixed; inset: 0; background: rgba(2, 6, 23, 0.9); color: white; display: grid; place-items: center; z-index: 1000; transition: opacity 0.3s ease; }
.loading-screen.hidden { opacity: 0; pointer-events: none; }
.spinner { width: 56px; height: 56px; border: 4px solid rgba(255,255,255,0.25); border-top-color: var(--accent); border-radius: 50%; animation: spin 0.9s linear infinite; margin-bottom: 1rem; }
@keyframes spin { to { transform: rotate(360deg); } }
.topbar { position: sticky; top: 0; z-index: 800; display: flex; justify-content: space-between; align-items: center; padding: 1rem 1.25rem; backdrop-filter: blur(18px); background: rgba(255,255,255,0.44); border-bottom: 1px solid var(--border); }
:root[data-theme="dark"] .topbar { background: rgba(2, 6, 23, 0.72); }
.brand { display: flex; align-items: center; gap: 0.85rem; font-weight: 700; }
.brand-mark { display: grid; place-items: center; width: 44px; height: 44px; border-radius: 14px; color: white; background: linear-gradient(135deg, var(--primary), var(--secondary)); box-shadow: var(--shadow); }
.brand small { display: block; font-size: 0.72rem; color: var(--muted); font-weight: 500; }
.top-nav { display: flex; gap: 0.8rem; align-items: center; }
.top-nav a, .theme-toggle { padding: 0.7rem 0.95rem; border-radius: 999px; border: 1px solid transparent; background: transparent; color: var(--text); }
.top-nav a:hover, .theme-toggle:hover { background: rgba(108, 99, 255, 0.12); }
.theme-toggle { cursor: pointer; }
.page-shell { max-width: 1280px; margin: 0 auto; padding: 1rem 1rem 4rem; display: grid; gap: 1.2rem; }
.sidebar { display: none; position: sticky; top: 88px; height: fit-content; }
.sidebar-card, .card, .calculator-card, .category-card, .quote-card, .stat-card, .faq-item, .calc-shell, .result-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); box-shadow: var(--shadow); backdrop-filter: blur(20px); }
.card, .calculator-card, .category-card, .quote-card, .stat-card, .faq-item, .calc-shell, .result-card { padding: 1.2rem; }
.hero { display: grid; gap: 1rem; align-items: center; padding: 2rem; background: linear-gradient(135deg, rgba(108, 99, 255, 0.18), rgba(0, 212, 255, 0.14)); }
.eyebrow { text-transform: uppercase; letter-spacing: 0.2em; color: var(--primary); font-size: 0.75rem; font-weight: 700; }
.hero h1 { font-size: clamp(1.8rem, 4vw, 3rem); margin: 0.3rem 0 0.8rem; }
.hero p { color: var(--muted); line-height: 1.7; }
.hero-actions { display: flex; gap: 0.9rem; flex-wrap: wrap; margin-top: 1rem; }
.hero-tags { display: flex; gap: 0.6rem; flex-wrap: wrap; margin-top: 1rem; }
.hero-tags span { padding: 0.55rem 0.8rem; border-radius: 999px; border: 1px solid var(--border); background: rgba(255,255,255,0.25); }
.hero-panel { display: grid; gap: 0.9rem; }
.metric-card { padding: 1rem; border-radius: 18px; background: var(--surface-strong); border: 1px solid var(--border); }
.metric-card strong { font-size: 1.7rem; display: block; }
.metric-card span { color: var(--muted); }
.search-panel { display: grid; gap: 0.9rem; }
.search-box { display: flex; align-items: center; gap: 0.65rem; padding: 0.9rem 1rem; border-radius: 999px; background: var(--surface-strong); border: 1px solid var(--border); }
.search-box input { width: 100%; border: none; outline: none; background: transparent; color: var(--text); }
.chip-row { display: flex; gap: 0.6rem; flex-wrap: wrap; }
.chip { border: 1px solid var(--border); border-radius: 999px; background: transparent; color: var(--text); padding: 0.5rem 0.8rem; cursor: pointer; }
.chip.is-active { background: linear-gradient(135deg, var(--primary), var(--secondary)); color: white; }
.section { display: grid; gap: 1rem; }
.section-heading h2 { margin: 0 0 0.2rem; }
.section-heading p { margin: 0; color: var(--muted); }
.grid { display: grid; gap: 1rem; }
.categories-grid, .calculator-grid, .testimonials-grid { grid-template-columns: repeat(1, minmax(0, 1fr)); }
.category-card { display: block; transition: transform 0.2s ease, box-shadow 0.2s ease; }
.category-card:hover, .calculator-card:hover { transform: translateY(-3px); }
.calculator-card { display: grid; gap: 0.8rem; }
.card-head { display: flex; justify-content: space-between; align-items: center; }
.favorite-btn { border: none; background: transparent; cursor: pointer; font-size: 1.1rem; }
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 0.4rem; border: none; border-radius: 999px; padding: 0.8rem 1rem; cursor: pointer; transition: transform 0.2s ease; position: relative; overflow: hidden; }
.btn:hover { transform: translateY(-1px); }
.btn-primary { background: linear-gradient(135deg, var(--primary), var(--secondary)); color: white; }
.btn-secondary { background: rgba(255,255,255,0.65); color: var(--text); }
.btn-mini { padding: 0.5rem 0.8rem; background: rgba(108, 99, 255, 0.14); }
.stats-grid { grid-template-columns: 1fr; }
.stat-card ul { padding-left: 1rem; color: var(--muted); }
.stat-card li { margin-bottom: 0.5rem; }
.quote-card p { color: var(--muted); }
.faq-list { display: grid; gap: 0.75rem; }
.faq-item summary { cursor: pointer; font-weight: 600; }
.faq-item p { color: var(--muted); margin-top: 0.7rem; }
.footer { text-align: center; padding: 2rem 1rem 3rem; color: var(--muted); }
.back-to-top, .fab { position: fixed; right: 1rem; z-index: 900; border: none; cursor: pointer; border-radius: 50%; color: white; background: linear-gradient(135deg, var(--primary), var(--secondary)); box-shadow: var(--shadow); }
.back-to-top { bottom: 1rem; width: 48px; height: 48px; display: none; }
.fab { bottom: 5rem; width: 56px; height: 56px; }
.back-to-top.show { display: grid; place-items: center; }
.toast-container { position: fixed; right: 1rem; bottom: 6rem; display: grid; gap: 0.6rem; z-index: 950; }
.toast { padding: 0.8rem 1rem; border-radius: 999px; background: var(--surface-strong); border: 1px solid var(--border); box-shadow: var(--shadow); }
.ripple { position: absolute; border-radius: 50%; transform: scale(0); animation: ripple 0.6s linear; pointer-events: none; background: rgba(255,255,255,0.45); }
@keyframes ripple { to { transform: scale(2.5); opacity: 0; } }
.page-intro { display: flex; justify-content: space-between; align-items: center; gap: 0.8rem; flex-wrap: wrap; }
.breadcrumbs { color: var(--muted); }
.calc-shell { display: grid; gap: 1rem; }
.form-grid { display: grid; gap: 0.9rem; }
label { display: grid; gap: 0.35rem; color: var(--muted); }
input, select, textarea { border: 1px solid var(--border); border-radius: 14px; padding: 0.8rem 0.95rem; background: var(--surface-strong); color: var(--text); outline: none; }
input:focus, select:focus, textarea:focus { border-color: var(--primary); box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.16); }
.result-card { display: grid; gap: 0.8rem; }
.result-card .result { font-size: 1.25rem; font-weight: 700; word-break: break-word; }
.result-actions { display: flex; flex-wrap: wrap; gap: 0.6rem; }
.scientific-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0.7rem; }
.scientific-grid button { border: none; border-radius: 16px; padding: 0.8rem; background: var(--surface-strong); color: var(--text); cursor: pointer; }
.scientific-grid button:hover { background: rgba(108, 99, 255, 0.12); }
.memory-row { display: flex; gap: 0.6rem; flex-wrap: wrap; }
@media (min-width: 768px) { .page-shell { padding: 1.25rem 1.4rem 4rem; } .categories-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } .calculator-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } .stats-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } .hero { grid-template-columns: 1.4fr 0.8fr; } .sidebar { display: block; width: 260px; } .page-shell { grid-template-columns: 260px minmax(0, 1fr); align-items: start; } }
@media (min-width: 1024px) { .categories-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); } .calculator-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); } .testimonials-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); } .stats-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
'''

script_js = '''const state = { theme: localStorage.getItem('allcalc-theme') || 'light', favorites: JSON.parse(localStorage.getItem('allcalc-favorites') || '[]'), history: JSON.parse(localStorage.getItem('allcalc-history') || '[]') };
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
function initHomePage() { applyTheme(state.theme); renderFavorites(); renderHistory(); animateCounters(); const search = document.getElementById('search'); if (search) search.addEventListener('input', (event) => filterCalculators(event.target.value)); document.querySelectorAll('.chip').forEach((chip) => { chip.addEventListener('click', () => { document.querySelectorAll('.chip').forEach((item) => item.classList.remove('is-active')); chip.classList.add('is-active'); const filter = chip.dataset.filter; document.querySelectorAll('.calculator-card').forEach((card) => { const matches = filter === 'all' || card.dataset.category === filter; card.style.display = matches ? 'grid' : 'none'; }); }); }); document.querySelectorAll('.favorite-btn').forEach((button) => { button.addEventListener('click', (event) => { event.preventDefault(); const id = button.dataset.fav || button.closest('.calculator-card').dataset.name; toggleFavorite(id); button.textContent = state.favorites.includes(id) ? '★' : '☆'; }); }); document.querySelectorAll('.btn').forEach((button) => button.addEventListener('click', handleRipple)); const faqItems = document.querySelectorAll('.faq-item'); faqItems.forEach((item) => { item.addEventListener('toggle', () => { if (item.open) faqItems.forEach((other) => { if (other !== item) other.open = false; }); }); }); const backToTop = document.querySelector('.back-to-top'); if (backToTop) { window.addEventListener('scroll', () => backToTop.classList.toggle('show', window.scrollY > 300)); backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' })); } document.addEventListener('keydown', (event) => { if (event.key === '/') { event.preventDefault(); const search = document.getElementById('search'); if (search) search.focus(); } if (event.key.toLowerCase() === 't') toggleTheme(); }); document.querySelector('.fab')?.addEventListener('click', () => showToast('Quick actions ready.')); document.querySelector('.loading-screen')?.classList.add('hidden'); }
window.addEventListener('DOMContentLoaded', () => { if (document.body.dataset.page) { if (typeof window.initCalculatorPage === 'function') window.initCalculatorPage(); } else { initHomePage(); } });
'''

calculators_js = '''const formatNumber = (value) => { if (!Number.isFinite(value)) return '—'; return new Intl.NumberFormat('en-US', { maximumFractionDigits: 2 }).format(value); };
const showToast = (message) => { const container = document.getElementById('toast-container'); if (!container) return; const toast = document.createElement('div'); toast.className = 'toast'; toast.textContent = message; container.appendChild(toast); setTimeout(() => toast.remove(), 2200); };
const saveHistory = (title, result) => { const history = JSON.parse(localStorage.getItem('allcalc-history') || '[]'); history.unshift({ title, result, time: new Date().toLocaleString() }); localStorage.setItem('allcalc-history', JSON.stringify(history.slice(0, 8))); };
const setResult = (selector, value) => { const target = document.querySelector(selector); if (target) target.textContent = value; };
const handleCopy = () => { const resultText = document.getElementById('result-output')?.textContent || document.querySelector('.result')?.textContent || ''; navigator.clipboard.writeText(resultText).then(() => showToast('Result copied')).catch(() => showToast('Copy failed')); };
const handleShare = async () => { const resultText = document.getElementById('result-output')?.textContent || document.querySelector('.result')?.textContent || ''; if (navigator.share) { try { await navigator.share({ title: document.title, text: resultText }); showToast('Shared successfully'); } catch { showToast('Share cancelled'); } } else { showToast('Sharing is not supported on this device'); } };
const handlePrint = () => window.print();
const handlePdf = () => { window.print(); showToast('Use the browser print dialog to save as PDF'); };
const initSharedFeatures = () => { const themeButton = document.getElementById('theme-toggle'); if (themeButton) themeButton.addEventListener('click', () => { const current = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light'; const next = current === 'dark' ? 'light' : 'dark'; document.documentElement.setAttribute('data-theme', next); localStorage.setItem('allcalc-theme', next); themeButton.textContent = next === 'dark' ? '☀️' : '🌙'; showToast(next === 'dark' ? 'Dark mode enabled' : 'Light mode enabled'); }); document.querySelectorAll('.btn').forEach((button) => button.addEventListener('click', (event) => { const ripple = document.createElement('span'); ripple.className = 'ripple'; const rect = button.getBoundingClientRect(); ripple.style.left = `${event.clientX - rect.left}px`; ripple.style.top = `${event.clientY - rect.top}px`; button.appendChild(ripple); setTimeout(() => ripple.remove(), 600); })); document.querySelector('.loading-screen')?.classList.add('hidden'); document.addEventListener('keydown', (event) => { if (event.key === '/') { event.preventDefault(); const firstInput = document.querySelector('input, select, textarea'); firstInput?.focus(); } }); document.querySelector('.copy-result')?.addEventListener('click', handleCopy); document.querySelector('.share-result')?.addEventListener('click', handleShare); document.querySelector('.print-result')?.addEventListener('click', handlePrint); document.querySelector('.pdf-result')?.addEventListener('click', handlePdf); };
const calculateBasic = (event) => { event.preventDefault(); const a = Number(document.getElementById('num-a').value); const b = Number(document.getElementById('num-b').value); const operation = document.getElementById('operation').value; if ([a, b].some((value) => Number.isNaN(value))) { setResult('#result-output', 'Please enter valid numbers.'); return; } let result; switch (operation) { case '+': result = a + b; break; case '-': result = a - b; break; case '*': result = a * b; break; case '/': result = b === 0 ? 'Cannot divide by zero.' : a / b; break; case '%': result = (a * b) / 100; break; default: result = a % b; break; } const text = typeof result === 'number' ? formatNumber(result) : result; setResult('#result-output', text); saveHistory('Basic Calculator', text); };
const calculateScientific = (event) => { event.preventDefault(); const display = document.getElementById('scientific-display'); if (!display) return; try { const result = Function(`"use strict"; return (${display.value})`)(); setResult('#result-output', formatNumber(result)); saveHistory('Scientific Calculator', formatNumber(result)); } catch { setResult('#result-output', 'Invalid expression'); } };
const calculateAge = (event) => { event.preventDefault(); const birth = new Date(document.getElementById('birth-date').value); const today = new Date(); if (Number.isNaN(birth.getTime())) { setResult('#result-output', 'Choose a valid birth date.'); return; } let years = today.getFullYear() - birth.getFullYear(); let months = today.getMonth() - birth.getMonth(); if (months < 0) { years--; months += 12; } const days = Math.floor((today - birth) / (1000 * 60 * 60 * 24)); const text = `${years} years, ${months} months, ${days} days old`; setResult('#result-output', text); saveHistory('Age Calculator', text); };
const calculateBMI = (event) => { event.preventDefault(); const kg = Number(document.getElementById('weight').value); const heightM = Number(document.getElementById('height').value) / 100; if (!kg || !heightM) { setResult('#result-output', 'Enter valid values.'); return; } const bmi = kg / (heightM * heightM); let remark = 'Healthy'; if (bmi < 18.5) remark = 'Underweight'; else if (bmi < 25) remark = 'Healthy'; else if (bmi < 30) remark = 'Overweight'; else remark = 'Obese'; const text = `${formatNumber(bmi)} — ${remark}`; setResult('#result-output', text); saveHistory('BMI Calculator', text); };
const calculateBMR = (event) => { event.preventDefault(); const weight = Number(document.getElementById('bmr-weight').value); const height = Number(document.getElementById('bmr-height').value); const age = Number(document.getElementById('bmr-age').value); const gender = document.getElementById('bmr-gender').value; const activity = Number(document.getElementById('activity').value); let bmr = gender === 'female' ? 10 * weight + 6.25 * height - 5 * age - 161 : 10 * weight + 6.25 * height - 5 * age + 5; const calories = bmr * activity; const text = `BMR ${formatNumber(bmr)} kcal/day • Daily calories ${formatNumber(calories)} kcal`; setResult('#result-output', text); saveHistory('BMR Calculator', text); };
const calculatePercentage = (event) => { event.preventDefault(); const value = Number(document.getElementById('value').value); const percent = Number(document.getElementById('percent').value); const result = (value * percent) / 100; setResult('#result-output', `${formatNumber(result)} (${percent}% of ${formatNumber(value)})`); saveHistory('Percentage Calculator', `${formatNumber(result)}`); };
const calculateDiscount = (event) => { event.preventDefault(); const price = Number(document.getElementById('price').value); const rate = Number(document.getElementById('discount-rate').value); const discount = price * (rate / 100); const final = price - discount; setResult('#result-output', `Discount ${formatNumber(discount)} • Final price ${formatNumber(final)}`); saveHistory('Discount Calculator', formatNumber(final)); };
const calculateEMI = (event) => { event.preventDefault(); const principal = Number(document.getElementById('loan-amount').value); const rate = Number(document.getElementById('interest-rate').value) / 100 / 12; const months = Number(document.getElementById('months').value); const emi = rate === 0 ? principal / months : principal * rate / (1 - Math.pow(1 + rate, -months)); setResult('#result-output', `EMI ${formatNumber(emi)}`); saveHistory('EMI Calculator', formatNumber(emi)); };
const calculateGST = (event) => { event.preventDefault(); const amount = Number(document.getElementById('gst-amount').value); const rate = Number(document.getElementById('gst-rate').value); const taxable = amount / (1 + rate / 100); const tax = amount - taxable; setResult('#result-output', `Tax ${formatNumber(tax)} • Total ${formatNumber(amount)}`); saveHistory('GST Calculator', formatNumber(tax)); };
const calculateSIP = (event) => { event.preventDefault(); const monthly = Number(document.getElementById('monthly-investment').value); const rate = Number(document.getElementById('sip-rate').value) / 100 / 12; const months = Number(document.getElementById('sip-months').value); const futureValue = monthly * (((1 + rate) ** months - 1) / rate) * (1 + rate); setResult('#result-output', `Future Value ${formatNumber(futureValue)}`); saveHistory('SIP Calculator', formatNumber(futureValue)); };
const calculateFD = (event) => { event.preventDefault(); const principal = Number(document.getElementById('fd-principal').value); const rate = Number(document.getElementById('fd-rate').value) / 100; const years = Number(document.getElementById('fd-years').value); const maturity = principal * Math.pow(1 + rate, years); setResult('#result-output', `Maturity ${formatNumber(maturity)}`); saveHistory('FD Calculator', formatNumber(maturity)); };
const calculateSimpleInterest = (event) => { event.preventDefault(); const principal = Number(document.getElementById('si-principal').value); const rate = Number(document.getElementById('si-rate').value); const years = Number(document.getElementById('si-years').value); const amount = principal * (1 + (rate / 100) * years); setResult('#result-output', `Amount ${formatNumber(amount)}`); saveHistory('Simple Interest', formatNumber(amount)); };
const calculateCompoundInterest = (event) => { event.preventDefault(); const principal = Number(document.getElementById('ci-principal').value); const rate = Number(document.getElementById('ci-rate').value) / 100; const years = Number(document.getElementById('ci-years').value); const frequency = Number(document.getElementById('ci-frequency').value); const amount = principal * Math.pow(1 + rate / frequency, frequency * years); setResult('#result-output', `Amount ${formatNumber(amount)}`); saveHistory('Compound Interest', formatNumber(amount)); };
const calculateLoan = (event) => { event.preventDefault(); const principal = Number(document.getElementById('loan-value').value); const rate = Number(document.getElementById('loan-rate').value) / 100 / 12; const months = Number(document.getElementById('loan-months').value); const result = rate === 0 ? principal / months : principal * rate / (1 - Math.pow(1 + rate, -months)); setResult('#result-output', `Monthly Payment ${formatNumber(result)}`); saveHistory('Loan Calculator', formatNumber(result)); };
const calculateCurrency = (event) => { event.preventDefault(); const amount = Number(document.getElementById('amount').value); const from = document.getElementById('from-currency').value; const to = document.getElementById('to-currency').value; const rates = { USD: 1, EUR: 0.92, GBP: 0.79, JPY: 155.6, INR: 83.4 }; const result = amount * (rates[to] / rates[from]); setResult('#result-output', `${formatNumber(result)} ${to}`); saveHistory('Currency Converter', `${formatNumber(result)} ${to}`); };
const calculateLength = (event) => { event.preventDefault(); const factors = { m: 1, km: 1000, cm: 0.01, mm: 0.001, ft: 0.3048, in: 0.0254, mi: 1609.34 }; const value = Number(document.getElementById('value-input').value); const from = document.getElementById('from-unit').value; const to = document.getElementById('to-unit').value; const meterEquivalent = value * factors[from]; const result = meterEquivalent / factors[to]; setResult('#result-output', `${formatNumber(result)} ${to}`); saveHistory('Length Converter', `${formatNumber(result)} ${to}`); };
const calculateWeight = (event) => { event.preventDefault(); const factors = { kg: 1, g: 0.001, mg: 0.000001, lb: 0.453592, oz: 0.0283495, ton: 1000 }; const value = Number(document.getElementById('value-input').value); const from = document.getElementById('from-unit').value; const to = document.getElementById('to-unit').value; const meterEquivalent = value * factors[from]; const result = meterEquivalent / factors[to]; setResult('#result-output', `${formatNumber(result)} ${to}`); saveHistory('Weight Converter', `${formatNumber(result)} ${to}`); };
const calculateTemperature = (event) => { event.preventDefault(); const value = Number(document.getElementById('temp-input').value); const from = document.getElementById('temp-from').value; const to = document.getElementById('temp-to').value; let celsius = value; if (from === 'F') celsius = (value - 32) * 5 / 9; if (from === 'K') celsius = value - 273.15; let result; if (to === 'C') result = celsius; if (to === 'F') result = celsius * 9 / 5 + 32; if (to === 'K') result = celsius + 273.15; setResult('#result-output', `${formatNumber(result)} ${to}`); saveHistory('Temperature Converter', `${formatNumber(result)} ${to}`); };
const calculateArea = (event) => { event.preventDefault(); const factors = { sqm: 1, sqft: 0.092903, acre: 4046.86, hectare: 10000, sqkm: 1000000 }; const value = Number(document.getElementById('value-input').value); const from = document.getElementById('from-unit').value; const to = document.getElementById('to-unit').value; const meterEquivalent = value * factors[from]; const result = meterEquivalent / factors[to]; setResult('#result-output', `${formatNumber(result)} ${to}`); saveHistory('Area Converter', `${formatNumber(result)} ${to}`); };
const calculateVolume = (event) => { event.preventDefault(); const factors = { l: 1, ml: 0.001, m3: 1000, gal: 3.78541, quart: 0.946353 }; const value = Number(document.getElementById('value-input').value); const from = document.getElementById('from-unit').value; const to = document.getElementById('to-unit').value; const meterEquivalent = value * factors[from]; const result = meterEquivalent / factors[to]; setResult('#result-output', `${formatNumber(result)} ${to}`); saveHistory('Volume Converter', `${formatNumber(result)} ${to}`); };
const calculateFuel = (event) => { event.preventDefault(); const distance = Number(document.getElementById('distance').value); const economy = Number(document.getElementById('economy').value); const price = Number(document.getElementById('fuel-price').value); const cost = (distance / economy) * price; setResult('#result-output', `Fuel Cost ${formatNumber(cost)}`); saveHistory('Fuel Cost', formatNumber(cost)); };
const calculateElectricity = (event) => { event.preventDefault(); const units = Number(document.getElementById('units').value); const rate = Number(document.getElementById('rate').value); const bill = units * rate; setResult('#result-output', `Bill ${formatNumber(bill)}`); saveHistory('Electricity Bill', formatNumber(bill)); };
const generatePassword = (event) => { event.preventDefault(); const length = Number(document.getElementById('password-length').value || 12); const chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'; let password = ''; for (let i = 0; i < length; i++) password += chars[Math.floor(Math.random() * chars.length)]; setResult('#result-output', password); saveHistory('Password Generator', password); };
const calculateCGPA = (event) => { event.preventDefault(); const values = document.getElementById('cgpa-input').value.split(',').map((v) => Number(v.trim())).filter(Boolean); if (!values.length) { setResult('#result-output', 'Enter valid values.'); return; } const avg = values.reduce((sum, value) => sum + value, 0) / values.length; setResult('#result-output', `CGPA ${formatNumber(avg)}`); saveHistory('CGPA Calculator', formatNumber(avg)); };
const calculateAttendance = (event) => { event.preventDefault(); const attended = Number(document.getElementById('attended').value); const total = Number(document.getElementById('total').value); const percentage = (attended / total) * 100; setResult('#result-output', `${formatNumber(percentage)}% attendance`); saveHistory('Attendance Calculator', `${formatNumber(percentage)}%`); };
const calculateDateDifference = (event) => { event.preventDefault(); const start = new Date(document.getElementById('start-date').value); const end = new Date(document.getElementById('end-date').value); const diff = Math.round((end - start) / (1000 * 60 * 60 * 24)); setResult('#result-output', `${diff} days`); saveHistory('Date Difference', `${diff} days`); };
const calculateTime = (event) => { event.preventDefault(); const value = Number(document.getElementById('time-value').value); const unit = document.getElementById('time-unit').value; const factors = { seconds: 1, minutes: 60, hours: 3600, days: 86400 }; const seconds = value * factors[unit]; setResult('#result-output', `${formatNumber(seconds)} seconds`); saveHistory('Time Converter', `${formatNumber(seconds)} seconds`); };
const calculateTax = (event) => { event.preventDefault(); const income = Number(document.getElementById('income').value); const tax = income > 500000 ? (income - 500000) * 0.2 + 500000 * 0.1 : income * 0.1; setResult('#result-output', `Tax ${formatNumber(tax)}`); saveHistory('Tax Calculator', formatNumber(tax)); };
const calculateSpeed = (event) => { event.preventDefault(); const factors = { kmh: 1, mph: 1.60934, mps: 3.6 }; const value = Number(document.getElementById('speed-value').value); const from = document.getElementById('speed-from').value; const to = document.getElementById('speed-to').value; const kmh = value / factors[from]; const result = kmh * factors[to]; setResult('#result-output', `${formatNumber(result)} ${to}`); saveHistory('Speed Converter', `${formatNumber(result)} ${to}`); };
const calculatePressure = (event) => { event.preventDefault(); const factors = { pa: 1, kpa: 1000, bar: 100000, psi: 6894.76 }; const value = Number(document.getElementById('pressure-value').value); const from = document.getElementById('pressure-from').value; const to = document.getElementById('pressure-to').value; const pa = value * factors[from]; const result = pa / factors[to]; setResult('#result-output', `${formatNumber(result)} ${to}`); saveHistory('Pressure Converter', `${formatNumber(result)} ${to}`); };
const calculateTip = (event) => { event.preventDefault(); const bill = Number(document.getElementById('bill').value); const tipPct = Number(document.getElementById('tip-percent').value); const people = Number(document.getElementById('people').value || 1); const tip = bill * (tipPct / 100); const total = bill + tip; setResult('#result-output', `Tip ${formatNumber(tip)} • Total ${formatNumber(total)} • Per person ${formatNumber(total / people)}`); saveHistory('Tip Calculator', formatNumber(total)); };
const startCountdown = (event) => { event.preventDefault(); const target = new Date(document.getElementById('countdown-target').value); const output = document.getElementById('result-output'); if (Number.isNaN(target.getTime())) { output.textContent = 'Choose a valid date.'; return; } const update = () => { const diff = Math.max(0, target - new Date()); const days = Math.floor(diff / (1000 * 60 * 60 * 24)); const hours = Math.floor((diff / (1000 * 60 * 60)) % 24); const minutes = Math.floor((diff / (1000 * 60)) % 60); const seconds = Math.floor((diff / 1000) % 60); output.textContent = `${days}d ${hours}h ${minutes}m ${seconds}s`; if (diff === 0) clearInterval(timer); }; update(); const timer = setInterval(update, 1000); saveHistory('Countdown Timer', output.textContent); };
const attachScientificButtons = () => { document.querySelectorAll('.scientific-grid button').forEach((button) => { button.addEventListener('click', () => { const display = document.getElementById('scientific-display'); const value = button.dataset.value || button.textContent; display.value += value; display.focus(); }); }); document.getElementById('clear-display')?.addEventListener('click', () => { document.getElementById('scientific-display').value = ''; }); document.getElementById('backspace-display')?.addEventListener('click', () => { const display = document.getElementById('scientific-display'); display.value = display.value.slice(0, -1); }); };
window.initCalculatorPage = () => { initSharedFeatures(); const page = document.body.dataset.page; const forms = { basic: (event) => calculateBasic(event), scientific: (event) => calculateScientific(event), age: (event) => calculateAge(event), bmi: (event) => calculateBMI(event), bmr: (event) => calculateBMR(event), percentage: (event) => calculatePercentage(event), discount: (event) => calculateDiscount(event), emi: (event) => calculateEMI(event), gst: (event) => calculateGST(event), sip: (event) => calculateSIP(event), fd: (event) => calculateFD(event), 'simple-interest': (event) => calculateSimpleInterest(event), 'compound-interest': (event) => calculateCompoundInterest(event), loan: (event) => calculateLoan(event), currency: (event) => calculateCurrency(event), length: (event) => calculateLength(event), weight: (event) => calculateWeight(event), temperature: (event) => calculateTemperature(event), area: (event) => calculateArea(event), volume: (event) => calculateVolume(event), fuel: (event) => calculateFuel(event), electricity: (event) => calculateElectricity(event), password: (event) => generatePassword(event), cgpa: (event) => calculateCGPA(event), attendance: (event) => calculateAttendance(event), date: (event) => calculateDateDifference(event), time: (event) => calculateTime(event), tax: (event) => calculateTax(event), speed: (event) => calculateSpeed(event), pressure: (event) => calculatePressure(event), tip: (event) => calculateTip(event), countdown: (event) => startCountdown(event) }; const form = document.querySelector('form'); if (form) form.addEventListener('submit', forms[page] || ((event) => event.preventDefault())); attachScientificButtons(); if (page === 'scientific') document.getElementById('scientific-form')?.addEventListener('submit', calculateScientific); };
'''

write(root / 'index.html', index_html)
write(root / 'style.css', style_css)
write(root / 'script.js', script_js)
write(root / 'js' / 'calculators.js', calculators_js)

pages = [
    ("basic", "Basic Calculator", "Fast arithmetic with addition, subtraction, multiplication, division, modulus, and percentages.", "Basic", "➕", "<form class=\"calc-shell\" id=\"basic-form\"><div class=\"form-grid\"><label>First number <input id=\"num-a\" type=\"number\" step=\"any\" required /></label><label>Second number <input id=\"num-b\" type=\"number\" step=\"any\" required /></label><label>Operation <select id=\"operation\"><option value=\"+\">Addition</option><option value=\"-\">Subtraction</option><option value=\"*\">Multiplication</option><option value=\"/\">Division</option><option value=\"%\">Percentage</option><option value=\"mod\">Modulus</option></select></label><button class=\"btn btn-primary\" type=\"submit\">Calculate</button></div></form>", "Use the calculator for everyday arithmetic."),
    ("scientific", "Scientific Calculator", "Perform advanced scientific calculations with buttons and memory-style input.", "Scientific", "🧮", "<form class=\"calc-shell\" id=\"scientific-form\"><div class=\"form-grid\"><label>Expression <input id=\"scientific-display\" type=\"text\" placeholder=\"e.g. 2+sin(30)\" autocomplete=\"off\" /></label><div class=\"scientific-grid\"><button type=\"button\" data-value=\"7\">7</button><button type=\"button\" data-value=\"8\">8</button><button type=\"button\" data-value=\"9\">9</button><button type=\"button\" data-value=\"/\">/</button><button type=\"button\" data-value=\"4\">4</button><button type=\"button\" data-value=\"5\">5</button><button type=\"button\" data-value=\"6\">6</button><button type=\"button\" data-value=\"*\">*</button><button type=\"button\" data-value=\"1\">1</button><button type=\"button\" data-value=\"2\">2</button><button type=\"button\" data-value=\"3\">3</button><button type=\"button\" data-value=\"-\">-</button><button type=\"button\" data-value=\"0\">0</button><button type=\"button\" data-value=\".\">.</button><button type=\"button\" data-value=\"+\">+</button><button type=\"button\" data-value=\"(\">(</button><button type=\"button\" data-value=\")\">)</button><button type=\"button\" data-value=\"Math.sin(30*Math.PI/180)\">sin</button><button type=\"button\" data-value=\"Math.cos(30*Math.PI/180)\">cos</button><button type=\"button\" data-value=\"Math.tan(30*Math.PI/180)\">tan</button><button type=\"button\" data-value=\"Math.log10(100)\">log</button><button type=\"button\" data-value=\"Math.log(2.718281828)\">ln</button><button type=\"button\" data-value=\"Math.sqrt(16)\">√</button><button type=\"button\" data-value=\"Math.pow(2,3)\">x²</button><button type=\"button\" data-value=\"Math.PI\">π</button><button type=\"button\" data-value=\"Math.E\">e</button><button type=\"button\" data-value=\"Math.pow(2,4)\">xʸ</button></div><div class=\"memory-row\"><button class=\"btn btn-secondary\" type=\"button\" id=\"clear-display\">Clear</button><button class=\"btn btn-secondary\" type=\"button\" id=\"backspace-display\">Backspace</button><button class=\"btn btn-primary\" type=\"submit\">Evaluate</button></div></div></form>", "Scientific calculations use JavaScript math expressions."),
    ("age", "Age Calculator", "Calculate age from birthday to today.", "Utility", "🎂", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Birth date <input id=\"birth-date\" type=\"date\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate age</button></div></form>", "This shows years, months, and days."),
    ("bmi", "BMI Calculator", "Calculate your Body Mass Index quickly.", "Health", "⚖️", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Weight (kg) <input id=\"weight\" type=\"number\" step=\"any\" required /></label><label>Height (cm) <input id=\"height\" type=\"number\" step=\"any\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate BMI</button></div></form>", "A BMI result is a helpful screening metric."),
    ("bmr", "BMR Calculator", "Estimate basal metabolic rate and daily calories.", "Health", "🔥", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Weight (kg) <input id=\"bmr-weight\" type=\"number\" step=\"any\" required /></label><label>Height (cm) <input id=\"bmr-height\" type=\"number\" step=\"any\" required /></label><label>Age <input id=\"bmr-age\" type=\"number\" required /></label><label>Gender <select id=\"bmr-gender\"><option value=\"male\">Male</option><option value=\"female\">Female</option></select></label><label>Activity factor <select id=\"activity\"><option value=\"1.2\">Sedentary</option><option value=\"1.375\">Light</option><option value=\"1.55\">Moderate</option><option value=\"1.725\">Very active</option></select></label><button class=\"btn btn-primary\" type=\"submit\">Calculate BMR</button></div></form>", "Use this to estimate how many calories your body burns at rest."),
    ("percentage", "Percentage Calculator", "Work out percentages, rates, and percent change.", "Education", "📊", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Value <input id=\"value\" type=\"number\" step=\"any\" required /></label><label>Percent <input id=\"percent\" type=\"number\" step=\"any\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate</button></div></form>", "Great for academic marks, finance, and discounts."),
    ("discount", "Discount Calculator", "Calculate how much you save and the final price.", "Finance", "🎟️", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Original price <input id=\"price\" type=\"number\" step=\"any\" required /></label><label>Discount rate (%) <input id=\"discount-rate\" type=\"number\" step=\"any\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate</button></div></form>", "Use this before making a purchase decision."),
    ("emi", "EMI Calculator", "Estimate monthly loan repayments.", "Finance", "🏦", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Loan amount <input id=\"loan-amount\" type=\"number\" step=\"any\" required /></label><label>Annual interest rate (%) <input id=\"interest-rate\" type=\"number\" step=\"any\" required /></label><label>Months <input id=\"months\" type=\"number\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate EMI</button></div></form>", "Perfect for home loans, car loans, and personal loans."),
    ("gst", "GST Calculator", "Calculate tax inclusive and exclusive amounts.", "Finance", "🧾", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Amount <input id=\"gst-amount\" type=\"number\" step=\"any\" required /></label><label>GST rate (%) <input id=\"gst-rate\" type=\"number\" step=\"any\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate GST</button></div></form>", "Useful for tax planning and invoice review."),
    ("sip", "SIP Calculator", "Estimate the future value of monthly investments.", "Finance", "📈", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Monthly investment <input id=\"monthly-investment\" type=\"number\" step=\"any\" required /></label><label>Expected annual return (%) <input id=\"sip-rate\" type=\"number\" step=\"any\" required /></label><label>Months <input id=\"sip-months\" type=\"number\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate SIP</button></div></form>", "Great for planning long-term wealth creation."),
    ("fd", "FD Calculator", "Estimate maturity value of fixed deposits.", "Finance", "💰", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Principal <input id=\"fd-principal\" type=\"number\" step=\"any\" required /></label><label>Annual interest rate (%) <input id=\"fd-rate\" type=\"number\" step=\"any\" required /></label><label>Years <input id=\"fd-years\" type=\"number\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate FD</button></div></form>", "Useful for comparing fixed-deposit growth options."),
    ("simple-interest", "Simple Interest Calculator", "Calculate amount from principal, rate, and time.", "Finance", "📉", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Principal <input id=\"si-principal\" type=\"number\" step=\"any\" required /></label><label>Rate (%) <input id=\"si-rate\" type=\"number\" step=\"any\" required /></label><label>Years <input id=\"si-years\" type=\"number\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate</button></div></form>", "Use this for straightforward interest calculations."),
    ("compound-interest", "Compound Interest Calculator", "Estimate growth with compounded returns.", "Finance", "🧠", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Principal <input id=\"ci-principal\" type=\"number\" step=\"any\" required /></label><label>Rate (%) <input id=\"ci-rate\" type=\"number\" step=\"any\" required /></label><label>Years <input id=\"ci-years\" type=\"number\" required /></label><label>Compounds per year <select id=\"ci-frequency\"><option value=\"1\">1</option><option value=\"2\">2</option><option value=\"4\">4</option><option value=\"12\">12</option></select></label><button class=\"btn btn-primary\" type=\"submit\">Calculate</button></div></form>", "Excellent for long-term savings and investment projections."),
    ("loan", "Loan Calculator", "Find the monthly installment for a loan.", "Finance", "🧮", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Loan amount <input id=\"loan-value\" type=\"number\" step=\"any\" required /></label><label>Annual rate (%) <input id=\"loan-rate\" type=\"number\" step=\"any\" required /></label><label>Months <input id=\"loan-months\" type=\"number\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate payment</button></div></form>", "Suitable for personal loans and consumer credit planning."),
    ("currency", "Currency Converter", "Convert amounts between major currencies.", "Utility", "💱", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Amount <input id=\"amount\" type=\"number\" step=\"any\" required /></label><label>From <select id=\"from-currency\"><option value=\"USD\">USD</option><option value=\"EUR\">EUR</option><option value=\"GBP\">GBP</option><option value=\"JPY\">JPY</option><option value=\"INR\">INR</option></select></label><label>To <select id=\"to-currency\"><option value=\"INR\">INR</option><option value=\"USD\">USD</option><option value=\"EUR\">EUR</option><option value=\"GBP\">GBP</option><option value=\"JPY\">JPY</option></select></label><button class=\"btn btn-primary\" type=\"submit\">Convert</button></div></form>", "Rates are approximate and update-ready for future integration."),
    ("length", "Length Converter", "Translate values between common length units.", "Converters", "📏", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Value <input id=\"value-input\" type=\"number\" step=\"any\" required /></label><label>From <select id=\"from-unit\"><option value=\"m\">meters</option><option value=\"km\">kilometers</option><option value=\"cm\">centimeters</option><option value=\"mm\">millimeters</option><option value=\"ft\">feet</option><option value=\"in\">inches</option><option value=\"mi\">miles</option></select></label><label>To <select id=\"to-unit\"><option value=\"km\">kilometers</option><option value=\"m\">meters</option><option value=\"cm\">centimeters</option><option value=\"ft\">feet</option><option value=\"in\">inches</option><option value=\"mi\">miles</option></select></label><button class=\"btn btn-primary\" type=\"submit\">Convert</button></div></form>", "Useful for travel, engineering, and everyday measurements."),
    ("weight", "Weight Converter", "Switch between metric and imperial weight units.", "Converters", "⚖️", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Value <input id=\"value-input\" type=\"number\" step=\"any\" required /></label><label>From <select id=\"from-unit\"><option value=\"kg\">kilograms</option><option value=\"g\">grams</option><option value=\"mg\">milligrams</option><option value=\"lb\">pounds</option><option value=\"oz\">ounces</option><option value=\"ton\">tons</option></select></label><label>To <select id=\"to-unit\"><option value=\"lb\">pounds</option><option value=\"kg\">kilograms</option><option value=\"g\">grams</option><option value=\"oz\">ounces</option></select></label><button class=\"btn btn-primary\" type=\"submit\">Convert</button></div></form>", "Helpful for recipes, fitness, and trade calculations."),
    ("temperature", "Temperature Converter", "Convert between Celsius, Fahrenheit, and Kelvin.", "Converters", "🌡️", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Value <input id=\"temp-input\" type=\"number\" step=\"any\" required /></label><label>From <select id=\"temp-from\"><option value=\"C\">Celsius</option><option value=\"F\">Fahrenheit</option><option value=\"K\">Kelvin</option></select></label><label>To <select id=\"temp-to\"><option value=\"F\">Fahrenheit</option><option value=\"C\">Celsius</option><option value=\"K\">Kelvin</option></select></label><button class=\"btn btn-primary\" type=\"submit\">Convert</button></div></form>", "Convenient when comparing scientific or weather data."),
    ("area", "Area Converter", "Switch between square meters, acres, hectares, and more.", "Converters", "🗺️", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Value <input id=\"value-input\" type=\"number\" step=\"any\" required /></label><label>From <select id=\"from-unit\"><option value=\"sqm\">square meters</option><option value=\"sqft\">square feet</option><option value=\"acre\">acres</option><option value=\"hectare\">hectares</option><option value=\"sqkm\">square kilometers</option></select></label><label>To <select id=\"to-unit\"><option value=\"sqft\">square feet</option><option value=\"sqm\">square meters</option><option value=\"acre\">acres</option><option value=\"hectare\">hectares</option></select></label><button class=\"btn btn-primary\" type=\"submit\">Convert</button></div></form>", "Perfect for land area, flooring, and planning tasks."),
    ("volume", "Volume Converter", "Convert between liters, milliliters, gallons, and cubic meters.", "Converters", "🫙", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Value <input id=\"value-input\" type=\"number\" step=\"any\" required /></label><label>From <select id=\"from-unit\"><option value=\"l\">liters</option><option value=\"ml\">milliliters</option><option value=\"m3\">cubic meters</option><option value=\"gal\">gallons</option><option value=\"quart\">quarts</option></select></label><label>To <select id=\"to-unit\"><option value=\"ml\">milliliters</option><option value=\"l\">liters</option><option value=\"m3\">cubic meters</option><option value=\"gal\">gallons</option></select></label><button class=\"btn btn-primary\" type=\"submit\">Convert</button></div></form>", "Helpful for recipes, chemistry, and liquid measurements."),
    ("fuel", "Fuel Cost Calculator", "Estimate fuel expenses for a trip.", "Utility", "⛽", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Distance (km) <input id=\"distance\" type=\"number\" step=\"any\" required /></label><label>Fuel economy (km/L) <input id=\"economy\" type=\"number\" step=\"any\" required /></label><label>Fuel price <input id=\"fuel-price\" type=\"number\" step=\"any\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate cost</button></div></form>", "Useful for planning trips and travel budgets."),
    ("electricity", "Electricity Bill Calculator", "Estimate monthly electricity costs.", "Utility", "💡", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Units consumed <input id=\"units\" type=\"number\" step=\"any\" required /></label><label>Rate per unit <input id=\"rate\" type=\"number\" step=\"any\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate bill</button></div></form>", "Simple estimation for monthly utility budgeting."),
    ("password", "Password Generator", "Generate strong passwords instantly.", "Utility", "🔐", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Password length <input id=\"password-length\" type=\"number\" min=\"6\" max=\"30\" value=\"14\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Generate</button></div></form>", "Creates a secure random password using letters, numbers, and symbols."),
    ("cgpa", "CGPA Calculator", "Calculate average grade points from multiple courses.", "Education", "🎓", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Grade points (comma separated) <textarea id=\"cgpa-input\" rows=\"4\" placeholder=\"e.g. 3.8, 4.0, 3.6\"></textarea></label><button class=\"btn btn-primary\" type=\"submit\">Calculate CGPA</button></div></form>", "Helpful for academic planning and performance tracking."),
    ("attendance", "Attendance Calculator", "Compute attendance percentage from attendance and total classes.", "Education", "🗓️", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Classes attended <input id=\"attended\" type=\"number\" required /></label><label>Total classes <input id=\"total\" type=\"number\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate attendance</button></div></form>", "Useful for students and trainers to track participation."),
    ("date", "Date Difference Calculator", "Find the number of days between two dates.", "Utility", "📅", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Start date <input id=\"start-date\" type=\"date\" required /></label><label>End date <input id=\"end-date\" type=\"date\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Find difference</button></div></form>", "Great for deadlines, project planning, and countdowns."),
    ("time", "Time Converter", "Convert between seconds, minutes, hours, and days.", "Converters", "⏱️", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Value <input id=\"time-value\" type=\"number\" step=\"any\" required /></label><label>Unit <select id=\"time-unit\"><option value=\"seconds\">seconds</option><option value=\"minutes\">minutes</option><option value=\"hours\">hours</option><option value=\"days\">days</option></select></label><button class=\"btn btn-primary\" type=\"submit\">Convert</button></div></form>", "Useful for scheduling and elapsed time calculations."),
    ("tax", "Tax Calculator", "Estimate tax from annual income.", "Finance", "🧾", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Annual income <input id=\"income\" type=\"number\" step=\"any\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Estimate tax</button></div></form>", "Approximate tax estimate for planning purposes."),
    ("speed", "Speed Converter", "Convert between kilometers per hour, miles per hour, and meters per second.", "Converters", "🚗", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Value <input id=\"speed-value\" type=\"number\" step=\"any\" required /></label><label>From <select id=\"speed-from\"><option value=\"kmh\">km/h</option><option value=\"mph\">mph</option><option value=\"mps\">m/s</option></select></label><label>To <select id=\"speed-to\"><option value=\"mph\">mph</option><option value=\"kmh\">km/h</option><option value=\"mps\">m/s</option></select></label><button class=\"btn btn-primary\" type=\"submit\">Convert</button></div></form>", "Useful for driving, cycling, and physics estimates."),
    ("pressure", "Pressure Converter", "Convert between pascals, kilopascals, bars, and psi.", "Converters", "💨", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Value <input id=\"pressure-value\" type=\"number\" step=\"any\" required /></label><label>From <select id=\"pressure-from\"><option value=\"pa\">Pa</option><option value=\"kpa\">kPa</option><option value=\"bar\">bar</option><option value=\"psi\">psi</option></select></label><label>To <select id=\"pressure-to\"><option value=\"kpa\">kPa</option><option value=\"pa\">Pa</option><option value=\"bar\">bar</option><option value=\"psi\">psi</option></select></label><button class=\"btn btn-primary\" type=\"submit\">Convert</button></div></form>", "Useful for engineering, weather forecasting, and fluid dynamics."),
    ("tip", "Tip Calculator", "Split tips and total bills with ease.", "Utility", "💵", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Bill amount <input id=\"bill\" type=\"number\" step=\"any\" required /></label><label>Tip (%) <input id=\"tip-percent\" type=\"number\" step=\"any\" required /></label><label>Number of people <input id=\"people\" type=\"number\" min=\"1\" value=\"1\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Calculate tip</button></div></form>", "Great for restaurants and shared expenses."),
    ("countdown", "Countdown Timer", "Track the time left to an event.", "Utility", "⏳", "<form class=\"calc-shell\"><div class=\"form-grid\"><label>Target date and time <input id=\"countdown-target\" type=\"datetime-local\" required /></label><button class=\"btn btn-primary\" type=\"submit\">Start countdown</button></div></form>", "Perfect for deadlines, launches, and important events."),
]

for slug, title, description, category, icon, form_html, notes in pages:
    html = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} | AllCalc Pro</title>
    <meta name="description" content="{description}" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="../style.css" />
  </head>
  <body data-page="{slug}">
    <div class="loading-screen"><div class="spinner"></div><p>Loading calculator…</p></div>
    <div class="toast-container" id="toast-container"></div>
    <header class="topbar">
      <a class="brand" href="../index.html"><span class="brand-mark">A</span><span><strong>AllCalc Pro</strong><small>{title}</small></span></a>
      <nav class="top-nav" aria-label="Calculator navigation"><a href="../index.html">Home</a><button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">🌙</button></nav>
    </header>
    <main class="page-shell">
      <aside class="sidebar">
        <div class="sidebar-card">
          <h3>Calculator suite</h3>
          <a class="nav-link" href="basic.html">Basic</a><a class="nav-link" href="scientific.html">Scientific</a><a class="nav-link" href="bmi.html">Health</a><a class="nav-link" href="emi.html">Finance</a><a class="nav-link" href="cgpa.html">Education</a><a class="nav-link" href="length.html">Converters</a><a class="nav-link" href="age.html">Utility</a>
        </div>
      </aside>
      <section class="calc-shell">
        <div class="page-intro"><div><p class="eyebrow">{category} • {icon}</p><h1>{title}</h1><p class="breadcrumbs"><a href="../index.html">Home</a> / {title}</p></div></div>
        {form_html}
        <div class="result-card">
          <div class="result-actions"><button class="btn btn-secondary copy-result" type="button">Copy result</button><button class="btn btn-secondary share-result" type="button">Share</button><button class="btn btn-secondary print-result" type="button">Print</button><button class="btn btn-secondary pdf-result" type="button">Save as PDF</button></div>
          <div class="result" id="result-output">Your result will appear here.</div>
          <p>{notes}</p>
        </div>
      </section>
    </main>
    <script src="../js/calculators.js"></script>
    <script src="../script.js"></script>
  </body>
</html>
'''
    write(root / 'calculators' / f'{slug}.html', html)

for name in ["health", "finance", "education", "converters", "utility"]:
    write(root / 'calculators' / f'{name}.html', '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8" /><meta http-equiv="refresh" content="0; url=basic.html" /></head><body></body></html>')

# create a small placeholder for assets
write(root / 'assets' / 'logo' / 'logo.svg', '<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" viewBox="0 0 120 120"><rect width="120" height="120" rx="28" fill="#6C63FF"/><path d="M33 82L60 32l27 50" stroke="white" stroke-width="10" fill="none" stroke-linecap="round"/></svg>')
print('Generated AllCalc Pro website files')
