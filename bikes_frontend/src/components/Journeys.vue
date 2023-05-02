<script setup lang="ts">
import { getJourneyData } from '@/api/journeys.api'
import { onMounted, ref } from 'vue'

const journeys = ref();

onMounted(async () => {
  journeys.value = await getJourneyData()
})
</script>

<template>
  <table>
    <thead>
        <tr>
          <th>Departure station</th>
          <th>Departure time</th>
          <th>Return station</th>
          <th>Return time</th>
          <th>Distance (m)</th>
          <th>Duration (s)</th>
        </tr>
      </thead>
      <tbody v-if="journeys && journeys.length > 0">
        <tr v-for="journey in journeys" :key="journey.id">
          <td>{{journey.departure_station_id}}</td>
          <td>{{ new Date(journey.departure_date).toLocaleString() }}</td>
          <td>{{  journey.return_station_id }}</td>
          <td>{{  new Date(journey.return_date).toLocaleString() }}</td>
          <td>{{journey.distance}}</td>
          <td>{{journey.duration}}</td>
        </tr>
      </tbody>
  </table>
</template>
