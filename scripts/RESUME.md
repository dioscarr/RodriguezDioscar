# Resume PDF

The navigation's Resume link downloads `assets/Dioscar-Rodriguez-Resume.pdf` directly, including without JavaScript. It uses a relative URL for GitHub Pages project hosting. Downloads bypass the site's exit animation.

To revise the content or layout, edit `scripts/build_resume.py`, then run:

```sh
python3 -m pip install -r scripts/requirements-resume.txt
python3 scripts/build_resume.py
```

Commit both the generator and regenerated PDF. ReportLab's bundled Bitstream Vera fonts are embedded so the output is portable. No CDN, browser printing, or runtime PDF library is needed on the website. The existing Pages workflow publishes the checked-in asset.

Content is grounded in the supplied resume, current portfolio and GlucoPlate README, and the owner's described enterprise and independent work. Keep employment titles and dates verified; the latest portfolio uses Programmer at McNeil and Company, while the older attachment says Lead Programmer. No separate Arch role or speculative dates were added. Current hiring emphasis informs ordering, not invented credentials or cloud experience.

Validation: render both Letter pages; inspect for clipping; verify text extraction, link annotations, and embedded fonts. Verify the download from desktop and mobile, and ensure it does not trigger the exit animation. Rebuilds are deterministic with the pinned dependency.
