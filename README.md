# Utilities 4 Dragon

Utilities 4 Dragon is a modern web application and product marketing site for speech-recognition utilities designed to improve the Dragon workflow. The project combines a polished landing page, product detail pages, supporting content pages, and interactive front-end features powered by JavaScript.

## Overview

This repository contains the web application for Utilities 4 Dragon, including:

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
- [submit.php](submit.php) — form-related backend endpoint file

## Technology stack

- HTML5
- CSS3
- JavaScript
- Tailwind CSS (loaded via CDN)
- Python 3 for generating product pages
- JavaScript for interactive UI behavior

## Getting started

### Option 1: Run locally with a web server

For local development, run a simple server from the project root:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

### Option 2: Deploy or preview with GitHub

The project can be hosted from GitHub Pages or a similar static hosting platform for front-end preview and deployment.

### Option 3: Production deployment

For production, deploy the site to a host that supports your JavaScript-based front end and any related server-side integrations.

## Regenerating product pages

The product pages are generated from text files in [products/details/](products/details/). To regenerate them, run:

```bash
python generate_product_pages.py
```

This will update the HTML files in [products/](products/) and refresh the product listing script used by the homepage.

## Deployment

The live site is hosted at https://www.utilities4d.org/.

This project can be deployed on GitHub or any hosting provider that supports a JavaScript-driven web application.

## Notes

- The site is designed as a modern web application with marketing, content, and interactive front-end features.
- Any additional server-side behavior should be supported by the hosting environment.

## License

No license has been specified for this repository yet.
