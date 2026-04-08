<script setup>
import { ref, onMounted, computed } from 'vue'
import { useLocale } from '../composables/useLocale.js'
import { useForm } from '../composables/useForm.js'
import { submitContact } from '../api/contact.js'
import { getSchedule } from '../api/schedule.js'

const { t, locale } = useLocale()

const calendlyUrl = ref(null)
const scheduleError = ref(false)

onMounted(async () => {
  try {
    const data = await getSchedule()
    calendlyUrl.value = data.calendly_url || data.url || null
  } catch {
    scheduleError.value = true
  }
})

const formData = ref({ name: '', email: '', message: '' })
const { loading, error, success, submit } = useForm(submitContact)

async function handleSubmit() {
  await submit({ ...formData.value })
  if (success.value) {
    formData.value = { name: '', email: '', message: '' }
  }
}

const submitLabel = computed(() =>
  loading.value ? t('contact.form.sending') : t('contact.form.submit')
)
</script>

<template>
  <section id="contact">
    <h2 class="section-title">{{ t('contact.title') }}</h2>
    <p class="contact-subtitle">{{ t('contact.subtitle') }}</p>

    <div class="contact-grid">
      <!-- Primary: Schedule -->
      <div class="schedule-card card">
        <div class="schedule-icon">📅</div>
        <h3 class="schedule-title">{{ t('contact.scheduleTitle') }}</h3>
        <p class="schedule-desc">
          {{ t('contact.subtitle') }}
        </p>
        <a
          v-if="calendlyUrl"
          :href="calendlyUrl"
          target="_blank"
          rel="noopener"
          class="btn-schedule"
        >
          {{ t('contact.scheduleBtn') }}
        </a>
        <span v-else-if="scheduleError" class="schedule-fallback">
          <a href="mailto:henriquediasjr@gmail.com" class="btn-schedule btn-schedule--email">
            henriquediasjr@gmail.com
          </a>
        </span>
        <span v-else class="schedule-loading">...</span>
      </div>

      <!-- Secondary: Contact form -->
      <div class="form-card card">
        <h3 class="form-title">{{ t('contact.formTitle') }}</h3>

        <div v-if="success" class="feedback success">{{ t('contact.form.success') }}</div>
        <div v-if="error" class="feedback error">{{ t('contact.form.error') }}</div>

        <form @submit.prevent="handleSubmit" novalidate>
          <div class="field">
            <label for="contact-name">{{ t('contact.form.name') }}</label>
            <input
              id="contact-name"
              v-model="formData.name"
              type="text"
              :placeholder="t('contact.form.namePlaceholder')"
              required
            />
          </div>

          <div class="field">
            <label for="contact-email">{{ t('contact.form.email') }}</label>
            <input
              id="contact-email"
              v-model="formData.email"
              type="email"
              :placeholder="t('contact.form.emailPlaceholder')"
              required
            />
          </div>

          <div class="field">
            <label for="contact-message">{{ t('contact.form.message') }}</label>
            <textarea
              id="contact-message"
              v-model="formData.message"
              rows="5"
              :placeholder="t('contact.form.messagePlaceholder')"
              required
            ></textarea>
          </div>

          <button type="submit" :disabled="loading">
            {{ submitLabel }}
          </button>
        </form>
      </div>
    </div>
  </section>
</template>

<style scoped>
.contact-subtitle {
  color: var(--muted);
  font-size: 1rem;
  margin-bottom: 2.5rem;
  max-width: 580px;
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  align-items: start;
}

.schedule-card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.75rem;
}

.schedule-icon {
  font-size: 2rem;
}

.schedule-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text);
}

.schedule-desc {
  font-size: 0.875rem;
  color: var(--muted);
  line-height: 1.6;
}

.btn-schedule {
  display: inline-block;
  margin-top: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: var(--accent);
  color: #fff;
  border-radius: var(--radius);
  font-weight: 600;
  font-size: 0.95rem;
  text-decoration: none;
  transition: background 0.15s;
}

.btn-schedule:hover {
  background: var(--accent-hover);
}

.btn-schedule--email {
  background: var(--surface2);
  font-size: 0.85rem;
  word-break: break-all;
}

.btn-schedule--email:hover {
  background: var(--border);
}

.schedule-loading {
  color: var(--muted);
  font-size: 0.875rem;
}

.form-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 1.25rem;
}

form {
  display: flex;
  flex-direction: column;
  gap: 1.1rem;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 0.375rem;
}

label {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

input,
textarea {
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  color: var(--text);
  font-family: inherit;
  font-size: 0.9rem;
  padding: 0.65rem 0.875rem;
  outline: none;
  transition: border-color 0.15s, box-shadow 0.15s;
  width: 100%;
}

input:focus,
textarea:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.12);
}

textarea {
  resize: vertical;
}

button[type='submit'] {
  align-self: flex-start;
  background: var(--accent);
  border: none;
  border-radius: var(--radius);
  color: #fff;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 600;
  padding: 0.7rem 1.5rem;
  transition: background 0.15s;
}

button[type='submit']:hover:not(:disabled) {
  background: var(--accent-hover);
}

button[type='submit']:disabled {
  opacity: 0.55;
  cursor: not-allowed;
}

.feedback {
  border-radius: var(--radius);
  font-size: 0.875rem;
  font-weight: 500;
  margin-bottom: 0.75rem;
  padding: 0.65rem 1rem;
}

.feedback.success {
  background: rgba(34, 197, 94, 0.1);
  border: 1px solid rgba(34, 197, 94, 0.3);
  color: var(--success);
}

.feedback.error {
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: var(--error);
}

@media (max-width: 700px) {
  .contact-grid {
    grid-template-columns: 1fr;
  }
}
</style>
