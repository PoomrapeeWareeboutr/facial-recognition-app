<script>
  import CircularAvatar from './CircularAvatar.vue'
  import jenny from '../assets/images/jenny.jpg'
  import blue from '../assets/images/blue.jpg'
  import koikwang from '../assets/images/koikwang.jpg'
  
  export default {
    components: {
      CircularAvatar,
    },
    data() {
      return {
        jenny,
        blue,
        koikwang,
      }
    }
  }
</script>

<template>
  <div class="max-w-5xl px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
    <!-- Title -->
    <div class="max-w-2xl mx-auto text-center mb-10 lg:mb-14">
      <h2 class="text-2xl font-bold md:text-4xl md:leading-tight dark:text-white">Team Member</h2>
      <p class="mt-1 text-gray-600 dark:text-gray-400">Section 3</p>
    </div>
    <!-- End Title -->
    <!-- Grid -->
    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-3 lg:grid-cols-3 gap-8 md:gap-12">
      <CircularAvatar 
        name="Poomrapee Wareeboutr" 
        role="Software Engineering Student" 
        :image="blue" 
      />
      <CircularAvatar 
        name="Pitchaya Teerawongpairoj" 
        role="Database & Intelligent Systems Student" 
        :image="koikwang"
      />
      <CircularAvatar 
        name="Sasima Srijanya" 
        role="Database & Intelligent Systems Student" 
        :image="jenny" 
      />
    </div>
    <!-- End Grid -->
  </div>
</template>

<style scoped></style>