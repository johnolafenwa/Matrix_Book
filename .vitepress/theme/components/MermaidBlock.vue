<script setup>
import { onMounted, ref } from "vue";
import mermaid from "mermaid";

const props = defineProps({
  graph: {
    type: String,
    required: true
  }
});

const target = ref(null);

onMounted(async () => {
  if (!target.value) {
    return;
  }

  const graph = decodeURIComponent(props.graph);

  mermaid.initialize({
    startOnLoad: false,
    theme: "base",
    securityLevel: "loose",
    fontFamily: "Source Sans 3, sans-serif",
    themeVariables: {
      primaryColor: "#d4f4ef",
      primaryTextColor: "#14312d",
      primaryBorderColor: "#0f766e",
      lineColor: "#28514a",
      secondaryColor: "#eef7f5",
      tertiaryColor: "#fbf6e8"
    }
  });

  try {
    const id = `mermaid-${Math.random().toString(36).slice(2)}`;
    const { svg } = await mermaid.render(id, graph);

    target.value.innerHTML = svg;
  } catch (error) {
    target.value.textContent = graph;
    target.value.classList.add("mermaid-render-fallback");
    console.error(error);
  }
});
</script>

<template>
  <div ref="target" class="mermaid-render"></div>
</template>
