import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('../views/Home.vue'),
    },
    {
        path: '/signin',
        name: 'SignIn',
        component: () => import('../views/SignIn.vue'),
    },
    {
        path: '/signup',
        name: 'SignUp',
        component: () => import('../views/SignUp.vue'),
    },
    {
        path: '/protected',
        name: 'Protected',
        component: () => import('../views/Protected.vue'),
        meta: {
            authRequired: true,
        },
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: ()=> import('../views/NotFound.vue'),
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

function authenticate() {
    if (!$cookies.isKey('user')) {
        return false
    }
    if (new Date($cookies.get('user').expires) > new Date()) {
        return false
    }
    return true
}

router.beforeEach((to, from) => {
    if (to.meta.authRequired && !authenticate()) {    
        return { name: 'SignIn', query: { redirect: to.fullPath } }
    }
})

export default router
