<script setup>
import { computed } from 'vue'
import { useLocale } from '../composables/useLocale.js'

const { t, locale } = useLocale()
const stats = computed(() => t('about.stats'))
</script>

<template>
  <section id="about">
    <h2 class="section-title">{{ t('about.title') }}</h2>

    <p class="about-text">{{ t('about.text') }}</p>

    <div class="stats-row">
      <div v-for="stat in stats" :key="stat.value" class="stat-card">
        <span class="stat-value">{{ stat.value }}</span>
        <span class="stat-label">{{ stat.label }}</span>
      </div>
    </div>
  </section>
</template>

<style scoped>
.about-text {
  color: var(--muted);
  font-size: 1.05rem;
  line-height: 1.8;
  max-width: 700px;
  margin-bottom: 2.5rem;
}

.stats-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}

.stat-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 1.5rem 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  text-align: center;
}

.stat-value {
  font-size: 2.25rem;
  font-weight: 800;
  color: var(--accent);
  line-height: 1;
}

.stat-label {
  font-size: 0.875rem;
  color: var(--muted);
  font-weight: 500;
}

@media (max-width: 600px) {
  .stats-row {
    grid-template-columns: 1fr;
  }
}
</style>
