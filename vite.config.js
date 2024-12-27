import { defineConfig } from 'vite';

export default defineConfig({
  root: './hi-friend-final-portfolio/template',
  server: {
    port: 3000,
    open: true,
  },
  build: {
    outDir: './hi-friend-final-portfolio/dist',
  },
});