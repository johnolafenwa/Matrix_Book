import katex from "katex";
import texmath from "markdown-it-texmath";
import { defineConfig } from "vitepress";
import { book, buildSidebar } from "../book.config.mjs";

function normalizeLatexDelimiters(source: string) {
  return source
    .replace(/\\\[\s*([\s\S]*?)\s*\\\]/g, (_, expression: string) => {
      return `$$\n${expression.trim()}\n$$`;
    })
    .replace(/\\\((.+?)\\\)/g, (_, expression: string) => {
      return `$${expression.trim()}$`;
    });
}

function escapeHtml(value: string) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

export default defineConfig({
  title: book.title,
  description: book.description,
  appearance: false,
  cleanUrls: true,
  outDir: "dist",
  lastUpdated: true,
  head: [
    ["link", { rel: "icon", href: "/matrix-book-mark.svg" }],
    ["meta", { name: "theme-color", content: "#0f766e" }]
  ],
  markdown: {
    config(md) {
      md.use(texmath, {
        engine: katex,
        delimiters: "dollars"
      });

      const defaultFence =
        md.renderer.rules.fence?.bind(md.renderer.rules) ??
        ((tokens, idx, options, env, self) => self.renderToken(tokens, idx, options));

      md.renderer.rules.fence = (tokens, idx, options, env, self) => {
        const token = tokens[idx];

        if (token.info.trim() === "mermaid") {
          const encoded = escapeHtml(encodeURIComponent(token.content));

          return `<ClientOnly><MermaidBlock graph="${encoded}" /></ClientOnly>`;
        }

        return defaultFence(tokens, idx, options, env, self);
      };
    }
  },
  vite: {
    plugins: [
      {
        name: "normalize-latex-delimiters",
        enforce: "pre",
        transform(code, id) {
          if (!id.endsWith(".md")) {
            return null;
          }

          return normalizeLatexDelimiters(code);
        }
      }
    ]
  },
  themeConfig: {
    logo: "/matrix-book-mark.svg",
    siteTitle: book.shortTitle,
    nav: [
      { text: "Home", link: "/" },
      { text: "Start Reading", link: "/chapters/01-why-matrices-matter" },
      { text: "Cheat Sheet", link: "/chapters/18-cheat-sheet-and-next-steps" }
    ],
    sidebar: buildSidebar(),
    outline: {
      label: "On This Page",
      level: [2, 3]
    },
    search: {
      provider: "local"
    },
    docFooter: {
      prev: "Previous",
      next: "Next"
    },
    footer: {
      message: "Built with VitePress for a polished, navigable reading edition.",
      copyright: "The Matrix Book"
    }
  }
});
