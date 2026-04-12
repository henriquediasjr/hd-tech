<template>
  <section id="experience">
    <div class="section-wrap">
      <div class="section-label" data-animate style="--i:0">{{ t('howICanHelp.title') }}</div>

      <div class="help-grid">
        <div
          v-for="(card, i) in cards"
          :key="i"
          class="card help-card"
          :class="{
            'php-card': card.icon === 'php',
            'ai-card':  card.icon === 'ai',
          }"
          data-animate
          :style="{ '--i': i + 1 }"
        >
          <div class="help-icon" :class="{ 'php-icon': card.icon === 'php', 'ai-icon': card.icon === 'ai' }">
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
import { computed } from 'vue'
import { useLocale } from '../composables/useLocale'

const { t } = useLocale()
const cards = computed(() => t('howICanHelp.items'))
</script>

<style scoped>
.help-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.help-card {
  padding: 24px;
  cursor: default;
}

/* PHP card — violet accent */
.php-card {
  border-color: rgba(139, 92, 246, 0.25) !important;
  background: rgba(139, 92, 246, 0.04) !important;
}
.php-card:hover {
  border-color: rgba(139, 92, 246, 0.4) !important;
  box-shadow: 0 12px 40px rgba(139,92,246,0.1) !important;
}

/* AI card — amber accent */
.ai-card {
  border-color: rgba(251, 191, 36, 0.2) !important;
  background: rgba(251, 191, 36, 0.03) !important;
}
.ai-card:hover {
  border-color: rgba(251, 191, 36, 0.38) !important;
  box-shadow: 0 12px 40px rgba(251,191,36,0.08) !important;
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
.php-icon {
  background: rgba(139, 92, 246, 0.15);
  color: #a78bfa;
}
.ai-icon {
  background: rgba(251, 191, 36, 0.12);
  color: #fbbf24;
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

@media (max-width: 900px) {
  .help-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 640px) {
  .help-grid { grid-template-columns: 1fr; }
}
</style>
