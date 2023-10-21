<script>
export default {
  data() {
    return {
      username: $cookies.get('user').username,
    };
  },

  methods: {
    signout() {
      $cookies.remove('user');
    },
  },
};
</script>

<template>
  <div class="max-w-[50rem] flex flex-col mx-auto w-full h-full">
    <main id="content" role="main">
      <div
        class="text-center max-w-[85rem] mx-auto px-4 sm:px-6 lg:px-8 py-10 lg:py-16"
      >
        <h1
          class="block font-semibold text-gray-800 text-4xl md:text-5xl lg:text-6xl dark:text-gray-200"
        >
          You're in,
          <span
            class="bg-clip-text bg-gradient-to-l from-blue-600 to-violet-500 text-transparent dark:from-blue-400 dark:to-violet-400"
          >
            {{ username }}!
          </span>
          🎉
        </h1>
        <p class="mt-3 text-lg text-gray-600 dark:text-gray-400">
          This route is restricted to authorized users only, and you are one of
          them! Congratulations on gaining access.
        </p>
        <div
          class="mt-5 flex flex-col justify-center items-center gap-2 sm:flex-row sm:gap-3"
        >
          <router-link
            :to="{ name: 'SignIn' }"
            @click="signout"
            class="w-full sm:w-auto inline-flex justify-center items-center gap-x-3 text-center bg-blue-600 hover:bg-blue-700 border border-transparent text-white text-sm font-medium rounded-md focus:outline-none focus:ring-2 focus:ring-blue-600 focus:ring-offset-2 focus:ring-offset-white transition py-3 px-4 dark:focus:ring-offset-gray-800"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-box-arrow-left"
              viewBox="0 0 16 16"
            >
              <path
                fill-rule="evenodd"
                d="M6 12.5a.5.5 0 0 0 .5.5h8a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5h-8a.5.5 0 0 0-.5.5v2a.5.5 0 0 1-1 0v-2A1.5 1.5 0 0 1 6.5 2h8A1.5 1.5 0 0 1 16 3.5v9a1.5 1.5 0 0 1-1.5 1.5h-8A1.5 1.5 0 0 1 5 12.5v-2a.5.5 0 0 1 1 0v2z"
              />
              <path
                fill-rule="evenodd"
                d="M.146 8.354a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L1.707 7.5H10.5a.5.5 0 0 1 0 1H1.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3z"
              />
            </svg>
            Sign out
          </router-link>
          <router-link
            :to="{ name: 'Home' }"
            class="w-full sm:w-auto inline-flex justify-center items-center gap-2 rounded-md border border-transparent font-semibold text-blue-500 hover:text-blue-700 focus:outline-none focus:ring-2 ring-offset-white focus:ring-blue-500 focus:ring-offset-2 transition-all text-sm py-3 px-4 dark:ring-offset-slate-900"
          >
            <svg
              class="w-2.5 h-2.5"
              width="16"
              height="16"
              viewBox="0 0 16 16"
              fill="none"
            >
              <path
                d="M11.2792 1.64001L5.63273 7.28646C5.43747 7.48172 5.43747 7.79831 5.63273 7.99357L11.2792 13.64"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
              />
            </svg>
            Back to home
          </router-link>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped></style>
