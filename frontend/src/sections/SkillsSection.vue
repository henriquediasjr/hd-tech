<script setup>
import { computed } from 'vue'
import { useLocale } from '../composables/useLocale.js'

const { t, locale } = useLocale()
const categories = computed(() => t('skills.categories'))
</script>

<template>
  <section id="skills">
    <h2 class="section-title">{{ t('skills.title') }}</h2>

    <div class="categories">
      <div v-for="cat in categories" :key="cat.name" class="category">
        <h3 class="category-name">{{ cat.name }}</h3>
        <div class="pills">
          <span v-for="item in cat.items" :key="item" class="pill">{{ item }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.categories {
  display: flex;
  flex-direction: column;
  gap: 1.75rem;
}

.category-name {
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-bottom: 0.75rem;
}

.pills {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.pill {
  background: var(--surface2);
  color: var(--text);
  border: 1px solid var(--border);
  border-radius: 999px;
  padding: 0.3rem 0.9rem;
  font-size: 0.85rem;
  font-weight: 500;
  transition: background 0.15s, border-color 0.15s, color 0.15s;
  cursor: default;
}

.pill:hover {
  background: rgba(59, 130, 246, 0.15);
  border-color: var(--accent);
  color: var(--accent);
}
</style>
