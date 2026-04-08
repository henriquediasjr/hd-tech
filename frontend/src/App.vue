<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="layout">
    <header>
      <span class="logo">Portfolio</span>
      <nav>
        <RouterLink to="/contact">Contact</RouterLink>
        <RouterLink to="/budget">Budget</RouterLink>
        <RouterLink to="/schedule">Schedule</RouterLink>
      </nav>
    </header>

    <main>
      <RouterView />
    </main>
  </div>
</template>

<style>
/* ── Global reset & tokens ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --color-bg: #f8f9fa;
  --color-surface: #ffffff;
  --color-text: #1a1a2e;
  --color-muted: #6b7280;
  --color-accent: #2563eb;
  --color-border: #e5e7eb;
  --color-success: #16a34a;
  --color-error: #dc2626;
  --radius: 8px;
  --shadow: 0 1px 4px rgba(0,0,0,.08);
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  background: var(--color-bg);
  color: var(--color-text);
  line-height: 1.6;
  min-height: 100vh;
}

/* ── Layout ── */
.layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

header {
  background: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
  padding: 0 2rem;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 10;
  box-shadow: var(--shadow);
}

.logo {
  font-weight: 700;
  font-size: 1.1rem;
  letter-spacing: -.5px;
  color: var(--color-accent);
}

nav {
  display: flex;
  gap: 0.25rem;
}

nav a {
  padding: 0.4rem 0.875rem;
  border-radius: var(--radius);
  color: var(--color-muted);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  transition: background 0.15s, color 0.15s;
}

nav a:hover { background: var(--color-bg); color: var(--color-text); }
nav a.router-link-active { background: #eff6ff; color: var(--color-accent); }

main {
  flex: 1;
  display: flex;
  justify-content: center;
  padding: 3rem 1rem;
}

/* ── Card / Section ── */
section {
  background: var(--color-surface);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  border: 1px solid var(--color-border);
  padding: 2.5rem;
  width: 100%;
  max-width: 560px;
  height: fit-content;
}

h1 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.subtitle {
  color: var(--color-muted);
  margin-bottom: 2rem;
  font-size: 0.95rem;
}

/* ── Form ── */
form { display: flex; flex-direction: column; gap: 1.25rem; }

.field { display: flex; flex-direction: column; gap: 0.375rem; }

label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--color-text);
}

input, select, textarea {
  padding: 0.6rem 0.875rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  font-size: 0.95rem;
  font-family: inherit;
  background: var(--color-bg);
  color: var(--color-text);
  transition: border-color 0.15s, box-shadow 0.15s;
  outline: none;
  width: 100%;
}

input:focus, select:focus, textarea:focus {
  border-color: var(--color-accent);
  box-shadow: 0 0 0 3px rgba(37,99,235,.1);
}

textarea { resize: vertical; }

button[type="submit"] {
  padding: 0.7rem 1.5rem;
  background: var(--color-accent);
  color: #fff;
  font-weight: 600;
  font-size: 0.95rem;
  border: none;
  border-radius: var(--radius);
  cursor: pointer;
  transition: opacity 0.15s;
  align-self: flex-start;
}

button[type="submit"]:hover:not(:disabled) { opacity: 0.88; }
button[type="submit"]:disabled { opacity: 0.55; cursor: not-allowed; }

/* ── Feedback ── */
.feedback {
  padding: 0.75rem 1rem;
  border-radius: var(--radius);
  font-size: 0.9rem;
  font-weight: 500;
}

.feedback.success {
  background: #f0fdf4;
  color: var(--color-success);
  border: 1px solid #bbf7d0;
}

.feedback.error {
  background: #fef2f2;
  color: var(--color-error);
  border: 1px solid #fecaca;
}
</style>
