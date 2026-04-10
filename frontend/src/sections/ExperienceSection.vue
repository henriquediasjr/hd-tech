<template>
  <section>
    <div class="section-wrap">
      <div class="section-label" data-animate style="--i:0">Experience</div>

      <div class="timeline">
        <div
          v-for="(job, i) in jobs"
          :key="job.company"
          class="card timeline-card"
          data-animate
          :style="{ '--i': i + 1 }"
        >
          <div class="timeline-dot"></div>

          <div class="timeline-header">
            <div class="timeline-left">
              <span class="timeline-company">{{ job.company }}</span>
              <span class="timeline-role">{{ job.role }}</span>
            </div>
            <div class="timeline-right">
              <span class="timeline-period">{{ job.period }}</span>
              <span v-if="job.current" class="timeline-badge">&#9679; Present</span>
            </div>
          </div>

          <ul class="timeline-bullets">
            <li v-for="bullet in job.bullets" :key="bullet">{{ bullet }}</li>
          </ul>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const jobs = [
  {
    company: 'QuiteJá',
    role:    'Backend Developer',
    period:  'Jan 2025 – Present',
    current: true,
    bullets: [
      'Developed and maintained Python microservices for financial system integrations and payment automation',
      'Built and optimized data pipelines for importing client portfolios and automating billing workflows',
      'Managed infrastructure using AWS (ECS, S3, CloudWatch), RabbitMQ, and SFTP',
    ],
  },
  {
    company: 'Inuar',
    role:    'Full-Stack Developer',
    period:  'Dec 2021 – Feb 2024',
    current: false,
    bullets: [
      'Built full-stack applications using Laravel + Vue.js with custom REST API and role-based auth',
      'Led Drupal 6→10 migration for a major news portal — all custom modules preserved, zero visual regressions',
      'Investigated and remediated incidents in compromised WordPress environments, implemented hardening',
    ],
  },
  {
    company: 'Gradeup',
    role:    'Developer & IT Support',
    period:  'Jun 2022 – Jun 2024',
    current: false,
    bullets: [
      '150% organic traffic growth via SEO audits with Lighthouse, maintained score above 85',
      'Implemented VR healthcare management platform (Oculus + Vue.js) with custom REST API and role-based auth',
      'Automated CRM lead pipelines in RD Station, cutting manual reporting overhead for the marketing team',
    ],
  },
]
</script>

<style scoped>
.timeline {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding-left: 28px;
}
.timeline::before {
  content: '';
  position: absolute;
  left: 7px;
  top: 0;
  bottom: 0;
  width: 1px;
  background: rgba(59, 130, 246, 0.4);
}

.timeline-card {
  padding: 24px;
  position: relative;
  border-left: 2px solid transparent;
  transition: border-color 0.25s var(--ease), border-left-color 0.25s var(--ease), transform 0.25s var(--ease);
}
.timeline-card:hover { border-left-color: var(--accent); }

.timeline-dot {
  position: absolute;
  left: -35px;
  top: 28px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  border: 2px solid var(--accent);
  background: var(--bg);
}

.timeline-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 16px;
  flex-wrap: wrap;
}
.timeline-left { display: flex; flex-direction: column; gap: 3px; }
.timeline-right { display: flex; flex-direction: column; align-items: flex-end; gap: 4px; flex-shrink: 0; }

.timeline-company { font-size: 0.9375rem; font-weight: 500; color: #f4f4f5; }
.timeline-role    { font-size: 0.8125rem; color: #71717a; font-weight: 300; }
.timeline-period  { font-size: 0.75rem; color: #52525b; font-family: 'Courier New', monospace; }
.timeline-badge   { font-size: 0.7rem; color: var(--accent); font-weight: 500; }

.timeline-bullets {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.timeline-bullets li {
  position: relative;
  padding-left: 14px;
  font-size: 0.85rem;
  font-weight: 300;
  color: #a1a1aa;
  line-height: 1.6;
}
.timeline-bullets li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0.6em;
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: rgba(59,130,246,0.6);
}

@media (max-width: 480px) {
  .timeline { padding-left: 20px; }
  .timeline-header { flex-direction: column; gap: 8px; }
  .timeline-right { align-items: flex-start; }
}
</style>
