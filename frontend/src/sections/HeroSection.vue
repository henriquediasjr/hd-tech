<script setup>
import { useLocale } from '../composables/useLocale.js'

const { t } = useLocale()

function scrollTo(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <section id="hero" class="hero-section">
    <div class="hero-content">
      <p class="hero-greeting">{{ t('hero.greeting') }}</p>
      <h1 class="hero-name">{{ t('hero.name') }}</h1>
      <p class="hero-title">{{ t('hero.title') }}</p>
      <p class="hero-subtitle">{{ t('hero.subtitle') }}</p>

      <div class="hero-location">
        <span class="location-icon">📍</span>
        <span>{{ t('hero.location') }}</span>
      </div>

      <div class="hero-socials">
        <a href="mailto:henriquediasjr@gmail.com" class="social-link" title="Email">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
          henriquediasjr@gmail.com
        </a>
        <a href="https://linkedin.com/in/henrique-dias" target="_blank" rel="noopener" class="social-link" title="LinkedIn">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/></svg>
          LinkedIn
        </a>
        <a href="https://github.com/henriquediasjr" target="_blank" rel="noopener" class="social-link" title="GitHub">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
          GitHub
        </a>
      </div>

      <div class="hero-ctas">
        <button class="btn-primary" @click="scrollTo('contact')">
          {{ t('hero.scheduleCta') }}
        </button>
        <button class="btn-secondary" @click="scrollTo('contact')">
          {{ t('hero.contactCta') }}
        </button>
      </div>
    </div>

    <div class="hero-bg" aria-hidden="true"></div>
  </section>
</template>

<style scoped>
.hero-section {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 6rem 1.5rem 4rem;
  max-width: var(--max-w);
  margin: 0 auto;
  overflow: hidden;
}

.hero-bg {
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 60% 40%, rgba(59, 130, 246, 0.08) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 640px;
}

.hero-greeting {
  font-size: 1.1rem;
  color: var(--accent);
  font-weight: 500;
  margin-bottom: 0.25rem;
}

.hero-name {
  font-size: clamp(2.5rem, 6vw, 4rem);
  font-weight: 800;
  color: var(--text);
  line-height: 1.1;
  margin-bottom: 0.5rem;
  letter-spacing: -1px;
}

.hero-title {
  font-size: 1.35rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 0.35rem;
}

.hero-subtitle {
  font-size: 1rem;
  color: var(--muted);
  margin-bottom: 1.25rem;
}

.hero-location {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  color: var(--muted);
  font-size: 0.9rem;
  margin-bottom: 1.75rem;
  background: var(--surface);
  padding: 0.35rem 0.75rem;
  border-radius: 999px;
  border: 1px solid var(--border);
}

.hero-socials {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 2rem;
}

.social-link {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.875rem;
  transition: color 0.15s;
}

.social-link:hover {
  color: var(--accent);
}

.hero-ctas {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.btn-primary {
  padding: 0.75rem 1.75rem;
  background: var(--accent);
  color: #fff;
  border: none;
  border-radius: var(--radius);
  font-weight: 600;
  font-size: 0.95rem;
  cursor: pointer;
  transition: background 0.15s, transform 0.1s;
}

.btn-primary:hover {
  background: var(--accent-hover);
}

.btn-secondary {
  padding: 0.75rem 1.75rem;
  background: transparent;
  color: var(--text);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  font-weight: 500;
  font-size: 0.95rem;
  cursor: pointer;
  transition: border-color 0.15s, color 0.15s;
}

.btn-secondary:hover {
  border-color: var(--accent);
  color: var(--accent);
}
</style>
