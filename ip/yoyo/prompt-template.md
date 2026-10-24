# 生图提示词

每张图单独生成。把 `{...}` 换成这一站的内容。

```text
Generate one standalone 16:9 horizontal Chinese illustration for a learning page.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines. Lots of empty white space. Sparse red/orange/blue handwritten Chinese annotations. Clean absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic photo, no photorealistic portrait.

Recurring IP character required:
YoYo, a simplified hand-drawn female character inspired by the reference images. Shoulder-length reddish-brown hair with short bangs. Bright yellow sleeveless loose dress — extends to KNEE length only, NOT calf, NOT ankle, NOT floor-length. Light and not dragging. NO pants. Slim energetic body. Natural warm expression with a gentle smile, lively eyes, NOT blank deadpan face. Black thin hand-drawn outlines with flat yellow dress fill. YoYo must perform the core conceptual action, not decorate the scene. Serious, clean, slightly absurd, not cute, not photorealistic.

Reference image guidance:
Use reference images only for hairstyle, yellow knee-length dress, and energetic personality. Stylize into hand-drawn sketch — do NOT paste the photo.

Theme:
{这一站的配图主题}

Structure type:
{结构类型}

Core idea:
{这张图要表达的核心意思}

Composition:
{YoYo 在哪里、正在做什么、主要物件、信息如何流动}

Chinese handwritten labels:
{标注1} / {标注2} / {标注3}

Color use:
Black for line art. Yellow for YoYo's dress. Orange for flow/arrows. Red for key points. Blue for secondary notes.

Constraints:
One image explains only one core structure. 40%-60% main subject. At least 35% blank white space. Max 5-8 short Chinese labels. No top-left title. Invent a fresh metaphor. Precise numbers and long sentences belong in the HTML, not in this image.
```

## GenerateImage 调用

路径改成这个 skill 的绝对路径。

```json
{
  "description": "<上面整段提示词>",
  "aspect_ratio": "16:9",
  "filename": "03-sort.png",
  "reference_image_paths": [
    "<skill-root>/ip/yoyo/assets/reference-photo.png",
    "<skill-root>/ip/yoyo/assets/yoyo-character-calibration-v5.png"
  ]
}
```

description 末尾补一句：`stylize into hand-drawn sketch, NOT photorealistic`
