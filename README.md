# Calculation Notebook Site

This `docs/` folder is a static website starter for long-form technical notes.

## Preview locally

From the repository root:

```bash
python3 -m http.server 8000 --directory docs
```

Then open `http://localhost:8000`.

## Create a new post

```bash
python3 docs/scripts/new_post.py "My New Note"
```

That creates:

- `docs/posts/my-new-note/index.html`
- `docs/posts/my-new-note/content.md`

## Rebuild the home page manifest

If you add, rename, or remove posts manually, run:

```bash
python3 docs/scripts/rebuild_posts.py
```

## Writing math

For the safest rendering, prefer LaTeX delimiters like:

- inline math: `\(...\)`
- display math: `\[...\]` or `$$...$$`

## Publish with GitHub Pages

1. Push the repository to GitHub.
2. In repo settings, open **Pages**.
3. Set the source to deploy from the `main` branch and the `/docs` folder.
4. Save, then wait for GitHub Pages to publish the site.

The site uses CDN-hosted `marked` and MathJax in the browser, so it does not need a local Node toolchain.
