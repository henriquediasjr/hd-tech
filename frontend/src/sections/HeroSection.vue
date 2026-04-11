<script setup>
import { onMounted } from 'vue'
import { useLocale } from '../composables/useLocale'

const { t } = useLocale()

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

    <!-- Animated floating orbs -->
    <div class="orb orb-1" aria-hidden="true"></div>
    <div class="orb orb-2" aria-hidden="true"></div>

    <div class="hero-inner">
      <div class="hero-content">

        <!-- Left: text -->
        <div class="hero-text">
          <h1 class="hero-headline" data-animate style="--i:0">
            <span class="brand-hd">HD</span><span class="brand-tech"> Tech</span>
          </h1>

          <p class="hero-tagline" data-animate style="--i:1">
            {{ t('hero.tagline') }}
          </p>

          <p class="hero-sub" data-animate style="--i:2">
            {{ t('hero.subheadline') }}
          </p>

          <div class="hero-ctas" data-animate style="--i:3">
            <a href="#contact" class="btn-primary" @click.prevent="document.getElementById('contact').scrollIntoView({behavior:'smooth'})">
              {{ t('hero.primaryCta') }}
            </a>
            <a href="#experience" class="btn-ghost" @click.prevent="document.getElementById('experience').scrollIntoView({behavior:'smooth'})">
              {{ t('hero.secondaryCta') }}
            </a>
          </div>

          <div class="availability" data-animate style="--i:4">
            <span class="badge-dot"></span>
            <span>Available for new projects</span>
          </div>
        </div>

        <!-- Right: animated visual -->
        <div class="hero-visual" data-animate style="--i:2" aria-hidden="true">
          <div class="code-card">
            <div class="code-header">
              <span class="dot red"></span>
              <span class="dot yellow"></span>
              <span class="dot green"></span>
            </div>
            <pre class="code-body"><span class="c-kw">async def</span> <span class="c-fn">process_pipeline</span>():
  events = <span class="c-kw">await</span> queue.<span class="c-fn">consume</span>()
  <span class="c-kw">async for</span> batch <span class="c-kw">in</span> events:
    <span class="c-kw">await</span> db.<span class="c-fn">bulk_insert</span>(batch)
    metrics.<span class="c-fn">record</span>(len(batch))
  <span class="c-cm"># 20M+ records/run ✓</span></pre>
            <div class="code-cursor"></div>
          </div>
        </div>

      </div>

      <!-- Stats strip -->
      <div class="hero-stats" data-animate style="--i:4">
        <div v-for="(stat, i) in t('socialProof.items')" :key="i" class="stat">
          <span class="stat-value">{{ stat.value }}</span>
          <span class="stat-label">{{ stat.label }}</span>
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
  padding: 80px 0 48px;
}

.hero-glow {
  position: absolute;
  top: 40%;
  left: 30%;
  transform: translate(-50%, -50%);
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(59,130,246,0.05) 0%, transparent 70%);
  filter: blur(100px);
  pointer-events: none;
}

/* Floating orbs */
.orb {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  opacity: 0.4;
}
.orb-1 {
  width: 300px;
  height: 300px;
  top: 15%;
  right: 5%;
  background: radial-gradient(circle, rgba(59,130,246,0.08) 0%, transparent 70%);
  animation: float 8s ease-in-out infinite;
}
.orb-2 {
  width: 200px;
  height: 200px;
  bottom: 20%;
  right: 20%;
  background: radial-gradient(circle, rgba(139,92,246,0.06) 0%, transparent 70%);
  animation: float 12s ease-in-out infinite reverse;
}
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50%       { transform: translateY(-24px); }
}

.hero-inner {
  position: relative;
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 48px;
  z-index: 1;
  width: 100%;
}

.hero-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  gap: 60px;
}

/* Text side */
.hero-text {
  display: flex;
  flex-direction: column;
}

/* Brand headline */
.hero-headline {
  font-size: clamp(3rem, 8vw, 5.5rem);
  font-weight: 700;
  line-height: 1;
  letter-spacing: -0.04em;
  margin-bottom: 16px;
}
.brand-hd   { color: var(--accent); }
.brand-tech { color: #f4f4f5; }

/* One-liner role tagline */
.hero-tagline {
  font-size: 0.8rem;
  font-weight: 400;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #52525b;
  margin-bottom: 20px;
}

.hero-sub {
  font-size: 1rem;
  font-weight: 300;
  color: #71717a;
  max-width: 380px;
  margin-bottom: 32px;
  line-height: 1.7;
}

.hero-ctas {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.availability {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.75rem;
  color: #52525b;
}
.badge-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #22c55e;
  flex-shrink: 0;
  animation: pulse-dot 2s infinite;
}
@keyframes pulse-dot {
  0%, 100% { box-shadow: 0 0 0 0 rgba(34,197,94,0.4); }
  50%       { box-shadow: 0 0 0 5px rgba(34,197,94,0); }
}

/* Visual side – code card */
.hero-visual {
  display: flex;
  justify-content: center;
  align-items: center;
}

.code-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px;
  overflow: hidden;
  width: 100%;
  max-width: 380px;
  animation: float 7s ease-in-out infinite;
  box-shadow: 0 24px 60px rgba(0,0,0,0.4);
}

.code-header {
  display: flex;
  gap: 6px;
  padding: 12px 16px;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}
.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.dot.red    { background: #ff5f57; }
.dot.yellow { background: #febc2e; }
.dot.green  { background: #28c840; }

.code-body {
  font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
  font-size: 0.78rem;
  line-height: 1.7;
  padding: 20px;
  margin: 0;
  color: #a1a1aa;
  white-space: pre;
}
.c-kw  { color: #818cf8; }
.c-fn  { color: #60a5fa; }
.c-cm  { color: #4b5563; font-style: italic; }

.code-cursor {
  display: inline-block;
  width: 8px;
  height: 1em;
  background: #60a5fa;
  margin: 0 20px 16px;
  border-radius: 1px;
  animation: blink 1.2s step-end infinite;
}
@keyframes blink {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0; }
}

/* Stats strip */
.hero-stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0;
  margin-top: 48px;
  padding-top: 28px;
  border-top: 1px solid rgba(255,255,255,0.07);
}
.stat {
  display: flex;
  flex-direction: column;
  gap: 5px;
  padding-right: 24px;
  border-right: 1px solid rgba(255,255,255,0.06);
}
.stat:last-child { border-right: none; padding-right: 0; }
.stat-value {
  font-size: 1.375rem;
  font-weight: 600;
  color: #f4f4f5;
  letter-spacing: -0.02em;
}
.stat-label { font-size: 0.68rem; color: #52525b; font-weight: 300; line-height: 1.5; }

/* Animations */
[data-animate] {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity 0.6s ease calc(var(--i, 0) * 120ms),
              transform 0.6s ease calc(var(--i, 0) * 120ms);
}
[data-animate].is-visible {
  opacity: 1;
  transform: none;
}

@media (max-width: 900px) {
  .hero-content {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  .hero-visual { order: -1; }
  .code-card { max-width: 340px; }
}
@media (max-width: 768px) {
  .hero-inner { padding: 0 24px; }
  .hero-stats { grid-template-columns: repeat(2, 1fr); gap: 0; }
  .stat { padding-right: 0; border-right: none; padding-bottom: 20px; }
  .stat:nth-child(odd) { padding-right: 24px; border-right: 1px solid rgba(255,255,255,0.06); }
}
@media (max-width: 480px) {
  .hero { padding: 72px 0 40px; }
  .hero-inner { padding: 0 20px; }
  .hero-headline { font-size: clamp(2.5rem, 14vw, 3.5rem); }
  .hero-ctas  { flex-direction: column; align-items: flex-start; }
  .hero-visual { display: none; }
  .hero-stats { grid-template-columns: repeat(2, 1fr); }
}
</style>
