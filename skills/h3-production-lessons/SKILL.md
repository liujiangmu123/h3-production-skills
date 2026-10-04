---
name: h3-production-lessons
description: The H3 production-lessons library — what H3 actually drew wrong, with the failing and the working sentence, the evidence and how often it reproduced. Use when writing H3 picture lines, visual_en, beats or segment prompts that touch anything H3 has got wrong before — glowing objects (lamps, screens, light cones), highlight / swipe / fade, canvas metaphors, negations ("no X"), exact counts, frames that move, marks that must stay, the first accent color, "everything outside vanishes"; when planning motion, glides vs snaps, rhythm or fluency; when a draft, 768 or 2K render shows something not asked for, drops or drifts something, reads low in h3_align or lands early / late; before rerolling (many failures survive a new seed); and after QC of every episode, to record what failed and what fixed it. 出片经验库 / 踩坑记录 / 提示词该怎么写 / 动画不流畅 / 画错了怎么改. All styles, both H3 lines.
metadata:
  kind: global
  version: "1.5.0"
  source: "H3 出片实测（G:/AI/H3分镜台 各期质检）+ Kiro 会话记录 09-26 ~ 10-01"
---

# H3 出片经验库

H3 实际画出来的东西和提示词想要的东西之间的差距。条目的观察来自看过画面的实测；其中原因分析和“可试/待验证”方案另标，不能把建议当已经成功。

分工：**稳定规则**在 `h3-storyboard-writing`（A 线逐句分镜）和 `h3-prompt-writing`（提示词语法）；风格偏好在风格 skill；创意与手法在 `creative-animation-treatment`。**这里是证据和还在长的经验**；复现稳定后升级到那些 skill，这里留一行指向。

## 一、什么时候查

| 时机 | 怎么查 |
|---|---|
| 写中文画面 / visual_en / 整段提示词之前 | 按物件与症状查下表，先看已测风格块/模型/档位/结果；同条件的已验证句型可复用，主体、材质、颜色、位置按本期改写；单次与待验证写法作为候选，不照搬历史场景 |
| 排运动、定 motion_rule、想要"更流畅"时 | 读 `references/motion-flow.md`（F-） |
| 质检看到画错 | 按症状查；有条目照改，没有就是新经验 |
| 想重摇之前 | 先查——标了"换种子没用"的，重摇只烧 GPU |

| 分类 | 文件 | 典型问题 |
|---|---|---|
| P 物件与措辞 | `references/prompt-wording.md` | 发光物、highlight/swipe 招光和笔触、比喻、否定、数量与边数、框类、首次上色、框外变化 |
| C 续接与漂移 | `references/continuation-drift.md` | 段 ≥2 旧元素晃/散、长段冒东西、首帧闪总结画面、草稿≠768、多出的线 |
| T 时机与对齐 | `references/timing-align.md` | 补偿实测、续接段偏早、句中事件偏晚、补偿不线性、until 拍提前起手 |
| F 运动与流畅 | `references/motion-flow.md` | 节奏规则叠加压死、瞬现 vs 滑动、细线动作量不到、块面才算动、长停 |
| G 配音、渲染与工具 | `references/pipeline-gotchas.md` | 空音频、单段报错、作废范围、2K 修不了结构、2K 小字、显存、大图卡死 |

## 二、什么时候记（触发）

每期**质检后**、每次**改词重渲看过画面后**，检查是否有可跨期复用的新发现或给旧结论追加的证据。下面四种值得记录，一次也可记（标“单次”）；普通通过无需凑条目：

1. 改了提示词才好的（失败原句 + 成功原句）
2. 换种子、改写法都没用的（列出试过的全部写法）
3. 工具或引擎行为出乎意料的（报错、作废范围、缓存、时长、读数）
4. 成片读数（`h3_align` 成片读数 / `h3_timecode` 节奏预检）和肉眼观感明显不一致的

不记：好不好看、节奏喜不喜欢（风格 skill 的事）；没看画面的推测；用户对流程的要求（交 `h3-director`）。

## 三、写到哪里

- **只改源目录**：`视频分析/skill/6_出片经验_h3-production-lessons/references/<分类>.md`。安装根 `montage/h3-agent/skills/global/h3-production-lessons/` 是拷贝，直接改会在下次 install 时被覆盖。
- 产线代码**不会**自动读写本库（`h3_align` / `h3_timecode` 只出读数和 ⚠，不落经验）；记录全靠 Agent 手动编辑，所以质检结束前必须做这一步。
- 改完：升 `metadata.version` → `h3_skill verify` → `pack` → `install overwrite=true confirmed=true`。Pi 读的是安装根。

## 四、条目模板

```markdown
### P-013 一句话说清问题（成熟度）
- 症状：画面上看到了什么
- 失败写法：`原英文句子`（结果）
- 有效写法：`原英文句子`（结果）；没找到写"未解决"
- 原因：已隔离验证的机制，或明确标“假设/未拆开测”；不要把同时改了多个条件的结果写成确定因果
- 适用：风格块 / 画布 / 模型 / 档位（draft/768/2K）；未留档写“未留档”，没测过写“未测”
- 证据：期 · 段 · 档 · 种子 · 日期（来源会话日期）；能定位时补分镜/提示词/片段路径与观察时间
```

编号：P / C / T / F / G 各自递增，**只增不改号**；删掉的号不复用。

## 五、成熟度、去重、合并、淘汰

| 档 | 含义 | 下一步 |
|---|---|---|
| 单次 | 一期一段见过一次 | 下次遇到时验证 |
| 复现 | 在已写明条件下 ≥2 期或 ≥2 种子都这样 | 在该范围内复用；不自动推广到所有风格/模型/档位，升级时保留范围 |
| 已升级 | 已写进目标 skill | 条目留着当证据，末行写"已升级 → 目标 §x"；写拍时照目标 skill 做，这里只查证据和失败原句 |
| 推翻 | 新证据否定它 | **不删**，写被哪次实测推翻、正确说法 |

- **记之前先搜**：在全部 references 里搜症状关键词和英文关键词；同一问题已有条目 → 往那条追加证据、升成熟度，不新开。
- **合并**：两条讲同一机制（例：P-002 比喻、P-003 否定都是"提到的名词会出现"），保留编号小的为主条，另一条写"并入 P-xxx"。
- **冲突**：新写法和旧条目矛盾时（例：P-011 有效写法里的 `highlight` 后来招来光锥，见 P-013），在旧条目里标注并指向新条，不悄悄改原句。
- **过时**：引擎、ComfyUI 版本或产线代码变了，旧数值（补偿、耗时）要标"旧版本测"并写版本；代码已修的 G 条标"已修代码"，保留症状方便认出旧片。
- **待验证方案**：成熟度描述已见症状，不能替候选修法背书。“单次/复现”的问题仍可能没有有效修法；逐条看有效句是否已看过画面、是否只在草稿通过，跨条件迁移先标待测。

## 六、回流到其他 skill

| 经验类型 | 升级到 | 条件 |
|---|---|---|
| 逐句画面、visual_en、beats、motion_rule、补偿 | `h3-storyboard-writing` | 复现，且不依赖某一风格 |
| 英文句法、措辞禁忌（highlight、swipe、否定） | `h3-prompt-writing` | 复现 |
| 只在某风格块成立 | 对应风格 skill | 复现，写明风格 |
| 手法、转场、运动工艺 | 交主会话决定是否改 `creative-animation-treatment` | 复现 |
| 流程（验收、跳步、看图尺寸） | `h3-director` | 用户明确提过 |

升级时：目标 skill 写规则 + 指回本条编号；本条末行加"已升级 → 目标 §x"，证据和原句不删。

## 七、铁律

- **证据先于结论**：每条有"期 · 段 · 档 · 日期"，没看画面不写。
- **写原句**：失败和成功的英文原样抄，差一个词结果就不一样。
- **不外推**：草稿过 ≠ 768 过（C-004）；暗底 ≠ 亮底。
- **不把经验变成美学**：锁机位、瞬现、少元素等局部解决方案不能替代本期动作设计；新写法需保住关键动作证据，若修词损失了核心过程，回创意层重做可控实现。
- **读数和眼睛都要**：对齐 pass ≠ 节奏够（G-005）；读数低也可能只是细线量不到（F-003）；读数达标也可能画面没有世界（F-007）。
- **读数先看口径**：10-01 前的节奏读数是 scene_score 旧口径，和现在的像素口径不能直接比（motion-flow.md 头注）；记新读数时写明口径。
- **结论错了就推翻**，写明哪条、被哪次实测推翻。
