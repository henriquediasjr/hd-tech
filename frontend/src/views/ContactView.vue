<script setup>
import { reactive } from 'vue'
import { submitContact } from '../api/contact'
import { useForm } from '../composables/useForm'

const { loading, error, success, submit } = useForm(submitContact)

const form = reactive({ name: '', email: '', message: '' })

async function handleSubmit() {
  await submit({ ...form })
  if (success.value) {
    form.name = ''
    form.email = ''
    form.message = ''
  }
}
</script>

<template>
  <section>
    <h1>Get in Touch</h1>
    <p class="subtitle">Have a project in mind? Send a message and I'll get back to you.</p>

    <form @submit.prevent="handleSubmit" novalidate>
      <div class="field">
        <label for="name">Name</label>
        <input id="name" v-model="form.name" type="text" placeholder="Your name" required />
      </div>

      <div class="field">
        <label for="email">Email</label>
        <input id="email" v-model="form.email" type="email" placeholder="you@example.com" required />
      </div>

      <div class="field">
        <label for="message">Message</label>
        <textarea id="message" v-model="form.message" rows="5" placeholder="Tell me about your project..." required />
      </div>

      <div v-if="error" class="feedback error">{{ error }}</div>
      <div v-if="success" class="feedback success">Message sent! I'll be in touch soon.</div>

      <button type="submit" :disabled="loading">
        {{ loading ? 'Sending…' : 'Send Message' }}
      </button>
    </form>
  </section>
</template>
