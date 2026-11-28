<script setup>
defineProps({ level: { type: String, required: true } })
</script>
<template><span class="risk-badge" :class="'risk-'+level.toLowerCase()"><span class="risk-dot"></span>{{ level }}</span></template>
