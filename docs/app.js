const state = {
  data: null,
  section: "all",
  query: "",
  activeId: null,
};

const els = {
  search: document.querySelector("#search"),
  sections: document.querySelector("#sections"),
  stats: document.querySelector("#stats"),
  notes: document.querySelector("#notes"),
  reader: document.querySelector("#reader"),
};

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function markdownToHtml(markdown) {
  const lines = markdown.split(/\r?\n/);
  const html = [];
  let inList = false;
  let inCode = false;
  let code = [];

  const flushList = () => {
    if (inList) {
      html.push("</ul>");
      inList = false;
    }
  };

  const inline = (text) =>
    escapeHtml(text)
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');

  lines.forEach((line) => {
    if (line.startsWith("```")) {
      if (inCode) {
        html.push(`<pre><code>${escapeHtml(code.join("\n"))}</code></pre>`);
        code = [];
        inCode = false;
      } else {
        flushList();
        inCode = true;
      }
      return;
    }

    if (inCode) {
      code.push(line);
      return;
    }

    if (/^###\s+/.test(line)) {
      flushList();
      html.push(`<h3>${inline(line.replace(/^###\s+/, ""))}</h3>`);
      return;
    }
    if (/^##\s+/.test(line)) {
      flushList();
      html.push(`<h2>${inline(line.replace(/^##\s+/, ""))}</h2>`);
      return;
    }
    if (/^#\s+/.test(line)) {
      flushList();
      html.push(`<h1>${inline(line.replace(/^#\s+/, ""))}</h1>`);
      return;
    }
    if (/^[-*]\s+/.test(line)) {
      if (!inList) {
        html.push("<ul>");
        inList = true;
      }
      html.push(`<li>${inline(line.replace(/^[-*]\s+/, ""))}</li>`);
      return;
    }
    if (!line.trim()) {
      flushList();
      return;
    }

    flushList();
    html.push(`<p>${inline(line)}</p>`);
  });

  flushList();
  return html.join("");
}

function filteredNotes() {
  const query = state.query.trim().toLowerCase();
  return state.data.notes.filter((note) => {
    const inSection = state.section === "all" || note.section === state.section;
    const haystack = `${note.title} ${note.sectionTitle} ${note.path} ${note.tags} ${note.excerpt} ${note.body}`.toLowerCase();
    return inSection && (!query || haystack.includes(query));
  });
}

function renderSections() {
  const counts = new Map();
  state.data.notes.forEach((note) => counts.set(note.section, (counts.get(note.section) || 0) + 1));
  const buttons = [
    { id: "all", title: "All", description: "全部内容", count: state.data.notes.length },
    ...state.data.sections.map((section) => ({
      ...section,
      count: counts.get(section.id) || 0,
    })),
  ];

  els.sections.innerHTML = buttons
    .map(
      (section) => `
        <button class="section-button ${state.section === section.id ? "active" : ""}" data-section="${section.id}">
          <span>${escapeHtml(section.title)}</span>
          <span class="count">${section.count}</span>
        </button>
      `,
    )
    .join("");
}

function renderNotes() {
  const notes = filteredNotes();
  els.stats.textContent = `${notes.length} 篇内容 · 生成于 ${new Date(state.data.generatedAt).toLocaleString("zh-CN")}`;

  if (!notes.length) {
    els.notes.innerHTML = '<div class="empty-state">没有匹配的内容。</div>';
    return;
  }

  els.notes.innerHTML = notes
    .map(
      (note) => `
        <button class="note-card ${state.activeId === note.id ? "active" : ""}" data-id="${note.id}">
          <span class="note-title">${escapeHtml(note.title)}</span>
          <span class="note-meta">
            <span>${escapeHtml(note.sectionTitle)}</span>
            <span>${escapeHtml(note.path)}</span>
          </span>
          <p class="note-excerpt">${escapeHtml(note.excerpt || "暂无摘要")}</p>
        </button>
      `,
    )
    .join("");
}

function renderReader(note) {
  if (!note) return;
  state.activeId = note.id;
  els.reader.innerHTML = `
    <h2>${escapeHtml(note.title)}</h2>
    <div class="reader-meta">
      <span>${escapeHtml(note.sectionTitle)}</span>
      <span>${escapeHtml(note.path)}</span>
      ${note.tags ? `<span>${escapeHtml(note.tags)}</span>` : ""}
    </div>
    <div class="reader-body">${markdownToHtml(note.body)}</div>
  `;
  renderNotes();
}

function bindEvents() {
  els.search.addEventListener("input", (event) => {
    state.query = event.target.value;
    renderNotes();
  });

  els.sections.addEventListener("click", (event) => {
    const button = event.target.closest("[data-section]");
    if (!button) return;
    state.section = button.dataset.section;
    renderSections();
    renderNotes();
  });

  els.notes.addEventListener("click", (event) => {
    const button = event.target.closest("[data-id]");
    if (!button) return;
    renderReader(state.data.notes.find((note) => note.id === button.dataset.id));
  });
}

fetch("./data.json")
  .then((response) => response.json())
  .then((data) => {
    state.data = data;
    renderSections();
    renderNotes();
    bindEvents();
    if (data.notes[0]) renderReader(data.notes[0]);
  })
  .catch(() => {
    els.notes.innerHTML = '<div class="empty-state">无法加载知识库索引。</div>';
  });
