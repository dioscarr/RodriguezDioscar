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

### Production Deployment
Pushing to `main` triggers the GitHub Actions workflow in `.github/workflows/deploy-pages.yml`, which builds the site and publishes it to GitHub Pages.

Your production site will be available at:
```
https://dioscarr.github.io/RodriguezDioscar/
```

### Staging/Preview Deployments
For feature development and previews:

1. **Branch Deployments**: Push to any branch (except `main`) to automatically deploy a staging preview
2. **Pull Request Previews**: Open a PR to get an automatic preview deployment with a comment containing the preview link
3. **Manual Deployments**: Use the "Deploy to Staging" workflow dispatch to deploy any specific branch

Staging previews will be available at:
```
# For pull requests
https://dioscarr.github.io/RodriguezDioscar/pr-{PR_NUMBER}

# For branches  
https://dioscarr.github.io/RodriguezDioscar/branch-{BRANCH_NAME}
```

All staging previews include a banner indicating they are preview versions.

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
