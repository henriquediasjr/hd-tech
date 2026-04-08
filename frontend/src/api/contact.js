import { http } from './client'

export const submitContact = (data) => http.post('/contact/', data)
