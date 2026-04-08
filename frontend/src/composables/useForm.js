import { ref } from 'vue'

export function useForm(submitFn) {
  const loading = ref(false)
  const error = ref(null)
  const success = ref(false)

  async function submit(data) {
    loading.value = true
    error.value = null
    success.value = false
    try {
      const result = await submitFn(data)
      success.value = true
      return result
    } catch (e) {
      error.value = e?.error ?? 'Something went wrong. Please try again.'
    } finally {
      loading.value = false
    }
  }

  function reset() {
    error.value = null
    success.value = false
  }

  return { loading, error, success, submit, reset }
}
