<template>
  <section id="projects">
    <div class="section-wrap">
      <div class="section-label" data-animate style="--i:0">{{ t('projects.title') }}</div>

      <div class="card proj-card" data-animate style="--i:1">
        <div class="proj-content">
          <h2 class="proj-title">{{ t('projects.items.0.name') }}</h2>
          <p class="proj-desc">
            {{ t('projects.items.0.desc') }}
          </p>
          <div class="proj-tags">
            <span v-for="tag in t('projects.items.0.tags')" :key="tag" class="tag">{{ tag }}</span>
          </div>
        </div>
        <div class="proj-preview">
          <span class="proj-preview-text">Preview soon</span>
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
.proj-card {
  padding: 32px;
  display: flex;
  align-items: flex-start;
  gap: 32px;
  cursor: default;
}

.proj-content { flex: 1; }
.proj-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: #f4f4f5;
  margin-bottom: 12px;
}
.proj-desc {
  font-size: 0.875rem;
  font-weight: 300;
  color: #71717a;
  line-height: 1.7;
  margin-bottom: 20px;
  max-width: 560px;
}
.proj-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.tag {
  font-family: 'Courier New', monospace;
  font-size: 0.6875rem;
  background: #1a1a1e;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 6px;
  padding: 2px 8px;
  color: #71717a;
}

.proj-preview {
  width: 160px;
  height: 120px;
  border: 1px dashed rgba(255,255,255,0.1);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.proj-preview-text {
  font-family: 'Courier New', monospace;
  font-size: 0.7rem;
  color: #3f3f46;
}

@media (max-width: 640px) {
  .proj-card { flex-direction: column; }
  .proj-preview { width: 100%; }
}
</style>
