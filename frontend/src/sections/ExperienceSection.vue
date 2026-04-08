<script setup>
import { computed } from 'vue'
import { useLocale } from '../composables/useLocale.js'

const { t, locale } = useLocale()
const items = computed(() => t('experience.items'))
</script>

<template>
  <section id="experience">
    <h2 class="section-title">{{ t('experience.title') }}</h2>

    <div class="timeline">
      <div
        v-for="(item, index) in items"
        :key="index"
        class="timeline-card"
        :class="{ current: index === 0 }"
      >
        <div class="card-header">
          <div class="card-title-group">
            <h3 class="card-role">{{ item.role }}</h3>
            <span class="card-company">{{ item.company }} · <span class="card-type">{{ item.type }}</span></span>
          </div>
          <div class="card-period">
            <span v-if="index === 0" class="current-badge">● {{ t('experience.present') }}</span>
            {{ item.start }} – {{ item.end }}
          </div>
        </div>

        <ul class="card-bullets">
          <li v-for="(bullet, bi) in item.bullets" :key="bi">{{ bullet }}</li>
        </ul>
      </div>
    </div>
  </section>
</template>

<style scoped>
.timeline {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.timeline-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.75rem;
  position: relative;
  transition: border-color 0.2s;
}

.timeline-card.current {
  border-left: 3px solid var(--accent);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 1.25rem;
  flex-wrap: wrap;
}

.card-role {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--accent);
  margin-bottom: 0.2rem;
}

.card-company {
  font-size: 0.9rem;
  color: var(--text);
  font-weight: 500;
}

.card-type {
  color: var(--muted);
}

.card-period {
  font-size: 0.8rem;
  color: var(--muted);
  text-align: right;
  white-space: nowrap;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.25rem;
}

.current-badge {
  color: var(--accent);
  font-weight: 600;
  font-size: 0.75rem;
  letter-spacing: 0.03em;
}

.card-bullets {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
}

.card-bullets li {
  position: relative;
  padding-left: 1.1rem;
  color: var(--muted);
  font-size: 0.9rem;
  line-height: 1.65;
}

.card-bullets li::before {
  content: '–';
  position: absolute;
  left: 0;
  color: var(--accent);
  font-weight: 700;
}
</style>
