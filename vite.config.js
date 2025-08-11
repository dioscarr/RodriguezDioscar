import { defineConfig } from "vite";

// IMPORTANT: base must match the repo name for GitHub Pages project sites.
// For staging deployments, use VITE_BASE_PATH environment variable
export default defineConfig({
  base: process.env.VITE_BASE_PATH || "/RodriguezDioscar/"
});