<template>
  <section id="stack">
    <div class="section-wrap">
      <div class="section-label" data-animate style="--i:0">{{ t('skills.title') }}</div>

      <div class="stack-grid">
        <div
          v-for="(cat, i) in t('skills.categories')"
          :key="cat.name"
          class="stack-card"
          :style="{ '--cat-color': cat.color, '--i': i + 1 }"
          data-animate
        >
          <h3 class="stack-cat">{{ cat.name }}</h3>
          <div class="stack-tags">
            <span v-for="item in cat.items" :key="item" class="stack-tag">{{ item }}</span>
          </div>
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
.stack-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 16px;
}

.stack-card {
  background: #111113;
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-left: 3px solid var(--cat-color);
  border-radius: 12px;
  padding: 20px;
  transition: border-color 0.25s var(--ease), transform 0.25s var(--ease), box-shadow 0.25s var(--ease);
}
.stack-card:hover {
  border-color: rgba(255, 255, 255, 0.13);
  border-left-color: var(--cat-color);
  transform: translateY(-2px);
  box-shadow: 0 12px 40px rgba(0,0,0,0.4);
}

.stack-cat {
  font-size: 0.8125rem;
  font-weight: 500;
  color: #f4f4f5;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.stack-cat::before {
  content: '';
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--cat-color);
  flex-shrink: 0;
}

.stack-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.stack-tag {
  font-family: 'Courier New', monospace;
  font-size: 0.7rem;
  padding: 3px 10px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 6px;
  color: #71717a;
}
</style>
