<script>
  import Navbar from './components/Navbar.vue'
  import Footer from './components/Footer.vue'

  export default {
    components: {
      Navbar,
      Footer,
    }
  }
</script>

<template>
  <Navbar />
  <div class="page">
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" :key="$route.path" />
      </transition> 
    </router-view>
  </div>
  <Footer />
</template>

<style lang="css" scoped>
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.6s;
  }
  .fade-enter,
  .fade-leave-to {
    opacity: 0;
  }
</style>