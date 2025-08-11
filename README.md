# RodriguezDioscar — Vite + Tailwind Portfolio

Modern, fast, and responsive portfolio built with Vite and Tailwind CSS. Deployed automatically to GitHub Pages.

## Local development

```bash
# Install dependencies
npm install

# Start dev server
npm run dev
# open http://localhost:5173
```

## Build

```bash
npm run build
npm run preview
```

## Deploy

Pushing to `main` triggers the GitHub Actions workflow in `.github/workflows/deploy-pages.yml`, which builds the site and publishes it to GitHub Pages.

Your site will be available at:
```
https://dioscarr.github.io/RodriguezDioscar/
```

If you later deploy to a user/org site (e.g., `dioscarr.github.io`) or a custom domain, update `vite.config.js`:

```js
import { defineConfig } from 'vite'
export default defineConfig({ base: '/' })
```

## Customize

- Edit content in `index.html`
- Add scripts/styles to `src/` (main entry: `src/main.js`)
- Tailwind rules in `src/index.css`
- Update colors/fonts in `tailwind.config.js`
