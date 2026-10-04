#!/usr/bin/env python3
"""Build every page of the site from the JSON files in content/.

    python3 scripts/build_site.py

Edit content/*.json (or add a note under posts/), then rerun this script and
commit the generated HTML. No third-party packages are needed.
"""

from __future__ import annotations

import html
import json
import re
from datetime import date
from pathlib import Path

import rebuild_posts

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
AUTOLINKS: dict = {}

FONTS = "/assets/fonts/fonts.css"  # self-hosted Newsreader + Inter

# (key, nav label, url, banner title)
PAGES = [
    ("home", "Home", "/", None),
    ("research", "Research", "/research/", "Research Interests"),
    ("publications", "Publications", "/publications/", "Publications"),
    ("talks", "Talks", "/talks/", "Talks"),
    ("teaching", "Teaching", "/teaching/", "Teaching"),
    ("conferences", "Conferences", "/conferences/", "Conferences &amp; Workshops"),
    ("notes", "Notes", "/notes/", "Notes"),
    ("links", "Links", "/links/", "Links"),
]

ICONS = {
    "email": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "github": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.48v-1.7c-2.78.6-3.37-1.34-3.37-1.34-.45-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.9 1.52 2.34 1.08 2.91.83.09-.65.35-1.08.63-1.33-2.22-.25-4.55-1.11-4.55-4.94 0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.27.1-2.64 0 0 .84-.27 2.75 1.02a9.56 9.56 0 0 1 5 0c1.91-1.29 2.75-1.02 2.75-1.02.55 1.37.2 2.39.1 2.64.64.7 1.03 1.59 1.03 2.68 0 3.84-2.34 4.68-4.57 4.93.36.31.68.92.68 1.85v2.75c0 .27.18.58.69.48A10 10 0 0 0 12 2Z"/></svg>',
    "scholar": "GS",
    "arxiv": "arX",
    "orcid": "iD",
    "cv": "CV",
    "linkedin": "in",
}


def load(name: str):
    return json.loads((CONTENT / name).read_text(encoding="utf-8"))


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def link(text: str, href: str = "") -> str:
    """Text, wrapped in a link when an address is given. Text may contain HTML."""
    return f'<a href="{esc(href)}">{text}</a>' if href else text


# ------------------------------------------------------------------ layout
def layout(site: dict, key: str, title: str, body: str, *, head_extra: str = "", hero: bool = True) -> str:
    current = ' aria-current="page"'
    nav = "\n".join(
        f'          <a href="{url}"{current if k == key else ""}>{label}</a>'
        for k, label, url, _ in PAGES
    )
    page_title = site["name"] if key == "home" else f"{title} | {site['name']}"
    year = date.today().year
    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{page_title}</title>
    <meta name="description" content="{esc(site['description'])}" />
    <link href="{FONTS}" rel="stylesheet" />
    <link rel="stylesheet" href="/assets/site.css" />{head_extra}
  </head>
  <body class="{"has-hero" if hero else "plain"}">
    <header class="topbar">
      <div class="topbar-inner">
        <a class="brand" href="/">{esc(site['name'])}</a>
        <input class="nav-toggle" id="nav-toggle" type="checkbox" />
        <label class="nav-toggle-label" for="nav-toggle" aria-label="Menu"><span></span><span></span><span></span></label>
        <nav class="topnav" aria-label="Primary">
{nav}
        </nav>
      </div>
    </header>
{body}
    <footer class="footer">
      <div class="footer-inner">
        <span>&copy; {year} {esc(site['name'])}</span>
        <span>Institute for Theoretical Physics, University of Cologne</span>
      </div>
    </footer>
  </body>
</html>
"""


def banner(site: dict, key: str, title: str, subtitle: str = "") -> str:
    image = site.get("banners", {}).get(key, "")
    position = "center"
    if isinstance(image, dict):
        image, position = image.get("src", ""), image.get("position", "center")
    style = (f' style="background-image: url(\'{esc(image)}\'); background-size: cover;'
             f' background-position: {esc(position)}"') if image else ""
    sub = f'\n        <p class="banner-sub">{subtitle}</p>' if subtitle else ""
    return (f'    <section class="banner banner-{key}"{style}>\n      <div class="banner-inner">\n'
            f'        <h1>{title}</h1>{sub}\n      </div>\n    </section>\n')


def intro(text: str) -> str:
    return f'      <p class="page-intro">{text}</p>\n' if text else ""


def empty(text: str = "To be added.") -> str:
    return f'      <p class="empty">{text}</p>\n'


def links_row(links: list[dict]) -> str:
    items = [link(esc(item["label"]), item["href"]) for item in links if item.get("href")]
    return f'<p class="entry-links">{"".join(f"<span>{i}</span>" for i in items)}</p>' if items else ""


def facts_sections(sections: list[dict]) -> str:
    """Compact CV-style lists: [{"heading": ..., "items": [{"text": ..., "when": ...}]}]."""
    out = []
    for section in sections:
        timeline = section.get("kind") == "timeline"
        rows = []
        for item in section.get("items", []):
            text = item["text"]
            if item.get("url"):
                head, sep, rest = text.partition("<span")
                text = f'<a class="fact-link" href="{esc(item["url"])}">{head}</a>' + (sep + rest if sep else "")
            marker = '<span class="tl-dot" aria-hidden="true"></span>' if timeline else ""
            current = ' class="is-current"' if item.get("current") else ""
            rows.append(f'          <li{current}><span class="fact-when">{item.get("when", "")}</span>'
                        f'{marker}<span class="fact-text">{text}</span></li>')
        cls = "facts timeline" if timeline else "facts"
        out.append(f'      <section class="section">\n        <h2>{section["heading"]}</h2>\n'
                   f'        <ul class="{cls}">\n' + "\n".join(rows) + '\n        </ul>\n      </section>\n')
    return "".join(out)


# ------------------------------------------------------------------ pages
def page_home(site: dict) -> str:
    paragraphs = "\n".join(f"          <p>{p}</p>" for p in site["home"])
    icons = []
    for item in site.get("links", []):
        if not item.get("href"):
            continue
        href = item["href"]
        if item["kind"] == "email" and not href.startswith("mailto:"):
            href = "mailto:" + href
        glyph = ICONS.get(item["kind"], esc(item["label"][:3]))
        icons.append(f'<a href="{esc(href)}" title="{esc(item["label"])}" aria-label="{esc(item["label"])}">{glyph}</a>')
    icon_row = f'          <div class="icon-row">{"".join(icons)}</div>\n' if icons else ""
    if site.get("photo"):
        photo = f'<img src="{esc(site["photo"])}" alt="Photo of {esc(site["name"])}" />'
    else:
        initials = "".join(part[0] for part in site["name"].split()[:2])
        photo = f'<div class="photo-placeholder" aria-hidden="true">{initials}</div>'
    body = banner(site, "home", esc(site["name"]), site.get("tagline", "")) + f"""    <main class="page">
      <div class="home-grid section">
        <div class="prose">
{paragraphs}
{icon_row}        </div>
        <figure class="photo-card" style="margin:0">{photo}</figure>
      </div>
{facts_sections(site.get("home_sections", []))}    </main>
"""
    return layout(site, "home", site["name"], body)


def page_research(site: dict, data: dict) -> str:
    out = [intro(data.get("intro", ""))]
    if data.get("paragraphs"):
        out.append('      <div class="prose">\n' + "\n".join(f"        <p>{p}</p>" for p in data["paragraphs"]) + "\n      </div>\n")
    for topic in data.get("topics", []):
        out.append(f'      <section class="section">\n        <h2>{topic["heading"]}</h2>\n        <div class="prose">\n')
        out.extend(f"          <p>{p}</p>\n" for p in topic.get("paragraphs", []))
        out.append("        </div>\n      </section>\n")
    body = banner(site, "research", "Research Interests") + '    <main class="page">\n' + "".join(out) + "    </main>\n"
    return layout(site, "research", "Research Interests", body)


def publication_entry(item: dict) -> str:
    meta = " ".join(x for x in [item.get("authors", ""), item.get("date", ""), item.get("status", "")] if x)
    lines = [f'        <li class="entry">\n          <p class="entry-title">{link(item["title"], item.get("url", ""))}</p>']
    if meta:
        lines.append(f'          <p class="entry-meta">{meta}</p>')
    if item.get("journal"):
        lines.append(f'          <p class="entry-meta">{link(item["journal"], ("https://doi.org/" + item["doi"]) if item.get("doi") else "")}</p>')
    if item.get("note"):
        lines.append(f'          <p class="entry-meta"><i>{item["note"]}</i></p>')
    extra = []
    if item.get("arxiv"):
        cat = f' [{item["category"]}]' if item.get("category") else ""
        extra.append({"label": f'arXiv:{item["arxiv"]}{cat}', "href": f'https://arxiv.org/abs/{item["arxiv"]}'})
    extra += item.get("links", [])
    if extra:
        lines.append("          " + links_row(extra))
    lines.append("        </li>")
    return "\n".join(lines)


def page_publications(site: dict, data: dict) -> str:
    out = [intro(data.get("intro", ""))]
    if data.get("in_preparation"):
        prep = "; ".join(
            f'<i>{p["title"]}</i>' + (f' (with {p["with"]})' if p.get("with") else "") for p in data["in_preparation"]
        )
        out.append(f'      <p class="prose"><b>In preparation:</b> {prep}.</p>\n')
    sections = [s for s in data.get("sections", []) if s.get("entries")]
    for section in sections:
        heading = f'        <h2>{section["heading"]}</h2>\n' if section.get("heading") else ""
        entries = "\n".join(publication_entry(e) for e in section["entries"])
        out.append(f'      <section class="section">\n{heading}        <ul class="entries">\n{entries}\n        </ul>\n      </section>\n')
    if not sections and not data.get("in_preparation"):
        out.append(empty())
    body = banner(site, "publications", "Publications") + '    <main class="page">\n' + "".join(out) + "    </main>\n"
    return layout(site, "publications", "Publications", body)


def page_talks(site: dict, data: dict) -> str:
    out = [intro(data.get("intro", ""))]
    talks = sorted(data.get("talks", []), key=lambda t: t.get("sort", t.get("date", "")), reverse=True)
    year = None
    for talk in talks:
        talk_year = str(talk.get("year") or talk.get("sort", talk.get("date", ""))[:4])
        if talk_year != year:
            if year is not None:
                out.append("      </ul>\n")
            out.append(f'      <h2 class="year-heading">{esc(talk_year)}</h2>\n      <ul class="entries">\n')
            year = talk_year
        where = ", ".join(x for x in [link(talk.get("event", ""), talk.get("event_url", "")), talk.get("place", "")] if x)
        meta = " &middot; ".join(x for x in [talk.get("date_text", talk.get("date", "")), where] if x)
        out.append(
            f'        <li class="entry">\n          <p class="entry-title">{pill(talk.get("role", ""))}{talk["title"]}</p>\n'
            f'          <p class="entry-meta">{meta}</p>\n          {links_row(talk.get("links", []))}\n        </li>\n'
        )
    if year is not None:
        out.append("      </ul>\n")
    else:
        out.append(empty())
    body = banner(site, "talks", "Talks") + '    <main class="page">\n' + "".join(out) + "    </main>\n"
    return layout(site, "talks", "Talks", body)


def page_teaching(site: dict, data: dict) -> str:
    out = [intro(data.get("intro", ""))]
    for inst in data.get("institutions", []):
        out.append(f'      <section class="section">\n        <h2>{inst["name"]}</h2>\n')
        if inst.get("text"):
            out.append(f'        <p class="prose">{inst["text"]}</p>\n')
        for term in inst.get("terms", []):
            out.append(f'        <h3>{term["term"]}</h3>\n')
            for course in term.get("courses", []):
                role = f'<br /><span class="entry-meta">{course["role"]}</span>' if course.get("role") else ""
                out.append(f'        <p class="entry-text">{link(course["title"], course.get("url", ""))}{role}</p>\n')
        out.append("      </section>\n")
    out.append(facts_sections(data.get("extra", [])))
    if not data.get("institutions"):
        out.append(empty())
    body = banner(site, "teaching", "Teaching") + '    <main class="page">\n' + "".join(out) + "    </main>\n"
    return layout(site, "teaching", "Teaching", body)


def pill(role: str) -> str:
    return f'<span class="pill">{esc(role)}</span>' if role else ""


def conference_list(items: list[dict]) -> str:
    rows = []
    for item in items:
        meta = " &middot; ".join(x for x in [item.get("date", ""), item.get("place", "")] if x)
        rows.append(
            f'        <li class="entry">\n          <p class="entry-title">{pill(item.get("role", ""))}{link(item["title"], item.get("url", ""))}</p>\n'
            f'          <p class="entry-meta">{meta}</p>\n        </li>'
        )
    return '      <ul class="entries">\n' + "\n".join(rows) + "\n      </ul>\n"


def page_conferences(site: dict, data: dict) -> str:
    out = [intro(data.get("intro", ""))]
    for key, heading in (("upcoming", "Upcoming"), ("past", "Past"), ("visits", "Research Visits")):
        if data.get(key):
            out.append(f'      <section class="section">\n        <h2>{heading}</h2>\n{conference_list(data[key])}      </section>\n')
    if not data.get("upcoming") and not data.get("past"):
        out.append(empty())
    title = "Conferences &amp; Workshops"
    body = banner(site, "conferences", title) + '    <main class="page">\n' + "".join(out) + "    </main>\n"
    return layout(site, "conferences", "Conferences & Workshops", body)


def page_links(site: dict, data: dict) -> str:
    """Press, media, videos and other links: content/media.json."""
    out = [intro(data.get("intro", ""))]
    for section in data.get("sections", []):
        items = section.get("items", [])
        if not items:
            continue
        out.append(f'      <section class="section">\n        <h2>{section["heading"]}</h2>\n')
        if section.get("kind") == "videos":
            out.append('        <div class="video-grid">\n')
            for v in items:
                src = f'https://www.youtube-nocookie.com/embed/{esc(v["youtube"])}'
                if v.get("start"):
                    src += f'?start={int(v["start"])}'
                caption = f'<figcaption>{v["caption"]}</figcaption>' if v.get("caption") else ""
                watch = f'https://www.youtube.com/watch?v={esc(v["youtube"])}' + (f'&amp;t={int(v["start"])}s' if v.get("start") else "")
                out.append(
                    f'          <figure class="video">\n            <div class="video-frame"><iframe src="{src}" '
                    f'title="{esc(v.get("title", "YouTube video"))}" loading="lazy" '
                    f'allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share" '
                    f'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>\n'
                    f'            {caption}<p class="entry-links"><span><a href="{watch}">Watch on YouTube</a></span></p>\n          </figure>\n')
            out.append('        </div>\n')
        else:
            rows = []
            for it in items:
                pill_html = pill(it.get("kind", ""))
                meta = " &middot; ".join(x for x in [it.get("source", ""), it.get("date", "")] if x)
                text = f'\n          <p class="entry-text">{it["text"]}</p>' if it.get("text") else ""
                rows.append(f'        <li class="entry">\n          <p class="entry-title">{pill_html}{link(it["title"], it.get("url", ""))}</p>\n'
                            f'          <p class="entry-meta">{meta}</p>{text}\n        </li>')
            out.append('        <ul class="entries">\n' + "\n".join(rows) + '\n        </ul>\n')
        out.append("      </section>\n")
    body = banner(site, "links", "Links") + '    <main class="page">\n' + "".join(out) + "    </main>\n"
    return layout(site, "links", "Links", body)


def page_notes(site: dict, posts: list[dict], lectures: dict) -> str:
    lecture_rows = []
    for lec in lectures.get("lectures", []):
        topics = "".join(f'<span class="tag">{esc(t)}</span>' for t in lec.get("tags", []))
        lecture_rows.append(
            f'        <li class="entry">\n          <p class="entry-title">{link(lec["title"], lec["pdf"])}</p>\n'
            f'          <p class="entry-meta">{lec.get("meta", "")}</p>\n'
            f'          <p class="entry-text">{lec.get("summary", "")}</p>\n'
            f'          <p class="entry-links"><span>{link("PDF", lec["pdf"])}</span></p>\n'
            f'          <div class="tag-row">{topics}</div>\n        </li>'
        )
    rows = []
    for post in posts:
        tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in post.get("tags", []))
        rows.append(
            f'        <li class="entry">\n          <p class="entry-title"><a href="/posts/{post["slug"]}/">{esc(post["title"])}</a></p>\n'
            f'          <p class="entry-meta">{esc(nice_date(post.get("date", "")))}</p>\n'
            f'          <p class="entry-text">{esc(post.get("excerpt", ""))}</p>\n'
            f'          <div class="tag-row">{tags}</div>\n        </li>'
        )
    listing = '      <ul class="entries">\n' + "\n".join(rows) + "\n      </ul>\n" if rows else empty()
    sections = ""
    if lecture_rows:
        sections += ('      <section class="section">\n        <h2>Lecture Notes</h2>\n'
                     + intro(lectures.get("intro", ""))
                     + '      <ul class="entries">\n' + "\n".join(lecture_rows) + "\n      </ul>\n      </section>\n")
    sections += '      <section class="section">\n        <h2>Calculation Notes</h2>\n' + listing + "      </section>\n"
    body = (
        banner(site, "notes", "Notes")
        + '    <main class="page">\n'
        + sections
        + "    </main>\n"
    )
    return layout(site, "notes", "Notes", body)


def nice_date(value: str) -> str:
    try:
        return date.fromisoformat(value).strftime("%B %-d, %Y")
    except ValueError:
        return value


POST_HEAD = """
    <script>
      window.MathJax = {
        tex: {
          inlineMath: [["\\\\(", "\\\\)"], ["$", "$"]],
          displayMath: [["\\\\[", "\\\\]"], ["$$", "$$"]],
        },
      };
    </script>
    <script defer src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
    <script type="module" src="/assets/post.js"></script>"""

POST_BODY = """    <main class="post-shell">
      <article>
        <header class="article-header">
          <p class="article-meta" data-post-date></p>
          <h1 data-post-title>Loading note&hellip;</h1>
          <p class="article-lede" data-post-lede></p>
          <div class="post-tags" data-post-tags></div>
        </header>
        <section class="article-body" data-post-body></section>
      </article>
      <aside class="toc-card">
        <p class="toc-label">On this page</p>
        <ol class="toc-list" data-post-toc></ol>
      </aside>
    </main>
"""


def page_post(site: dict, post: dict) -> str:
    return layout(site, "notes", post["title"], POST_BODY, head_extra=POST_HEAD, hero=False)


# ------------------------------------------------------------------ autolinks
def autolink(page: str, links: dict) -> str:
    """Link known names (universities, people) in the text of <main>, outside existing links."""
    names = sorted(links, key=len, reverse=True)
    pattern = re.compile("|".join(re.escape(n) for n in names)) if names else None

    def link_text(text: str) -> str:
        return pattern.sub(lambda m: f'<a href="{esc(links[m.group(0)])}">{m.group(0)}</a>', text)

    def process(main: str) -> str:
        out, depth = [], 0
        for part in re.split(r"(<[^>]+>)", main):
            if part.startswith("<"):
                if re.match(r"<a[\s>]", part):
                    depth += 1
                elif part.startswith("</a"):
                    depth -= 1
                out.append(part)
            else:
                out.append(link_text(part) if depth == 0 and part.strip() else part)
        return "".join(out)

    if not pattern:
        return page
    return re.sub(r"(<main[^>]*>)(.*?)(</main>)", lambda m: m.group(1) + process(m.group(2)) + m.group(3), page, flags=re.S)


# ------------------------------------------------------------------ main
def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    text = autolink(text, AUTOLINKS)
    target.write_text(text, encoding="utf-8")
    print(f"  wrote {path}")


def main() -> None:
    global AUTOLINKS
    AUTOLINKS = load("links.json")
    site = load("site.json")
    posts = rebuild_posts.build_manifest()
    write("index.html", page_home(site))
    write("research/index.html", page_research(site, load("research.json")))
    write("publications/index.html", page_publications(site, load("publications.json")))
    write("talks/index.html", page_talks(site, load("talks.json")))
    write("teaching/index.html", page_teaching(site, load("teaching.json")))
    write("conferences/index.html", page_conferences(site, load("conferences.json")))
    write("notes/index.html", page_notes(site, posts, load("lectures.json")))
    write("links/index.html", page_links(site, load("media.json")))
    for post in posts:
        write(f"posts/{post['slug']}/index.html", page_post(site, post))


if __name__ == "__main__":
    main()
