import { http } from './client'

export const submitBudget = (data) => http.post('/budget/', data)
