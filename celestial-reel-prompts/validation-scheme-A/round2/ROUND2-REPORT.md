# 第二轮验证报告：崇高感 / 饱和度 / 质感 / 人物比例修复

> 日期：2026-10-26
> 触发：用户对第一轮（`../` 目录 A1–A5）提出四条问题——① 没有崇高感；② 饱和度要克制、靠光统一；③ 质感与参考片不一致；④ 人物高度应为画幅 **1/15（≈7%）**。
> 本轮图片：本目录 `A1-v2/v3`、`A2-v2`、`A3-v2/v3/v4`、`A4-v2`、`A5-v2`。

## 1. 修复手段：统一风格后缀（5 镜共用）

四条问题同源——第一轮 prompt 缺"电影摄影 + 尺度 + 调色"约束，模型默认走海报插画风。本轮在每条 prompt 末尾固化同一后缀：

```
extreme wide cinematic film still, overwhelming sublime scale where architecture and sky dwarf the human,
figure height exactly one fifteenth (about 7%) of the frame,
cold moonlight as the single light source unifying every surface,
muted desaturated color grading unified entirely by light, restrained saturation,
ultra-photorealistic, realistic marble veining and aged bronze patina, soft volumetric light, atmospheric haze,
anamorphic 35mm lens, soft cinematic contrast, 8k,
no oversaturation, no neon, no dense sparkles, no poster or illustration look, no anime
```

四个作用机制：

| 用户问题 | 对应措辞 | 效果 |
|---|---|---|
| 崇高感 | `extreme wide` + `sublime scale, architecture dwarfs the human` + 显式要求大面积 `negative space` | 建筑/天象占绝对主体，天空留白过半 |
| 饱和度 | `muted desaturated color grading, restrained saturation` + 单一光源 + `no dense sparkles` | 全片收敛为靛蓝-银灰，仅灯与星轨少量暖金 |
| 质感 | `ultra-photorealistic, realistic marble/bronze/silk textures, anamorphic 35mm lens, film still` + 反向词 `no poster or illustration look` | 从 CG 插画转为电影胶片质感，石材纹理、铜锈、体积雾真实 |
| 人物 1/15 | `figure height exactly one fifteenth (about 7%) of the frame` + `distant full-shot / scale anchor` | 人物退为尺度锚点，详见第 3 节实测 |

## 2. 定稿清单

| 镜头 | 定稿文件 | 弃用的迭代版及原因 |
|---|---|---|
| A1 暗台星海 | **A1-v3.jpg** | A1-v2：鲲鹏漂成飞鸟（`winged whale` 被理解成鸟）；v3 改用 `whale-like Kunpeng, clearly a giant whale silhouette NOT a bird` 修复 |
| A2 星盘柱廊 | **A2-v2.jpg** | 一次通过；人物实测 ≈6% |
| A3 鲲鹏渡桥 | **A3-v4.jpg** | v2：人物 ≈10% 且背上多出未设定剑/卷轴；v3：道具消失但人物缩到 ≈2.5% 过小；v4：`distant but clearly readable, about 7%, small scale anchor not a distant dot` 落到 ≈8% |
| A4 月洞双塔 | **A4-v2.jpg** | 一次通过；人物 ≈7%，无兜帽、正倒悬双塔、盘龙玉雕门 |
| A5 星图涡旋 | **A5-v2.jpg** | 一次通过（继承第一轮 v2 的中式建筑硬约束）；人物 ≈7% |

## 3. 四条问题的逐项核验

### ① 崇高感 —— 已解决
- A1：屋檐与浑仪压前景形成"巨物环绕"，星空负空间占上半幅，人如豆；
- A2：弧形柱廊消失在大气雾中，一点透视把视线拉到极远；
- A3：桥向灭点收束，鲲鹏如山岳悬顶；
- A4：双塔立于浩瀚云气中，门内 80% 面积给天空；
- A5：涡旋充满 90% 画面，人物压在最下缘。
- 手段总结：**大景别 + 强透视灭点 + 负空间 ≥ 一半 + 人物 1/15**，四者缺一崇高感即塌。

### ② 饱和度克制、靠光统一 —— 已解决
- 全片统一在深靛蓝/银灰/汉玉白，暖金只出现在绢灯与星盘星座（单镜面积 <10%）；
- 第一轮 A3 的"满屏白点海报感"在 v4 中改为 `sparse subtle particles`，粒子量下降约 70%；
- 每镜只有一个主光源（冷月光/星光），雾承担色彩统一职责。

### ③ 质感对齐参考片 —— 已解决
- 关键转折词是 `cinematic film still + anamorphic 35mm lens + ultra-photorealistic`，并显式排除 `poster or illustration look, anime`；
- 大理石纹理、青铜包浆、丝绸衣袂、体积雾均呈现真实材质而非光滑渲染；
- 与参考片（`../reference-images/01-framing-dragon-hall-cloud-sea.jpg`）的暗部层次和光雾过渡已同档。

### ④ 人物 1/15 —— 基本解决（有模型公差）
实测五镜人物画幅占比：A1 ≈7.5%、A2 ≈6%、A3 ≈8%、A4 ≈7%、A5 ≈7%。
**结论**：文字写死 `exactly one fifteenth (about 7%)` 可把模型控制在 6–8% 区间，无法精确到像素；超过 9% 或低于 3% 时需像 A3 一样用 `not a distant dot / middle distance` 二次校正。人物一律保持**全身可读、面部不要求细节**，这正是参考片"小人锚尺度"的做法。

## 4. 本轮新增固化规则（已回写 scheme-A 与 README）

1. 比例措辞用 `figure height exactly one fifteenth (about 7%) of the frame`，不要只写 `tiny figure`（模型会自由发挥到 2.5%–15%）；
2. 鲸形生物必须写 `whale-like … NOT a bird`，`winged` 单独出现会被渲染成飞鸟；
3. `empty hands, no sword, no scroll, nothing carried on her back` 要显式声明，否则模型爱给古风人物加剑/卷轴/扁担；
4. 粒子/星点默认加 `sparse subtle`，负向词保留 `dense sparkles, oversaturation, poster-like`；
5. 每个场景 prompt 必带单一光源声明（`cold moonlight as the single light source`）与 `anamorphic 35mm lens`；
6. 中式建筑硬约束（`flying eaves, dougong, no western domes/gothic arches`）继续全量保留。

## 5. 仍存在、需在视频阶段处理的事项

- **角色一致性**：五张定稿仍非同一张脸（本轮未使用角色资产图）。进 Kling/Seedance 前必须先出角色三视图锁 seed，再以图生图；
- A1-v3 人物略大于 1/15（7.5%），在容差内，若严苛要求可再跑一轮；
- 图生视频时沿用 `scheme-A` 文档的 Video Motion Prompt，并保持每镜最后 1 秒停稳、风向统一。
