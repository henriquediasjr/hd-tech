<template>
  <section id="experience">
    <div class="section-wrap">
      <div class="section-label" data-animate style="--i:0">{{ t('experience.title') }}</div>

      <div class="exp-list">
        <div
          v-for="(job, i) in t('experience.items')"
          :key="job.company"
          class="exp-card"
          data-animate
          :style="{ '--i': i + 1 }"
        >
          <div class="exp-header">
            <div class="exp-left">
              <div class="exp-company-row">
                <span class="exp-company">{{ job.company }}</span>
                <span class="exp-type-badge" :class="`badge--${job.icon}`">{{ job.type }}</span>
              </div>
              <span class="exp-role">{{ job.role }}</span>
            </div>
            <div class="exp-right">
              <span class="exp-period">{{ job.start }} – {{ job.end }}</span>
              <span v-if="job.end === t('experience.present') || job.end === 'Present' || job.end === 'Atual'" class="exp-live">
                <span class="live-dot"></span>{{ t('experience.present') }}
              </span>
            </div>
          </div>

          <ul class="exp-bullets">
            <li v-for="(bullet, bi) in job.bullets" :key="bi">{{ bullet }}</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useLocale } from '../composables/useLocale'

const { t } = useLocale()
</script>

<style scoped>
.exp-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.exp-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px 24px 22px;
  position: relative;
  overflow: hidden;
  transition: border-color 0.25s var(--ease), transform 0.25s var(--ease), box-shadow 0.25s var(--ease);
}
.exp-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--accent), transparent 60%);
  opacity: 0.5;
  transition: opacity 0.25s var(--ease);
}
.exp-card:hover {
  border-color: var(--border-h);
  transform: translateY(-2px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.4);
}
.exp-card:hover::before { opacity: 1; }

.exp-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 18px;
  flex-wrap: wrap;
}

.exp-left  { display: flex; flex-direction: column; gap: 5px; }
.exp-right { display: flex; flex-direction: column; align-items: flex-end; gap: 6px; flex-shrink: 0; }

.exp-company-row {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}
.exp-company {
  font-size: 1rem;
  font-weight: 500;
  color: #f4f4f5;
}
.exp-type-badge {
  font-size: 0.65rem;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 2px 8px;
  border-radius: 999px;
  border: 1px solid;
}
.badge--fintech {
  color: #60a5fa;
  border-color: rgba(96, 165, 250, 0.3);
  background: rgba(96, 165, 250, 0.06);
}
.badge--agency {
  color: #a78bfa;
  border-color: rgba(167, 139, 250, 0.3);
  background: rgba(167, 139, 250, 0.06);
}
.badge--education {
  color: #34d399;
  border-color: rgba(52, 211, 153, 0.3);
  background: rgba(52, 211, 153, 0.06);
}

.exp-role {
  font-size: 0.8125rem;
  color: #71717a;
  font-weight: 300;
}

.exp-period {
  font-size: 0.75rem;
  color: #52525b;
  font-family: 'JetBrains Mono', 'Courier New', monospace;
}
.exp-live {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 0.7rem;
  color: #22c55e;
  font-weight: 500;
}
.live-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #22c55e;
  animation: pulse-dot 2s infinite;
  flex-shrink: 0;
}
@keyframes pulse-dot {
  0%, 100% { box-shadow: 0 0 0 0 rgba(34,197,94,0.4); }
  50%       { box-shadow: 0 0 0 4px rgba(34,197,94,0); }
}

.exp-bullets {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.exp-bullets li {
  position: relative;
  padding-left: 14px;
  font-size: 0.85rem;
  font-weight: 300;
  color: #a1a1aa;
  line-height: 1.65;
}
.exp-bullets li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0.62em;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: rgba(59,130,246,0.55);
}

@media (max-width: 480px) {
  .exp-header { flex-direction: column; gap: 8px; }
  .exp-right  { align-items: flex-start; }
}
</style>
