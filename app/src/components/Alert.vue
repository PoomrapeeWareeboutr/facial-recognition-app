<script>
  export default {
    props: {
      title: { type: String, default: 'Error' },
    }
  }
</script>

<template>
  <div class="bg-red-500 text-sm text-white rounded-md p-4" role="alert">
    <span class="font-bold">{{ title }}</span> 
    <slot></slot>
  </div>
</template>

<style scoped></style>