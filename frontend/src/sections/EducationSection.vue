<template>
  <section id="education">
    <div class="section-wrap">
      <div class="section-label" data-animate style="--i:0">{{ t('education.title') }}</div>

      <div class="edu-entries" data-animate style="--i:1">
        <div class="edu-row">
          <div class="edu-meta">
            <span class="edu-school">{{ t('education.degree.institution') }}</span>
            <span class="edu-period">{{ t('education.degree.period') }}</span>
          </div>
          <span class="edu-degree">{{ t('education.degree.name') }}</span>
        </div>
      </div>

      <div class="cert-section" data-animate style="--i:2">
        <p class="cert-heading">{{ t('education.certifications') }}</p>
        <ul class="cert-list">
          <li v-for="cert in t('education.courses')" :key="cert.name">
            {{ cert.name }} — {{ cert.issuer }}, {{ cert.year }}
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useLocale } from '../composables/useLocale'

const { t } = useLocale()
</script>

<style scoped>
.edu-entries {
  display: flex;
  flex-direction: column;
  gap: 0;
  border-top: 1px solid rgba(255,255,255,0.06);
  margin-bottom: 40px;
}

.edu-row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 24px;
  padding: 16px 0;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  flex-wrap: wrap;
}

.edu-meta {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.edu-degree {
  font-size: 0.875rem;
  font-weight: 500;
  color: #f4f4f5;
  order: -1;
  flex: 1;
  min-width: 220px;
}
.edu-school {
  font-size: 0.75rem;
  color: var(--accent);
  font-weight: 500;
}
.edu-period {
  font-family: 'Courier New', monospace;
  font-size: 0.7rem;
  color: #52525b;
}

.cert-section {}
.cert-heading {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #52525b;
  font-weight: 500;
  margin-bottom: 12px;
}
.cert-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.cert-list li {
  font-family: 'Courier New', monospace;
  font-size: 0.775rem;
  color: #71717a;
  padding-left: 14px;
  position: relative;
}
.cert-list li::before {
  content: '—';
  position: absolute;
  left: 0;
  color: #3f3f46;
}

@media (max-width: 480px) {
  .edu-row { flex-direction: column; gap: 4px; }
}
</style>
