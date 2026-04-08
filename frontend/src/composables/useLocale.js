import { ref } from 'vue'
import en from '../i18n/en.js'
import pt from '../i18n/pt.js'

const translations = { en, pt }
const locale = ref(localStorage.getItem('locale') || 'en')

function setLocale(lang) {
  locale.value = lang
  localStorage.setItem('locale', lang)
}

function t(key) {
  const keys = key.split('.')
  let val = translations[locale.value]
  for (const k of keys) {
    val = val?.[k]
    if (val === undefined) return key
  }
  return val
}

export function useLocale() {
  return { locale, setLocale, t }
}
