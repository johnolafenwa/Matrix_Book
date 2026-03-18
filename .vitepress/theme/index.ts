import DefaultTheme from "vitepress/theme";
import BookToc from "./components/BookToc.vue";
import MermaidBlock from "./components/MermaidBlock.vue";
import "./custom.css";

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component("BookToc", BookToc);
    app.component("MermaidBlock", MermaidBlock);
  }
};
