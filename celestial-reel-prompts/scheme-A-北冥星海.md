# 方案一：北冥星海 · 鲲鹏渡

> **一句话概念**：北冥有鱼，其名为鲲——把原片的"金色白昼天宫"整体翻转为**夜间观星仙界**，云海变成发光的星海，仙宫是司掌星历的观星台群。
> **与原片的差异点**：夜场冷色（原片为暖金白昼）、水生物奇观鲲鹏（原片为鹤与云涡）、星仪/星盘道具系统（原片无道具叙事）。
> **总时长**：5 镜 × 5s = 25s ｜ 9:16 ｜ 情绪线：静 → 疑 → 撼 → 幻 → 定

## 全局锁定

- **配色**：深靛蓝 `#0B1E3F` + 寒玉白 `#DCE6F2` + 星屑金 `#E8C77A`（仅用于灯与星轨点缀，面积 <10%）
- **光线**：单一冷月光 + 星云海自发光 + 暖灯小面积对冲；全片光向统一为左上方
- **角色锚点**：一名**年轻女性**司星仙官，月白广袖深衣、银线云纹、束发戴小莲冠、手提六角绢灯（全片唯一人物，5 镜同款；英文 prompt 统一写 `young female astronomer`，正式制作须先出角色三视图并锁 seed——首轮验证已出现跨镜性别漂移，见 validation-scheme-A 报告）
- **关键道具**：六角绢灯、青玉星册、璇玑青铜星盘
- **主奇观配额**：鲲鹏（2 镜，远景/剪影）、星盘（1 镜）、倒悬星塔（1 镜）、星图涡旋（1 镜）
- **雅事**：提灯远望 → 校星册 → 凭栏渡桥 → 穿星门 → 静立观涡（5 种不重复）
- **人物画幅占比（第二轮验证锁定）**：每镜人物高度 = 画幅 **1/15（≈7%）**，全身可读、面部不要求细节，仅作尺度锚点；prompt 固定写 `figure height exactly one fifteenth (about 7%) of the frame`，模型公差约 6–8%
- **统一风格后缀（5 镜共用，第二轮验证版）**：
```
extreme wide cinematic film still, overwhelming sublime scale, vast negative space,
cold moonlight as the single light source unifying every surface,
muted desaturated color grading unified entirely by light, restrained saturation,
ultra-photorealistic, realistic marble veining and aged bronze patina, soft volumetric light, atmospheric haze,
anamorphic 35mm lens, soft cinematic contrast, 8k,
no oversaturation, no neon, no dense sparkles, no poster or illustration look, no anime,
strictly traditional Chinese architecture with flying eaves and dougong brackets, no western domes, no gothic arches
```
- **硬约束**：鲸形生物写 `whale-like … NOT a bird`；人物写 `empty hands, no sword, no scroll`；粒子写 `sparse subtle particles`

---

## Shot A1 — 暗台框景，星海初现（静）

- **构图**：深色青铜观星仪与朱柱构成前景框，人物位于中景下三分线，远景发光云海
- **空间**：观星台外廊 ｜ **主奇观**：发光云海 + 鲲鹏剪影初现 ｜ **雅事**：提灯远望

**EN Keyframe**
```
Vertical 9:16 extreme wide cinematic film still, night view from a vast ancient Chinese observatory terrace, immense dark cinnabar-red columns and a giant bronze armillary sphere on an ornate bronze stand looming as dark silhouettes in the near foreground framing the scene, far below at center a tiny distant young female astronomer in moon-white wide-sleeved Han robes holding a small hexagonal silk lantern, her figure height exactly one fifteenth (about 7%) of the frame, beyond the white jade balustrade an endless sea of clouds glowing faint bioluminescent blue beneath cold moonlight, on the far horizon a colossal whale-like Kunpeng leviathan with small wing-fins gliding half-submerged through the clouds, clearly a giant whale silhouette NOT a bird, deep indigo starry sky with vast empty negative space dominating the upper half, overwhelming sublime scale where architecture and sky dwarf the human, ultra-photorealistic, realistic marble veining and aged bronze patina, soft volumetric moonlight as the single light source, atmospheric haze, muted desaturated indigo and silver color grading unified entirely by light, restrained saturation, anamorphic 35mm lens, soft cinematic contrast, 8k, strictly traditional Chinese architecture with flying eaves and dougong brackets, no oversaturation, no neon, no dense sparkles, no poster or illustration look, no anime, no bird, no western domes, no gothic arches
```
**中文**：竖屏 9:16 夜间电影关键帧，幽暗古观星台：深色青铜浑天仪与朱柱框住前景，月白银纹广袖的年轻司星仙官立于下三分线、手提六角绢灯；栏外浩瀚云海泛着生物荧光般的幽蓝、宛若星海，海天交界处巨型鲲鹏剪影正贴着云面滑行；深靛夜空星辰清晰，左上冷月光，绢灯暖光小面积点缀，写实电影 CG，三层纵深，崇高静谧，8k。

**Video Motion**
```
Very slow dolly-in past the bronze armillary sphere, lantern swaying once gently, the Kunpeng silhouette drifting across the far horizon with slow tail motion, glowing cloud waves breathing softly, sleeves drifting left in unified wind, end on stable hold
```
**运镜中文**：越过浑天仪极慢前推；绢灯轻晃一次；远景鲲鹏缓缓摆尾游过；发光云浪如呼吸起伏；衣袖统一向左微动；结尾停稳。

**声音**：箜篌泛音单音起 + 极低频鲸鸣般空响 + 风声。

---

## Shot A2 — 星盘柱廊，玉册校星（疑）

- **构图**：一点透视无限柱廊，镜面地面，人物小而居中偏下
- **空间**：璇玑殿外环廊 ｜ **主奇观**：巨型璇玑青铜星盘缓转 ｜ **雅事**：伏案校星册

**EN Keyframe**
```
Vertical 9:16 extreme wide cinematic film still, an endless curved colonnade of pale jade pillars on a celestial observatory floating above a night cloud sea, the pillars repeating into deep atmospheric haze with strong one-point perspective, mirror-polished black obsidian solid stone floor (not water) reflecting the columns and a faint river of stars, at a far distance a tiny kneeling young female astronomer in moon-white Han robes at a low desk lit by one small warm lantern, her figure height exactly one fifteenth (about 7%) of the frame, beside her a gigantic bronze armillary astrolabe disc towering overhead with faintly glowing engraved constellations, cold moonlight from upper left as the single dominant light source, deep indigo and cold silver muted palette, vast sublime emptiness, ultra-photorealistic, realistic jade and bronze textures, soft volumetric light, atmospheric depth, restrained desaturated color grading unified by light, anamorphic 35mm lens, 8k, strictly traditional Chinese architecture, no oversaturation, no neon, no dense sparkles, no poster or illustration look, no anime, no western domes, no gothic arches
```
**中文**：竖屏 9:16，夜间悬浮于幽蓝发光云海之上的观星台，淡玉柱围成的无尽环形柱廊，镜面黑曜石地面倒映柱列与柱间星河；渺小的白衣司星官跪坐矮案前校阅青玉星册，身旁巨型青铜璇玑星盘缓缓转动，盘上雕刻星座泛淡金微光；深靛+寒银配色，案灯一点暖光，一点透视纵深，写实电影 CG，神话尺度。

**Video Motion**
```
Slow lateral tracking along the colonnade, astrolabe rings rotating at barely visible speed, star reflections shimmering on the floor as clouds pass beneath, the figure turning one page with a small deliberate hand motion, no cuts, settle to stillness
```
**运镜中文**：沿柱廊极慢横移；星盘环以几乎不可察的速度转动；云流经过时地面星影轻闪；人物小幅翻页一次；无切镜，结尾静止。

**声音**：箫声长音 + 星盘金属轻碰（细碎、稀疏）+ 衣料摩擦。

---

## Shot A3 — 玉桥渡星，鲲鹏腾云（撼，全片情绪峰）

- **构图**：长桥中轴（全片唯一一次中轴桥），人物背影极小，鲲鹏占远景主体
- **空间**：渡星桥 ｜ **主奇观**：鲲鹏自云海腾起环绕桥身 ｜ **雅事**：凭栏停步

**EN Keyframe**
```
Vertical 9:16 extreme wide cinematic film still, a straight symmetrical central-axis white jade bridge with faintly glowing railings spanning an ocean of bioluminescent blue clouds at night, a young female astronomer in moon-white Han robes seen from behind paused on the bridge at middle distance, distant but clearly readable full-body figure whose height is about one fifteenth of the frame, roughly seven percent of image height, small scale anchor not a distant dot, empty hands, no sword, no scroll, nothing carried on her back, a colossal serene humpback-whale-like Kunpeng leviathan rising from the cloud sea beside the bridge and arcing overhead like a living mountain, occupying about one third of the frame, faint constellation patterns across its skin, only a few sparse subtle luminous particles in its wake, thin crescent moon, deep indigo sky with vast negative space, overwhelming sacred sublime scale, cold moonlight as the single light source unifying every surface, muted desaturated indigo and silver grading, restrained saturation, ultra-photorealistic, polished marble and silk textures, soft volumetric haze, anamorphic 35mm lens, soft cinematic contrast, 8k, no oversaturation, no neon, no dense sparkles, no poster or illustration look, no anime, no sword, no shoulder pole
```
**中文**：竖屏 9:16，渺小白衣人物背影停在一座无尽白玉桥上，栏杆微微发光，桥横跨漂浮星光的幽蓝生物荧光云海；一头巨大而安详的鲲鹏自身侧云海腾起、如活的山岳般从桥顶弓身掠过，体表隐现星座纹路，银色雾霭与发光粒子随其尾流盘旋；深靛夜空、冷月清辉，压倒性的神圣尺度，写实电影 CG，竖向构图强化鲲鹏上升动势。

**Video Motion**
```
Slow push-in toward the figure's back while the Kunpeng rises in a single continuous graceful arc, cloud waves parting and closing around its body, particles spiraling upward, the figure's sleeves and sash lifted by the slow wake wind, camera holds as the creature disappears into the star clouds
```
**运镜中文**：向人物背影慢推；鲲鹏以一个完整舒缓的弧线腾起、掠过、没入星云；云浪在其身躯两侧分合；粒子盘旋上升；尾流带起人物衣袖丝绦；鲲鹏没入后镜头停稳。

**声音**：鼓点极弱滚奏 + 低频鲸鸣放大 + 一声悠远鹤鸣（全片唯一鹤鸣，做流派呼应）。

---

## Shot A4 — 月洞星门，倒悬双宫（幻）

- **构图**：巨型月洞门做框（全片第一个大圆环），门框内上下镜像的正立/倒悬星塔
- **空间**：太虚门 ｜ **主奇观**：重力反转的倒悬观星塔 ｜ **雅事**：提灯穿门

**EN Keyframe**
```
Vertical 9:16 wide cinematic film still, a giant circular white jade moon gate carved with coiling dragons and cloud motifs set into a dark ancient observatory wall, through the gate a surreal mirrored realm: an upright traditional Chinese pagoda observatory and an identical upside-down pagoda hanging from the cloud ceiling above, their spires nearly touching at the center line, a thin river of glowing stars flowing between the two mirrored towers, at the gate threshold a tiny young female astronomer in moon-white Han robes without hood carrying a small hexagonal lantern, her figure height exactly one fifteenth (about 7%) of the frame, reflections physically consistent, cold moonlight as the single light source, muted desaturated indigo silver and faint gold palette, dreamlike but structurally stable architecture, sublime scale with vast cloud space around the towers, ultra-photorealistic, realistic carved jade and glazed tile textures, soft volumetric light and haze, restrained saturation unified by light, anamorphic 35mm lens, 8k, no oversaturation, no neon, no dense sparkles, no poster or illustration look, no anime, no western domes, no gothic arches
```
**中文**：竖屏 9:16，深色观星台墙上开巨型汉白玉雕花月洞门，门内是超现实镜像仙界：一座正立宝塔观星台与一座完全相同的倒悬宝塔自云顶垂下，塔尖在中线几乎相触，发光星河在两塔之间流淌；提灯白衣司星官以小剪影正步入月门；倒影数量与方向物理一致；深靛、银、淡金配色，梦幻但结构稳定，写实电影 CG。

**Video Motion**
```
Slow forward glide through the moon gate, the figure stepping forward in sync with the camera, star river flowing upward toward the inverted tower, lantern glow reflecting once on the jade gate rim, clouds drifting in opposite directions above and below the center line, gentle parallax, final hold centered on the twin spires
```
**运镜中文**：穿过月门缓慢滑行；人物与镜头同步迈步；星河向倒悬塔方向上流；灯光在玉门边缘映出一次反光；中线上方云与下方云反向流动；轻度视差；最终双塔尖居中停稳。

**声音**：古筝刮奏一段 + 水滴般回响（表现重力反转的空灵感）+ 风声分层。

---

## Shot A5 — 星图涡旋，万象归位（定，收束/可循环点）

- **构图**：露台仰视，栏杆压下缘（全片第二个大圆环，配额用满），云涡呈星图
- **空间**：摘星台 ｜ **主奇观**：星辰云涡，中心为不动北极星 ｜ **雅事**：静立仰观

**EN Keyframe**
```
Vertical 9:16 low-angle wide cinematic film still, silhouettes of traditional Chinese flying-eave rooftops with dougong brackets and glazed tile ridges at the lower frame corners and a dark carved white jade balustrade with cloud motifs, the vast night sky filled by a slow enormous vortex of clouds and stars rotating around one brilliant fixed pole star at the center, concentric rings of deep indigo, silver and muted rose-gold nebula, faint glowing constellation lines within the swirl, a tiny young female astronomer in moon-white Han robes standing still at the railing holding a small hexagonal lantern, her figure height exactly one fifteenth (about 7%) of the frame, sparse snow-like luminous particles, cosmic calm and overwhelming sublime scale, cold starlight and moonlight as the single light source, muted desaturated color grading unified entirely by light, ultra-photorealistic, realistic stone and silk textures, soft volumetric haze, chiaroscuro, anamorphic 35mm lens, soft cinematic contrast, 8k, no oversaturation, no neon, no dense sparkles, no poster or illustration look, no anime, no western domes, no gothic arches, no cathedral
```
**中文**：竖屏 9:16，自观星台露台低角度仰视，深色雕花栏杆沿画面下缘；夜空被巨大缓慢旋转的星辰云涡充满，环绕中心一颗明亮不动的北极星，深靛、银、玫瑰金色星云成同心环，涡旋中隐约发光的星座连线；白衣司星官提灯垂手、渺小静立栏边，发光粒子如雪飘散；神圣秩序与宇宙般宁静，油画感写实 CG，明暗对照，8k。

**Video Motion**
```
Extremely slow tilt-up from the railing to the vortex center, cloud and star rings rotating imperceptibly, particles drifting downward at low frequency, the figure motionless except faint sleeve movement, final one-second hold on the pole star designed as a seamless loop point back to Shot A1
```
**运镜中文**：自栏杆向涡心极慢上摇；星云环以不可察速度旋转；粒子低频下落；人物仅衣袖微动；最后北极星定格 1 秒，作为无缝循环点接回 A1。

**声音**：箜篌主题再现 + 全体器乐收束于一个长音 + 风声留白。

---

## 资产锚点（生图前先建库，保证 5 镜连续）

| 类型 | 资产 | 用途与要求 |
|---|---|---|
| 角色 | 司星仙官 character sheet（正侧背三视图） | 月白深衣银线云纹、莲冠、六角绢灯；GPT Image/MJ 出图后锁 seed |
| 道具 | 六角绢灯、青玉星册、璇玑星盘 独立图 | 材质、尺寸、发光方式固定；星盘星座纹样需五镜一致 |
| 场景 | 观星台外廊、璇玑环廊、渡星桥、太虚门、摘星台 5 张场景锚点 | 统一夜靛色调与左上月光方向；建筑只用中式构件，禁飞扶壁等西式结构 |
| 生物 | 鲲鹏设定图（侧视 + 腾跃姿态） | 鲲→鹏过渡态：鱼身鲸形、背鳍展开为羽翼、体表星座纹 |

## 去重检查表

| 镜 | 空间类型 | 前景框架 | 主奇观 | 构图语法 | 对称？ |
|---|---|---|---|---|---|
| A1 | 观星外廊 | 浑天仪+朱柱 | 鲲鹏剪影+荧光云海 | 暗部框景 | 否 |
| A2 | 环形柱廊 | 玉柱列 | 璇玑星盘 | 一点透视+镜面 | 否 |
| A3 | 渡星桥 | 桥栏 | 鲲鹏腾起 | 长桥中轴（唯一） | 是（1/2） |
| A4 | 太虚门 | 月洞门 | 倒悬双塔 | 圆环框中框（圆环 1/2） | 是（2/2） |
| A5 | 摘星台 | 露台栏杆 | 星辰云涡 | 仰视涡旋（圆环 2/2） | 否 |

✅ 五项主奇观全异；雅事 5 种不重复；对称 2 镜、圆环 2 镜、中轴桥 1 镜，均达上限未超；鲲鹏仅 A1/A3 两镜；纯净观景镜 A1、A5 共 2 镜。
