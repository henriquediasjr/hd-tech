import { http } from './client'

export const getSchedule = () => http.get('/schedule/')
