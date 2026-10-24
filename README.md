# yoyo-html-skill

把讲稿或指令，做成一条带 YoYo 配图的 HTML 学习路径。

打开是一篇能往下读的正文，不是一组排好序的页。

教学判断来自 [visual-cognition-slides](https://github.com/edu-ai-builders/visual-cognition-slides)：一次只推进一个想法，讲稿不上屏。页面不继承它的幻灯片外壳。配图是 YoYo 小人，放在句子旁边。

## 它产出什么

一份 HTML + 若干张 16:9 手绘配图。

- 默认外观：米底、点阵、窄正文栏。硬阴影只留给可点的卡片和按钮
- 默认角色：YoYo（膝盖长度黄裙子、红棕短发）
- 两种读法：自己往下读，或按「带领」先揭开这一段，再滑到下一段
- 链接、任务页、工具可以插在某一段后面

## 怎么用

在对话里说：

```
用 yoyo-html-skill，把下面这份讲稿做成学习路径。
```

或：

```
用 yoyo-html-skill。受众是新老师，走完要能自己改一节课的提问。
我想讲：先问对问题，再让 AI 出力。
```

Agent 会先分成几章，再复制 `template/journey.html` 生成页面，并在认知转折处生成 YoYo 图。

## 给别人用

```bash
git clone https://github.com/qiuyue-lab/yoyo-html-skill.git
mkdir -p ~/.cursor/skills
ln -s "$PWD/yoyo-html-skill" ~/.cursor/skills/yoyo-html-skill
```

用 `template/journey.html` 当骨架，不要从零写。想换形象：复制 `ip/_template/`，按里面的空表填自己的角色和参考图。

## 目录

```
yoyo-html skill/
├── SKILL.md                 Agent 主控
├── README.md
├── template/journey.html    通用 HTML 骨架（从这里复制）
├── ip/yoyo/                 默认 IP：外形、提示词、参考图
├── ip/_template/            空白 IP 档案
├── references/              教学、版式、组件、质检
├── examples/conversations.md
└── scripts/extract_shots.py 从 HTML 抽出配图清单
```

## 和原来两个 skill 的关系

| | visual-cognition-slides | yoyo-illustrations | 本 skill |
|---|---|---|---|
| 产出 | 翻页 HTML slides | 文章配图 PNG | 流动的 HTML 学习路径 + PNG |
| 擅长 | 叙事、认知动作、动画 | YoYo 隐喻图 | 把两件事接到同一条路径上 |
| 还在 | 独立 skill，讲座/投影仍可用 | 独立 skill，公众号正文仍可用 | 做课、工作坊、自走学习页 |

## 许可

沿用原两个 skill 的精神：可改、可传、可换 IP。YoYo 的真人参考图由 TeacherYo 提供，传播时请保留角色来源说明。
