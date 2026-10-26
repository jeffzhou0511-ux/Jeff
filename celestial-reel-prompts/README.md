# 天宫仙镜 Reel：分镜提示词反推 × 三套原创方案

> 目标链接：https://www.instagram.com/reel/Ddy70oZtVHH/
> 创作者：**GFW-（@agen_i_alpha）**，自述 "AI Visual Creator | Cinematic Art & Fantasy Scenes / Prompt engineer"
> 帖子文案：*Explore the mythical celestial realm.*
> 发布时间：2026-09-27 ｜ 时长 24s ｜ 竖屏 9:16 ｜ 点赞 1.1w+
> 整理日期：2026-10-26

---

## 0. 可信度说明（先读）

Instagram 本体在当前环境返回 403，无法直接抽帧。本文件的反推基于以下**可核验的间接证据**，而非逐帧目击：

1. 镜像站 imginn 上该 Reel 的完整帖子元数据（文案、标签、时长 24s、账号信息、64 条评论）；
2. 该账号主页与该 Reel 同期发布的**同系列九宫格帖子及其英文配文**，包括：
   - *Palace Among the Clouds* — "A grand palace floats above endless clouds, bathed in soft sunlight as a lone figure gazes toward the celestial moon."
   - *Palace of Clouds — Thrones carved in light.*
   - *Vortex of the Heavens* — "Clouds swirl into a vast celestial vortex, a balcony overlooks the storm as a divine face forms within the sky."
   - *Celestial Palace Above Clouds* — "A palace floats among radiant clouds, illuminated by the eternal moon."
3. 评论区语义（"Immortal emperors realm""heavenly court""这个 bgm 是最配这种恢弘的天宫仙境的""Gu change"）；
4. 该题材所属的 2026 年爆款类型 **Chinese Heaven / 中式天宫 AI 视频**的公开风格研究（ACAS 建筑评论、同类平台 9 组官方案例提示词、开源仙宫视频 Skill 的镜头语言规范）。

因此下文的"原片 6 镜"是**基于证据的重建（reconstruction）**：镜头家族与画面元素有账号帖子原文支撑，精确到帧的顺序与时长为按 24s ÷ 每镜 4–5s 的行业惯例推断。实际使用时把它当作"同风格可复刻模板"，而不是逐帧抄本。

---

## 1. 这条 Reel 是什么：题材定位

这是 2026 年 8 月起在全网病毒传播的 **Chinese Heaven（天宫/中式仙宫）AI 电影感视频**流派：

- 标准工作流（据 ACAS 对该流派首创者陈艾军案例的考证）：**Midjourney 类文生图出关键帧 → Kling / 即梦 / Seedance / Veo 类图生视频做镜头动画 → 剪辑配恢弘 BGM**；
- 几乎无对白、无叙事，靠**空间揭示 + 神话尺度 + 统一光影**制造崇高感（the sublime）；
- 该账号在流派基础上加重了"仪式/朝会"元素（标签 `#ceremonialmoments #sacredgatherings #mountainfestival`），评论区普遍读作"天庭朝会/帝王仙境"。

---

## 2. 视觉 DNA：从原片拆出的 8 条可迁移规则

| # | 规则 | 画面证据/表现 |
|---|---|---|
| 1 | **建筑词汇表**：重檐飞檐、斗拱、朱柱、汉白玉栏杆与地砖、龙纹浮雕、月洞门、须弥座台基 | 朱红殿宇 + 白玉云台是识别度第一来源 |
| 2 | **神话尺度**：人物永远小而可读（画面高度 1/8–1/15），用人体反衬建筑与云海的超大尺度；台阶可伸入天际、柱础比人高 | "one or two figures in the foreground … an enormous palace far behind" |
| 3 | **三层纵深**：暗色前景框（柱/廊/松枝/栏杆）→ 中景人物与云台 → 远景云海、群峰或天象奇观 | 即"暗宫明境"：从幽暗建筑内部望向明亮仙境 |
| 4 | **框景揭示**：用屋檐、柱列、月洞门做"框中框"，镜头极慢前推让遮挡逐步退去 | 参考图 01 |
| 5 | **光线二元**：黄金时刻体积光（god rays，暖金）或永恒月色/天穹涡旋（冷银+粉霞）；全片光向统一，不允许中途变天 | 标签 `#goldenlightmagic #atmosphericart` |
| 6 | **配色锁定**：汉玉白 + 朱砂红 + 鎏金黄 + 云白（夜色版换靛蓝+银白）；饱和度克制，靠雾与光统一 | — |
| 7 | **材质 CG 感**：抛光大理石镜面地面（倒映柱列/人物/云海）、丝绸衣袂、体积雾、无源瀑布从悬浮岛坠入云海 | 参考图 02 |
| 8 | **运动语法**：极慢推/拉/横移/小幅升起，统一风向的微动（衣袖、披帛、云雾、花瓣、鹤），每镜最后 1 秒停稳；禁止快切、手持、无目的飞行 | 24s 仅 5–6 个镜头，每镜 4–5s |

**构图库（每条 Reel 从中取 5–6 种，不重复）**：深色大殿框景、巨型月洞门、无限柱廊、镜面玉池、临崖露台、云桥中轴、孤峰远景、天穹云涡、倒悬天宫、完整宫城外景（全片最多 1 次）、严格对称（全片最多 2 次）、醒目大圆环（全片最多 2 次）。

---

## 3. 原片分镜反推（6 镜 × 4s ≈ 24s，9:16）

> 每镜给四段内容：**画面描述（推断依据）｜英文关键帧提示词（MJ/GPT Image 通用）｜中文对照｜图生视频运动提示词（Kling/Seedance/Veo 通用）**。
> 关键帧统一后缀与负向词见第 5 节，下文 prompt 不再重复粘贴。

### Shot 1 — 暗殿框景，云海初现（开场定调）

**依据**：账号 *Palace Among the Clouds* 系列反复使用"孤影望云海"构图；参考图 01 即该流派标准开场。

- **EN Keyframe Prompt**
```
Vertical 9:16 cinematic keyframe, view from inside a dim grand Chinese celestial hall: dark cinnabar-red columns and carved dougong brackets frame the foreground, a white marble dragon relief on the left wall, a lone figure in flowing white Han robes standing with back to camera at the center of a polished marble terrace; beyond the terrace an endless sea of clouds with distant misty mountain peaks, warm golden-hour volumetric light rays breaking through the eaves, photorealistic cinematic CG, mythic scale, three-layer depth, ethereal atmosphere, 8k
```
- **中文对照**：竖屏 9:16 电影感关键帧，幽暗恢弘的中式仙宫殿内视角，前景为朱砂红巨柱与斗拱、左侧汉白玉龙纹浮雕，一名白衣长袍人物背对镜头立于抛光大理石云台中央；台外是无尽云海与雾中群峰，暖金色体积光穿过檐角洒下，写实电影 CG，神话尺度，三层纵深，空灵氛围，8k。
- **Video Motion Prompt**
```
Slow dolly-in through the column frame, the lone figure's sleeves and hair ribbon gently drifting in one unified wind direction, clouds rolling slowly below the terrace, god rays subtly shimmering, no cuts, camera ends on a stable hold
```

### Shot 2 — 无限玉廊，人影如豆（尺度建立）

**依据**：流派官方案例 9（white jade heavenly palace corridor, lone dark-robed figure, reflective floor）；账号标签 `#epicvibesonly #scenicwonder`。

- **EN Keyframe Prompt**
```
Vertical 9:16, an endless white jade corridor of a celestial palace floating above a vast sea of clouds, ornate carved pillars repeating into deep perspective, mirror-polished floor reflecting the columns and drifting clouds, a tiny lone figure in dark robes walking far down the corridor as a scale anchor, massive stone gates and multi-tier flying-eave pavilions visible at the vanishing point, waterfalls cascading from floating platforms into clouds, warm sunset volumetric light, cinematic Chinese mythology aesthetic, photoreal CG
```
- **中文对照**：竖屏 9:16，悬浮于浩瀚云海之上的无尽汉白玉仙宫长廊，雕花巨柱向透视深处重复，镜面地面倒映柱列与流云；远处一个微小的黑衣行人作为尺度锚点，消失点处可见巨大石门与重檐飞阁，悬浮平台瀑布坠入云海，暖色落日体积光，中式神话电影感，写实 CG。
- **Video Motion Prompt**
```
Very slow tracking shot following the tiny figure from behind, gentle parallax between near columns and far cloud sea, robe hem swaying lightly, reflections shifting on the polished floor, restrained and reverent pace, final second fully stable
```

### Shot 3 — 天宫全貌，玉阶穿云（唯一全景，世界观揭示）

**依据**：参考图 02 同构；账号 *Celestial Palace Above Clouds* 配文 "radiant clouds, eternal moon" 与完整宫城图。

- **EN Keyframe Prompt**
```
Vertical 9:16 epic establishing shot, a grand multi-tier Chinese celestial palace floating on an island above a sea of clouds, gilded flying eaves with cinnabar and teal ornamentation, glowing warm windows, a single monumental white marble staircase descending from the main gate through the clouds toward the viewer, waterfalls pouring off the floating island's edges into glowing mist, golden sunrise behind the roof ridges, two tiny white cranes circling, symmetrical ceremonial composition, ultra-detailed cinematic CG, sublime scale
```
- **中文对照**：竖屏 9:16 史诗级建立镜头，一座重檐叠嶂的中式仙宫悬浮于云海岛礁之上，鎏金飞檐配朱砂与石青纹饰，窗棂透出暖光；一道宏伟汉白玉台阶从正门穿过云层直落画面前方，岛缘瀑布倾入发光雾霭，屋脊后金色朝阳，两只小白鹤盘旋，对称仪式感构图，极致细节电影 CG，崇高尺度。
- **Video Motion Prompt**
```
Slow crane-up and slight push-in revealing the full palace tier by tier, clouds drifting across the staircase, waterfalls flowing continuously, cranes gliding in a slow arc, light flickering gently on gilt eaves, end on a locked symmetrical hold
```

### Shot 4 — 云桥渡影，鹤唳金霞（人物中景，情感锚点）

**依据**：流派官方案例 3（golden reflective bridge, white cranes, golden hour）；评论 "immortal cultivation / dream life"。

- **EN Keyframe Prompt**
```
Vertical 9:16, a woman in flowing pale celestial robes seen from behind, walking along a golden reflective white-jade bridge suspended over a sea of clouds, heading toward a distant multi-tier palace gate, a flock of white cranes soaring across the warm sunset sky, her long silk sash and sleeves billowing softly, cloud light reflected on the polished bridge surface, petals of light drifting in the air, cinematic ethereal Chinese heaven aesthetic, volumetric golden hour
```
- **中文对照**：竖屏 9:16，一名浅色仙袍女子背影行走在悬浮云海之上的鎏金反光玉桥，走向远处重檐宫门；一群白鹤掠过暖色晚霞天空，长丝绦与衣袖轻扬，抛光桥面映出云光，空中漂浮光之花瓣，空灵中式天宫美学，金色时刻体积光。
- **Video Motion Prompt**
```
Gentle follow shot from behind at walking pace, cranes crossing frame in layered depth, sash and sleeves moving in the same wind as the clouds, faint light petals drifting upward, no speed changes, settle to a still final frame
```

### Shot 5 — 天穹云涡，神颜显形（全片最高奇观）

**依据**：账号原帖 *Vortex of the Heavens* 原文："Clouds swirl into a vast celestial vortex, a balcony overlooks the storm as a divine face forms within the sky." 参考图 03。

- **EN Keyframe Prompt**
```
Vertical 9:16, looking upward from a celestial balcony with dark carved railing in the lower foreground, immense clouds spiral into a vast luminous vortex filling the sky, layers of pearl-white and rose-gold cloud rings rotating around a blazing divine light at the center, a faint serene divine face subtly forming within the brightest cloud layer, tiny glowing particles scattered like stardust, awe and sacredness, painterly photoreal CG, dramatic chiaroscuro
```
- **中文对照**：竖屏 9:16，自仙宫露台仰视，深色雕花栏杆压在画面下缘；浩瀚云层螺旋成巨大发光涡旋布满天空，珍珠白与玫瑰金云环层层旋转环绕中心炽烈神光，最亮云层中隐约浮现一张宁静神颜，微小发光粒子如星屑飘散，敬畏与神圣感，油画感写实 CG，戏剧性明暗。
- **Video Motion Prompt**
```
Extremely slow tilt-up from the railing into the vortex center, cloud rings rotating at barely perceptible speed, the divine face emerging and dissolving softly within the light, particles drifting, no fast motion, hold one second on the brightest center
```

### Shot 6 — 月下仙庭，孤影仰望（收束，回扣文案 celestial moon）

**依据**：账号 *Palace Among the Clouds* 原文 "a lone figure gazes toward the celestial moon"；*…illuminated by the eternal moon*。

- **EN Keyframe Prompt**
```
Vertical 9:16, night scene of a celestial palace courtyard above the clouds, silver moonlight bathing white marble terraces and a quiet multi-tier pavilion, a huge luminous full moon hanging low over a sea of silver-edged clouds, a lone robed figure standing small at the balustrade gazing up at the moon, faint lantern glow under the eaves, mist curling around pillar bases, serene immortal realm, cinematic CG, cool silver and deep indigo palette with warm lantern accents
```
- **中文对照**：竖屏 9:16，云海之上仙宫庭院夜景，银色月光洒满白玉云台与静谧重檐亭阁，一轮巨大明月低垂在银边云海之上；一个渺小长袍身影凭栏仰望明月，檐下灯笼微光，雾气绕柱基缓流，宁静仙界，电影 CG，冷银深靛配色点缀暖灯。
- **Video Motion Prompt**
```
Slow pull-back widening the frame so the figure grows smaller against the moonlit palace, mist drifting at ground level, lantern light flickering once, sleeves moving faintly, final frame held in perfect stillness for a clean loop point
```

---

## 4. 万能提示词公式（举一反三的模板）

把任意题材代入下面 10 个槽位，即可保持该流派的"仙宫感"：

```
[1 画幅/景别] + [2 人物：小尺度锚点 + 服饰 + 一个雅事动作]
+ [3 建筑锚点：材质(汉白玉/青铜/木构) + 构件(飞檐/斗拱/月洞门/柱廊/栏杆)]
+ [4 三层纵深：暗色前景框 → 中景云台/桥/廊 → 远景云海/群峰/天象]
+ [5 唯一主奇观：云涡/无源瀑布/倒悬天宫/鲲鹏/星盘/月池……每镜只许一个]
+ [6 光线：黄金时刻体积光 或 永恒月色，全片光向统一]
+ [7 配色：主色2个 + 点缀色1个，提前锁死]
+ [8 环境微动：云海/衣袂/花瓣/鹤/雾，方向统一、幅度低]
+ [9 镜头：极慢推/拉/横移/升起/固定，最后1秒停稳]
+ [10 风格后缀：cinematic photoreal CG, Chinese mythology aesthetic, ethereal, sublime scale, volumetric light, 8k, --ar 9:16]
```

**去重检查（每组 5 镜必须全部通过）**：

1. 任意两镜在「空间类型 / 前景框架 / 主奇观」三项中不得有两项相同；
2. 5 种不同构图语法、5 个不同主奇观、≥4 种雅事、无连续重复动作；
3. 严格对称 ≤2 镜、完整宫城外景 ≤1 镜、长桥中轴 ≤1 镜、醒目大圆环 ≤2 镜；
4. 每镜灵动元素（鹤/锦鲤/蝴蝶/鲲鹏）最多 1 种，全片最多 3 镜出现；
5. 至少保留 2 镜纯净观景空间，不塞人物互动。

---

## 5. 通用技术参数与负向词

**规格**

- 画幅 9:16（1080×1920，Reels 安全区：顶部 14%、底部 35% 不放关键信息）；若做横屏版整体改 `--ar 16:9`；
- 每镜 4–5s，全片 5–6 镜 ≈ 24–30s，30fps；
- 关键帧模型：Midjourney V6/V7 或 GPT Image；图生视频：Kling / 即梦 Seedance / Veo；
- 角色与建筑用**同一 seed + 角色资产图（character sheet）**锁连续性；场景资产图单独建库复用。

**通用 Negative Prompt**

```
text, watermark, logo, subtitle, caption, modern objects, wires, cars, neon signs, LED, sci-fi HUD, data streams, robot, mecha, fast motion, handheld shake, lens distortion, warped architecture, floating roof with no support, extra limbs, deformed hands, mutated face, duplicated people, crowded marketplace, combat, weapon fire, sudden weather change, global light shift, cartoon, anime, lowres, jpeg artifacts, oversaturation, dense sparkles, poster-like look, western domes, gothic arches, cathedral, greek columns, european castle, byzantine architecture
```

**中文负向提示**：文字、水印、字幕、现代物体、电线、汽车、霓虹、LED、科幻界面、数据流、机器人机甲、快速运动、手持抖动、畸形建筑、无支撑飞檐、多余肢体、崩坏人脸、重复人物、拥挤集市、打斗、武器火光、天气突变、全局光线跳变、卡通动漫脸、低分辨率、过饱和。

---

## 6. 三套原创方案索引

在同一视觉 DNA 下更换**世界观、配色、主奇观与雅事系统**，每套 5 镜、含中英文关键帧 prompt + 图生视频 prompt + 声音设计 + 资产锚点 + 去重检查表：

| 方案 | 一句话概念 | 配色转向 | 核心新奇观 | 链接 |
|---|---|---|---|---|
| 一、北冥星海 · 鲲鹏渡 | 夜色观星仙界，云海化为发光星海 | 靛蓝 × 银白（夜场） | 云海鲲鹏、璇玑星盘、倒悬星塔 | [scheme-A-北冥星海.md](./scheme-A-北冥星海.md) ｜✅ 已出图验证（[报告](./validation-scheme-A/VALIDATION-REPORT.md)） |
| 二、东海龙庭 · 潮生月府 | 云海与潮海交界的龙族水府 | 青玉 × 珍珠白 × 灯金 | 月池镜宫、龙门瀑布、呼吸月潮 | [scheme-B-东海龙庭.md](./scheme-B-东海龙庭.md) |
| 三、昆仑悬圃 · 霜松工坊 | 古松嵌入宫殿的秋日昆仑工坊 | 琥珀金 × 霜白 × 松绿 | 松构一体、青铜星盘、素钟回廊 | [scheme-C-昆仑悬圃.md](./scheme-C-昆仑悬圃.md) |

**参考图（同流派公开画面，仅作风格证据，勿逐帧复刻）**：`./reference-images/`

| 文件 | 对应规则 |
|---|---|
| 01-framing-dragon-hall-cloud-sea.jpg | 规则 3/4：暗殿框景 + 三层纵深 + 龙纹 |
| 02-floating-palace-staircase.jpg | 规则 1/7：完整悬浮宫城、玉阶穿云、无源瀑布 |
| 03-celestial-cloud-vortex.jpg | Shot 5：天穹云涡、粉金云环 |
| 04-golden-court-assembly.jpg | 仪式朝会变体（金殿、列座、神光） |
| 05-chinese-heavenly-court-hierarchy.webp | 天庭朝会人物层级参考 |
