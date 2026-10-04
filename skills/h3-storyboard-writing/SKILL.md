---
name: h3-storyboard-writing
description: 配音先行 A 线的中文画面与英文分镜写法。将原稿或创意编译稿落入 visual_en、sfx_en、beats、until、still 和本期 style，保留动作因果、可见过程与段间终态；处理 h3_timecode 缺画面、节奏/时间码核对和旧稿格式转换。Use for timecode-line Chinese picture lines, storyboard beat placement and episode style settings. Narration belongs to the style skill, idea selection to creative-animation-treatment, and other H3 modes or multi-shot prompts to h3-prompt-writing and h3-director.
metadata:
  kind: global
  version: "1.8.0"
  source: "G:/AI/H3动画量产_AI总指导.md"
---

# H3 分镜写法（visual_en / beats / still / 风格块 / 旧稿转换）

生产线用（只用于配音先行线），分两次读：**写稿时读 §0**，和风格 explainer 一起写中文画面；**建期后、配音前读 §1–7**，把中文画面逐句翻成英文分镜。多镜头线（诗词长卷、木刻拼贴）不用本技能，整段提示词按官方 `h3-prompt-writing` 写，格式与续接按 `h3-director`「多镜头线出片」。

时间码提示词由 `h3_timecode` 自动拼：风格块 + 每句的英文拍（按配音时间码）+ 收尾句。**你只写分镜，不写整段提示词、不写秒数、不写 2K 提示词**（2K 自动用本段原提示词）。写得好不好，决定 H3 画得对不对、`h3_align` 过不过。

**先保住动画，再安排时间码。** 创意交接单的「因果骨架 / 不可丢的动作证据 / 动作设计表」是语义约束；一句旁白是定时单元，不自动等于换一张图。一个主体可以在多个句子中继承状态。过程动作、多拍、跨句动作或片子过于机械时，读 [references/animation-intent.md](references/animation-intent.md)：它说明如何映射到现有工具，并给出工具装不下时的交接方式；这些导演说明不能作为新字段写进 JSON。

## 0. 写中文画面时就要守的（写稿阶段读）

中文画面是英文分镜的底稿。写稿时就按 H3 做得出来的样子写，建期后第 1–7 节就只是逐句翻译；写稿时不管，到翻英文才发现做不出，就得回头改画面甚至改旁白。

分工：**旁白、配色与风格允许的表现听已选风格，动作意图听创意交接单**；下表只管 H3 与工具的落实。例：要求渐进描画就按第 6 节采用有结束点的混合写法，不能因默认是瞬现而删掉过程。若真实工具装不下已定动作，明确冲突并交回创意层调整跨度或制作路线。

| 写中文画面时 | 这样写 | 不这样写，到第 3 步会怎样 |
|---|---|---|
| 一拍一个主因果事件 | 结果本来瞬变可写"中央落下一个黑点"；过程有意义就写"纸片碰到横杆，沿折痕弯下，停在横杆两侧"；同一动作的过程与附属反应不按动词数拆拍 | 无主次的并列动作会被合并或丢掉；只留终态则丢掉创意机制 |
| 瞬变与过程按意图区分 | 出现、切换、标签等不需过程的瞬变用清脆动词；传递、受力、展开、遮挡揭晓等要看过程，写路径、材料反应、终态与句内结束点 | 全写瞬现会变成机械图解；只写"慢慢"不说怎么走、停在哪，H3 会拖或漂 |
| 长动作写终点 | "描出一圈，这句说完时画完""展开到一半停住" | 没终点就没有 `until`，H3 一直画，后面的事件全被推迟（§3） |
| 写清主体、位置、颜色 | "右边那根强调色的箭头""刚才那个点变红"；小物件写清几个、各在哪（"两个小白圆，一个在三分之一处、一个在五分之二处"） | "它动了""那个东西"：翻不成英文，H3 会乱找对象；只写"两个小圆"：续接段里会多一个、并成一个（`h3-production-lessons` P-004）。要靠数清楚的（多边形边数、>3 个同类小物件）H3 画不稳，写数字也不行（P-015，未解决） |
| 关键动作要看得清 | 主体与背景拉开，路径或形变幅度能被辨认；任何档位都可写起态/触发 + 过程 + 终态/反应。质检锚来自实际主动作，不另加一个无关块面来造帧差 | 细线、小幅变化可能低于 `h3_align` 的帧差阈值，报"未检到动作"；先目检动作是否执行和焦点是否清楚，不能直接推成观众看不见或创意不成立 |
| 世界写在风格块里 | 地点、景深层、住户外形、光与影、材质、声音底，在本期风格块里写一次（§6；写什么见 `h3-prompt-writing` creative-compile §7 满配八槽）；中文画面只写这一句的变化和谁有反应，段 ≥2 点名"那两只麻雀""那块银幕" | 每句重述世界：段 ≥2 被当成新画面重画、漂；世界一句不写：H3 用它的默认补，画面就是空底加图标（10-01 画框 v3"元素极简、动画中等"） |
| 整片节奏按预算写 | 按本期目标的事件密度写：目标是 `action=style` 里的 `target_events_per_min`（代码缺省 17.0，取自深海原片下沿；别的风格按自己 skill 的读数改，口径见 §6）。我们的配音约 28 句/分（`h3-production-lessons` F-001），17 个/分 ≈ 每句 0.6 个事件；哪些句静止、静止占多少听风格 skill，按整片算、不逐段凑配额（§4）；事件可以落在句首，也可以落在句中关键名词上（at 0.4–0.7，句中偏晚见 §3）；`h3_timecode` 的「节奏预检」会算整片事件/分、运动占比、静止中位，低于本期目标就报 ⚠ | 只按"事件少于句数"写、再逐段凑静止配额，会写到 5–7 个/分（09-30 画框两期，scene_score 旧口径），画面大部分时间是死的 |
| 一段的动作数有上限 | 一段 ≤6 个动作为宜（12 s = 8 个是 `h3_lint` `too_many_events` 的上限；只数起点，`finishing by` 不算） | 一段装不下，动作会赶、会丢 |
| 独立起点之间要拉开 | A 线相邻独立时间码起点相隔约 ≥1.2 秒；同一主动作的碰触、弯曲、落定留在一个事件内；两个独立揭示才挪位置或拆拍 | 两个挨得太近的小事件可能被并成一个；机械拆子动作则反而破坏连续运动 |
| 每段开口那一下动不了 | 每段第一句要"开口就动"的，接受约 0.3 秒延迟，或第一句写（静止） | 首事件最早 0.3 秒（段 ≥2 是时间码 1.217 = 续接头 0.917 + 0.3，前面 0.917 是续接重放；本期把续接头调大时下限跟着变，§3） |
| 段 ≥2 接着上一段 | 引用已有元素："上一段那张卡片翻面"；不重新描述整张画面（英文分镜在段首补一句点名清单，§2） | 续接已经把画面带过来了，重述是多余的，还可能被 H3 当成一张新画面重画 |
| 镜头不动 | 变化都发生在画面里：元素出现、移动、变形；要"运镜感"就让内容动：内容整排平移＝横移，子框放大＝推近，前景层滑过＝视差（待测，`creative-animation-treatment` transitions.md §3） | "推近、拉远、摇过去、跟着走"：这条线的 motion_rule 写死了镜头锁定，两边矛盾，动作时间也对不准 |
| 换场 / 转场 | 都写成画面里的变化：原位替换（"中央那枚硬币瞬间换成同样大小的满月"）、容器里换画面（容器原地不动："银幕里的画面瞬间换成……"）、子框放大到越过画布四边、整张画布先铺满一种材质再收成新形、同构图整屏亮一档又落回（落回时状态已变）；长变化写终点。手法怎么选见 `creative-animation-treatment` 的 transitions，英文模板见 `h3-prompt-writing` 的 creative-compile | "切到 / 转场到 / 叠化 / 镜头推进去 / 甩过去"：motion_rule 锁死了镜头，两边矛盾，H3 会画成两个物同屏或镜头运动；"A 变成 B"写成"A 和 B"会同屏两物 |
| 思考留白（参与式） | 要观众想的句子（出题、反省）：旁白句末写 MiniMax 停顿标记 `<#秒#>`（≤10，只对 minimax 引擎有效），这句或下一句画面写（静止），画面上留一个**静止**的"等待物"（发光的空格、悬停的问号）——等待物由前面某一句的事件放上去，留白那句只写（静止）；留白里不安排事件；装置怎么选见 `participation-design`。⚠ 现在（10-01 核实，未修）：配音层剪句尾静音会把句末停顿剪掉，标记还会原样进字幕。**现在怎么做**：原稿照样写停顿标记；修好前这类期别真跑配音（`h3_plan_durations` 真跑会合成、扣声贝），停在分镜这一步告诉用户在等修复；问题与修法以总指导（`H3动画量产_AI总指导.md`）§13 第 10 条为准，不自己换写法 | 不留白：问题只是修辞，观众来不及想；留白里安排事件：观众被画面拉走；写"闪烁 / 呼吸"的等待物：违反事件间绝对静止，`h3_align` 会多出起点 |
| 画面上的字 | 只放大字标签，原字加引号："一个大字标签「冰的晶格」"；数字、单位、上标一字不差写全 | 小字、长句、旁白原文上画面：少步数下会变形；旁白字幕后期加 |
| 底部五分之一 | 什么都不放 | 给后期字幕留的，风格块里写明了留空 |
| 人物按档位 | R1–R2（符号、图解）不写人物；R3 起风格允许的住户（无五官剪影演员、设计过的动物、简化五官的角色）照写，用风格块里那一句定稿外形点名，**先在 action=style 改 `no_voice_en`**（原句由风格 skill 给；风格没给就用 §6 表里的例句，只换成本期登记的住户）；任何档位都不写写实人脸、台词、配乐 | 默认收尾句是 `no people or faces appear`：画面里写了人却没改收尾句，两边矛盾，H3 画不准；把人换成圆点、头像图标或卵形，知识就跟着没了（电影、心理、体育、穿搭这类知识住在人身上） |
| 音效 | 写在动作后面："……，伴一声轻嗒"；静止句没有音效 | 音效离开动作就对不上帧（§5） |
| 静止句 | 写 `→ 视觉：（静止）`，后面不再跟字（停着的画面是什么，写在让它出现的那一句里）；每段至少一句有动作 | `（静止）` 后面加了描述，解析器就不认它是静止句，建期后要你补英文画面；整段全静止会被警告，也没有可对齐的动作（§4） |

写完原稿自查：每个主事件都能译出“谁从什么状态、受什么触发、怎样变化、停成什么状态”，不需要过程的动作可以短写。不可丢的动作证据在中文里就要能看见；不要到 visual_en 另起画面。建期后才发现要改中文：`h3_storyboard action=set` 改不了中文画面，只能改原稿后 `h3_storyboard action=init md_path=<原稿> overwrite=true confirmed=true` 重建——会盖掉已写的英文拍和旁白 txt（旧分镜留 `.bak`，可 `h3_undo` 退回），所以先复述给用户，并尽量在补英文之前改。

## 1. 分镜数据长什么样

```
分镜_长版.json
  style: {visual_prefix, motion_rule, compensation_s(+0.2), continuation_head_s(0.917), min_first_s(0.3), …}
  segments[]: {index, title, sentences[]}
    sentences[]: {n, text（旁白）, visual_zh（原稿中文画面）, beats[], still?}
      beats[]: {at, until?, visual_en, sfx_en?}
```

- `at ∈ [0,1)`：动作起点在这句话说话跨度里的比例（0 = 开口，0.6 = 说到六成）。
- `until ∈ (at,1]`：动作必须做完的比例点 → 提示词里写 `finishing by MM:SS.mmm`。
- `still: true`：这句话说的时候画面不动，不写画面、不出时间码。

写入：

```
h3_storyboard action=set items=[
  {index:1, n:1, visual_en:"a single black dot instantly pops in at the exact center of the canvas", sfx_en:"one soft dry pop"},
  {index:1, n:2, still:true},
  {index:1, n:3, beats:[{at:0.0, until:0.5, visual_en:"a thin black circle draws itself around the dot", sfx_en:"a faint pen scratch"},
                        {at:0.7, visual_en:"a small seal-red label \"光圈\" snaps in beside the circle", sfx_en:"a gentle tick"}]}
]
h3_storyboard action=view        # "缺英文画面 0 句" 才能往下走
```

## 2. visual_en 怎么写（2026-09 实测）

一拍 = 一个主因果事件，**不是一个英文动词**。同一事件可以含起势、路径、材料反应与落定；彼此独立的信息揭晓才拆 beats。按 [animation-intent.md](references/animation-intent.md) 核对中文、创意证据与英文。

| 要 | 不要 |
|---|---|
| 不需过程用 `instantly pops in / snaps into place`；有意义的过程用明确路径与终态，例如 `bends down along the existing crease and comes to rest across the bar`，配 until | 把连续动作一律换成 `instantly changes into`；或只写 `slowly / gently / gradually` 而没有路径、终态 |
| 写清主体、位置、颜色：`a small seal-red arrow at the right edge of the grid`；小物件的数量和位置写死：`two small white circles standing on the ground at about one third and two fifths of the canvas width with a clear gap between them`，之后每拍点名 `exactly two small white circles … in their exact original places and sizes, with nothing added` | 代词、指代不明：`it moves`、`the thing`；`two small white circles side by side`（续接段里多出一个、两个并成一个，`h3-production-lessons` P-004） |
| 写明其余不动：`every other element remains exactly unchanged` | 默认 H3 会自己保持静止 |
| 不要的东西写成描述画面的正句：`everything is grey and white only, with no color at all`、`nothing else stands on the ground line`；排除效果的否定可以直接写：`no halo, no bloom` | 点名否定物件：`there are no lamps, lights or glowing things anywhere` 反而画出亮灯——提到的名词会被画出来，不论肯定否定（P-003）；也别指望 H3 自己不加刻度、数字、灯光 |
| 画面里的实景光源（路灯、屏幕、窗）照常写，写成扁平形状并写清亮灭：`… already lit: … its lamp head a small solid warm amber disc, and directly beneath the head a flat triangular cone of amber light with crisp straight edges …, with no halo, no bloom and no soft glow around them`；亮起是剧情就先写灭着（`switched off … it gives no light at all`），亮起另写一拍（P-001，草稿三组成立，768 未单独测） | 只当背景道具、不说亮灭：H3 按常识画成亮的；`highlight / glow` 也会被当成光（P-013，单次） |
| 画框 / 取景框 / 选框留在框里的主体上：要挪写成边线动作 `the left edge of the amber frame instantly snaps inward to the gap between the two white circles while its right edge stays exactly where it is`；要换写成原地变形 `the amber frame instantly changes, in place, … into …` | 让框离开框里的主体（`jumps to an empty patch of ground`、`slides … and stops dead on the empty ground`）：768 四次都错，换种子也没用（P-005） |
| 镜头锁死（默认 motion_rule 已写） | `zoom / pan / dolly / camera moves` |
| 换场写成画面内的结构：`X is instantly replaced in place by Y of exactly the same size and position; X no longer exists anywhere`；容器里换画面：`the picture inside the screen instantly changes into …; the screen frame itself stays exactly where it is`；形变一个主语到底：瞬变写 `instantly changes into …`，要看过程写 `one single shape changing continuously in place, until it has become …`（`h3-prompt-writing` creative-compile §2） | 效果词 `cut to / transition / dissolve / morph into / crossfade`（与总指导 §7 禁镜头切换词一致）；`morphs … finishing by` 在草稿里叠成两个半透明形、一格变两格（P-016，单次；原位替换的句式还待测，`creative-animation-treatment` transitions.md §7 T2） |
| 引用已有元素：`the dot from before turns seal-red` | 段 ≥2 重述整张画面（latent 续接已带过来） |
| 大字标签，原字加引号：`a bold black label "冰的晶格"` | 小字、长句、段落文字（Turbo 少步数下中小字会变形） |

- **画面里有小字（数字、单位、上标）时，原字串必须一字不差写进 visual_en**：2K 重绘靠提示词才能把小字画对（实测不写会把"密"画错、"³"画成"²"）。
- **写拍之前查 `h3-production-lessons`**：上表已收了复现过的几条（数量位置、否定、发光物、框类）；还在长的（要留住的标记、强调色第一次出现、同一强调色、框外变淡 / 消失、形变歪斜、精确数量……）在那里，有实测过的有效写法和失败写法，按"要画的东西"查。质检时发现新问题、改好后记到那里。
- 细线描画、轻微亮度变化可能低于帧差阈值。质检锚优先选实际主动作中最清楚的形变/移动；未检到时用关键帧或局部回看区分执行失败与检测遗漏，不能仅为通过 align 把过程改成出现/变色。
- 不写：时间、秒数、`At …`、`<d>` 台词、narrator / voice-over、subtitle bar、写实人物与人脸（风格块登记过的住户按那一句点名写，§0「人物按档位」）、配乐。
- 一句里有两个独立揭示才拆 beats。相隔约 1.2 s 以内的两个小动作可能被合并：同一因果可保为一拍，独立事件就拉开。配音前按句内约 4.4 字/秒估间隔（(at₂ − at₁) × 句子字数 ÷ 4.4 秒，总指导 §4.2）；配音后看 `h3_timecode preview` 的事件表核对，工具不报这条间隔。
- 需要过程或反应的拍，可按 **起态/触发 + 锚/包络 + 结果/反应 + 保持** 写：`the long shadow of a crouching cat slides in from the upper left edge and stops dead across the wire beneath the two sparrows; as it stops, the thin sparrow pulls its neck in and the plump one does the same a hair later; the railing, the wall and the frame remain exactly unchanged`。附属反应不另占时间码；无反应的图解不强加人物，R1–R2 也能保留过程（creative-compile §7.2）。
- **段 ≥2**：这一段第一个有画面的拍，visual_en 开头先写开场清单——上一段末帧还在的东西逐项点名成持续状态（谁在哪、什么亮着），只点名、不重写外形（外形在风格块里；`h3-prompt-writing` creative-compile §7.3）；之后每拍写明哪些旧元素不动（`the frame, the arcs and every silhouette remain exactly unchanged`）。没点名的旧元素会漂、散、消失（C-001，复现）；开场清单让续接处的轻晃减轻、没去干净（C-005）。

## 3. beats 与 until

- 长动作（逐笔描画、渐变、展开、生长）**必须给 until**，否则 H3 一直画下去，把后面所有事件推迟（实测整段 +0.55 s、丢两拍）。
- 同句前拍 `until` 不晚于下一拍 `at`；跨句不能直接比较比例，配音后看 preview 的 `until_written` 不晚于下一事件 `at_written`，否则两拍可能被并成一个动作。
- **until 只在当前句内，工具每个事件句尾都会追加 hold_en**（bridge/h3_storyboard.py build_prompt）。多拍可在同一句的 at/until 里完成；跨句不停的动作不能靠超界 until、下一句 still 或删掉保持实现。可在语义允许的稳定里程碑切成接续事件；必须不停时交回导演选择 B 线或有产物的代码层（[animation-intent.md](references/animation-intent.md)）。
- 事件落在句首（`at: 0`）或关键名词处（`at: 0.4–0.7`）。关键名词的 `at` ≈ 这个词前面的字数 ÷ 整句字数（配音句内约匀速）。句中事件实测偏晚（`h3-production-lessons` T-002：at≈0.5 的一拍 768 上晚 0.70 s，单次）——要准的放句首，句中的按需把 `at` 提前。
- 首事件下限 = 续接头 + `min_first_s`：段 1 是 0.3 s；段 ≥2 缺省 0.917 + 0.3 = 1.217 s，本期按 §6 把 `continuation_head_s` 调到 1.2 时是 1.5 s。首句开口就要动的，接受这个下限或并到下一拍；两拍被抬到同一时间码时 `h3_timecode` 会警告。
- **一段 ≤6 个时间码为宜**（按拍数算，不是句数；lint 上限 ⌊段长/1.5⌋，下限 ⌊段长/6⌋）。

## 4. still：静止句

静止比例按本期风格与已定的注意力节奏；风格没给就不设比例，不把来自深海的代码缺省推广成所有风格要求。按 §6 设置本期目标，预检读数是诊断。**按整片算，不逐段凑配额**：逐段配额和"事件少于句数"叠在一起，曾把画框两期的事件压到原片的约四分之一（`h3-production-lessons` F-001）。

- 原稿写 `整句 → 视觉：（静止）`，建期后自动标 `still`；或 `h3_storyboard set items=[{index, n, still:true}]`。`（静止）` 后面不再跟字（§0「静止句」）。
- `still` 与 `visual_en` / `beats` 互斥；之后再写 visual_en 会自动取消 still。
- **每段至少要有一个事件**（整段全静止会被警告，H3 也没有可对齐的动作）。
- 预检报"节奏偏疏/停得太长"时，先看停顿是否承担观察、等待或揭晓，再看目标是否适用于本风格。语义确实空转才调整停顿或动作安排；不要为清零 warning 每句加一次弹出（刻意长停见 F-004）。
- 一段装不下时，合并同一主因果的子动作、重分段或返回创意层调整。承载核心证据的事件不能直接改成 still。

## 5. sfx_en

- 一个短名词短语，贴着动作：`one soft dry pop`、`a gentle paper flip`、`a faint pen scratch`、`a low soft thud`。
- 只有动作有音效；still 句没有。禁写 `near-silent`、音乐、人声。连发写 `three staggered soft pops`。

## 6. 本期风格块（action=style）

建期后、写拍前设一次。不设就是默认深海块（米白 #EBEBEB + 印章红 #D8382E）——那是 R1 符号档的块，**只适合知识住在记号上的期**；别的档位不设就会得到"空底 + 图标"。

**风格块写什么**按 `h3-prompt-writing` creative-compile §7 的适用信息（媒介、主体身份、空间、光材质、色彩、运动、声音）。八槽不是全部加满的配额。本期块每段重复，只放不变量；会随剧情改变的位置/姿态/明暗放进对应事件与段首状态。本节只管工具键、运动写法、补偿与目标。

```
h3_storyboard action=style style={
  "visual_prefix": "<满配槽 1–6 + 保留区：风格词与媒介、地点与景深层、住户圣经、光与影、材质与颗粒、色彩基调>",
  "motion_rule":   "<槽 7：运动写法（下表三选一）+ 活层（若有）+ 不动清单>",
  "sound_suffix":  "<槽 8：这个地方的底，具体、低、恒定> ; no voices.",
  "no_voice_en":   "<住户政策：R1–R2 用默认句；R3 起用风格 skill 给的放开住户的句子>",
  "hold_en":       "<事件后的保持：R1–R2 默认 then the canvas freezes；R3 起见下>",
  "closing_en":    "<段尾收束：默认 and everything holds completely still until the end；R3 起见下>"
}
```

`action=style` 只认 DEFAULT_STYLE 的键（`bridge/h3_storyboard.py`），只写要改的键，其余保留（合并进分镜的 style）；未知键、空字符串、越界数值一次全拒。文本键：visual_prefix / motion_rule / hold_en / closing_en / no_voice_en / sound_suffix / music。数值键与允许区间：`compensation_s` −3–3、`continuation_head_s` 0–5、`min_first_s` 0–3、`until_lead_s` 0–2、`target_events_per_min` 0–120、`target_motion_share` 0–1、`max_still_p50_s` 0–60、`target_ink` 0–1、`target_color_area` 0–1（用法见本节末三条）。桌面面板只能改 `compensation_s` / `continuation_head_s` / `min_first_s`，其余交 Agent 设。改了 style 要重跑 `h3_timecode`（先 preview）才进提示词。

| 键 | R1–R2（符号、图解） | R3–R5（有世界） |
|---|---|---|
| `visual_prefix` | 画布与必要的色彩/关系规则；光池、颗粒和强调色按风格选，不强加 | 按已定动作与风格写适用语义，不要求槽1–6全填；需要保留区时写成"在场的平面占住"：`the lower fifth of the frame is a plain, dark, even strip of ground with nothing on it` |
| `no_voice_en` | 默认 `No speech, no dialogue, no human voice of any kind; no people or faces appear; no on-screen text other than the labels described.` | 风格 skill 给的放开句，如 `No speech, no dialogue, no human voice of any kind; no realistic people or faces — the only figures are the flat featureless silhouettes described, with their mouths closed; no on-screen text other than the labels described.`；只有动物时 `no people appear`。只在风格块真登记了住户的期用放开句：收尾句里允许 figures，没住户的期会多画出人形（P-003） |
| `hold_en` | `then the canvas freezes` | `then the figures and the set hold still in their new positions`（有活层时活层照常，motion_rule 里已写） |
| `closing_en` | `and everything holds completely still until the end` | `and the figures and the set hold still in place until the end` |
| `sound_suffix` | `Quiet room tone underneath; no voices.` 可留 | 存在对应场所且声音有用时可改；无场景/无声设计不凭档位硬加底噪，如 `A distant street and the low steady hum of a window air conditioner underneath; no voices.` |

- **档位、画布、强调色从哪来**（按这个顺序取，不在这一步另起）：创意交接单的「档位」「世界与住户圣经」（有交接单时）→ 原稿 ① 章或任务消息写明的档位与风格块 → 本期风格 skill 自己的推导法和档位规则（例（仅示格式）：某风格把档位规则写在它的 style-dna 档位一节）；风格还没有档位规则，按 `creative-animation-treatment` Step 2b（参考片的档位是默认）。哪里都没写：用默认 R1 块之前先问用户。写成文字（可带 hex）；画布句只写光和质感，不写比喻（`like a darkened cinema` 会画出放映机和夜街，`h3-production-lessons` P-002）。
- **"底部五分之一留空"必须保留**（给后期字幕）；R3 起用占位正句写，不写"empty"让 H3 自己猜。
- **动作写法三选一**（10-01 同稿两段草稿对照实测，见 `h3-production-lessons` T-004；全滑动列在最后作对照）。怎么选：这一期没有一拍要看过程 → 瞬现；有拍的演示本身就是过程（拉宽、垂下、变形）→ 混合；本期需要持续环境动作且符合风格/配置 → 活层（待测）：

  | 写法 | motion_rule | 用在哪 |
  |---|---|---|
  | 瞬现（缺省） | 默认块：每个事件四分之一秒内完成 | 出现、变色、填色、实虚转换、标签 |
  | **混合** | "没给结束点的是四分之一秒内的瞬变；给了结束点的按描述路径到点停止"，见下方已测的匀速/不回弹模板 | 任何档位，只要动作证据需要过程就给 `until`；采用模板前核对它与已定的重量/速度关系一致 |
  | 活层（按任务需要，**待测**） | 混合 + 一句活层 + 不动清单，见下 | 本期若选持续环境动作：按任务区分保持的主体与环境层，小动静可恒定低幅（窗里窗帘的影子、一缕蒸汽、一朵烛火）；先出两段草稿跑 `h3_align`（占 GPU，先问用户），看有没有多出的起点、有没有漏检（待测项 T8，`creative-animation-treatment` transitions.md §7），过了再量产 |
  | 全滑动 | 每拍都给 until | 不推荐：填色会被画成刷子笔触，段 1 首事件晚约 0.5 s；"成片读数也没升"是 scene_score 旧口径量的，它把平滑运动读成没动，待像素口径复量（T-004） |

  混合写法的 motion_rule（已有实测支持匀速、不回弹的运动方式；下列“主因果”措辞为本次修订，仍需草稿验证，把末两句换成本期的不动元素）：

  ```
  One continuous shot with a perfectly locked camera: no zoom, no pan, no camera drift. Each timed event has one main causal action; any smaller reaction belongs to that action. A change with no finishing time is a single crisp change completed within a quarter second; a change with a finishing time moves steadily and stops dead exactly at that time, with no bounce. After each event everything holds absolutely still until the next timed event. The <不动的元素> are fixed flat cut-outs that never move, deform or drift. Everything already on the canvas keeps its exact shape, size, position and brightness unless a timed event changes it; nothing fades, flickers or sheds fragments on its own.
  ```

  若交接单明确要加速、回弹或材料缓冲，这个匀速/不回弹模板就不适合：按动作表改 `motion_rule` 的这句，并保持镜头锁定、明确结束点与无关元素不动。该新措辞属于待测，先验证代表性过程拍；不能一边写 no bounce 一边在 visual_en 保留回弹，也不能静默删掉导演已经选定的运动关系。

  活层写法的 motion_rule（R3 起，**待测**；把活层那句和不动清单换成本期的）：

  ```
  One continuous shot with a perfectly locked camera: no zoom, no pan, no camera drift. Each timed event has exactly one main change, and at most one smaller reaction that belongs to it. A change with no finishing time is a single crisp change completed within a quarter second; a change with a finishing time moves steadily and stops dead exactly at that time. Between events the figures, the set and any frame hold perfectly still; the only thing that ever moves on its own is <活层：一处小面积、恒定、不载信息的动静，例 the faint shadow of a curtain inside the lit window, swaying very slightly and constantly>. The <不动的布景> are fixed painted flats that never move, resize or drift. Everything already in the frame keeps its exact shape, size, position and brightness unless a timed event changes it; nothing fades, flickers or sheds fragments on its own.
  ```

  活层的面积预算：`h3_align` 按整帧帧差找动作起点，阈值是每帧约 0.25% / 0.35% 的像素在变、不扣基线（`bridge/h3_align.py`）。活层只用一处小动静，每帧变化面积留在阈值下；整屏的雨、雪、落叶、雾流会让每一帧都"在动"，对齐直接失败——这些只放 B 线。

- 补偿：瞬现 / 混合写法 `compensation_s` 缺省 0.2，先用 0.06–0.2（T-001）；新风格线第一期两段草稿跑 `h3_align` 定一次（总指导 §7），768 第一轮再看一次——草稿上测的偏差搬到 768 不完全一样（T-001、C-004）。一期定一个值，不要每段反复微调：小幅改补偿，动作时刻几乎不跟着动（T-005）。**续接段（段 ≥2）比段 1 系统性早约 0.3 s**（画框 v2 768 与 v3 两版草稿，T-003）：本期 style 把 `continuation_head_s` 设到 1.2 左右，比全片加补偿准（首事件下限跟着变，§3）。
- 带 until 的拍：两段草稿里它们若整体提前起手（T-006，单次：画框 v3 草稿 6 拍早 0.04–1.32 s，中位 0.83），设 `until_lead_s`（缺省 0 = 不推）——until 拍的起点和结束点一起往后推这么多秒，瞬现拍不动；`h3_align` 和节奏预检都按推后前的位置算。
- **节奏目标键**（数值，只出警告，0 = 不查）：`target_events_per_min`（缺省 17）、`target_motion_share`（0.25）、`max_still_p50_s`（2.0）、`target_ink`（0.05，比墨量中位）、`target_color_area`（0.10，比色面 p90）。缺省是深海 13 支原片用 `h3_rhythm` 像素口径量出的下沿（10-01 起，代码 `bridge\h3_storyboard.py` DEFAULT_STYLE；旧值 14 / 0.12 / 3.0 / 0.04 / 0.03 是 scene_score 口径，已作废）。别的风格按自己 skill 的读数在本期 style 里改，**读数要是同一把尺**：研发线 `analyze_reference.py` 的节奏数（事件/分、运动占比、静止）还是 scene_score 口径，会把平滑运动读成没动，不能直接填；画布两项（墨量、色面）与 `h3_rhythm` 同算法，可以填。风格 skill 没有像素口径的读数：先设 0（不查），或按它的主配方推一个暂定值，写明是暂定。`h3_timecode` 用前三个做「节奏预检」，`h3_align` 用全部五个做「成片读数」。

## 7. 写完自检（进 h3_plan_durations 之前）

- [ ] `h3_storyboard action=view`：缺英文画面 0 句
- [ ] 中文与英文一一对应；因果骨架与动作证据能逐条指向具体事件，没有把过程只译成终态瞬现
- [ ] 每段至少一个事件、≤6 个时间码；静止比例符合本风格（风格没给比例，就看节奏预检，§4），按整片算
- [ ] 每拍一个主因果事件、主体/位置清楚；需要看见的路径、速度关系与材料反应已保留；长动作有 until
- [ ] 段 ≥2：第一个有画面的拍开头有开场清单（上一段末帧布局写成持续状态），每拍点名不动的旧元素（§2）
- [ ] 事件与 motion_rule / hold_en 不冲突；段尾终态供下一段继承；跨句动作未靠 still 或越界 until 假装连续
- [ ] 画面小字原样写进 visual_en；没有写实人物、字幕条、台词、镜头运动；出现的住户都是风格块里登记过的，`no_voice_en` 已按档位改
- [ ] 本期 style 已按所选风格设定，八槽适用项已覆盖；代码缺省没有变成通用审美；底部五分之一留空，`hold_en` / `closing_en` / `sound_suffix` 与本期运动一致

配音出来以后（`h3_plan_durations` → `h3_timecode preview` → 出片）再查：

- [ ] `h3_timecode preview` 的错误已解决；节奏 warning 已核对适用目标与动作意图，保留有理由的观察/等待，不为清零强加事件
- [ ] `h3_timecode preview` 的事件表里，相邻两拍写入时间差都 ≥1.2 s（工具不报这条，§2）
- [ ] 出片后先回看动作证据、因果与段间交接，再看 align/成片读数；读数低时区分执行失败、检测遗漏与目标不适用，按证据改画面

## 8. 旧稿转换（进 h3_new_episode 之前）

工具只认这种 ② 章（`h3_new_episode storyboard=true` 解析）：

```markdown
## ② 长版旁白时间轴

【第 1 段 | 冷开场 | 拍型：B1 冷开场】
这是光。 → 视觉：画面中央落下一个小黑点
它从一个点开始。 → 视觉：（静止）

【第 2 段 | 对比 | 拍型：B2 概念对比】
……
```

章标题以 `##` 开头、含"旁白时间轴"；抖音版另起 `## ④ 抖音版旁白时间轴`（同格式，章名含"抖音"）。段头也认 `【第 N 段】` 和全角 `｜`；工具读段号，`拍型：` 那格拿来当段标题显示，其余格子（段名 / 锚点…）只给人看，多个锚点用顿号隔开。句行必须是 `整句 → 视觉：中文画面`（也认 `-> 视觉:`；句和画面之间不认 `|`）；句子里只放要念的字，括注（`（7字）` 之类）会被念出来；音效写在中文画面末尾（"……，伴一声轻嗒"），英文进 `sfx_en`，不另开一格。格式以总指导 §4.3 为准。

| 旧稿类型 | 特征 | 改法 |
|---|---|---|
| 旧量产六件套 | `[00:00-00:05] 句（7字） → 视觉：…` | 删每行 `（N字）`（会被念出来）；时间前缀可留（会被剥掉）；③ 章的 `<d>`、字幕条、`<Picture N>`、配乐全不要 |
| `|` 分隔稿 | `句 | 画面` | 把 ` | ` 改成 ` → 视觉：` |
| 配音先行代码块稿（09-08~09-12，约 290 期） | ` ```旁白脚本_长版 ` 里 `S01 句`，另有"分段"表和分镜表（`At {S01}` 英文） | ① 按"分段"表把 Sxx 切成段，写 `【第 N 段 | 标题 | 拍型：…】`；② 每句去掉 `Sxx` 编号，接 ` → 视觉：` + 分镜表中文列（无事件的写 `（静止）`）；③ 建期后把分镜表英文列按第 2–5 节改写，用 `h3_storyboard set items=[…]` 批量写入（`{Sxx}` 占位全部丢掉，时间码由工具生成）；④ ③ 章风格块改写成 `action=style` 的 visual_prefix |

所有旧稿都要重新按 **目标秒数 × 3.5 字** 核字数（旧稿按 ×5 写的会长约 30%），超出就删句或拆期。改完先 `h3_new_episode … storyboard=true`，`h3_storyboard action=view` 看段数、句数、静止句对不对，再补英文。

## 9. 拼好的时间码提示词长什么样（核对或不走工具手写时用）

产线里这段提示词由 `h3_timecode` 生成，`h3_lint` 检查，你不用手写。下面是它遵守的规则，用来核对 `h3_timecode preview` 的结果，或在 Kiro / Cursor 里脱离工具写一段时照着写。字段名和顺序仍按官方 `h3-prompt-writing`（`integrated_multimodal_description` → `overall_soundscape` → `non_diegetic_music`）；官方里的 `<d>` 台词、画外音写法**不用于这条产线**。

- 不写 `<d>…</d>`、`(S1)`、narrator / voice-over / narration：H3 听不到配音，写了会自己编一个声音（lint `dialogue_tag` / `narration_in_prompt`）。
- 不写字幕条、不把旁白原文放上画面：字幕后期加（lint `subtitle_bar`）。画面底部五分之一留空；画面里本来就有的标签、概念卡照常加引号写。
- 画面字段 = `[Shot 1]` + `visual_prefix` + `motion_rule` + 各句事件 + `no_voice_en`。每个事件写成 `At MM:SS.mmm, <visual_en>`，有音效接 ` with <sfx_en>`；同一句的第二拍起写小写 `at`。
- 时间码 = 句子在本段内的开口时刻 + `at` × 这句的说话时长 + `compensation_s`（默认 +0.2；渐进描画类约 −0.5）；段 ≥2 再加续接头（缺省 0.917 s）；带 until 的拍再加 `until_lead_s`（缺省 0）；不早于续接头 + `min_first_s`（段 1 即 0.300，段 ≥2 缺省 1.217）。长动作写 `, finishing by MM:SS.mmm`（同样的加法，且至少比起点晚 0.25 s）。
- 时间码单调递增，每段 ≤6 个为宜，末个离段尾 ≥0.8 s 最稳（<0.8 s `h3_timecode` 先给 warning，看的是最后一拍的起点；<0.5 s lint warn `timecode_overflow`，≥ 段长是 error `timecode_past_end` 会被拒——lint 把 `finishing by` 也算进去，长动作的结束点同样不能压到段尾）。静止句没有事件。
- 每句（不是每拍）的最后一拍后写风格块的 `hold_en`（默认 `then the canvas freezes`）；最后一句改写 `closing_en`（默认 `and everything holds completely still until the end`）；同一句的多拍之间用分号连。R3 起这两句按 §6 改——有活层时不能写 "the canvas freezes"。
- 画面字段末尾是风格块的 `no_voice_en`，默认 `No speech, no dialogue, no human voice of any kind; no people or faces appear; no on-screen text other than the labels described.`；R3 起按 §6 换成放开住户的句子，开头的 no speech / no dialogue / no human voice 必须留着（缺了是 info 级 `no_voice_missing`）。
- `overall_soundscape` 按同样的时间码列音效，结尾是风格块的 `sound_suffix`（默认 `Quiet room tone underneath; no voices.`；R3 起写这个地方的底）；`non_diegetic_music: N/A`（不生成配乐）。
- 段长由 `h3_plan_durations` 按配音反推，不按字数估。
