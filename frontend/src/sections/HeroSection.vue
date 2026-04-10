<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  const els = document.querySelectorAll('[data-animate]')
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('is-visible'); obs.unobserve(e.target) }
    })
  }, { threshold: 0.05 })
  els.forEach(el => obs.observe(el))
})
</script>

<template>
  <section id="hero" class="hero">
    <div class="hero-glow" aria-hidden="true"></div>
    <div class="hero-inner">

      <!-- Badge -->
      <div class="badge" data-animate style="--i:0">
        <span class="badge-dot"></span>
        Available for new projects
      </div>

      <!-- Headline -->
      <h1 class="hero-headline" data-animate style="--i:1">
        Backend engineer scaling systems to
        <em class="serif-italic">20M+ records</em>
        per pipeline
      </h1>

      <!-- Subline -->
      <p class="hero-sub" data-animate style="--i:2">
        I build reliable, event-driven backend systems using Python, RabbitMQ and AWS.
      </p>

      <!-- CTAs -->
      <div class="hero-ctas" data-animate style="--i:3">
        <a href="#contact" class="btn-primary" @click.prevent="document.getElementById('contact').scrollIntoView({behavior:'smooth'})">
          Book a 15-min call
        </a>
        <a href="#experience" class="btn-ghost" @click.prevent="document.getElementById('experience').scrollIntoView({behavior:'smooth'})">
          View my work
        </a>
      </div>
      <p class="hero-microcopy" data-animate style="--i:4">
        No commitment — just a quick technical chat
      </p>

      <!-- Stats strip -->
      <div class="hero-stats" data-animate style="--i:5">
        <div class="stat">
          <span class="stat-value">20M+</span>
          <span class="stat-label">Records per run</span>
        </div>
        <div class="stat">
          <span class="stat-value">~0</span>
          <span class="stat-label">Manual ops remaining</span>
        </div>
        <div class="stat">
          <span class="stat-value">3+</span>
          <span class="stat-label">Years in prod</span>
        </div>
        <div class="stat">
          <span class="stat-value">150%</span>
          <span class="stat-label">Organic traffic growth</span>
        </div>
      </div>

    </div>
  </section>
</template>

<style scoped>
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  overflow: hidden;
  padding-top: 60px;
}

.hero-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -60%);
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(59,130,246,0.06) 0%, transparent 70%);
  filter: blur(80px);
  pointer-events: none;
}

.hero-inner {
  position: relative;
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 48px;
  z-index: 1;
}

/* Badge */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 5px 12px;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 400;
  color: #a1a1aa;
  background: rgba(255,255,255,0.03);
  margin-bottom: 32px;
}
.badge-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #22c55e;
  animation: pulse-dot 2s infinite;
  flex-shrink: 0;
}
@keyframes pulse-dot {
  0%, 100% { box-shadow: 0 0 0 0 rgba(34,197,94,0.4); }
  50%       { box-shadow: 0 0 0 5px rgba(34,197,94,0); }
}

/* Headline */
.hero-headline {
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 600;
  line-height: 1.1;
  letter-spacing: -0.03em;
  max-width: 760px;
  margin-bottom: 24px;
  color: #f4f4f5;
}
.serif-italic {
  font-family: 'Instrument Serif', Georgia, serif;
  font-style: italic;
  font-weight: 400;
  color: var(--accent);
}

/* Sub */
.hero-sub {
  font-size: clamp(1rem, 2vw, 1.125rem);
  font-weight: 300;
  color: #71717a;
  max-width: 480px;
  margin-bottom: 40px;
  line-height: 1.7;
}

/* CTAs */
.hero-ctas {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}
/* btn-primary / btn-ghost from App.vue global */

.hero-microcopy {
  font-size: 0.75rem;
  color: #52525b;
  margin-bottom: 64px;
}

/* Stats */
.hero-stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 32px;
  padding-top: 40px;
  border-top: 1px solid rgba(255,255,255,0.07);
}
.stat { display: flex; flex-direction: column; gap: 4px; }
.stat-value {
  font-size: 1.5rem;
  font-weight: 600;
  color: #f4f4f5;
  letter-spacing: -0.02em;
}
.stat-label { font-size: 0.75rem; color: #71717a; font-weight: 300; }

@media (max-width: 768px) {
  .hero-inner { padding: 0 24px; }
  .hero-stats { grid-template-columns: repeat(2, 1fr); gap: 24px; }
}
@media (max-width: 480px) {
  .hero-inner { padding: 0 20px; }
  .hero-stats { grid-template-columns: repeat(2, 1fr); gap: 16px; }
  .hero-ctas { flex-direction: column; align-items: flex-start; }
}
</style>
