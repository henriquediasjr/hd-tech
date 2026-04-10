<script setup>
import { ref, computed } from 'vue'

// ── Calendar state ──────────────────────────────────────────────────────────
const today     = new Date()
const calYear   = ref(today.getFullYear())
const calMonth  = ref(today.getMonth())
const selDay    = ref(null)
const selSlot   = ref(null)
const bookName  = ref('')
const bookEmail = ref('')

// ── Message form state ───────────────────────────────────────────────────────
const msgName    = ref('')
const msgEmail   = ref('')
const msgNeed    = ref('')
const msgMessage = ref('')
const msgSent    = ref(false)

// ── Constants ────────────────────────────────────────────────────────────────
const MONTH_NAMES = [
  'January','February','March','April','May','June',
  'July','August','September','October','November','December',
]
const DAY_NAMES = ['Mo','Tu','We','Th','Fr','Sa','Su']
const TIME_SLOTS = ['09:00','10:00','11:00','14:00','15:00','16:00']

// ── Calendar computed ────────────────────────────────────────────────────────
const monthLabel = computed(() => `${MONTH_NAMES[calMonth.value]} ${calYear.value}`)

const daysInMonth = computed(() =>
  new Date(calYear.value, calMonth.value + 1, 0).getDate()
)

const startOffset = computed(() => {
  const dow = new Date(calYear.value, calMonth.value, 1).getDay()
  return dow === 0 ? 6 : dow - 1  // Mon=0 … Sun=6
})

const calCells = computed(() => {
  const cells = []
  for (let i = 0; i < startOffset.value; i++) cells.push(null)
  for (let d = 1; d <= daysInMonth.value; d++) cells.push(d)
  while (cells.length % 7 !== 0) cells.push(null)
  return cells
})

function isPast(d) {
  const date  = new Date(calYear.value, calMonth.value, d)
  const start = new Date(today.getFullYear(), today.getMonth(), today.getDate())
  return date < start
}

function isWeekend(d) {
  const dow = new Date(calYear.value, calMonth.value, d).getDay()
  return dow === 0 || dow === 6
}

function isDisabled(d) {
  if (!d) return true
  return isPast(d) || isWeekend(d)
}

function isToday(d) {
  return (
    d === today.getDate() &&
    calMonth.value === today.getMonth() &&
    calYear.value  === today.getFullYear()
  )
}

function pickDay(d) {
  if (isDisabled(d)) return
  selDay.value  = d
  selSlot.value = null
}

function prevMonth() {
  if (calMonth.value === 0) { calMonth.value = 11; calYear.value-- }
  else calMonth.value--
  selDay.value = null; selSlot.value = null
}

function nextMonth() {
  if (calMonth.value === 11) { calMonth.value = 0; calYear.value++ }
  else calMonth.value++
  selDay.value = null; selSlot.value = null
}

// TODO: integrate with Google Calendar API or Calendly
function confirmBooking() {
  if (!selDay.value || !selSlot.value || !bookName.value || !bookEmail.value) return
  alert(`Booking confirmed: ${selDay.value}/${calMonth.value + 1}/${calYear.value} at ${selSlot.value}`)
}

async function sendMessage() {
  if (!msgName.value || !msgEmail.value || !msgMessage.value) return
  try {
    await fetch('/api/contact/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: msgName.value,
        email: msgEmail.value,
        need: msgNeed.value,
        message: msgMessage.value,
      }),
    })
  } catch {}
  msgSent.value = true
}
</script>

<template>
  <section id="contact">
    <div class="section-wrap">
      <div class="section-label" data-animate style="--i:0">Let's Build Something</div>

      <div class="contact-grid">

        <!-- LEFT: Calendar booking -->
        <div class="contact-col" data-animate style="--i:1">
          <h2 class="col-heading">Book a 15-min call</h2>
          <p class="col-sub">No commitment — just a quick technical introduction.</p>

          <div class="calendar">
            <!-- Header -->
            <div class="cal-header">
              <button class="cal-nav" @click="prevMonth" aria-label="Previous month">&#8249;</button>
              <span class="cal-month-label">{{ monthLabel }}</span>
              <button class="cal-nav" @click="nextMonth" aria-label="Next month">&#8250;</button>
            </div>

            <!-- Day names -->
            <div class="cal-day-names">
              <span v-for="d in DAY_NAMES" :key="d" class="cal-dn">{{ d }}</span>
            </div>

            <!-- Day grid -->
            <div class="cal-grid">
              <button
                v-for="(cell, idx) in calCells"
                :key="idx"
                class="cal-cell"
                :class="{
                  'cal-cell--empty':     !cell,
                  'cal-cell--disabled':   cell && isDisabled(cell),
                  'cal-cell--today':      cell && isToday(cell),
                  'cal-cell--selected':   cell && cell === selDay,
                  'cal-cell--available':  cell && !isDisabled(cell),
                }"
                :disabled="!cell || isDisabled(cell)"
                @click="pickDay(cell)"
                :aria-label="cell ? String(cell) : ''"
              >
                <span v-if="cell">{{ cell }}</span>
              </button>
            </div>

            <!-- Time slots -->
            <div v-if="selDay" class="time-slots">
              <button
                v-for="slot in TIME_SLOTS"
                :key="slot"
                class="time-slot"
                :class="{ 'time-slot--sel': selSlot === slot }"
                @click="selSlot = slot"
              >{{ slot }}</button>
            </div>

            <!-- Booking inputs -->
            <div v-if="selDay && selSlot" class="booking-inputs">
              <div class="field-row">
                <input v-model="bookName"  class="c-input" placeholder="Your name" />
                <input v-model="bookEmail" class="c-input" type="email" placeholder="your@email.com" />
              </div>
              <button class="btn-primary btn-full" @click="confirmBooking" data-action="book-calendar">
                Confirm Booking
              </button>
            </div>
          </div>
        </div>

        <!-- RIGHT: Message form -->
        <div class="contact-col" data-animate style="--i:2">
          <h2 class="col-heading">Send a message</h2>
          <p class="col-sub">Prefer async? Fill this in and I'll reply within 24h.</p>

          <div v-if="msgSent" class="sent-msg">
            Message sent — I'll get back to you shortly.
          </div>

          <form v-else class="msg-form" @submit.prevent="sendMessage">
            <div class="field-row">
              <div class="field">
                <label class="field-label">Name</label>
                <input v-model="msgName" class="c-input" placeholder="Your name" required />
              </div>
              <div class="field">
                <label class="field-label">Email</label>
                <input v-model="msgEmail" class="c-input" type="email" placeholder="your@email.com" required />
              </div>
            </div>

            <div class="field">
              <label class="field-label">What do you need?</label>
              <select v-model="msgNeed" class="c-input c-select">
                <option value="">Select an option</option>
                <option value="pipeline">Build a data pipeline</option>
                <option value="architecture">Review my architecture</option>
                <option value="hire">Hire me as backend engineer</option>
                <option value="other">Other</option>
              </select>
            </div>

            <div class="field">
              <label class="field-label">Message</label>
              <textarea
                v-model="msgMessage"
                class="c-input c-textarea"
                rows="5"
                placeholder="Tell me about your project..."
                required
              ></textarea>
            </div>

            <button type="submit" class="btn-ghost btn-full">Send Message</button>
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

@media (max-width: 768px) {
  .contact-grid { grid-template-columns: 1fr; gap: 40px; }
  .field-row { grid-template-columns: 1fr; }
}
</style>
