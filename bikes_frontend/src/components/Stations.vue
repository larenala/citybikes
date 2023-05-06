<script setup lang="ts">
    import { getStations } from '@/api/stations.api'
    import { onMounted, ref } from 'vue'

    const stations = ref();

    onMounted(async () => {
        stations.value = await getStations()
    })
</script>

<template>
  <h1>Stations</h1>
  <table>
    <thead>
        <tr>
          <th>Station name</th>
          <th>Address</th>

        </tr>
      </thead>
      <tbody v-if="stations && stations.length > 0">
        <tr v-for="station in stations" :key="station.id">
          <td>{{station.name}}</td>
          <td>{{ station.address }}</td>
        </tr>
      </tbody>
  </table>
</template>
