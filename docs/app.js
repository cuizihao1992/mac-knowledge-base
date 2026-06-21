const state = {
  data: null,
  section: "all",
  query: "",
  askQuery: "",
  activeId: null,
};

const els = {
  overviewCards: document.querySelector("#overviewCards"),
  quickLinks: document.querySelector("#quickLinks"),
  search: document.querySelector("#search"),
  askForm: document.querySelector("#askForm"),
  askInput: document.querySelector("#askInput"),
  askSuggestions: document.querySelector("#askSuggestions"),
  answerPanel: document.querySelector("#answerPanel"),
  sections: document.querySelector("#sections"),
  stats: document.querySelector("#stats"),
  notes: document.querySelector("#notes"),
  reader: document.querySelector("#reader"),
};

const suggestedQuestions = [
  "jun-dd-web 有哪些可复用资产？",
  "哪些 CETC 项目可以归档？",
  "信访项目的技术结构是什么？",
  "哪些项目有敏感配置风险？",
  "这个知识库如何给 AI 使用？",
];

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
  let table = [];

  const flushList = () => {
    if (inList) {
      html.push("</ul>");
      inList = false;
    }
  };

  const flushTable = () => {
    if (!table.length) return;
    const rows = table.filter((row) => !/^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$/.test(row));
    if (rows.length) {
      html.push("<table>");
      rows.forEach((row, index) => {
        const cells = row
          .trim()
          .replace(/^\|/, "")
          .replace(/\|$/, "")
          .split("|")
          .map((cell) => cell.trim());
        const tag = index === 0 ? "th" : "td";
        html.push(`<tr>${cells.map((cell) => `<${tag}>${inline(cell)}</${tag}>`).join("")}</tr>`);
      });
      html.push("</table>");
    }
    table = [];
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

    if (/^\s*\|.+\|\s*$/.test(line)) {
      flushList();
      table.push(line);
      return;
    }

    flushTable();

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

  flushTable();
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

function noteByPath(path) {
  return state.data.notes.find((note) => note.path === path);
}

function tokenize(text) {
  const normalized = String(text)
    .toLowerCase()
    .replace(/[^\p{L}\p{N}]+/gu, " ")
    .trim();
  const words = normalized.split(/\s+/).filter((word) => word.length >= 2);
  const cjk = [...String(text).matchAll(/[\u4e00-\u9fa5]{2,}/g)]
    .flatMap((match) => {
      const value = match[0];
      const grams = [];
      for (let index = 0; index < value.length - 1; index += 1) {
        grams.push(value.slice(index, index + 2));
      }
      return grams;
    });
  return [...new Set([...words, ...cjk])];
}

function splitBodyIntoBlocks(note) {
  return note.body
    .split(/\n{2,}/)
    .map((block) => block.replace(/\s+/g, " ").trim())
    .filter((block) => block && !/^---$/.test(block) && block.length > 18)
    .slice(0, 180)
    .map((block) => ({ note, block }));
}

function scoreBlock(block, queryTokens, rawQuery) {
  const haystack = `${block.note.title} ${block.note.path} ${block.note.tags} ${block.block}`.toLowerCase();
  const score = queryTokens.reduce((sum, token) => {
    if (!haystack.includes(token)) return sum;
    if (block.note.title.toLowerCase().includes(token)) return sum + 7;
    if (block.note.path.toLowerCase().includes(token)) return sum + 5;
    return sum + 2;
  }, 0);
  return haystack.includes(rawQuery.toLowerCase()) ? score + 10 : score;
}

function findAnswerSources(query) {
  const queryTokens = tokenize(query);
  if (!queryTokens.length) return [];
  return state.data.notes
    .flatMap(splitBodyIntoBlocks)
    .map((block) => ({ ...block, score: scoreBlock(block, queryTokens, query) }))
    .filter((block) => block.score > 0)
    .sort((left, right) => right.score - left.score)
    .slice(0, 8);
}

function conciseBlock(block) {
  return block
    .replace(/^#+\s+/g, "")
    .replace(/^[-*]\s+/g, "")
    .replace(/\|/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, 260);
}

function renderAskSuggestions() {
  els.askSuggestions.innerHTML = suggestedQuestions
    .map(
      (question) => `
        <button type="button" data-question="${escapeHtml(question)}">${escapeHtml(question)}</button>
      `,
    )
    .join("");
}

function renderAnswer(query) {
  const sources = findAnswerSources(query);
  if (!sources.length) {
    els.answerPanel.innerHTML = `
      <div class="answer-empty">
        <h3>没找到足够相关的内容</h3>
        <p>可以换一个关键词，或先在上方搜索框里搜项目名、文档名。</p>
      </div>
    `;
    return;
  }

  const topSources = sources.slice(0, 4);
  const bullets = topSources
    .map((source) => `<li>${escapeHtml(conciseBlock(source.block))}</li>`)
    .join("");
  const sourceLinks = sources
    .map(
      (source) => `
        <button type="button" class="source-card" data-path="${escapeHtml(source.note.path)}">
          <span>${escapeHtml(source.note.title)}</span>
          <small>${escapeHtml(source.note.path)}</small>
        </button>
      `,
    )
    .join("");

  els.answerPanel.innerHTML = `
    <article class="answer-card">
      <div class="answer-title">
        <p class="panel-kicker">Local Answer</p>
        <h3>${escapeHtml(query)}</h3>
      </div>
      <p class="answer-note">这是基于当前静态知识库的检索式回答，适合快速定位；需要自然语言总结时，可以把这些来源交给 DeepSeek。</p>
      <ul class="answer-points">${bullets}</ul>
      <div class="answer-sources">
        <h4>来源</h4>
        <div>${sourceLinks}</div>
      </div>
    </article>
  `;
}

function openNoteByPath(path) {
  const note = noteByPath(path);
  if (note) {
    renderReader(note);
  }
}

function renderDashboard() {
  const referenceCount = state.data.notes.filter((note) => note.section === "references").length;
  const cetcCount = state.data.notes.filter((note) => /cetc/i.test(`${note.title} ${note.path} ${note.tags}`)).length;
  const chunkCount = state.data.corpusManifest?.chunkCount || state.data.vectorManifest?.chunkCount || "—";
  const vectorBackend = state.data.vectorManifest?.backend || "local";

  const cards = [
    { label: "文档总数", value: state.data.notes.length, detail: "Markdown 已同步到网站" },
    { label: "References", value: referenceCount, detail: "项目盘点、AI、清理计划" },
    { label: "CETC 文档", value: cetcCount, detail: "旧项目价值和删除决策" },
    { label: "AI 切块", value: chunkCount, detail: `${vectorBackend} 向量索引` },
  ];

  els.overviewCards.innerHTML = cards
    .map(
      (card) => `
        <div class="overview-card">
          <span>${escapeHtml(card.label)}</span>
          <strong>${escapeHtml(card.value)}</strong>
          <p>${escapeHtml(card.detail)}</p>
        </div>
      `,
    )
    .join("");

  const links = [
    {
      title: "CETC 清理命令计划",
      path: "30_References/cetc-cleanup-command-plan.md",
      desc: "第一批移动归档 dry-run 命令，只生成不执行。",
    },
    {
      title: "CETC 清理执行计划",
      path: "30_References/cetc-cleanup-execution-plan.md",
      desc: "把项目拆成可删、归档、脱敏、保留四个执行批次。",
    },
    {
      title: "CETC 自动资产抽取报告",
      path: "30_References/cetc-asset-extraction-report.md",
      desc: "删除前项目快照，包含页面/API/后端/配置线索。",
    },
    {
      title: "CETC 高价值项目深度资产报告",
      path: "30_References/cetc-high-value-project-deep-assets.md",
      desc: "深挖页面、路由、组件、接口、GIS 线索和配置风险。",
    },
    {
      title: "CETC 删除前资产抽取清单",
      path: "30_References/cetc-delete-prep-asset-extraction.md",
      desc: "决定哪些项目可删、归档或先脱敏。",
    },
    {
      title: "CETC 旧项目业务价值与架构判断",
      path: "30_References/cetc-project-business-value-and-architecture.md",
      desc: "按业务价值和架构组判断保留意义。",
    },
    {
      title: "云端模型知识库问答使用说明",
      path: "30_References/cloud-model-kb-qa-guide.md",
      desc: "用 DeepSeek / OpenAI 读取本地知识库。",
    },
    {
      title: "cuizihao 目录代码项目盘点",
      path: "30_References/mac-code-projects-inventory.md",
      desc: "查看 Mac 上主要代码项目分布。",
    },
  ];

  els.quickLinks.innerHTML = links
    .map((link) => {
      const note = noteByPath(link.path);
      return `
        <button class="quick-link" type="button" data-path="${escapeHtml(link.path)}" ${note ? "" : "disabled"}>
          <span>${escapeHtml(link.title)}</span>
          <small>${escapeHtml(link.desc)}</small>
        </button>
      `;
    })
    .join("");
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

function renderReader(note, options = {}) {
  if (!note) return;
  const { updateHash = true, enterReading = true } = options;
  state.activeId = note.id;
  els.reader.innerHTML = `
    <div class="reader-shell">
      <div class="reader-top">
        <button class="back-button" type="button" data-back>返回列表</button>
      </div>
      <h2>${escapeHtml(note.title)}</h2>
      <div class="reader-meta">
        <span>${escapeHtml(note.sectionTitle)}</span>
        <span>${escapeHtml(note.path)}</span>
        ${note.tags ? `<span>${escapeHtml(note.tags)}</span>` : ""}
      </div>
      <div class="reader-body">${markdownToHtml(note.body)}</div>
    </div>
  `;
  if (enterReading) {
    document.body.classList.add("reading");
  }
  if (updateHash) {
    history.replaceState(null, "", `#${encodeURIComponent(note.id)}`);
  }
  renderNotes();
  if (enterReading && window.matchMedia("(max-width: 900px)").matches) {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
}

function bindEvents() {
  els.search.addEventListener("input", (event) => {
    state.query = event.target.value;
    renderNotes();
  });

  els.askForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const query = els.askInput.value.trim();
    if (!query) return;
    state.askQuery = query;
    renderAnswer(query);
  });

  els.askSuggestions.addEventListener("click", (event) => {
    const button = event.target.closest("[data-question]");
    if (!button) return;
    els.askInput.value = button.dataset.question;
    state.askQuery = button.dataset.question;
    renderAnswer(button.dataset.question);
  });

  els.answerPanel.addEventListener("click", (event) => {
    const button = event.target.closest("[data-path]");
    if (!button) return;
    openNoteByPath(button.dataset.path);
    document.querySelector(".workspace")?.scrollIntoView({ behavior: "smooth", block: "start" });
  });

  els.sections.addEventListener("click", (event) => {
    const button = event.target.closest("[data-section]");
    if (!button) return;
    state.section = button.dataset.section;
    renderSections();
    renderNotes();
  });

  els.quickLinks.addEventListener("click", (event) => {
    const button = event.target.closest("[data-path]");
    if (!button) return;
    openNoteByPath(button.dataset.path);
  });

  els.notes.addEventListener("click", (event) => {
    const button = event.target.closest("[data-id]");
    if (!button) return;
    renderReader(state.data.notes.find((note) => note.id === button.dataset.id));
  });

  els.reader.addEventListener("click", (event) => {
    if (!event.target.closest("[data-back]")) return;
    document.body.classList.remove("reading");
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
}

fetch("./data.json")
  .then((response) => response.json())
  .then((data) => {
    state.data = data;
    renderDashboard();
    renderAskSuggestions();
    renderSections();
    renderNotes();
    bindEvents();
    const idFromHash = decodeURIComponent(window.location.hash.replace(/^#/, ""));
    const selectedFromHash = data.notes.find((note) => note.id === idFromHash);
    const isMobile = window.matchMedia("(max-width: 900px)").matches;
    const selected = selectedFromHash || data.notes[0];
    if (selected) {
      renderReader(selected, {
        updateHash: Boolean(selectedFromHash),
        enterReading: Boolean(selectedFromHash) || !isMobile,
      });
    }
  })
  .catch(() => {
    els.notes.innerHTML = '<div class="empty-state">无法加载知识库索引。</div>';
  });
