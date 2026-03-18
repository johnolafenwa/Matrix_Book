<script setup>
import { book } from "../../../book.config.mjs";
</script>

<template>
  <div class="book-toc">
    <section
      v-for="part in book.parts"
      :key="part.title"
      class="book-part-card"
    >
      <header class="book-part-header">
        <p class="book-part-kicker">Book Part</p>
        <h2>{{ part.title }}</h2>
        <p>{{ part.summary }}</p>
      </header>

      <ol class="book-part-list">
        <li v-for="item in part.items" :key="item.link">
          <a :href="item.link">{{ item.text }}</a>
          <p>{{ item.description }}</p>
        </li>
      </ol>
    </section>

    <section class="book-part-card book-appendix-card">
      <header class="book-part-header">
        <p class="book-part-kicker">Reference</p>
        <h2>Appendices</h2>
        <p>Practice support and quick-reference material for revision and review.</p>
      </header>

      <ul class="book-part-list appendix-list">
        <li v-for="item in book.appendices" :key="item.link">
          <a :href="item.link">{{ item.text }}</a>
          <p>{{ item.description }}</p>
        </li>
      </ul>
    </section>
  </div>
</template>
