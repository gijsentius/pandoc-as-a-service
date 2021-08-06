<template>
  <v-app>
    <v-app-bar
      app
      color="grey lighten-2"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-light.png"
          width="100"
        />
      </div>
    </v-app-bar>

    <v-main>
      <v-container fluid>
        <Converter/>
      </v-container>
    </v-main>

    <v-footer app padless>
      <v-col
        class="text-center"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Gijs Entius</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import Converter from './views/Converter.vue'

@Component({
  components: {
    Converter
  }
})
export default class App extends Vue {

}
</script>
