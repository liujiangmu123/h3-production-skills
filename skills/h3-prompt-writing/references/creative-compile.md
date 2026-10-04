# 创意编译：creative-animation-treatment 交接单 → H3 提示词

> 本库本地文件（非上游）。2026-10 建，依据 `一些最近的想法\08\动画效果研究_定风波\03` §7、`一些最近的想法\10\高级转场研究\02` §2–§6、`15\电子智人…\视频分析\05/06`（参与机制的停顿与提问帧）。
> 数字（段长、每段时间码数、两事件最小间隔、首事件下限、续接重放、补偿）以 `h3-storyboard-writing` §0 / §3 / §6 / §9 为准；本文只引用，下面出现的 1.217 s、1.2 s 都是那里的缺省值。手法卡在 `creative-animation-treatment/references/transitions.md`，本文不重复它的效果说明，只管"怎么编进字段"。H3 历史失败按 `h3-production-lessons` 的样本范围复用；当本期目的、模型或动作形式不同，记录风险，不把旧失败写成跨模式禁令。
> 2026-10-03 修订：先保住动画因果与动作证据，再检查适用的世界信息。§7 的「满配」沿用原索引名，表示必要信息完整，不再用八槽全填或词数比例评定创意。

## 1. 接收格式（创意交接单）

treatment 的创意交接单。新版先读「因果骨架」「不可丢的动作证据」「动作设计表」；旧版从内动词、中文画面、动量链与转场清单提取同样的信息。核心动作不明才退回；“无住户 / 无活层 / 无看不见的细节”可以明确写无，不能为了格式自行添一套世界。

「动作设计表」是普通 Markdown，列为 `主体与起态｜触发/目标｜可见过程（路径/速度/材料反应）｜终态及下一拍继承｜焦点/镜头｜实现路线与风险`。它不直接传给工具。编译后用「证据 → 对应句/镜」核对保留情况。

| 交接单字段 | 编译成什么 | 缺了怎么办 |
|---|---|---|
| 档位（R1–R5） | 选 §7.4 的适用骨架；住户政策与运动形式按实际创意与风格，不由高档位自动添加 | 已选风格足以确定则沿用；不明时退回 |
| 内动词 | 每段主事件的动词；检查每句 visual_en 是否在演它 | 退回 |
| 媒介 / 形变 / 空间 | A 线 → 风格块 visual_prefix 首句（风格词 + 媒介，§7.1 槽 1）；B 线 → `[Shot 1]` 开头的媒介句 | 风格已锁则用风格块，再按动作需要补适用信息 |
| 因果骨架 / 不可丢的动作证据 | 主体的触发、过程、结果与跨拍继承分别落入对应 visual_en 或镜头；检验创意没有被终态瞬现替代 | 旧单中可明确提取则兼容；核心不明退回 |
| 动作设计表 | 用现有 beat 的 at/until 表达主事件跨度，用 visual_en 表达路径、速度关系与材料反应；B 线写入镜内连续动作 | 可由旧中文画面提取；不虚构阶段时长 |
| 世界与住户圣经 | §7.1 槽 2–3；共用身份与外形进 visual_prefix，变化的位置/姿态进事件与开场清单；段 ≥2 只点名 | 无场景或无住户可写无；会影响主体辨认时退回 |
| 视觉语言四条（光 / 重量与时序 / 镜头 / 质地） | 光 → 适用的槽 4；重量 → 包络与怎么停；镜头 → A 线内容运动 / B 线运镜三维；质地 → 槽 5 | 已锁约束沿用，影响核心动作而不明时退回 |
| 活层 | motion_rule 里一句恒定状态（§7.1 槽 7）；R1–R2 写"无"就不写 | 默认无 |
| 表演 | 每个事件的"反应"部件（§7.2）；不单独占时间码 | 无人物则跳过 |
| 颜色关系 / 色彩剧本 | 槽 6 写本期基调与强调色关系；首次强调色的出现按交接指定。只有此前全部无彩色时才写 `the first color in the film`，不能与本来彩色的世界冲突（P-007）；变化进对应事件 | 按风格块 |
| 招牌镜头 | 保留其识别锚与动作证据，落在指定句/镜；前面是否停由交接节奏决定 | 简单任务无招牌镜头可跳过 |
| 间（停顿的位置与用途） | A 线静止句写 still；B 线写定好的保持状态与时长；不把运动中的等待强译成冻结 | 未指定则不强加最长停顿 |
| 看不见的细节 | 只在不抢焦点、且 motion_rule 允许时译入所在拍 | 可明确写无；不自行加装饰 |
| 删掉的默认 | 编译后全文检索，命中即删 | — |
| 制作路由与分层 | 剥层：代码层的字/数不进 H3；留空区写成位置 + 光 | 默认全 H3 |
| 转场清单 | 逐行套 §3 模板 | 无接缝就跳过 |
| 参与位（参与拍表中已锁的位置与装置） | 依拍表保留等待物、留白、揭晓与命名（若有）。A线思考窗需静态可读时用still；运动本身构成问题时先检查本期motion_rule和时窗，不硬冻结。B线写实际等待状态与镜内时间。揭晓可用运动、遮挡打开、路径改变、重排或光，取拍表的可见证据，不强加光脉冲。无命名句不添命名卡；精确文字/代码需求按实际已接入能力，不冒称已实现。没有参与拍表不自动添一套互动 | 无＝本期没有额外参与设计 |

## 2. 词译表（交接单里常见的说法 → H3 写法）

下表处理本地 A 线常见的空效果名和已记录失败，不是全模式词汇禁令。B 线可按官方使用 `cinematic` 等风格词、真实光照与用户指定的转场。真实灯、屏幕、窗及其光照照常写清形状/亮灭（P-001），不为避开一个效果词删掉可见世界。

| 交接单写 | 不要写进 H3 | 写成 |
|---|---|---|
| "形变成" | morph / transform effect / dissolve；`morphs … finishing by`（草稿里叠成两个半透明形，P-016） | 要看过程：一个主语 + 轮廓动词 + `one single shape changing continuously in place, until it has become …`（过程版待测，transitions.md §7 T1）；不要过程：`instantly changes into …`（P-016 实测干净） |
| "转场到 / 切到" | transition / cut（A 线） | A：§3 五种转译；B：`[Shot N] At MM:SS.mmm, the camera cuts to …` |
| "镜头推进去" | zoom / push（A 线） | A：`… expands evenly from its center until its edges pass beyond all four edges of the canvas`；B：`The camera pushes in with large amplitude at fast speed through …` |
| "闪一下 / 亮起来" | flash / glow / light / bloom（A 线） | `the whole canvas brightens one step for an instant and settles back, and as it settles, …` |
| "发光的" | glowing / luminous | `a thin pale rim along its left edge`（细亮边）；光源写成灯的方向 |
| "沉一下不弹 / 最后一个迟到" | gently / smoothly / slowly | `settles once and stops dead`；`the last one lands a hair later than the others`（写在一个复合事件里） |
| "电影感 / 梦幻" | cinematic / dreamy | 删；换成光源、质地、构图句 |
| "不要 X" | no X（P-003 否定也会画出 X） | 写在场的东西把位置占满："the upper third holds only rain and mist" |
| 留给代码层的标题 | "space for the title" | "the upper middle third holds only rain and mist"（不提字） |
| 比喻（"像时间的伤口"） | 画布句里写比喻（P-002） | 写字面画面 |
| "有质感 / 高级 / 电影感" | premium / high-end / cinematic | 材质句 + 光句：`matte painted surfaces with a fine dry-brush texture`、`low warm sunlight from the back left, every object casts one long soft shadow toward the lower right` |
| "底部留空"（R3 以上有场景时） | 只写 `the lower fifth stays empty`（场景里会被画进东西或被当成画框） | 用在场的东西占住：`the lower fifth of the frame is a plain, dark, even strip of ground with nothing on it` |
| "一个人 / 演员" | a person / a man（会画成写实人或随机人） | 住户圣经那一句原样：`the tall figure in the long coat and short-brimmed hat`；住户政策按档位写进 no_voice_en（§7.1） |
| "活的世界 / 有生命" | alive / dynamic / breathing | 一句恒定的小状态：`the only thing that ever moves on its own is the faint shadow of a curtain inside the lit window, swaying very slightly and constantly` |
| "他有反应" | reacts / is surprised | 身体动作：`the thin sparrow pulls its neck in, and the plump one does the same a hair later` |

## 3. 转场编译模板

### 3.1 A 线（段内，一拍一句 visual_en）

```text
原位替换   X is instantly replaced in place by Y of exactly the same size and position; X no longer exists anywhere, and every other element remains exactly unchanged      (点名 X 有招回它的风险，P-003；待测 T2)
容器换内容 the picture inside the {container} instantly changes into …; the {container} itself stays exactly where it is
内容平移   the whole row of {n} {items} slides {dir} by exactly one {item} width in one quick move and stops dead      (until 0.6；不写 sweep / swipe，P-011)
子框放大   the {frame} at the center expands evenly from its center until its edges pass beyond all four edges of the canvas, so that its plain {color} interior now fills the entire frame      (until 0.9；下一句才放新东西)
全屏枢纽   a still field of {material} instantly covers the whole canvas, hiding everything beneath it; the {material} stays perfectly still      (正面持续状态，不写 does not flicker，C-005)
形变       the outline of the {shape} pushes outward and … , one single shape changing continuously in place, until it has become a {new shape} of the same size at the same spot      (until 0.85)
光脉冲     the whole canvas brightens one step for an instant and settles back, and as it settles, … ; {anchor} remains exactly unchanged
2D→3D      the flat {shape} instantly extrudes into a {solid} seen from slightly above, its front face exactly where the {shape} was
页面倒地   the upright {page} tips backward, pivoting on its bottom edge, and lands flat as a floor …, settling with one small bounce      (不写 like a … 比喻，P-002；锁机位由 motion_rule 写)
```

规则：一拍一个主因果事件，允许同一动作的接触、推进、落定与附属反应，不按英文动词数拆拍。长动作必有 until；两个独立揭示才拆拍，A 线相邻独立起点按 storyboard §2 留出间隔。两变化确实属于同一因果且过近时可合为一拍，不能把不相干事件硬塞一起。A 线不写运镜/剪辑词，优先用正面持续状态点名不动的元素。模板的 until 比例只是示例，要按真实句长重算；“小回弹”等模板细节若被本期 motion_rule 禁止，先解决冲突，不能两边照抄。

### 3.2 B 线（镜间，`integrated_multimodal_description` 里一截）

```text
图形匹配   …the shot ends centered on {A} … [Shot N] At MM:SS.mmm, the camera cuts to {B} at the same position and scale in the frame …      (后镜不提 A)
动作匹配   …{action} midway— [Shot N] At MM:SS.mmm, the camera cuts to … continuing the {action} without a pause …
声音匹配   …; the {sound A} continues seamlessly across the cut and becomes {sound B} …
甩镜       …the camera pans {dir} with large amplitude at fast speed into a streaked blur— [Shot N] At MM:SS.mmm, the camera cuts as the same {dir} whip settles onto …
遮挡擦除   …{object} passes close in front of the lens, filling the frame; the cut hides inside the passing {object}, and as it clears frame-{side} the next scene is revealed: …
推穿       The camera pushes in with large amplitude at fast speed through {opening}, and the shot continues inside …      (一镜内完成，不切)
叠化       只在用户明确要求时：[Shot N] At MM:SS.mmm, the shot cross-dissolves over about one second to … {anchor} held at exactly the same position
```

规则：转场写观看理由和所需的跨场锚；`[Shot N]` 时间严格递增；镜数依任务与实际路线，不设通用≤4门槛；运镜按 base-en §4.3 写成自然英文动作。声音字段遵守官方 Tips，不用空泛的 near-silent。

## 4. 分段与衔接

1. **长效果切段**：>一段能装下的形变链，在"稳定中间态"切开——形状最简、细节最少的那一刻（钟面→空圆环→地球，切在空圆环）。上一段末拍让它 holds still。
2. **段 ≥2 开头**：A 线点名所有在场元素（`the empty black ring from before`），首事件不早于下限（缺省 1.217 s；本期调了续接头时见 storyboard §3），首句宜 still；B 线采用 latent 续接时 `[Shot 1]` 承接上段末态，保护重放窗，新镜不早于当前工具规定的下限（本地常见1.217s）；独立生成片段剪接按其实际起态写。
3. **续接头是重放，不能在里面创作新动作**：本地产线段 ≥2 的头来自上一段已生成的 22 帧。藏切要让上一段先到稳定的遮挡/同构状态，重放继续保持该状态；新景揭晓放在首事件下限之后。连续甩镜不能假装在冻结头中继续；需要另一条制作路线时回 treatment。
4. **整屏重构**：在语义允许的稳定交接点安排，配音先行 A 线以画内变化实现；B 线按镜头表写。段首附近通常利于接缝检查，但不强加最长停顿，不挪掉已定的揭晓位置。
5. **回扣**：保留能被辨认的主体、构图/动作锚与声音关系，按交接单写清发生的变化；不要用重复全文替代结果的意义。
6. **声音跨段**：本地 H3 产线依总指导不生成 BGM，`non_diegetic_music: N/A`；声音桥列入后期交接。脱离本地流程的官方独立请求，只有用户要配乐时才按 base-en §4.7 描写，不能从模板默认添音乐。
7. **大形变段 ≤12 s**，形变放前半（C-002）。

## 5. 编译示例（交接单 → 两线）

交接单节选（例（仅示格式）：锁定的是一种扁平 MG 风格，强调色由它的风格块定）：内动词"冻住"；转场清单：句 2 · D01 · 锚＝同一位置同大小 · 原因＝温度降 · A 线形变；最长停顿在句 3；看不见的细节＝六边形落定时比水滴小一丝又回原大。

> 这个例子演示句式。六边形这类要数边的形 H3 画不稳（曾画成七八边，`h3-production-lessons` P-015，未解决）：真要准确边数，交代码层或换一个不靠数边的形。

A 线编译稿（交 h3-storyboard-writing 落位）：

| 句 | 原句 | 中文画面 | visual_en 草案 | until | sfx_en | still | 转场 |
|---|---|---|---|---|---|---|---|
| 1 | 水结冰的时候。 | （静止） | — | — | — | ✓ | — |
| 2 | 它先改了形状。 | 中央水滴轮廓向外撑开、圆边拉直，这句说完时成同样大小的六边形 | `the outline of the {accent} water drop at the exact center pushes outward and its curved edge straightens into six equal flat sides, one single shape changing continuously in place, until it has become a {accent} hexagon of the same size at the same spot, settling a hair smaller and back; every other element remains exactly unchanged` | 0.85 | a thin crisp ice crackle | | D01 |
| 3 | 六条边，一样长。 | （静止） | — | — | — | ✓（最长停顿） | — |

B 线同一拍：`[Shot 1] … a single {accent} water drop sits at the exact center of the pale canvas under one soft light from the upper left. Its outline pushes outward and its curved edge straightens into six equal flat sides, one single shape changing continuously in place, until it has become a hexagon of the same size, settling a hair smaller and back. The camera holds a static shot and everything holds completely still.`

## 6. 编译自检（交 production-lessons 前）

- [ ] 因果骨架与不可丢动作证据逐条能指向具体句/镜；接触、路径、材料反应没有被瞬现终态取代
- [ ] 代码层的字/数没有一个出现在 H3 文本里；留空区写成位置 + 光
- [ ] A 线无运镜/剪辑指令，不以空效果名替代可见动作；真实光源、实际光照与官方风格名称未被误删
- [ ] A 线长动作有 until；独立起点跨度够，同一因果的子动作没有被机械拆拍；跨句动作已按实际句尾保持处理
- [ ] 转场清单每行都有对应句子，且写了锚与画内原因
- [ ] 段 ≥2：点名在场元素；首事件不早于下限（storyboard §3）；B 线若为 latent 续接，保护实际重放/首事件窗；独立片段按真实剪接方案
- [ ] 有参与位时保留拍表锁定的位置、等待证据与揭晓动作；静止/命名只在实际计划需要时编译，没有强塞光脉冲或命名卡
- [ ] 已决定的停顿、迟到元素、细节、首次上色都落在指定位置；没有强加一个招牌前 still 或额外回弹
- [ ] 否定句已改写为占位句；画布句无比喻
- [ ] 删掉的默认在全文检索为零
- [ ] 推断级手法（transitions.md 标"待测"）已在交付说明里标出
- [ ] 适用的世界信息已覆盖（§7.6）；共用不变量与剧情状态分开，段首/段尾交接一致；代码层未实现项已标明

## 7. 满配（旧索引名）：把必要语义写清

### 7.0 为什么要写清必要信息

- 官方 H3 系统是三段：**H3-Context-IR**（把用户的话"理解并整理"成 H3 读得懂的中间表示，**在不偏离原意的前提下补足缺失或不够具体的语义细节**）→ H3-Base（出 768）→ H3-Regenerate-2K。官方说 Context-IR 对成片质量"至关重要"，建议接入或按 Prompting Guidance 自建（huggingface.co/MiniMaxAI/MiniMax-H3 模型卡，2026-10-01 读）。
- **本地 h3_timecode 是结构化提示词编译器**，是否接 Context-IR、选择何种 H3 模型以实际 workflow 配置为准。它的文本不是经过官方 Context-IR 验证的等价实现；必要语义须写清，但少字不等于中等，多字也不等于好动画。
- 实测对照（10-01 画框 v3）：每段画面描述 445–556 词；其中整期共用的固定块 264 词（visual_prefix 116 + motion_rule 125 + no_voice_en 23），**描述看得见的世界的约 60 词**，其余是规则和否定；声音字段是逐条 UI 音加一句 room tone。官方 README 的 T2VA 示例（10 s、两镜）画面描述 250 词，几乎全写可见之物：场所与陈设（材质、颜色、位置）、人物外形（年龄、体型、发型、服装）、光（光从哪来、什么颜色、落在哪）、动作与反应；声音另写四句分层（底噪 → 渐强 → 冲击 → 回落）。
- 这个对照说明有些稿子的可见描述不足，不能推出“更多词/更多住户/更多景深就更有创意”。**词花在决定行为的东西上**：材料怎样受力、路径怎样改变、谁看见了结果。必要规则留下（A 线锁机位、事件后保持、保留区、不说话、不动清单），不为风格补无关场景。

### 7.1 八槽的适用信息（A 线：共用不变量写进本期风格块）

八槽是检漏表，按已选风格与动作需要取用：无住户不补角色，图解不补街景，平面风格不补真实阴影，事件本身已足够时不补活层。`visual_prefix` 每段重复，故只放不随剧情变化的媒介、外形与空间规则；会改变的位置、姿态、明暗由对应事件与开场清单负责，不在共用块中反复宣告初始状态。

| 槽 | 写什么 | 进哪个键 | 交接单来源 | 中等写法 → 满配写法 |
|---|---|---|---|---|
| 1 风格词 + 媒介 | 官方风格词开头（`2D-animated` / `3D CG` / `claymation` / `stop-motion` …，base-en §4.1）+ 媒介的具体做法 | visual_prefix 首句 | 档位、媒介 | `A 2D-animated minimalist motion-graphics explainer.` → `2D-animated illustrated scene in flat gouache shapes with a soft dry-brush texture` |
| 2 地点与景深层 | 需要空间时写地点及必要层次/位置，不固定四层或每层一件 | visual_prefix | 世界与住户圣经 | `one even sheet of cream paper` → `a narrow back alley at dusk: a soft-focus iron railing along the left edge in the dark foreground; a slack power line across the middle distance; a red-brick wall with one lit window behind it; a strip of warm sky above the rooftops` |
| 3 住户圣经 | 每个反复出现的住户一句：必要比例、材质与身份特征；不变量写共用块，随剧情变化的数量/位置写事件，精确数值查实际能力 | visual_prefix | 世界与住户圣经 | `two small solid black bird silhouettes` → `two sparrows on the line: a round plump one with a short tail at about two fifths of the frame width, and a thin long-necked one that tilts its head to the left at about three fifths` |
| 4 光 | 主光方向、软硬、色温；影子朝哪；画面里的实景光源写成形状 + 亮灭（P-001），不写 glow / highlight（P-013） | visual_prefix | 视觉语言四条 · 光 | `no shadows, no glow` → `low warm sunlight comes from the back left and every object casts one long soft shadow toward the lower right; the window is a flat cool-blue rectangle, lit` |
| 5 材质与颗粒 | 影响动作与风格的材质；纹理是否存在按锁定风格 | visual_prefix | 视觉语言四条 · 质地 | `flat vector shapes` → `matte painted surfaces, one even fine film grain over everything` |
| 6 色彩基调 + 强调色政策 | 基调的明度与色温；强调色用词描述（风格有色规则时按风格）；第一次上色之前的状态 | visual_prefix | 颜色关系、色彩剧本 | 补一句 `until the accent's first arrival, nothing in the frame carries the accent`（P-007） |
| 7 运动模式 + 活层 + 不动清单 | 瞬现 / 混合 / 活层（h3-storyboard-writing §6）；活层一句恒定状态；哪些东西永不移动 | motion_rule | 重量与时序、活层 | 见下方示例 |
| 8 声音底 | 这个地方的底：具体、低、恒定、无旋律 + `no voices` | sound_suffix | 声音怎么帮 | `Quiet room tone underneath; no voices.` → `A distant street and the low steady hum of a window air conditioner underneath; no voices.` |
| + 保留区与住户政策 | 底部五分之一（后期字幕）、右上角（水印）；R3 以上写成"在场的平面占住"（§2）；no_voice_en 按档位，原句由风格 skill 给 | visual_prefix 末句 / no_voice_en | 风格 | `the lower fifth stays empty` → `the lower fifth of the frame is a plain, dark, even strip of ground with nothing on it` |

判断标准是必要信息是否明确、有没有互相冲突，**不设词数或比例配额**。主体要能辨认，材料与光只写影响动作/观感的部分；优先用在场元素说明空区，避免为排除物件反而提到它（P-003）。

### 7.2 每一拍：锚 + 包络 + 反应 + 保持

A 线每个时间码代表一个主因果事件。过程有意义时先说明已有起态/触发，再描述主运动与结果；四部件可用于组织句子，不强制每拍都有小反应：

```text
[起态 / 触发与可见锚]; [包络：预备 / 路径 / 速度关系 / 材料反应 / 落定]; [结果与附属反应，若需要]; [保持：哪些东西不动]
```

示例（R3，招牌镜头那一拍）：

```text
the long soft shadow of a crouching cat slides in from the upper left edge of the frame and stops dead across the wire beneath the two sparrows, its edge crisp and the cat itself never shown; as it stops, the thin sparrow pulls its neck in and the plump one does the same a hair later; the railing, the wall, the lit window and the viewfinder frame remain exactly unchanged
```

规则：锚供定位与对齐，不能为了造一个块面起点而把后面的动作改成瞬现。包络与附属反应属于同一主动作时不另占时间码，独立信息揭晓才拆拍。R1–R2 也可以有过程（例如填充、传递、连通或受力变形），是否保留过程由动作证据决定。A 线起止用 at/until 表达，不在 visual_en 中手写时间；`finishing by` 由工具追加在完整事件之后。

### 7.3 段首开场清单 · 段尾终态 · 逐秒覆盖

- **段 1 首句**：先把画面里一切写成持续状态（地点、住户的位置和朝向、光的基线），再写第一个事件。
- **段 ≥2 首句**：开场清单＝上一段末帧的布局逐项写成持续状态（`the same alley at dusk; the two sparrows sit on the wire at …; the viewfinder frame stays over …`），只点名，不重写外形（外形在风格块里；C-001、C-005）。
- **段尾**：最后一拍写清终态（谁在哪、朝哪、什么亮着），它就是下一段开场清单的底稿。
- **跨度覆盖检查**：从起态到终态，能说清动作区间和保持区间即可；不用为每秒制造事件。A 线 until 只覆盖当前句说话跨度，句尾工具会自动加 hold_en，跨句不停的过程要按 `h3-storyboard-writing/references/animation-intent.md` 处理。

口径来自官方 3D 短片风格包的镜头表规范 shot-table-spec（GitHub MiniMax-AI/MiniMax-H3 的 skills 目录，包名 3d-animation-short-generator，2026-10-01 读；没有装进本库，本机研究副本在 `G:\AI\研究\MiniMax-H3-Director-Cut-Studio\skill special\3d-animation-short-generator\` 的 references 目录）：每镜写**连续交接**、**空间锚**（固定地标在画面的位置、角色位置与朝向、离场角色去向、光的基线）、**钩子类型**、**逐秒指令**（动作、镜头、位置、声音、交接）、**音轨**。B 线直接按这五项写；A 线的逐秒指令由句子时间码代替，其余四项进开场清单与段尾终态。

### 7.4 档位块起手式（可选示例；花括号中不适用的光、颗粒、景深、环境等直接省略；风格块优先）

```text
R1 符号  2D-animated minimalist motion-graphics explainer on {canvas: base color + light pool + grain}; flat vector {lines / fills} in {body palette} with a single {accent} accent …
R2 图解  2D-animated technical illustration: a {object} drawn as a clean cutaway at correct proportions, {n} parts {each named by shape and position}, {material} surfaces, lit by one {direction} light that lays a short contact shadow; {one or two environment cues} …
R3 插画  2D-animated illustrated scene in {flat gouache / cel-shaded / screen-printed} shapes, {place} at {time}: {foreground occluder}; {subject plane}; {background}; {far}. {inhabitant bible}. {key light + shadow direction}. {grain}.
R4 材质  {paper-craft / claymation / felt} stop-motion diorama photographed in macro: {planes, each with its material}, visible thickness, cut edges and fibres, one {direction} key light with real contact shadows between layers, shallow depth of field on the {subject plane} …
R5 电影  3D CG, stylized {painterly / NPR} rendering: {place} with atmospheric perspective and {haze}, key light {direction, temperature}, fill {…}, rim {…}, depth of field on {subject}; {inhabitant bible} …
```

### 7.5 声音字段

- A 线：`overall_soundscape` = 时间码音效列表（`h3_timecode` 生成）+ `sound_suffix` 的底。底要低、恒定、不要旋律和人声，装配时压在旁白下；`non_diegetic_music` 仍是 `N/A`。
- B 线：写本期必要的环境/物理动作声音；可以分层，但不为句数填底→重音→回落配额。无配乐按本地交付口径写 N/A，官方独立请求按用户要求。

### 7.6 满配自检

- [ ] 八槽适用信息明确，无适用项不强填；共用块没有把已改变的剧情状态重置
- [ ] 每个反复出现的住户有一句定稿外形；段 ≥2 只点名、不重写
- [ ] 光与影符合本期媒介；实景光源写清亮灭；A 线的效果词有实际可见动作，B 线不误删官方允许的风格/光照描述
- [ ] 活层（若有）服务本片且与实际 motion_rule 相容；不能用几何面积保证帧差阈值，持续动作另查指标适用性（treatment world-class.md §五）
- [ ] 每个主事件保留了需要的过程与终态，不为达帧差读数添加无意义块面或小反应
- [ ] 段首开场清单、段尾终态都写了；逐秒覆盖测过了
- [ ] `sound_suffix` 与场所相符，无场景图解可用默认 room tone；本地产线无音乐与人声
- [ ] 保留区写成"在场的平面占住"（R3 以上）；no_voice_en 和本期档位一致

### 7.7 编译示例：R3 风格块（接 treatment examples.md 反例 F 的修正版，开放媒介）

```text
visual_prefix: 2D-animated illustrated scene in flat gouache shapes with a soft dry-brush texture and one even fine film grain over everything. A narrow back alley at dusk, seen straight on: a soft-focus black iron fire-escape railing runs down the left edge in the dark foreground; in the middle distance a slack black power line crosses the frame a little above mid-height; behind it a warm red-brick wall with one small window, lit as a flat cool-blue rectangle; above the rooftops a strip of warm apricot sky. Two sparrows sit on the line: a round plump one with a short tail at about two fifths of the frame width, and a thin long-necked one that tilts its head to the left at about three fifths. Low warm sunlight comes from the back left, and every object casts one long soft shadow toward the lower right. The lower fifth of the frame is a plain, dark, even strip of cobblestone ground with nothing on it, and the top-right corner holds only sky.

motion_rule: One continuous shot with a perfectly locked camera: no zoom, no pan, no camera drift. Each timed event has exactly one main change, and at most one smaller reaction that belongs to it. A change with no finishing time is a single crisp change completed within a quarter second; a change with a finishing time moves steadily and stops dead exactly at that time. Between events the alley, the line, the sparrows and any frame hold perfectly still; the only thing that ever moves on its own is the faint shadow of a curtain inside the lit window, swaying very slightly and constantly. The railing, the wall, the window and the power line are fixed painted flats that never move, resize or drift.

sound_suffix: A distant street and the low steady hum of a window air conditioner underneath; no voices.

no_voice_en: No speech, no dialogue, no human voice of any kind; no people appear; no on-screen text other than the labels described.

hold_en: then the sparrows, the line and the set hold still in their new positions

closing_en: and the sparrows, the line and the set hold still in place until the end
```

此示例只展示实体场景的字段组织，不用词数作门槛，不给极简风格添实体光、街景或活层。活层那一句是待测写法（待测项 T8，`creative-animation-treatment` transitions.md §7）。
