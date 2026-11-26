<script setup>
defineProps({ level: { type: String, required: true } })
</script>
<template><span class="badge" :class="level === 'TINGGI' ? 'text-bg-danger' : level === 'SEDANG' ? 'text-bg-warning' : level === 'RENDAH' ? 'text-bg-success' : 'text-bg-secondary'">{{ level }}</span></template>
