<script setup>
import { onMounted, ref, watch } from "vue";
import { useData } from "vitepress";
import mermaid from "mermaid";

const props = defineProps({
  graph: {
    type: String,
    required: true
  }
});

const target = ref(null);
const { isDark } = useData();

const lightThemeVariables = {
  primaryColor: "#d4f4ef",
  primaryTextColor: "#14312d",
  primaryBorderColor: "#0f766e",
  lineColor: "#28514a",
  secondaryColor: "#eef7f5",
  tertiaryColor: "#fbf6e8"
};

const darkThemeVariables = {
  primaryColor: "#173733",
  primaryTextColor: "#e5f2ef",
  primaryBorderColor: "#57b8aa",
  lineColor: "#93d8cf",
  secondaryColor: "#12211f",
  tertiaryColor: "#1a2b29"
};

async function renderGraph() {
  if (!target.value) {
    return;
  }

  const graph = decodeURIComponent(props.graph);

  mermaid.initialize({
    startOnLoad: false,
    theme: "base",
    securityLevel: "loose",
    fontFamily: "Source Sans 3, sans-serif",
    themeVariables: isDark.value ? darkThemeVariables : lightThemeVariables
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
}

onMounted(() => {
  void renderGraph();
});

watch(isDark, () => {
  void renderGraph();
});
</script>

<template>
  <div ref="target" class="mermaid-render"></div>
</template>
