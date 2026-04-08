import { createRouter, createWebHistory } from 'vue-router'
import ContactView from '../views/ContactView.vue'
import BudgetView from '../views/BudgetView.vue'
import ScheduleView from '../views/ScheduleView.vue'

const routes = [
  { path: '/', redirect: '/contact' },
  { path: '/contact', component: ContactView, meta: { title: 'Contact' } },
  { path: '/budget', component: BudgetView, meta: { title: 'Budget Request' } },
  { path: '/schedule', component: ScheduleView, meta: { title: 'Schedule a Call' } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.afterEach((to) => {
  document.title = to.meta.title ? `${to.meta.title} — Portfolio` : 'Portfolio'
})

export default router
