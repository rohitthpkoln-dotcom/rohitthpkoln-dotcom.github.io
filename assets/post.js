const titleNode = document.querySelector("[data-post-title]");
const dateNode = document.querySelector("[data-post-date]");
const ledeNode = document.querySelector("[data-post-lede]");
const bodyNode = document.querySelector("[data-post-body]");
const tagNode = document.querySelector("[data-post-tags]");
const tocNode = document.querySelector("[data-post-toc]");

const FRONTMATTER_PATTERN = /^---\s*\n([\s\S]*?)\n---\s*\n?/;
const HTML_ESCAPE_LOOKUP = {
  "&": "&amp;",
  "<": "&lt;",
  ">": "&gt;",
  '"': "&quot;",
  "'": "&#39;",
};

const slugify = (value) =>
  value
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, "")
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");

const escapeHtml = (value) => value.replace(/[&<>"']/g, (character) => HTML_ESCAPE_LOOKUP[character]);

const extractFrontmatter = (rawText) => {
  const match = rawText.match(FRONTMATTER_PATTERN);
  if (!match) {
    return { metadata: {}, body: rawText };
  }

  const metadata = {};
  for (const line of match[1].split(/\r?\n/)) {
    if (!line.includes(":")) {
      continue;
    }
    const [key, ...valueParts] = line.split(":");
    const value = valueParts.join(":").trim().replace(/^"(.*)"$/, "$1");
    metadata[key.trim()] = value;
  }

  metadata.tags = (metadata.tags || "")
    .split(",")
    .map((tag) => tag.trim())
    .filter(Boolean);

  return {
    metadata,
    body: rawText.slice(match[0].length),
  };
};

const protectMarkdown = (rawText) => {
  const tokens = [];
  let text = rawText;

  const stash = (pattern, label, kind) => {
    text = text.replace(pattern, (match) => {
      const token = `@@${label}_${tokens.length}@@`;
      tokens.push({ token, match, kind });
      return token;
    });
  };

  stash(/```[\s\S]*?```/g, "CODE_BLOCK", "code");
  stash(/`[^`\n]+`/g, "INLINE_CODE", "code");
  stash(/\$\$[\s\S]*?\$\$/g, "MATH_BLOCK", "math");
  stash(/\\\[[\s\S]*?\\\]/g, "MATH_BLOCK", "math");
  stash(/\\\([\s\S]*?\\\)/g, "MATH_INLINE", "math");

  const markdown = tokens
    .filter((item) => item.kind === "code")
    .reduce((output, item) => output.replace(item.token, item.match), text);

  return {
    markdown,
    restoreMath(rendered) {
      const unwrapped = rendered.replace(/<p>\s*(@@MATH_BLOCK_\d+@@)\s*<\/p>/g, "$1");
      return tokens
        .filter((item) => item.kind === "math")
        .reduce((output, item) => output.replace(item.token, escapeHtml(item.match)), unwrapped);
    },
  };
};

const formatDate = (value) => {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) {
    return value;
  }
  return new Intl.DateTimeFormat("en-US", { dateStyle: "long" }).format(date);
};

const waitForMathJax = async () => {
  for (let attempt = 0; attempt < 120; attempt += 1) {
    if (window.MathJax?.typesetPromise) {
      return true;
    }
    await new Promise((resolve) => window.setTimeout(resolve, 250));
  }
  return false;
};

const waitForMarked = async () => {
  for (let attempt = 0; attempt < 40; attempt += 1) {
    if (window.marked?.parse) {
      return true;
    }
    await new Promise((resolve) => window.setTimeout(resolve, 100));
  }
  return false;
};

const buildToc = () => {
  if (!tocNode || !bodyNode) {
    return;
  }

  const headings = [...bodyNode.querySelectorAll("h2, h3")];
  if (!headings.length) {
    tocNode.innerHTML = "<p class=\"toc-empty\">No section headings in this note.</p>";
    return;
  }

  tocNode.innerHTML = headings
    .map((heading) => {
      if (!heading.id) {
        heading.id = slugify(heading.textContent || "section");
      }
      const levelClass = heading.tagName.toLowerCase() === "h3" ? "toc-item toc-item-sub" : "toc-item";
      return `<li class="${levelClass}"><a href="#${heading.id}">${heading.textContent}</a></li>`;
    })
    .join("");
};

const renderTags = (tags) => {
  if (!tagNode) {
    return;
  }

  tagNode.innerHTML = tags.map((tag) => `<span class="tag">${tag}</span>`).join("");
};

const renderPost = async () => {
  if (!bodyNode) {
    return;
  }

  try {
    const response = await fetch("./content.md", { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`Failed to load content.md: ${response.status}`);
    }

    if (!(await waitForMarked())) {
      throw new Error("Markdown renderer failed to load.");
    }

    const rawText = await response.text();
    const { metadata, body } = extractFrontmatter(rawText);
    const protectedMarkdown = protectMarkdown(body);
    const rendered = window.marked.parse(protectedMarkdown.markdown);

    document.title = `${metadata.title || "Untitled note"} | Rohit's Notebook`;

    if (titleNode) {
      titleNode.textContent = metadata.title || "Untitled note";
    }
    if (dateNode) {
      dateNode.textContent = formatDate(metadata.date || "");
    }
    if (ledeNode) {
      ledeNode.textContent = metadata.excerpt || "";
    }

    renderTags(metadata.tags || []);

    bodyNode.innerHTML = protectedMarkdown.restoreMath(rendered);
    buildToc();

    if (await waitForMathJax()) {
      await window.MathJax.typesetPromise([bodyNode]);
    }
  } catch (error) {
    bodyNode.innerHTML = `
      <div class="error-panel">
        <h2>Post failed to load</h2>
        <p>Check that this folder contains a <code>content.md</code> file with frontmatter.</p>
      </div>
    `;
    console.error(error);
  }
};

renderPost();
