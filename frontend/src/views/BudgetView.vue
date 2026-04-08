<script setup>
import { reactive } from 'vue'
import { submitBudget } from '../api/budget'
import { useForm } from '../composables/useForm'

const { loading, error, success, submit } = useForm(submitBudget)

const form = reactive({
  project_type: '',
  description: '',
  budget: '',
  deadline: '',
})

const projectTypes = [
  { value: 'website', label: 'Website' },
  { value: 'ecommerce', label: 'E-commerce' },
  { value: 'saas', label: 'SaaS' },
  { value: 'mobile', label: 'Mobile App' },
  { value: 'other', label: 'Other' },
]

async function handleSubmit() {
  await submit({ ...form, budget: Number(form.budget) })
  if (success.value) {
    form.project_type = ''
    form.description = ''
    form.budget = ''
    form.deadline = ''
  }
}
</script>

<template>
  <section>
    <h1>Request a Budget</h1>
    <p class="subtitle">Tell me about your project and I'll send you a proposal.</p>

    <form @submit.prevent="handleSubmit" novalidate>
      <div class="field">
        <label for="project_type">Project Type</label>
        <select id="project_type" v-model="form.project_type" required>
          <option value="" disabled>Select a type…</option>
          <option v-for="t in projectTypes" :key="t.value" :value="t.value">
            {{ t.label }}
          </option>
        </select>
      </div>

      <div class="field">
        <label for="description">Project Description</label>
        <textarea
          id="description"
          v-model="form.description"
          rows="5"
          placeholder="Describe your project in detail (min. 20 characters)"
          required
        />
      </div>

      <div class="row">
        <div class="field">
          <label for="budget">Budget (USD)</label>
          <input id="budget" v-model="form.budget" type="number" min="1" placeholder="5000" required />
        </div>

        <div class="field">
          <label for="deadline">Deadline</label>
          <input id="deadline" v-model="form.deadline" type="date" required />
        </div>
      </div>

      <div v-if="error" class="feedback error">{{ error }}</div>
      <div v-if="success" class="feedback success">Budget request received! I'll review and contact you shortly.</div>

      <button type="submit" :disabled="loading">
        {{ loading ? 'Sending…' : 'Submit Request' }}
      </button>
    </form>
  </section>
</template>

<style scoped>
.row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}
</style>
