<script>
  export default {
    props: {
      name: { type: String, required: true },
      role: { type: String, required: true },
      image: { type: String, required: true },
      github: { type: String, default: '' },
    }
  }
</script>

<template>
  <div class="text-center">
    <a :href="github">
      <img class="rounded-full w-24 h-24 mx-auto" :src="image" :alt="`${name} picture`">
    </a>
    <div class="mt-2 sm:mt-4">
      <h3 class="font-medium text-gray-800 dark:text-gray-200">
        {{ name }}
      </h3>
      <p class="text-sm text-gray-600 dark:text-gray-400">
        {{ role }}
      </p>
    </div>
  </div>
</template>

<style scope></style>