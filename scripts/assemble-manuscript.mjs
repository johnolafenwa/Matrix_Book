import { mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { allEntries, book } from "../book.config.mjs";

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const outDir = path.join(rootDir, "dist");
const outFile = path.join(outDir, "book-manuscript.md");

const tocLines = [];

for (const entry of allEntries) {
  tocLines.push(`- [${entry.text}](${entry.link})`);
}

const chapterBodies = await Promise.all(
  allEntries.map(async (entry) => {
    const source = path.join(rootDir, entry.file);
    const content = await readFile(source, "utf8");

    return content.trim();
  })
);

const manuscript = [
  `# ${book.title}`,
  "",
  `## ${book.subtitle}`,
  "",
  book.description,
  "",
  "## Table of Contents",
  "",
  ...tocLines,
  "",
  "---",
  "",
  ...chapterBodies.flatMap((body, index) => {
    if (index === chapterBodies.length - 1) {
      return [body, ""];
    }

    return [body, "", "---", ""];
  })
].join("\n");

await mkdir(outDir, { recursive: true });
await writeFile(outFile, manuscript, "utf8");

console.log(`Wrote ${path.relative(rootDir, outFile)}`);
