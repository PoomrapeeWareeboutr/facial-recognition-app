<script>
import CircularAvatar from './CircularAvatar.vue';
import Jenny from '../assets/images/jenny.jpg';
import Blue from '../assets/images/blue.jpg';
import Koikwang from '../assets/images/koikwang.jpg';

export default {
  components: {
    CircularAvatar,
  },
  data() {
    return {
      Jenny,
      Blue,
      Koikwang,
    };
  },
};
</script>

<template>
  <div class="max-w-5xl px-4 py-10 sm:px-6 lg:px-8 lg:py-14 mx-auto">
    <!-- Title -->
    <div class="max-w-2xl mx-auto text-center mb-10 lg:mb-14">
      <h2
        class="text-2xl font-bold md:text-4xl md:leading-tight dark:text-white"
      >
        Collaborators
      </h2>
      <p class="mt-1 text-gray-600 dark:text-gray-400">Section 3</p>
    </div>
    <!-- End Title -->
    <!-- Grid -->
    <div
      class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-3 lg:grid-cols-3 gap-8 md:gap-12"
    >
      <CircularAvatar
        name="Poomrapee Wareeboutr"
        role="Software Engineering Student"
        :image="Blue"
        github="https://github.com/PoomrapeeWareeboutr"
      />
      <CircularAvatar
        name="Pitchaya Teerawongpairoj"
        role="Database & Intelligent Systems Student"
        :image="Koikwang"
        github="https://github.com/Koikwang"
      />
      <CircularAvatar
        name="Sasima Srijanya"
        role="Database & Intelligent Systems Student"
        :image="Jenny"
        github="https://github.com/Jenny-Sasima"
      />
    </div>
    <!-- End Grid -->
  </div>
</template>

<style scoped></style>
