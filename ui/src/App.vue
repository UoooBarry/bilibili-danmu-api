<template>
  <v-app>
    <v-main>
      <Dashboard />
    </v-main>
    <v-footer dark>
      <div>
        <a
          href="https://github.com/UoooBarry/bilibili-danmu-api"
          target="_blank"
          style="text-decoration: none"
        >
          <v-icon> mdi-github </v-icon>
          <strong> UoooBarry </strong></a
        >
      </div>
    </v-footer>
  </v-app>
</template>

<script>
import Dashboard from "./components/Dashboard";

export default {
  name: "App",
  components: {
    Dashboard,
  },
  data() {
    return {
      icons: ["mdi-github-circle"],
    };
  },
};
</script>
