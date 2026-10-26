# 方案一《北冥星海·鲲鹏渡》关键帧验证报告

> 验证日期：2026-10-26
> 验证方式：用 `scheme-A-北冥星海.md` 的 5 条英文关键帧 prompt 直接文生图（单模型直出，未做 seed 锁定/角色资产图），逐张对照 prompt 与方案配额做质检。
> 图片目录：本文件同级，A1–A5 为首轮，`A5-star-vortex-v2.jpg` 为修复轮。

## 1. 总览

| 镜头 | 文件 | 结论 | 主要偏差 |
|---|---|---|---|
| A1 暗台框景·星海初现 | A1-star-sea-terrace.jpg | ✅ 通过（小偏差） | 无臂浑仪缺支架；月亮为新月（prompt 只写了月光） |
| A2 星盘柱廊·玉册校星 | A2-colonnade-astrolabe.jpg | ✅ 通过（小偏差） | 镜面地像水面；人物渲染为男性，与 A1 女官不一致 |
| A3 玉桥渡星·鲲鹏腾云 | A3-kunpeng-bridge.jpg | ⚠️ 有条件通过 | 星点过密过饱和；鲲鹏占画面 >1/2，尺度压过人物；桥为 S 形而非中轴直桥 |
| A4 月洞星门·倒悬双宫 | A4-moon-gate-twin-pagodas.jpg | ✅ 通过（优秀） | 门为葫芦形变体（可接受）；人物兜帽遮面 |
| A5 星图涡旋·万象归位 | A5-star-vortex.jpg（弃用）→ A5-star-vortex-v2.jpg（采用） | ✅ 修复后通过 | 首版建筑跑成西式穹顶/哥特拱、人物变黑袍僧侣；v2 已全部修正 |

**整体判断**：5 镜的构图语法、三层纵深、靛蓝/银白/星金配色、夜场光影与"暗宫明境"气质全部成立，方案可直接进入制作流程；但暴露两个必须在正式制作前解决的系统性问题（见第 3 节）。

## 2. 逐镜质检

### A1 — 通过
- **命中**：朱柱斗拱前景框、青铜浑仪、六角绢灯、白衣银纹、生物荧光蓝云海、鲲鹏剪影（有翼鲸形，与设定"鲲→鹏过渡态"一致）、深靛星空、冷暖光对冲。
- **偏差**：① 浑仪为悬浮环、无支架（轻微结构不合理）；② 人物为女性、面容年龄偏幼，与后续镜头性别不统一（责任在跨镜，不在本镜）。
- **制作建议**：正式版补 `armillary sphere mounted on an ornate bronze stand`。

### A2 — 通过
- **命中**：弧形玉柱廊一点透视、镜面反射、星河、青铜星盘星座发光、矮案校册、暖灯一点，神话尺度出色。
- **偏差**：① 黑曜石镜面地面的反射过强，读作"水面浮台"而非石材地面；② 人物渲染为男性束发，与 A1 女官矛盾。
- **制作建议**：prompt 改为 `mirror-polished black obsidian stone floor (solid reflective stone, not water)`；人物统一见第 3 节。

### A3 — 有条件通过（情绪峰成立，需压饱和度）
- **命中**：鲲鹏体表星座纹、腾起弧线、发光粒子尾流、玉桥发光栏杆、渺小背影、冷月，震撼感达到全片峰值设计。
- **偏差**：① 全屏白色星点过密、对比过强，呈"装饰海报感"，偏离方案的克制写实 CG；② 鲲鹏体量占画面约 2/3，人物-桥-兽的尺度层次被压扁；③ 桥渲染为 S 形弯道，方案设计为直桥中轴（全片唯一中轴配额）。
- **制作建议**：负向词加 `oversaturation, dense sparkles, poster-like`；新增约束 `the Kunpeng occupies no more than one third of the frame, straight central-axis bridge`。

### A4 — 通过（5 镜中完成度最高）
- **命中**：玉雕月洞门（盘龙+星座浮雕）、正立/倒悬双塔塔尖相对、星河穿门、提灯小剪影、物理一致的镜像结构、靛蓝银金配色。
- **偏差**：① 门洞为葫芦形而非正圆，仍属中式月洞门类，可接受；② 人物带兜帽、面部不可读，与 A1 散发女官不统一。
- **制作建议**：视频阶段用 A1 角色资产图做形象参考即可解决；保留此版构图。

### A5 — 首轮失败，修复轮通过
- **首版问题（典型风格漂移）**：prompt 中的 `observatory / balcony / railing` 触发了西式天文意象——两侧变成拜占庭式穹顶与哥特尖拱、栏杆是欧式宝瓶柱、人物变成黑袍秃顶僧侣；只有云涡与北极星命中。
- **修复手段（已验证有效）**：prompt 显式写入 `traditional Chinese celestial observatory, Chinese flying-eave rooftops with dougong brackets, white-jade balustrade with cloud motifs, female astronomer in moon-white Han robes with lotus crown`，并加硬性负向 `no western domes, no gothic arches, no cathedral`。
- **v2 结果**：中式飞檐檐角落在两侧、白玉云龙纹栏杆、与 A1 同款白衣女官+六角灯、北极星居中的玫瑰金星涡、星座连线，全部归位。
- **遗留小偏差**：人物为中景而非方案要求的"渺小静立"，崇高尺度略弱；收尾镜头可接受，若追求极致可在 prompt 加 `small figure seen from a distance, figure height under one sixth of frame`。

## 3. 系统性问题与正式制作规则

### 问题 1：跨镜角色不连续（最严重）
同一"司星仙官"在 5 镜中被渲染成：A1 年轻女子 / A2 男子 / A3 长发背影 / A4 兜帽人 / A5 女子。这是无参考图直出的必然结果。
**规则**：正式制作先出角色资产图（正侧背三视图，明确 `young female astronomer`），后续每镜以图生图/多模态参考携带，并锁 seed；prompt 中统一写死性别、莲冠、月白银纹深衣、六角绢灯四要素。

### 问题 2：西式建筑元素泄漏
"observatory / vortex / balcony"等英文词会把模型带向希腊-拜占庭天文建筑。
**规则**：所有场景 prompt 固定追加 `strictly traditional Chinese architecture, flying eaves, dougong brackets, glazed tile roofs` 与负向 `western domes, gothic arches, cathedral, greek columns, european castle`（A5 v2 已验证该补丁有效）。

### 其他固化经验
- 镜面地面必须注明 `solid stone, not water`，否则模型默认生成水面；
- "发光粒子/星点"要加数量约束 `sparse subtle particles`，否则易过饱和海报化；
- 中轴桥等几何要求需显式写 `straight symmetrical central-axis bridge`，"endless bridge"会被自由发挥成 S 形；
- 新月/满月差异：方案 A5 需要满月级光场时应显式写 `brilliant full moon`，本轮 A1 出现的新月本身美学成立，可保留。

## 4. 可直接复用的 A5 修复版 Prompt（替换 scheme 文档原句）

```
Vertical 9:16, low-angle upward view from a traditional Chinese celestial observatory balcony, dark carved white-jade balustrade with cloud motifs along the bottom edge, silhouettes of Chinese flying-eave rooftops with dougong brackets and glazed tile ridges at both frame corners, the night sky filled by a vast slow vortex of clouds and stars rotating around a single brilliant fixed pole star at the center, concentric rings of deep indigo, silver and rose-gold nebula, faint glowing constellation lines within the swirl, a young female astronomer in moon-white wide-sleeved Han robes with silver cloud embroidery and a small lotus crown standing still at the railing, holding a small hexagonal silk lantern, luminous particles drifting like snow, sacred order and cosmic calm, painterly photoreal cinematic CG, chiaroscuro, 8k, strictly traditional Chinese architecture, no western domes, no gothic arches, no cathedral
```

## 5. 下一步建议

1. 先做角色资产图 + 5 张场景锚点图（按 `scheme-A` 文档的资产锚点表），再重跑 5 镜，预计一致性问题可消除 80%；
2. A3 按第 2 节补丁重跑一版做对比；
3. 关键帧定稿后，用方案文档里的 Video Motion Prompt 进 Kling/Seedance 做 5s 图生视频，每镜最后 1 秒停稳；
4. 方案 B、C 的 prompt 已同步吸收本次两条规则（中式建筑硬约束、固体镜面措辞），验证前可先回补。
