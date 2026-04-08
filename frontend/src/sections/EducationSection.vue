<script setup>
import { computed } from 'vue'
import { useLocale } from '../composables/useLocale.js'

const { t, locale } = useLocale()
const degree = computed(() => t('education.degree'))
const courses = computed(() => t('education.courses'))
</script>

<template>
  <section id="education">
    <h2 class="section-title">{{ t('education.title') }}</h2>

    <div class="degree-card card">
      <div class="degree-header">
        <div>
          <h3 class="degree-name">{{ degree.name }}</h3>
          <p class="degree-institution">{{ degree.institution }}</p>
          <p class="degree-location">{{ degree.location }}</p>
        </div>
        <div class="degree-meta">
          <span class="degree-period">{{ degree.period }}</span>
          <span class="degree-status">{{ degree.status }}</span>
        </div>
      </div>
    </div>

    <h3 class="certs-title">{{ t('education.certifications') }}</h3>

    <ul class="certs-list">
      <li v-for="course in courses" :key="course.name" class="cert-item">
        <div class="cert-info">
          <span class="cert-name">{{ course.name }}</span>
          <span class="cert-issuer">{{ course.issuer }}</span>
        </div>
        <span class="cert-year">{{ course.year }}</span>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.degree-card {
  margin-bottom: 2.5rem;
}

.degree-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
  flex-wrap: wrap;
}

.degree-name {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 0.35rem;
}

.degree-institution {
  color: var(--accent);
  font-size: 0.95rem;
  font-weight: 600;
  margin-bottom: 0.2rem;
}

.degree-location {
  color: var(--muted);
  font-size: 0.85rem;
}

.degree-meta {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.4rem;
}

.degree-period {
  font-size: 0.85rem;
  color: var(--muted);
}

.degree-status {
  background: rgba(59, 130, 246, 0.15);
  color: var(--accent);
  border: 1px solid rgba(59, 130, 246, 0.3);
  border-radius: 999px;
  padding: 0.2rem 0.75rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.certs-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 1.25rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  font-size: 0.8rem;
  color: var(--muted);
}

.certs-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.cert-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.85rem 0;
  border-bottom: 1px solid var(--border);
  gap: 1rem;
}

.cert-item:last-child {
  border-bottom: none;
}

.cert-info {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}

.cert-name {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text);
}

.cert-issuer {
  font-size: 0.8rem;
  color: var(--muted);
}

.cert-year {
  font-size: 0.8rem;
  color: var(--muted);
  white-space: nowrap;
}
</style>
