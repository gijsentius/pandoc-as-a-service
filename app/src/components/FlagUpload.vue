<template>
  <v-form v-model="valid">
    <v-container>
      <v-row>
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="flag"
            label="Flag"
            :rules="rules"
            required
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
          md="4"
        >
          <v-text-field
            v-model="value"
            label="Value"
          ></v-text-field>
        </v-col>
        <v-col
          cols="12"
          md="4"
        >
          <v-btn
            :disabled="!valid"
            class="mr-4"
            color="primary"
            @click="submit"
          >
            <v-icon dark left>
              mdi-plus
            </v-icon>
            Add
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
// import { Store } from 'vuex'
import { Flag } from '@/interfaces'
import { dispatchAddFlag } from '@/store/main/actions'

@Component
export default class FlagUpload extends Vue {
  public flag = '';
  public value = '';
  public valid = false;

  public rules = [
    (v: string) => !!v || 'Identifier is required'
  ]

  public submit(): void {
    if (this.valid) {
      dispatchAddFlag(this.$store, { identifier: this.flag, value: this.value } as Flag)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
