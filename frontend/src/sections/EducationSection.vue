<template>
  <section id="education">
    <div class="section-wrap">
      <div class="section-label" data-animate style="--i:0">Education</div>

      <div class="edu-entries" data-animate style="--i:1">
        <div v-for="edu in education" :key="edu.degree" class="edu-row">
          <div class="edu-meta">
            <span class="edu-school">{{ edu.school }}</span>
            <span class="edu-period">{{ edu.period }}</span>
          </div>
          <span class="edu-degree">{{ edu.degree }}</span>
        </div>
      </div>

      <div class="cert-section" data-animate style="--i:2">
        <p class="cert-heading">Certifications</p>
        <ul class="cert-list">
          <li v-for="cert in certs" :key="cert">{{ cert }}</li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script setup>
const education = [
  {
    degree: 'B.Sc. Information Systems',
    school: 'PUC-PR',
    period: 'Jun 2025 – Mar 2029',
  },
  {
    degree: 'B.Sc. Computer Engineering',
    school: 'PUC-PR',
    period: 'Mar 2024 – Jun 2025 (transferred)',
  },
]

const certs = [
  'Harvard CS50W Django — Jan 2025',
  'Symfony Framework Hands-On — Udemy, Oct 2024',
  'PHP Bootcamp with CMS Project — Udemy, Dec 2022',
  'JavaScript Complete Course — Udemy, Oct 2021',
  'TOEFL 600 — English Fluent (TALKEN, 2014–2022)',
]
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
