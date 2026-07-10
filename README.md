# Utilities 4 Dragon

Utilities 4 Dragon is a static website and product marketing site for speech-recognition utilities designed to improve the Dragon workflow. The project combines a polished landing page, product detail pages, supporting content pages, and a simple contact/submission flow.

## Overview

This repository contains the front-end website for Utilities 4 Dragon, including:

- A responsive marketing homepage
- Product cards and individual product pages
- Blog and support-style content pages
- Legal, privacy, and purchase-related pages
- A small Python script to generate product pages from text-based product definitions

## Features

- Responsive, modern layout for desktop and mobile
- Product showcase for multiple Dragon-related utilities
- Clear calls to action for trials, purchases, and support
- Cookie consent and contact form support
- Simple content organization for marketing, blog, and legal pages

## Project structure

- [index.html](index.html) — main homepage
- [products/](products/) — generated product detail pages
- [products/details/](products/details/) — source data files for product pages
- [assets/](assets/) — CSS, JavaScript, and image assets
- [blog/](blog/) — blog and help content pages
- [buy/](buy/) — purchase-related page
- [legal/](legal/) and [privacy/](privacy/) — legal pages
- [generate_product_pages.py](generate_product_pages.py) — generates product pages from the text files in [products/details/](products/details/)
- [submit.php](submit.php) — simple PHP form handler

## Technology stack

- HTML5
- CSS3
- JavaScript
- Tailwind CSS (loaded via CDN)
- Python 3 for generating product pages
- PHP for form submission handling

## Getting started

### Option 1: Open directly in a browser

You can view the site locally by opening [index.html](index.html) in a browser.

### Option 2: Run a local web server

For a more reliable local preview, use a simple static server:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

## Regenerating product pages

The product pages are generated from text files in [products/details/](products/details/). To regenerate them, run:

```bash
python generate_product_pages.py
```

This will update the HTML files in [products/](products/) and refresh the product listing script used by the homepage.

## Deployment

Because this is a static website, it can be hosted on any standard web host or static hosting provider such as:

- GitHub Pages
- Netlify
- Vercel
- Any shared hosting service with support for PHP files

## Notes

- The site is designed as a marketing and content website rather than a full application.
- Some form-related functionality depends on PHP being available on the hosting environment.

## License

No license has been specified for this repository yet.
