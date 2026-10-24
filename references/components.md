# 组件写法

> 改已有 HTML、插入链接或配图时读这个。模板里都已实现，复制即可。

---

## 站点

```html
<section class="station st-figure turn" id="s3" data-title="核心判断" data-phase="s3">
  <div class="kicker">只要记住一件事</div>
  <div class="beat">
    <div>
      <h2>把散落的想法收成一个结构</h2>
    </div>
    <!-- 图放在 beat 的第二列，见下 -->
  </div>
  <aside class="notes">口播/带领时才看。屏幕上不要出现。</aside>
</section>
```

`id` 是 `s` + 数字，给脚本用，不要显示成「第 3 页」。
同一阶段的几站共用一个 `data-phase`，左侧 spine 只链到阶段起点。
`data-title` 短，给顶栏那一句用。
`.turn` 只加在阶段开头，多留一段空白。不要每站都加，不要画分隔线。
`.go` 在模板里是隐藏的，不要再写「下一步 →」。

---

## YoYo 配图插槽

有图（放进 `.beat`，和句子并排）。图大约占这一行的四成，仍然是抠出来浮在纸上的，不要加白卡片。默认图在右。某一处想把图放在左边，给这一行加 `fig-lead`，不要整篇锁死同一种方向：

```html
<div class="beat">
  <div>
    <h2>把散落的想法收成一个结构</h2>
    <p class="lede">一句读图。</p>
  </div>
  <figure class="yo-fig"
          data-yo-prompt="YoYo 把散落的想法拉进写着「整理」的箱子"
          data-yo-type="概念隐喻"
          data-yo-labels="认知锚点/整理/一张一结构">
    <img src="assets/03-sort.png" alt="把散落的想法收成一个结构">
    <figcaption>一站只收一件事。</figcaption>
  </figure>
</div>
```

还没出图（占位，页面仍可打开）：

```html
<figure class="yo-fig yo-slot"
        data-yo-prompt="YoYo 站在「听懂」和「能走」之间的桥上铺木板"
        data-yo-type="概念隐喻"
        data-yo-labels="听懂/能走/下一步">
  <div class="yo-ph">这里将放：YoYo 在「听懂」和「能走」之间铺桥</div>
</figure>
```

规则：

- 提示词写在 HTML 上，不另存文档。换一站的图 = 改属性和重生成那一张
- `data-yo-type` 取：`前后对比` / `概念隐喻` / `角色状态` / `Workflow` / `系统局部` / `方法分层` / `地图路线` / `小漫画分镜`
- 标注最多 5 个词，用 `/` 分隔
- 图是 16:9 白底。模板用 `mix-blend-mode: multiply` 让白底融进米纸

---

## 链接（随时可插）

页面里任何位置：

```html
<a class="btn" href="https://example.com" target="_blank" rel="noopener">打开工具 ↗</a>
<a class="btn ghost" href="./task.html" target="_blank" rel="noopener">去做这一步 ↗</a>
<a class="text-link" href="#s7">跳到「试一试」</a>
```

同一站多个出口，用出口列表：

```html
<ul class="exits">
  <li><a class="btn" href="./task.html" target="_blank" rel="noopener">任务页 ↗</a></li>
  <li><a class="btn ghost" href="https://..." target="_blank" rel="noopener">阅读原文 ↗</a></li>
</ul>
```

点击 `a` / `button` / `iframe` / `[data-interactive]` 不得进入下一站。模板 JS 已经排除。

---

## 站内逐步揭开

```html
<div class="step" data-step="1">先出现这一句</div>
<div class="step" data-step="2">再出现这一块</div>
<div class="step" data-step="3">最后出现出口</div>
```

浏览模式：全部可见。
带领模式：空格 / 右箭头先揭开这一段里还没出现的内容，揭完再往下移。

---

## 嵌入

```html
<div class="embed" data-interactive>
  <iframe src="./task.html" title="任务页"></iframe>
</div>
```

嵌入放在正在读的那一段里，不要弹到全屏新世界，除非读者自己点链接。

---

## 左侧只留阶段词

一项对应一章，用那一章的词。不要按段落编号：

```html
<nav class="spine" aria-label="路径">
  <a href="#s1">打开</a>
  <a href="#s4">用得了</a>
  <a href="#s8">留下</a>
</nav>
```

顶栏的 `#where` 跟着当前阶段换成一句人话，例如「还会有人打开吗」。不要写「3 / 15」。
