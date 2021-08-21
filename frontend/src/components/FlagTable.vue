<template>
  <v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            Flag
          </th>
          <th class="text-left">
            Value
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-on:mouseenter="showDelete = true"
          v-on:mouseleave="showDelete = false"
          v-for="flag in flags" :key="flag.identifier"
        >
          <td>{{ flag.identifier }}</td>
          <td>
            {{ flag.value }}
          </td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'
import { Flag } from '@/interfaces'

@Component
export default class FlagTable extends Vue {
  @Prop() public flags!: Flag[];

  public showDelete = false;
}
</script>

<style scoped>

</style>
