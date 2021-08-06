<template>
  <v-container>
    <v-card>
      <v-toolbar
        flat
        color="blue lighten-3"
      >
        <v-toolbar-title>Convert document to pdf with pandoc</v-toolbar-title>
      </v-toolbar>

      <v-card-text>
        <h2>Upload Files</h2>
        <document-upload label="Document" v-bind:multiple="false"></document-upload>
        <files-upload label="Other files" v-bind:multiple="true"></files-upload>

        <h2>Flags</h2>
        <flag-upload></flag-upload>
        <flag-table :flags="flags"></flag-table>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn depressed v-on:click="submit" color="primary">
          <v-icon left>
            mdi-update
          </v-icon>
          Convert
        </v-btn>
        <v-btn depressed @click="reset">
          reset
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import FilesUpload from '@/components/FilesUpload.vue'
import DocumentUpload from '@/components/DocumentUpload.vue'
import FlagTable from '@/components/FlagTable.vue'
import FlagUpload from '@/components/FlagUpload.vue'
import { readDocumentPDFName, readFlags } from '@/store/main/getters'
import { Flag } from '@/interfaces'
import { dispatchConvert, dispatchReset } from '@/store/main/actions'

@Component({
  components: {
    FilesUpload,
    DocumentUpload,
    FlagTable,
    FlagUpload
  }
})
export default class Converter extends Vue {
  public test = false;

  get flags(): Flag[] {
    return readFlags(this.$store)
  }

  reset(): void {
    dispatchReset(this.$store)
  }

  submit(): void {
    dispatchConvert(this.$store)
  }
}
</script>
