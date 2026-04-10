<template>
  <section id="experience">
    <div class="section-wrap">
      <div class="section-label" data-animate style="--i:0">{{ t('howICanHelp.title') }}</div>

      <div class="help-grid">
        <div
          v-for="(card, i) in cards"
          :key="card.title"
          class="card help-card"
          data-animate
          :style="{ '--i': i + 1 }"
        >
          <div class="help-icon">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" v-html="card.iconPath"></svg>
          </div>
          <h3 class="help-title">{{ card.title }}</h3>
          <p class="help-desc">{{ card.desc }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useLocale } from '../composables/useLocale'

const { t } = useLocale()
const cards = t('howICanHelp.items')
</script>

<style scoped>
.help-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.help-card {
  padding: 24px;
  cursor: default;
}

.help-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: rgba(59, 130, 246, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--accent);
  margin-bottom: 16px;
  flex-shrink: 0;
}

.help-title {
  font-size: 0.9375rem;
  font-weight: 500;
  color: #f4f4f5;
  margin-bottom: 8px;
}

.help-desc {
  font-size: 0.85rem;
  font-weight: 300;
  color: #71717a;
  line-height: 1.65;
}

@media (max-width: 640px) {
  .help-grid { grid-template-columns: 1fr; }
}
</style>
