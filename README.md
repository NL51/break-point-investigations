# Break Point Investigations

Responsive, buildless, multipage marketing website for Delvin J. Watts (DJ).

## Pages
Home, Services, Background Investigations, About, Contact, plus Privacy and a 404 page.

## Edit and run
Edit `build.py` for page copy, metadata and shared layout. Run `python build.py`. Styles and interactions live in `dist/assets/site.css` and `site.js`. Serve `dist` using any static host. The site has no build dependencies.

## Contact behavior
Persistent phone, text and email links are available on every page. The contact form intentionally prepares a mailto email draft, requires the visitor to send in their email client, and clearly states that no submission occurs on the website. No data is stored and no backend email delivery provider is configured. Do not relabel this as a submitted contact form without implementing and testing server delivery.

## Search and sharing
Unique titles, descriptions, canonical URLs, Open Graph images, ProfessionalService JSON-LD, robots.txt, and sitemap.xml. Canonical origin currently points to the published Sites address. Update `ORIGIN` and rebuild before migrating to a custom domain. Google indexing and rankings are not guaranteed.

## Important identity distinction
The user supplied breakpointpi.com, but on November 3, 2026 that site identified Karen, a Southern California process-serving operation, phone 310-874-3294. It did not identify DJ Watts. Its Google/Yelp reviews, pricing, process service claims, and social profiles were therefore not copied. This website uses DJ's supplied signature and matching agency public records. Do not associate the other business's listings with this firm.

The supplied license number PI188952 is displayed as provided; current license standing has not been independently confirmed. The street address is designated as a mailing address, not a walk-in office. No unverified social URLs, ratings, review counts, testimonials, or guarantees are published.

## Original assets
Original AI-generated Northern California illustrative landscape and casework still life are in `dist/assets`. They are illustrative, not actual premises, cases or staff. Custom vector wordmark, favicon, regional connection graphic and social preview are included. Prompts are documented in SOURCES.md.
