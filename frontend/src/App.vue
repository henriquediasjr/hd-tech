<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useLocale } from './composables/useLocale.js'
import HeroSection from './sections/HeroSection.vue'
import AboutSection from './sections/AboutSection.vue'
import ExperienceSection from './sections/ExperienceSection.vue'
import SkillsSection from './sections/SkillsSection.vue'
import EducationSection from './sections/EducationSection.vue'
import ContactSection from './sections/ContactSection.vue'

const { t, locale, setLocale } = useLocale()

const activeSection = ref('hero')
const navOpen = ref(false)

const navLinks = ['about', 'experience', 'skills', 'education', 'contact']

function scrollTo(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
  navOpen.value = false
}

function toggleLocale() {
  setLocale(locale.value === 'en' ? 'pt' : 'en')
}

let observers = []

onMounted(() => {
  const sections = ['hero', ...navLinks]
  sections.forEach((id) => {
    const el = document.getElementById(id)
    if (!el) return
    const obs = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) activeSection.value = id
      },
      { threshold: 0.25 }
    )
    obs.observe(el)
    observers.push(obs)
  })
})

onUnmounted(() => {
  observers.forEach((o) => o.disconnect())
})
</script>

<template>
  <div class="app">
    <!-- Sticky nav -->
    <header class="nav">
      <div class="nav-inner">
        <button class="nav-logo" @click="scrollTo('hero')">HD</button>

        <nav class="nav-links" :class="{ open: navOpen }">
          <button
            v-for="link in navLinks"
            :key="link"
            class="nav-link"
            :class="{ active: activeSection === link }"
            @click="scrollTo(link)"
          >
            {{ t(`nav.${link}`) }}
          </button>
        </nav>

        <div class="nav-right">
          <button class="locale-toggle" @click="toggleLocale">
            <span :class="{ 'locale-active': locale === 'en' }">EN</span>
            <span class="locale-sep">|</span>
            <span :class="{ 'locale-active': locale === 'pt' }">PT</span>
          </button>
          <button class="hamburger" @click="navOpen = !navOpen" aria-label="Toggle menu">
            <span></span><span></span><span></span>
          </button>
        </div>
      </div>
    </header>

    <main>
      <HeroSection />
      <AboutSection />
      <ExperienceSection />
      <SkillsSection />
      <EducationSection />
      <ContactSection />
    </main>

    <footer class="site-footer">
      <p>Henrique Dias de Carvalho Jr · Curitiba, Brazil · henriquediasjr@gmail.com</p>
    </footer>
  </div>
</template>

<style>
/* ── Reset ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html {
  scroll-behavior: smooth;
}

/* ── Design tokens ── */
:root {
  --bg: #0f172a;
  --surface: #1e293b;
  --surface2: #263348;
  --text: #e2e8f0;
  --muted: #94a3b8;
  --accent: #3b82f6;
  --accent-hover: #2563eb;
  --border: #334155;
  --success: #22c55e;
  --error: #ef4444;
  --radius: 10px;
  --max-w: 900px;
}

body {
  background: var(--bg);
  color: var(--text);
  font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
  line-height: 1.6;
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}

/* ── Nav ── */
.nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(15, 23, 42, 0.92);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
}

.nav-inner {
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 1.5rem;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.nav-logo {
  font-weight: 800;
  font-size: 1.15rem;
  color: var(--accent);
  background: none;
  border: none;
  cursor: pointer;
  letter-spacing: -0.5px;
  padding: 0;
  flex-shrink: 0;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.nav-link {
  background: none;
  border: none;
  color: var(--muted);
  cursor: pointer;
  font-size: 0.875rem;
  font-weight: 500;
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  transition: color 0.15s, background 0.15s;
}

.nav-link:hover {
  color: var(--text);
  background: var(--surface);
}

.nav-link.active {
  color: var(--accent);
  background: rgba(59, 130, 246, 0.1);
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.locale-toggle {
  background: none;
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--muted);
  cursor: pointer;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.3rem 0.6rem;
  display: flex;
  align-items: center;
  gap: 0.3rem;
  letter-spacing: 0.05em;
  transition: border-color 0.15s;
}

.locale-toggle:hover {
  border-color: var(--accent);
}

.locale-sep {
  opacity: 0.4;
}

.locale-active {
  color: var(--accent);
}

.hamburger {
  display: none;
  flex-direction: column;
  gap: 4px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
}

.hamburger span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--muted);
  border-radius: 2px;
}

/* ── Main sections ── */
main section {
  padding: 5rem 1.5rem;
  max-width: var(--max-w);
  margin: 0 auto;
}

.section-title {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 2.5rem;
  padding-bottom: 0.75rem;
  border-bottom: 2px solid var(--accent);
  display: inline-block;
}

/* ── Shared card ── */
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.75rem;
}

/* ── Footer ── */
.site-footer {
  border-top: 1px solid var(--border);
  padding: 1.5rem;
  text-align: center;
  color: var(--muted);
  font-size: 0.8rem;
}

/* ── Mobile nav ── */
@media (max-width: 640px) {
  .hamburger {
    display: flex;
  }

  .nav-links {
    display: none;
    position: absolute;
    top: 60px;
    left: 0;
    right: 0;
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    flex-direction: column;
    padding: 1rem;
    gap: 0.25rem;
  }

  .nav-links.open {
    display: flex;
  }

  .nav-link {
    width: 100%;
    text-align: left;
    padding: 0.6rem 1rem;
  }
}
</style>
