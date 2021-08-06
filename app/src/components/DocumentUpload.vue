<template>
  <v-file-input
    v-model="document"
    label="Document"
    prepend-icon="mdi-paperclip"
    :clearable=false
    :show-size="1000"
  >
  </v-file-input>
</template>

<script lang="ts">
import { dispatchAddDocument } from '@/store/main/actions'
import { readDocument } from '@/store/main/getters'
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class DocumentUpload extends Vue {
  get document(): File | undefined {
    return readDocument(this.$store)
  }

  set document(file: File | undefined) {
    if (file !== undefined) {
      dispatchAddDocument(this.$store, file)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
