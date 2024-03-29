<script>
import Alert from '../components/Alert.vue';

export default {
  components: {
    Alert,
  },

  created() {
    this.startCamera();
  },

  unmounted() {
    this.stopCamera();
  },

  watch: {
    $route(to, from) {
      this.redirectPath = this.$route.query.redirect || '/';
    },
  },

  data() {
    return {
      videoStream: null,
      username: '',
      unauthorized: false,
      redirectPath: this.$route.query.redirect || '/',
    };
  },

  methods: {
    async startCamera() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({
          video: true,
        });
        this.$refs.video.srcObject = stream;
        this.videoStream = stream;
      } catch (error) {
        console.error(error);
      }
    },

    stopCamera() {
      if (this.videoStream) {
        this.videoStream.getTracks().forEach((track) => {
          track.stop();
        });
      }
    },

    takePicture() {
      const canvas = document.createElement('canvas');
      canvas.width = this.$refs.video.videoWidth;
      canvas.height = this.$refs.video.videoHeight;
      const context = canvas.getContext('2d');
      context.drawImage(this.$refs.video, 0, 0, canvas.width, canvas.height);
      const dataURL = canvas.toDataURL('image/jpeg');
      return dataURL;
    },

    async signin() {
      this.unauthorized = false;
      try {
        const dataURL = this.takePicture();
        const formData = new FormData();
        formData.append('username', this.username);
        formData.append('picture', dataURL);
        const response = await fetch('http://127.0.0.1:5000/signin', {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          this.unauthorized = true;
          throw new Error('signin failed');
        }

        const user = { username: this.username };
        $cookies.set('user', user, '5min');
        this.$router.push(this.redirectPath);
      } catch (error) {
        console.error('signin failed:', error);
      }
    },
  },
};
</script>

<template>
  <div class="w-full max-w-md mx-auto p-6">
    <Alert
      v-if="redirectPath !== '/'"
      :title="`Unable to access '${redirectPath}'`"
    >
      you are unauthorized, please sign in.
    </Alert>
    <div
      class="mt-7 bg-white border border-gray-200 rounded-xl shadow-sm dark:bg-gray-800 dark:border-gray-700"
    >
      <div class="p-4 sm:p-7">
        <div class="text-center">
          <h1 class="block text-2xl font-bold text-gray-800 dark:text-white">
            Sign in
          </h1>
          <p class="mt-2 text-sm text-gray-600 dark:text-gray-400">
            Don't have an account yet?
            <router-link
              :to="{ name: 'SignUp' }"
              class="text-blue-600 decoration-2 hover:underline font-medium"
              href="../examples/html/signup.html"
            >
              Sign up here
            </router-link>
          </p>
        </div>
        <div class="mt-5">
          <div
            class="py-3 flex items-center text-xs text-gray-400 uppercase before:flex-[1_1_0%] before:border-t before:border-gray-200 before:mr-6 after:flex-[1_1_0%] after:border-t after:border-gray-200 after:ml-6 dark:text-gray-500 dark:before:border-gray-600 dark:after:border-gray-600"
          >
            Or
          </div>
          <!-- Sign-up form -->
          <form>
            <div class="grid gap-y-4">
              <!-- Form Group -->
              <div>
                <label for="username" class="block text-sm mb-2 dark:text-white"
                  >Username</label
                >
                <div class="relative">
                  <input
                    v-model="username"
                    type="text"
                    id="username"
                    name="username"
                    class="input-border py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400"
                    required
                    aria-describedby="username-error"
                  />
                  <div
                    v-if="username.length === 0"
                    class="absolute inset-y-0 right-0 flex items-center pointer-events-none pr-3"
                  >
                    <svg
                      class="h-5 w-5 text-red-500"
                      width="16"
                      height="16"
                      fill="currentColor"
                      viewBox="0 0 16 16"
                      aria-hidden="true"
                    >
                      <path
                        d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z"
                      />
                    </svg>
                  </div>
                </div>
              </div>
              <!-- End Form Group -->
              <!-- Form Group -->
              <div>
                <label for="username" class="block text-sm mb-2 dark:text-white"
                  >Face ID</label
                >
                <div class="relative">
                  <div
                    class="input-border py-3 px-4 block w-full border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400"
                  >
                    <video ref="video" autoplay></video>
                  </div>
                </div>
              </div>
              <p v-if="unauthorized" class="text-xs text-red-600 mt-2">
                Your username does not exist or your Face ID does not match.
              </p>
              <!-- End Form Group -->
              <button
                :disabled="username.length === 0 ? true : false"
                @click.prevent="signin"
                type="submit"
                class="py-3 px-4 inline-flex justify-center items-center gap-2 rounded-md border border-transparent font-semibold bg-blue-500 text-white hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-all text-sm dark:focus:ring-offset-gray-800"
              >
                Sign in
              </button>
            </div>
          </form>
          <!-- End Form -->
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.input-border {
  border: #e5e7eb solid 0.1rem;
}
</style>
