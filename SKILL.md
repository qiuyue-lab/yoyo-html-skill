---
name: yoyo-html-skill
description: >
  把讲稿或具体指令写成一篇能往下读的 HTML，关键处配 YoYo 手绘小图。
  教学判断来自 visual-cognition-slides（一次只推进一个想法、讲稿不上屏、走完要能做事）。
  页面不要继承它的幻灯片外壳。配图角色来自 yoyo-illustrations，在正文里跟句子并排、大约占这一行的四成，抠出来浮在纸上。
  触发：做学习页 / 学习路径 / HTML 课 / yoyo-html / 讲稿做成页面 / 配图+HTML / 工作坊引导页。
---

# yoyo-html-skill

> 地图，不是说明书。细节按需读取子文件。
> 默认 IP 是 YoYo。换形象 → 读 `ip/_template/IP.md`。

你在写一篇别人能顺着读完的东西。打开是一条往下走的正文，不是一组被排好序的页。

输出：单文件 HTML（可另附 `assets/` 配图）。打开就能用，随时能插链接。

---

## 为什么上一版会做死

禁止项写过「不要翻页」。Agent 还是做出了大图、虚线、左侧 01 到 15。因为更具体的指令在要求它做幻灯片：

1. **单位换了名字，形状没换。** visual-cognition-slides 的单位是「一张 slide 一个认知动作」。这里把它改叫「站点」，又要求先交一张编号表，一行一个动作。讲稿一切，就变成十几行。每一行再被做成一块，目录就天然是 01 到 15。编号表是幻灯片排序器。
2. **让人继承了幻灯片的视觉语言。** 卡片、硬阴影、一页一块主视觉，是那套 slides 的外壳。该留下的只有教学判断：一次只推进一个想法、讲稿进 notes、走完要能做事。外壳一继承，页面就会长出框和缝。
3. **两套 skill 对「图」的职位相反，这里没有裁决。** yoyo-illustrations 的图是一张让人停下来看的 16:9。放进正文时，它跟句子并排，大约占这一行的四成，抠出来浮在纸上。太小就成邮票，加白框或铺满就又成海报。

所以下面不按「一站一行」来切。按篇章来写。一个想法是一段话，不是一块新的页。

---

## 工作流

### Step 0：判断入口

| 用户给了什么 | 做什么 |
|---|---|
| 粗想法（「我想讲 X」） | Step 1 问诊 |
| 讲稿 / 口播稿 / 具体指令 | 跳到 Step 2 |
| 已有 HTML，要加图 / 加链接 / 改一站 | 只改那一处，读 `references/components.md` |
| 「先不要生成，只出结构」 | 做到 Step 2 的篇章提纲就停 |

### Step 1：问诊（只在粗想法时）

一次问两件：

1. **走完这条路径的人，要能做什么？**（行动，不是「记住一句话」）
2. **他们现在卡在哪？**

按需追问：已经知道多少、大概走多久、在什么场景打开（自己看 / 带着一群人走 / 公众号配套）。

输出 3–5 行内容简报，确认后再继续。

### Step 2：分成少数几章

读取 `references/pedagogy.md` 的「叙事结构」，选一个并说一句原因。再读 `references/layouts.md`。

一篇东西只分 **3 到 5 章**。章是读者能感到的转折（从「我会用」到「别人用得了」），不是讲稿里的每一个要点。

章里面是连续的段落。一个段落只推进一个想法。多数段落没有自己的标题，也没有自己的目录项。讲稿原文进 `<aside class="notes">`，不上屏。

先写给自己看的提纲，不要交一张编号表：

```
章（读者能感到的转折）
  - 这一段要让人发生什么
  - 下一段接上它的哪一句
哪里配一张图，图在替哪一句做事
```

提纲里的每一行不要变成页面上的一节。行数远多于 `<section>` 的数量，是正常的。

### Step 3：视觉分工（图跟句子并排，大约四成）

| 类型 | 用什么 | 何时 |
|---|---|---|
| **A 结构** | HTML / SVG / CSS 动画 | 框架、对比、步骤、数字、清单 |
| **B 隐喻** | YoYo 生成图 | 封面钩子、认知转折、概念隐喻、情绪 |
| **C 出口** | `<a>` / 嵌入 | 工具、任务页、阅读、下一条路径 |

一篇里 B 类通常 3–6 张。图多了，阅读会不断停下来看海报。
默认是米底、点阵、正文栏窄。硬阴影只用在真正可点的卡片和按钮上，不要用在图上，也不要用来把每一段框成一页。用户点名换主题时读 `references/styles.md`。

B 类每一张先在 HTML 里写好插槽，不要先空着再补：

```html
<div class="beat">
  <div>
    <h2>把散落的想法，收成一个结构。</h2>
    <p class="lede">一句解释。图在旁边，不另起一块海报。</p>
  </div>
  <figure class="yo-fig" data-yo-prompt="YoYo 把散落的想法拉进「整理」箱"
          data-yo-type="概念隐喻" data-yo-labels="认知锚点/整理/一张一结构">
    <img src="assets/03-sort.png" alt="把散落的想法收成一个结构">
  </figure>
</div>
```

链接随时可插，写法见 `references/components.md`。点链接不能误触发带领模式下的往下走。

### Step 4：从模板生成 HTML

1. 复制 `template/journey.html`（这是通用骨架，别人也从这里改）
2. 改 `<title>`、顶栏、`<nav class="spine">`。spine 一项对应一章，用那一章的词，不要按段落编号。同一章里的段落共用一个 `data-phase`
3. 保留模板里的 CSS / JS（浏览模式 + 带领模式）
4. 精确内容用 HTML/SVG；需要动画时读 `references/animations.md`
5. B 类插槽先写 `data-yo-*`。图还没有时用 `.yo-slot` 占位，页面也要能先打开

### Step 5：生成 YoYo 配图并回填

用户说「生成 / 出图 / 做图」就不要停下来等确认。

读取 `ip/yoyo/prompt-template.md` + `ip/yoyo/yoyo-ip.md`。
每张图单独调用 `GenerateImage`：

- `aspect_ratio`: `"16:9"`
- `reference_image_paths` 必须带上（用本 skill 的绝对路径）：
  - `ip/yoyo/assets/reference-photo.png`
  - `ip/yoyo/assets/yoyo-character-calibration-v5.png`
- description 里写：`stylize into hand-drawn sketch, NOT photorealistic`

真人参考图可以用于提炼外形，也可以传播，不要把它当写真贴进画面。

图保存到与 HTML 同级的 `assets/`，按它服务的那一句命名：`leave.jpg`，不要按页码 `03-`。
回填 `<img src>`，去掉 `.yo-slot`。

也可用 `python scripts/extract_shots.py 那份.html` 抽出 shot list、检查缺图。

### Step 6：检查

读取 `references/qa.md`。至少确认：

- [ ] 读起来是一篇文字：章节远少于想法的数量，目录不是段落清单
- [ ] 图跟句子并排，大约占这一行的四成，抠出来浮着，没有白卡片。某一处可以改到左边，不要整篇锁死方向
- [ ] 链接能点、会新开，点它不会被带着往下翻
- [ ] YoYo 图在做核心动作，裙子到膝盖
- [ ] 手机上标题和正文够大
- [ ] 缺图的插槽还在，没有破图

---

## 文件地图

| 文件 | 何时读 |
|---|---|
| `SKILL.md` | 始终 |
| `template/journey.html` | Step 4，复制后改 |
| `references/pedagogy.md` | Step 2 |
| `references/layouts.md` | Step 2 选序列 / 版式 |
| `references/components.md` | 插图、链接、带领、嵌入 |
| `references/styles.md` | 用户要换主题 |
| `references/animations.md` | 某站需要概念动画 |
| `references/qa.md` | Step 6 |
| `ip/yoyo/*` | Step 5 生图 |
| `ip/_template/IP.md` | 别人要换成自己的形象 |
| `scripts/extract_shots.py` | 抽 shot list / 查缺图 |

---

## 换 IP（给后来者）

默认走 `ip/yoyo/`。若用户要自己的小人：

1. 复制 `ip/_template/` 成 `ip/<名字>/`
2. 填外形、禁止项、参考图
3. 生图时改读那份档案，提示词里替换角色描述
