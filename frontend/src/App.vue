<template>
  <div id="app">
    <a href="#main-content" class="skip-link">Direct naar inhoud</a>
    <header class="rijk-header" role="banner">
      <div class="rijk-logo-block">
        <img src="/rijksoverheid-logo.svg" alt="Rijksoverheid logo" class="rijk-logo" />
      </div>
      <div class="rijk-banner">
        <div class="rijk-banner-inner">
          <span class="rijk-title">Personen Demo Portaal</span>
        </div>
        <nav aria-label="Hoofdmenu" class="rijk-nav">
          <ul>
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="/persons">Personen</router-link></li>
            <li><router-link to="/add">Persoon toevoegen</router-link></li>
          </ul>
        </nav>
      </div>
    </header>
    <main id="main-content">
      <router-view />
    </main>
    <footer class="rijk-footer" role="contentinfo">
      <div class="footer-inner">
        <span>&copy; {{ new Date().getFullYear() }} Rijksoverheid</span>
        <span>
          <a href="https://www.digitoegankelijk.nl/" target="_blank" rel="noopener noreferrer">Toegankelijkheid</a> |
          <a href="https://www.rijksoverheid.nl/copyright" target="_blank" rel="noopener noreferrer">Copyright</a>
        </span>
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>

<style>
@import url('https://www.rijkshuisstijl.nl/binaries/content/assets/rijkshuisstijl/online/rijkswebfont/stylesheet.css');

body {
  background: #fff;
  color: #1e1e1e;
  font-family: 'RijksoverheidSansWeb', Arial, sans-serif;
  margin: 0;
}
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
.rijk-header {
  background: #fff;
  color: #1e1e1e;
  padding: 0;
  border-bottom: none;
}
.rijk-logo-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 2rem;
  padding-bottom: 1rem;
}
.rijk-logo {
  height: 70px;
  margin-bottom: 0.5rem;
}
.rijk-banner {
  background: #00337f;
  color: #fff;
  width: 100%;
  padding: 0;
  margin: 0;
  border-bottom: 1px solid #00337f;
}
.rijk-banner-inner {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  padding: 1.5rem 2rem 0.5rem 2rem;
}
.rijk-title {
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: 0.5px;
  color: #fff;
}
.rijk-nav {
  background: #00337f;
  padding: 0 2rem 1rem 2rem;
}
.rijk-nav ul {
  list-style: none;
  display: flex;
  gap: 2rem;
  margin: 0;
  padding: 0.5rem 0 0 0;
}
.rijk-nav a {
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  font-size: 1.1rem;
  padding: 0.2rem 0.5rem;
  border-radius: 2px;
  transition: background 0.2s;
}
.rijk-nav a.router-link-exact-active {
  background: #ffd200;
  color: #00337f;
}
.rijk-nav a:focus, .rijk-nav a:hover {
  background: #ffd200;
  color: #00337f;
  outline: 2px solid #00337f;
}
main {
  flex: 1 0 auto;
  padding: 2rem;
  background: #fff;
}
.skip-link {
  position: absolute;
  left: -999px;
  top: auto;
  width: 1px;
  height: 1px;
  overflow: hidden;
  z-index: 100;
  background: #ffd200;
  color: #00337f;
  padding: 8px;
}
.skip-link:focus {
  left: 0;
  width: auto;
  height: auto;
}
.rijk-footer {
  background: #f5f5f5;
  color: #1e1e1e;
  border-top: 1px solid #d1d1d1;
  padding: 1rem 0;
  font-size: 1rem;
}
.footer-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 2rem;
}
.rijk-footer a {
  color: #00337f;
  text-decoration: underline;
  margin-left: 1rem;
}
.rijk-footer a:focus, .rijk-footer a:hover {
  color: #ffd200;
  background: #00337f;
  outline: 2px solid #00337f;
}
</style>