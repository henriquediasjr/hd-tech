<script setup>
import { ref, onMounted } from 'vue'
import { useLocale } from '../composables/useLocale'

const { t } = useLocale()

const msgName    = ref('')
const msgEmail   = ref('')
const msgNeed    = ref('')
const msgMessage = ref('')
const msgState   = ref('idle') // idle | sending | sent | error

async function sendMessage() {
  if (!msgName.value || !msgEmail.value || !msgMessage.value) return
  msgState.value = 'sending'
  try {
    const res = await fetch('/api/contact/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name:    msgName.value,
        email:   msgEmail.value,
        need:    msgNeed.value,
        message: msgMessage.value,
      }),
    })
    msgState.value = res.ok ? 'sent' : 'error'
  } catch {
    msgState.value = 'error'
  }
}

onMounted(() => {
  const script = document.createElement('script')
  script.src = 'https://assets.calendly.com/assets/external/widget.js'
  script.async = true
  document.head.appendChild(script)
})
</script>

<template>
  <section id="contact">
    <div class="section-wrap">
      <div class="section-label" data-animate style="--i:0">{{ t('contact.title') }}</div>

      <div class="contact-grid">

        <!-- LEFT: Calendar booking -->
        <div class="contact-col" data-animate style="--i:1">
          <h2 class="col-heading">{{ t('contact.scheduleTitle') }}</h2>
          <p class="col-sub">{{ t('contact.subtitle') }}</p>

          <div class="calendar">
            <!-- Calendly inline widget begin -->
            <div class="calendly-inline-widget" data-url="https://calendly.com/henriquediasjr/30min" style="min-width:320px;height:700px;"></div>
            <!-- Calendly inline widget end -->
          </div>
        </div>

        <!-- RIGHT: Message form -->
        <div class="contact-col" data-animate style="--i:2">
          <h2 class="col-heading">{{ t('contact.formTitle') }}</h2>
          <p class="col-sub">{{ t('contact.microcopy') }}</p>

          <div v-if="msgState === 'sent'" class="sent-msg">
            {{ t('contact.form.success') }}
          </div>

          <div v-else-if="msgState === 'error'" class="error-msg">
            {{ t('contact.form.error') }}
            <button class="retry-btn" @click="msgState = 'idle'">Try again</button>
          </div>

          <form v-else class="msg-form" @submit.prevent="sendMessage">
            <div class="field-row">
              <div class="field">
                <label class="field-label">{{ t('contact.form.name') }}</label>
                <input v-model="msgName" class="c-input" :placeholder="t('contact.form.namePlaceholder')" required />
              </div>
              <div class="field">
                <label class="field-label">{{ t('contact.form.email') }}</label>
                <input v-model="msgEmail" class="c-input" type="email" :placeholder="t('contact.form.emailPlaceholder')" required />
              </div>
            </div>

            <div class="field">
              <label class="field-label">{{ t('contact.form.need') }}</label>
              <input v-model="msgNeed" class="c-input" type="text" :placeholder="t('contact.form.needPlaceholder')" />
            </div>

            <div class="field">
              <label class="field-label">{{ t('contact.form.message') }}</label>
              <textarea
                v-model="msgMessage"
                class="c-input c-textarea"
                rows="5"
                :placeholder="t('contact.form.messagePlaceholder')"
                required
              ></textarea>
            </div>

            <button type="submit" class="btn-ghost btn-full" :disabled="msgState === 'sending'">
              {{ msgState === 'sending' ? t('contact.form.sending') : t('contact.form.submit') }}
            </button>
          </form>
        </div>

      </div>
    </div>
  </section>
</template>

<style scoped>
.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: start;
}

.contact-col { display: flex; flex-direction: column; gap: 0; }

.col-heading {
  font-size: 1.125rem;
  font-weight: 600;
  color: #f4f4f5;
  margin-bottom: 6px;
}
.col-sub {
  font-size: 0.8125rem;
  font-weight: 300;
  color: #71717a;
  margin-bottom: 24px;
  line-height: 1.6;
}

/* Calendar */
.calendar {
  background: #111113;
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 12px;
  padding: 20px;
}

.cal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}
.cal-month-label {
  font-size: 0.8125rem;
  font-weight: 500;
  color: #f4f4f5;
}
.cal-nav {
  width: 28px;
  height: 28px;
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 6px;
  background: transparent;
  color: #71717a;
  cursor: pointer;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: border-color 0.15s, color 0.15s;
  line-height: 1;
  padding: 0;
}
.cal-nav:hover { border-color: rgba(255,255,255,0.15); color: #f4f4f5; }

.cal-day-names {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  margin-bottom: 8px;
}
.cal-dn {
  text-align: center;
  font-family: 'Courier New', monospace;
  font-size: 0.65rem;
  color: #52525b;
  padding: 4px 0;
}

.cal-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 2px;
}

.cal-cell {
  aspect-ratio: 1;
  border: none;
  background: transparent;
  border-radius: 6px;
  font-family: inherit;
  font-size: 0.75rem;
  color: #a1a1aa;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.15s, color 0.15s;
  padding: 0;
}
.cal-cell--empty    { pointer-events: none; }
.cal-cell--disabled { opacity: 0.22; cursor: default; pointer-events: none; }
.cal-cell--today    { color: var(--accent); font-weight: 600; }
.cal-cell--selected { background: var(--accent) !important; color: #fff !important; font-weight: 600; }
.cal-cell--available:hover { background: rgba(59,130,246,0.12); }

/* Time slots */
.time-slots {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid rgba(255,255,255,0.06);
}
.time-slot {
  padding: 5px 12px;
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 999px;
  background: transparent;
  color: #71717a;
  font-family: 'Courier New', monospace;
  font-size: 0.7rem;
  cursor: pointer;
  transition: border-color 0.15s, background 0.15s, color 0.15s;
}
.time-slot:hover { border-color: rgba(255,255,255,0.15); color: #f4f4f5; }
.time-slot--sel   { background: var(--accent); border-color: var(--accent); color: #fff; }

/* Booking inputs */
.booking-inputs {
  margin-top: 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* Inputs */
.c-input {
  width: 100%;
  height: 40px;
  background: #18181b;
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 8px;
  padding: 0 14px;
  color: #f4f4f5;
  font-family: inherit;
  font-size: 0.875rem;
  outline: none;
  transition: border-color 0.15s, box-shadow 0.15s;
}
.c-input:focus {
  border-color: rgba(59,130,246,0.5);
  box-shadow: 0 0 0 3px rgba(59,130,246,0.1);
}
.c-input::placeholder { color: #3f3f46; }
.c-select { cursor: pointer; height: 40px; }
.c-select option { background: #18181b; color: #f4f4f5; }
.c-textarea {
  height: auto;
  padding: 10px 14px;
  resize: vertical;
  min-height: 110px;
}

/* Form */
.msg-form { display: flex; flex-direction: column; gap: 14px; }
.field-row { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.field { display: flex; flex-direction: column; gap: 6px; }
.field-label { font-size: 0.75rem; color: #52525b; font-weight: 400; }

.sent-msg {
  padding: 20px;
  background: rgba(34,197,94,0.06);
  border: 1px solid rgba(34,197,94,0.15);
  border-radius: 8px;
  font-size: 0.875rem;
  color: #22c55e;
  text-align: center;
}

.error-msg {
  padding: 20px;
  background: rgba(239,68,68,0.06);
  border: 1px solid rgba(239,68,68,0.18);
  border-radius: 8px;
  font-size: 0.875rem;
  color: #f87171;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: center;
}
.retry-btn {
  background: transparent;
  border: 1px solid rgba(239,68,68,0.3);
  border-radius: 6px;
  color: #f87171;
  font-size: 0.75rem;
  padding: 5px 14px;
  cursor: pointer;
  transition: background 0.15s;
}
.retry-btn:hover { background: rgba(239,68,68,0.08); }

button[disabled] {
  opacity: 0.55;
  cursor: not-allowed;
}

@media (max-width: 768px) {
  .contact-grid { grid-template-columns: 1fr; gap: 40px; }
  .field-row { grid-template-columns: 1fr; }
}
</style>
