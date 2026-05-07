const grid = document.querySelector("[data-post-grid]");
const postCount = document.querySelector("[data-post-count]");

const formatDate = (value) => {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) {
    return value;
  }
  return new Intl.DateTimeFormat("en-US", { dateStyle: "long" }).format(date);
};

const renderPosts = (posts) => {
  if (!grid) {
    return;
  }

  if (!posts.length) {
    grid.innerHTML = `
      <article class="post-card post-card-placeholder">
        <p>No posts yet. Scaffold one with <code>python3 docs/scripts/new_post.py "My First Note"</code>.</p>
      </article>
    `;
    return;
  }

  grid.innerHTML = posts
    .map(
      (post) => `
        <article class="post-card">
          <p class="post-card-date">${formatDate(post.date)}</p>
          <h3><a href="${post.href}">${post.title}</a></h3>
          <p class="post-card-excerpt">${post.excerpt}</p>
          <div class="tag-row">
            ${(post.tags || []).map((tag) => `<span class="tag">${tag}</span>`).join("")}
          </div>
        </article>
      `,
    )
    .join("");
};

const loadPosts = async () => {
  try {
    const response = await fetch("./content/posts.json", { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`Failed to load post list: ${response.status}`);
    }

    const posts = await response.json();
    posts.sort((left, right) => right.date.localeCompare(left.date));
    if (postCount) {
      postCount.textContent = String(posts.length);
    }
    renderPosts(posts);
  } catch (error) {
    if (grid) {
      grid.innerHTML = `
        <article class="post-card post-card-placeholder">
          <p>Couldn't load the post list. Run <code>python3 docs/scripts/rebuild_posts.py</code> and refresh.</p>
        </article>
      `;
    }
    console.error(error);
  }
};

loadPosts();
