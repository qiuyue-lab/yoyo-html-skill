# 视觉主题

默认用手绘创意。用户没点名就不要问八选一。

生成时：复制 `template/journey.html` 顶部的 `:root`，不要另起一套颜色。

---

## 默认：手绘创意

```css
:root {
  --bg: #f5f0e8;
  --ink: #1a1410;
  --a1: #c8432a;   /* 红：强调 */
  --a2: #2a5fc8;   /* 蓝：信息 */
  --a3: #e8a020;   /* 金：高亮 */
  --a4: #2a8c4a;   /* 绿：正向 */
  --a5: #6b3fa0;   /* 紫：次要 */
  --paper: #ffffff;
  --muted: rgba(26,20,16,.56);
  --line: rgba(26,20,16,.14);
  --shadow: 6px 6px 0 var(--ink);
  --radius: 6px;
  --fb: "PingFang SC","Hiragino Sans GB","Noto Sans SC","Microsoft YaHei",sans-serif;
  --fm: "Space Mono",ui-monospace,Menlo,Consolas,monospace;
}
```

规则：米底 + 点阵；卡片白底、2px 黑边、硬阴影；不要渐变、不要模糊阴影、不要玻璃拟态。

YoYo 图的黄裙子是角色识别色，页面强调色仍用 `--a1` 红，不要满页铺黄。

---

## 要换主题时

去读 [visual-cognition-slides/STYLES.md](https://github.com/edu-ai-builders/visual-cognition-slides/blob/main/STYLES.md)，把对应主题的 CSS 变量替换进 `:root`。

常用备选：

| 主题 | 什么时候 |
|---|---|
| 学术简约 | 研究分享、论文配套 |
| 商务专业 | 对学校管理层、提案 |
| 暖色插画 | K12 学生自己走 |
| 纯动画概念 | 几乎没有配图、全靠运动讲原理 |

换主题时仍保留：流动布局、站点、YoYo 插槽、链接不被拦截。只换颜色和字体，不换骨架。
