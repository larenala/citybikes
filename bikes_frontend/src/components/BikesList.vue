<script setup lang="ts">
import { getBikeData } from '@/api/bikes.api'
import { onMounted, ref } from 'vue'

const bikes = ref();

onMounted(async () => {
  const res = await getBikeData()
  bikes.value = res?.data.message;
})
</script>

<template>
  <p>{{ bikes }}</p>
</template>
