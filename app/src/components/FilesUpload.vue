<template>
  <v-file-input
    v-model="files"
    :label="label"
    counter
    prepend-icon="mdi-paperclip"
    outlined
    :clearable=false
    multiple
    :show-size="1000"
  >
    <template v-slot:selection="{ index, text }">
      <v-chip
        v-if="index < 4"
        label
        small
      >
        {{ text }}
      </v-chip>

      <span
        v-else-if="index === 4"
        class="text-overline grey--text text--darken-3 mx-2"
      >
        +{{ files.length - 4 }} File(s)
      </span>
    </template>
  </v-file-input>
</template>

<script lang="ts">
import { dispatchAddFiles } from '@/store/main/actions'
import { readFiles } from '@/store/main/getters'
import { Component, Prop, Vue } from 'vue-property-decorator'

@Component
export default class FilesUpload extends Vue {
  @Prop() private label!: string;

  get files(): File[] {
    return readFiles(this.$store)
  }

  set files(files: File[]) {
    dispatchAddFiles(this.$store, files)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
