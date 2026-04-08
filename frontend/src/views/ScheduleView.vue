<script setup>
import { ref, onMounted } from 'vue'
import { getSchedule } from '../api/schedule'

const calendlyUrl = ref(null)
const message = ref('')
const error = ref(null)

onMounted(async () => {
  try {
    const data = await getSchedule()
    calendlyUrl.value = data.calendly_url
    message.value = data.message
  } catch {
    error.value = 'Could not load scheduling info. Please try again later.'
  }
})
</script>

<template>
  <section class="schedule">
    <h1>Schedule a Call</h1>
    <p class="subtitle">{{ message || 'Pick a time that works best for you.' }}</p>

    <div v-if="error" class="feedback error">{{ error }}</div>

    <a v-if="calendlyUrl" :href="calendlyUrl" target="_blank" rel="noopener noreferrer" class="btn-calendly">
      Open Calendly →
    </a>

    <p v-if="calendlyUrl" class="hint">
      You'll be redirected to Calendly to pick a date and time.
    </p>
  </section>
</template>

<style scoped>
.schedule {
  text-align: center;
}

.btn-calendly {
  display: inline-block;
  margin-top: 2rem;
  padding: 0.875rem 2rem;
  background: var(--color-accent);
  color: #fff;
  border-radius: 8px;
  font-weight: 600;
  text-decoration: none;
  font-size: 1.05rem;
  transition: opacity 0.15s;
}

.btn-calendly:hover {
  opacity: 0.85;
}

.hint {
  margin-top: 1rem;
  font-size: 0.875rem;
  color: var(--color-muted);
}
</style>
