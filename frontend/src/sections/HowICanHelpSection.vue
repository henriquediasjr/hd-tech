<template>
  <section id="experience">
    <div class="section-wrap">
      <div class="section-label" data-animate style="--i:0">How I Can Help</div>

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
const cards = [
  {
    title: 'Scalable Backend Systems',
    desc:  'Python microservices, data pipelines, handling high volumes in production without degradation.',
    iconPath: '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
  },
  {
    title: 'Large-scale Data Pipelines',
    desc:  'Processing data efficiently using RabbitMQ, Parquet, S3 and async batch patterns that scale.',
    iconPath: '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"/>',
  },
  {
    title: 'Microservices Architecture',
    desc:  'Event-driven services using Django, REST APIs and AWS ECS that stay observable and maintainable.',
    iconPath: '<circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M6 21V9a9 9 0 0 0 9 9"/>',
  },
  {
    title: 'Workflow Automation',
    desc:  'Replace manual workflows with structured, reliable automations that eliminate human error.',
    iconPath: '<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/>',
  },
]
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
