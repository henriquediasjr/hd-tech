<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useLocale }      from './composables/useLocale'
import HeroSection        from './sections/HeroSection.vue'
import HowICanHelpSection from './sections/HowICanHelpSection.vue'
import ExperienceSection  from './sections/ExperienceSection.vue'
import ProjectsSection    from './sections/ProjectsSection.vue'
import SkillsSection      from './sections/SkillsSection.vue'
import ContactSection     from './sections/ContactSection.vue'
import EducationSection   from './sections/EducationSection.vue'

const { locale, setLocale, t } = useLocale()

const scrolled  = ref(false)
const navOpen   = ref(false)
const activeSection = ref('')

const navLinks = computed(() => [
  { id: 'experience', label: t('nav.experience') },
  { id: 'projects',   label: t('nav.projects')   },
  { id: 'stack',      label: t('nav.skills')     },
  { id: 'contact',    label: t('nav.contact')    },
])

function scrollTo(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' })
  navOpen.value = false
}

const cleanups = []

onMounted(() => {
  // Nav blur on scroll
  const onScroll = () => { scrolled.value = window.scrollY > 40 }
  window.addEventListener('scroll', onScroll, { passive: true })
  cleanups.push(() => window.removeEventListener('scroll', onScroll))

  // Active section tracking
  navLinks.forEach(({ id }) => {
    const el = document.getElementById(id)
    if (!el) return
    const obs = new IntersectionObserver(
      ([e]) => { if (e.isIntersecting) activeSection.value = id },
      { threshold: 0.25 }
    )
    obs.observe(el)
    cleanups.push(() => obs.disconnect())
  })

  // Scroll-triggered animations
  const animEls = document.querySelectorAll('[data-animate]')
  const animObs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('is-visible')
        animObs.unobserve(e.target)
      }
    })
  }, { threshold: 0.08, rootMargin: '0px 0px -32px 0px' })
  animEls.forEach(el => animObs.observe(el))
  cleanups.push(() => animObs.disconnect())
})

onUnmounted(() => cleanups.forEach(fn => fn()))
</script>

<template>
  <div class="app">
    <!-- ── Navigation ── -->
    <header class="nav" :class="{ 'nav--scrolled': scrolled }">
      <div class="nav-inner">
        <button class="nav-logo" @click="scrollTo('hero')" aria-label="Home">
          <span>HD</span>
        </button>

        <nav class="nav-center">
          <button
            v-for="link in navLinks"
            :key="link.id"
            class="nav-link"
            :class="{ 'nav-link--active': activeSection === link.id }"
            @click="scrollTo(link.id)"
          >{{ link.label }}</button>
        </nav>

        <div class="nav-right">
          <div class="locale-toggle">
            <button
              class="locale-opt"
              :class="{ 'locale-opt--active': locale === 'en' }"
              @click="setLocale('en')"
              aria-label="English language"
            >EN</button>
            <span class="locale-sep">|</span>
            <button
              class="locale-opt"
              :class="{ 'locale-opt--active': locale === 'pt' }"
              @click="setLocale('pt')"
              aria-label="Portuguese language"
            >PT</button>
          </div>
          <button class="btn-nav-cta" @click="scrollTo('contact')">Book a call</button>
          <button
            class="hamburger"
            :class="{ 'hamburger--open': navOpen }"
            @click="navOpen = !navOpen"
            aria-label="Toggle menu"
          >
            <span></span><span></span><span></span>
          </button>
        </div>
      </div>
    </header>

    <!-- Mobile overlay -->
    <div v-if="navOpen" class="nav-overlay" @click.self="navOpen = false">
      <button
        v-for="link in navLinks"
        :key="link.id"
        class="nav-overlay-link"
        @click="scrollTo(link.id)"
      >{{ link.label }}</button>
      <button class="btn-nav-cta nav-overlay-cta" @click="scrollTo('contact')">Book a call</button>
    </div>

    <!-- ── Sections ── -->
    <main>
      <HeroSection />
      <HowICanHelpSection />
      <ExperienceSection />
      <ProjectsSection />
      <SkillsSection />
      <ContactSection />
      <EducationSection />
    </main>

    <!-- ── Footer ── -->
    <footer class="footer">
      <div class="footer-inner">
        <div class="footer-left">
          <p class="footer-name">Henrique Dias · Backend Engineer · Curitiba, Brazil</p>
          <div class="footer-socials">
            <a href="https://github.com/henriquediasjr" target="_blank" rel="noopener" class="social-link">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
              GitHub
            </a>
            <a href="https://linkedin.com/in/henrique-dias-jr" target="_blank" rel="noopener" class="social-link">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/></svg>
              LinkedIn
            </a>
            <a href="mailto:Henriquediasjr@gmail.com" class="social-link">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
              Email
            </a>
          </div>
        </div>
        <div class="footer-right">
          <span class="footer-built">Built with Vue 3 + Python</span>
        </div>
      </div>
    </footer>
  </div>
</template>

<style>
/* ── Reset ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }

/* ── Tokens ── */
:root {
  --bg:       #0a0a0b;
  --surface:  #111113;
  --border:   rgba(255, 255, 255, 0.07);
  --border-h: rgba(255, 255, 255, 0.13);
  --accent:   #3b82f6;
  --text:     #f4f4f5;
  --muted:    #71717a;
  --radius:   12px;
  --max-w:    1100px;
  --ease:     cubic-bezier(0.16, 1, 0.3, 1);
}

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Geist', system-ui, -apple-system, sans-serif;
  font-weight: 400;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

::selection { background: rgba(59, 130, 246, 0.3); color: #fff; }

::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #0a0a0b; }
::-webkit-scrollbar-thumb { background: #3b82f6; border-radius: 99px; }
* { scrollbar-width: thin; scrollbar-color: #3b82f6 #0a0a0b; }

/* ── Scroll animations ── */
[data-animate] {
  opacity: 0;
  transform: translateY(20px);
  transition:
    opacity  0.5s var(--ease) calc(var(--i, 0) * 80ms),
    transform 0.5s var(--ease) calc(var(--i, 0) * 80ms);
}
[data-animate].is-visible { opacity: 1; transform: translateY(0); }

/* ── Layout helpers ── */
.section-wrap {
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 96px 48px;
}

.section-label {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--muted);
  font-weight: 500;
  margin-bottom: 48px;
}
.section-label::before {
  content: '';
  flex-shrink: 0;
  width: 3px;
  height: 14px;
  background: var(--accent);
  border-radius: 2px;
}

/* ── Shared card ── */
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  transition: border-color 0.25s var(--ease), transform 0.25s var(--ease), box-shadow 0.25s var(--ease);
}
.card:hover {
  border-color: var(--border-h);
  transform: translateY(-2px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
}

/* ── Buttons ── */
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 20px;
  background: var(--accent);
  color: #fff;
  border: none;
  border-radius: 8px;
  font-family: inherit;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: opacity 0.2s var(--ease), transform 0.2s var(--ease);
}
.btn-primary:hover { opacity: 0.88; transform: translateY(-1px); }
.btn-primary:active { transform: scale(0.97); }

.btn-ghost {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 20px;
  background: transparent;
  color: var(--text);
  border: 1px solid var(--border);
  border-radius: 8px;
  font-family: inherit;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: border-color 0.2s var(--ease), color 0.2s var(--ease), transform 0.2s var(--ease);
}
.btn-ghost:hover { border-color: var(--border-h); color: var(--text); transform: translateY(-1px); }

.btn-full { width: 100%; }

/* ── Navigation ── */
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  z-index: 100;
  transition: background 0.3s var(--ease), border-color 0.3s var(--ease), backdrop-filter 0.3s;
  border-bottom: 1px solid transparent;
}
.nav--scrolled {
  background: rgba(10, 10, 11, 0.85);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom-color: rgba(255, 255, 255, 0.07);
}

.nav-inner {
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 48px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.nav-logo {
  width: 28px;
  height: 28px;
  background: var(--accent);
  border: none;
  border-radius: 7px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  flex-shrink: 0;
  transition: opacity 0.15s;
}
.nav-logo span {
  font-size: 0.7rem;
  font-weight: 600;
  color: #fff;
  letter-spacing: -0.02em;
  line-height: 1;
}
.nav-logo:hover { opacity: 0.85; }

.nav-center {
  display: flex;
  align-items: center;
  gap: 4px;
}
.nav-link {
  background: none;
  border: none;
  color: var(--muted);
  cursor: pointer;
  font-family: inherit;
  font-size: 0.875rem;
  font-weight: 400;
  padding: 6px 12px;
  border-radius: 6px;
  transition: color 0.15s, background 0.15s;
}
.nav-link:hover { color: var(--text); background: rgba(255,255,255,0.04); }
.nav-link--active { color: var(--text); }

.nav-right {
  display: flex;
  align-items: center;
  gap: 12px;
}

.locale-toggle {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--muted);
  letter-spacing: 0.06em;
  user-select: none;
}
.locale-sep { opacity: 0.3; }
.locale-opt--active { color: var(--text); }

.btn-nav-cta {
  padding: 6px 14px;
  background: var(--accent);
  color: #fff;
  border: none;
  border-radius: 999px;
  font-family: inherit;
  font-size: 0.8rem;
  font-weight: 500;
  cursor: pointer;
  transition: opacity 0.15s;
}
.btn-nav-cta:hover { opacity: 0.85; }

.hamburger {
  display: none;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  width: 28px;
  height: 28px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
}
.hamburger span {
  display: block;
  width: 100%;
  height: 1.5px;
  background: var(--text);
  border-radius: 2px;
  transition: all 0.25s var(--ease);
  transform-origin: center;
}
.hamburger--open span:nth-child(1) { transform: translateY(6.5px) rotate(45deg); }
.hamburger--open span:nth-child(2) { opacity: 0; transform: scaleX(0); }
.hamburger--open span:nth-child(3) { transform: translateY(-6.5px) rotate(-45deg); }

/* Mobile overlay */
.nav-overlay {
  position: fixed;
  inset: 0;
  background: var(--bg);
  z-index: 99;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
}
.nav-overlay-link {
  background: none;
  border: none;
  color: var(--text);
  font-family: inherit;
  font-size: 1.5rem;
  font-weight: 300;
  cursor: pointer;
  padding: 8px 24px;
  transition: color 0.15s;
}
.nav-overlay-link:hover { color: var(--accent); }
.nav-overlay-cta { margin-top: 16px; font-size: 0.9rem; }

/* ── Footer ── */
.footer {
  border-top: 1px solid var(--border);
  padding: 40px 0;
}
.footer-inner {
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 48px;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 24px;
  flex-wrap: wrap;
}
.footer-name {
  font-size: 0.875rem;
  color: var(--muted);
  margin-bottom: 16px;
}
.footer-socials {
  display: flex;
  gap: 20px;
}
.social-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: var(--muted);
  text-decoration: none;
  font-size: 0.8rem;
  transition: color 0.15s;
}
.social-link:hover { color: var(--accent); }
.footer-built {
  font-family: 'Courier New', monospace;
  font-size: 0.75rem;
  color: var(--muted);
}

/* ── Responsive ── */
@media (max-width: 768px) {
  .nav-inner { padding: 0 24px; }
  .nav-center { display: none; }
  .hamburger { display: flex; }
  .section-wrap { padding: 64px 24px; }
  .footer-inner { padding: 0 24px; }
}
@media (max-width: 480px) {
  .section-wrap { padding: 48px 20px; }
  .nav-inner { padding: 0 20px; }
  .footer-inner { padding: 0 20px; flex-direction: column; }
}
</style>
