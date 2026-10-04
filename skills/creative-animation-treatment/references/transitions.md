# Transitions, joins & 2D/3D craft（转场与接缝、创意动画手法卡）

> 2.2.0 边界：手法卡与编号保留。旧卡的镜数/力度/静音/最长停/次数是特定示例建议，不能升成通用门槛；当前 SKILL、animation-design.md 和实际风格/工具优先。过程有意义时不能被卡里的 instantly 替换；A/B 续接时间按实际配置。证据只在记录的场景、模型和路线内复用。

> 2.2.0 边界：手法卡与编号保留。旧卡的镜数/力度/静音/最长停/次数是特定示例建议，不能升成通用门槛；当前 SKILL、animation-design.md 和实际风格/工具优先。过程有意义时不能被卡里的 instantly 替换；A/B 续接时间按实际配置。证据只在记录的场景、模型和路线内复用。

> 2026-10 并入：`一些最近的想法\08\动画效果研究_定风波\`（2D/3D 结合、字当演员）与 `一些最近的想法\10\高级转场研究\`（41 种转场的 H3 落法）。
> 本文是共享工具：**不引用风格 skill 文件、不存风格读数**；风格锁定时先读该风格自己的转场规则，它赢。
> 数字（段长、首事件下限、合并阈值、时间码个数）以 `h3-storyboard-writing` §0 / §3 / §6 / §9 为准，这里只引用。英文怎么编进 H3 字段见 `h3-prompt-writing` 的「创意编译」节。下面卡片里的英文句是**句式示意**：H3 画错过的写法以 `h3-production-lessons` 为准，卡片与它冲突时它赢。
> 证据等级：**实**＝本库出片实测；**线**＝风格线规则未端到端跑；**推**＝推断，标"待测"，测完写进 `h3-production-lessons`，复现两次再升级。

读的时机：整片语言需要转场时；Step 4 发现内动词本身是一次接缝（变成、换代、回到、进入）；Step 7b / 7c（world-class.md §五）核对时。

## 0. 三条元规则

1. **动机在画里**：每个接缝都有画内原因（动作、遮挡、视线、材料、光、声）。没有原因＝软件转场。
2. **保住一两条通道，断掉其余**：视线落点、运动矢量、形状与尺度、明度色彩、声音、意义。
3. **先定藏还是显**：藏切让观众留在空间里，显切让观众看见关系。写法相反。

## 1. 选择流程（5 步）

1. 产线与风格许可：一画布 / A 线 → 只用画内手法（§3 五种转译）；B 线 → 加直切与运镜类，限风格允许的。
2. 接缝位置：段内 / 段界（段 ≥2 前 0.917 s 是重放）/ 镜间（B）。
3. 两侧关系 → 候选：同物异态 D01 · 异物同形 D05 · 同一动作 D04 · 同一声音 H21 · 同一意思 D03 · 同地异时 C17 · 部分→整体 B17 · 进入内部 F05/B28 · 反差 C27 · 并行 C28 · 回到开头 X08/E31 · 换维度 B31/B32/D33。
4. 藏还是显；保住哪条通道。
5. 选择本片需要的转场语法，不凑种类或峰终配额；显切/藏切取决于观众该发现什么。然后按需过 feel.md §一与§七。

## 2. 制作路由一句话

H3 出世界（有机材质、光、生命感），代码出思维（准确字、数、遮罩、帧级卡拍、跨段一致）。判据表见 catalog「制作路由判据」。下面每张卡都写两种做法；**同一效果只在一层做**。

## 3. A 线五种转译（镜头锁死时怎么"假装剪辑、假装运镜"）

| 想要 | A 线写成 | 中文画面句式 | visual_en 骨架 |
|---|---|---|---|
| 切（换一个东西） | 原位替换 | "中央那枚硬币瞬间换成同样大小的满月" | `X is instantly replaced in place by Y of exactly the same size and position; X no longer exists anywhere` |
| 换镜头 | 容器换内容 | "银幕里的画面瞬间换成她肩膀以上的近景" | `the picture inside the screen instantly changes into …; the screen frame itself stays exactly where it is` |
| 横摇 / 甩镜 | 内容整排平移 | "四格面板整排向左滑过一格" | `the whole row of four panels slides left by exactly one panel width in one quick move and stops dead` |
| 推拉 / 推穿 | 子框放大 | "中央小窗从中心均匀放大，这句说完时窗框越过画布四边" | `the small window at the center expands evenly from its center until its edges pass beyond all four edges of the canvas` |
| 叠化 / 黑场 | 全屏枢纽态 | "灰白雪花颗粒瞬间铺满整张画布" | `a still field of grey-white static grain instantly covers the whole canvas, hiding everything beneath it` |
| 视差横移（R3 以上的有景深世界，**待测**） | 前景层滑过 + 中景少挪 | "前景那截栏杆从右向左滑出画面，中景的电线和鸟只向左挪了一点，这句说完时停住" | `the dark foreground railing slides out past the left edge of the canvas while the wire and the two birds in the middle distance shift left by only a small step, both stopping dead together; the far sky stays exactly where it is` |

视差横移是第六种，2026-10 加入、未出片验证：两层不同速度的平移在帧差里是一个大事件（对齐靠前景层的面积），但 H3 可能把两层画成同速或把中景拖走；先出两段草稿看，过了再进 h3-production-lessons。

共同规则：不写镜头运动词和效果词（zoom / pan / dolly / camera moves / cut / transition / dissolve / morph into）；锁机位由本期 motion_rule 写，事件句里不再重复 · 不写否定从句（`nothing else moves`、`does not move`），写正面的持续状态（`every other element remains exactly unchanged`；否定句照样晃，h3-production-lessons C-005）· 枢纽态要空，下一句再放东西 · 容器不离开内容（P-005，换种子没用）· 长变化给终点（`until`）· 段 ≥2 点名所有在场元素（C-001）。

原位替换骨架里的 `X no longer exists anywhere` 点了 X 的名字，有招回 X 的风险（P-003：提到的名词会出现，不论肯定否定）；这句是 `h3-storyboard-writing` §2 的推荐骨架，先照写，结果记进待测 T2（§7）。

## 4. 手法卡（效果 → 何时用 → H3 提示词写法 → 代码动画写法）

格式：**编号 名称**｜效果｜何时用（及不用）｜H3（A 线 visual_en / B 线片段）｜代码（Remotion / three.js）｜证据。

### 4.1 匹配剪辑类

**D05/D03 图形·概念匹配**｜两物同形同位，一刀换身份，观众自己补出关系｜两物在文本里有因果或等价（硬币→月：钱与时间）；匹配形要被准备（先剥开才是白球）；不靠字幕补不出就别用｜A：`the seal-red coin at the exact center is instantly replaced in place by a seal-red full moon of exactly the same size and position; the coin no longer exists anywhere, and every other element remains exactly unchanged`｜B：前镜止于圆形物居中，`[Shot 2] At 00:04.200, the camera cuts to the full moon hanging at the same position and scale in the frame …`（后镜不点前镜物名）｜代码：两层同一 `<AbsoluteFill>`，`opacity` 在同一帧 0/1 互换，中心与尺寸取同一常量｜A 推 / B 线

**D04 动作匹配（含旋转对位）**｜动作中段切，下一镜从下一帧接，动量不停｜动作本身就是两场的共同点（推门→门开、摆锤→铃）｜A（until 0.8）：`the pendulum bob, swinging left at the bottom of its arc, turns into a small brass bell that keeps swinging left along the same arc and stops dead at the top of it; every other element remains exactly unchanged`｜B：`…her hand presses the door handle down— [Shot 2] At 00:03.000, the camera cuts to the inside of the room as the same door swings open toward the camera, continuing the push without a pause`｜代码：两段共用一条 `spring()` 曲线，切点取曲线中段帧｜推

**F27 视线切**｜看 → 所看之物｜文本有"看见/注意到"；A 线写成朝向→所指处变化（两句两拍）｜A：n `the flat silhouette instantly snaps into a pose facing right; every other element remains exactly unchanged` → n+1 `at the right edge, exactly where the silhouette now faces, a seal-red window instantly appears`｜B：`he lifts his gaze toward … [Shot 2] … cuts to what he sees`｜代码：朝向箭头 `rotate` + 目标处 scale-in｜推

**C27 反差硬切**｜高点或长静后一次改完所有大变量｜需要强调反差时可在读清前态后突变；次数和停的位置按内容｜A·段界：本段首事件（≥1.217 s）`the whole canvas instantly recomposes into a new picture: …`｜B：`the camera cuts abruptly to …` + 声音同时换｜代码：`<Series>` 硬接 + 音频同帧切｜推

**C28 交叉剪辑 / 双栏**｜两线并行、越切越快｜两个同时进行的过程（蜡烛燃尽 vs 沙漏）｜A：`in the left panel, … ; the right panel stays exactly unchanged`，下一事件换栏｜B：`[Shot 2]/[Shot 3]/[Shot 4]` 交替，镜数按本期观看任务与实际路线确定（此卡少镜示例不作为上限）｜代码：两栏组件，事件表交替、间隔递减｜推

**C12 跳切**｜同机位只换主体位置｜表现时间跳过、重复劳作｜A：`the silhouette instantly reappears at the right end of the table in the same pose; every other element remains exactly unchanged`｜代码：位置关键帧无插值（`step`）｜推

### 4.2 形变与身份类

**D01 形状 morph**｜一个形连续变成另一个形，不叠化｜同物异态（水滴→冰晶）；简单轮廓才稳，脸/手/字不用｜A（until 0.85）：`the outline of the seal-red water drop at the exact center pushes outward and its curved edge straightens into six equal flat sides, one single shape changing continuously in place, until it has become a seal-red hexagon of the same size at the same spot; every other element remains exactly unchanged`（句式示意：边数要准的形 H3 画不稳，六边形曾画成七八边，P-015 未解决——要精确边数交代码层，或选轮廓不靠数边的形）｜B：写材质动作 `… liquefy into black ink that reshapes into …`｜代码：`flubber`/`interpolatePath` SVG 路径插值，点数对齐｜A 部分实测：瞬变 `instantly changes into …` 干净、`morphs … finishing by` 叠成两个半透明形（P-016）、形变时歪一两帧（P-009）；`changing continuously … until it has become` 的过程版还待测（T1）

**D33 同一身份重排**｜相同元素保身份滑到新位置，可跨维度｜公式变形、句子重组、3D 字块回到纸面；每次一处，观众说得出"哪个没变"｜A（只做形状）：`the same seven red blocks slide from the curved row into one straight line, each keeping its own size and color, while nothing new appears`（同类小物件超过三个，数量 H3 画不稳，P-015；按 P-004 写死每一块的位置，或交代码层）｜代码：FLIP——记录起止 bbox，`interpolate` 平移缩放；字面全在代码层（manim `TransformMatchingTex` 同理）｜推

**T19 字出列**｜一行里一个字离队演剧情，空位留着｜承载转折的那一个字（"盛"升起坠落）；一行只一个｜A（字块 ≤2 可读，整行字交代码）：`a row of seven small red blocks stands on the white floor; only the second block lifts straight up out of the row and hangs high above it, leaving a clear gap in the row, while the other six stay exactly in place`（七个同类块数量不稳，同 D33 的注）｜代码：字块数组，目标索引单独 `spring`，其余冻结｜推

**D34 光脉冲换态**｜整屏亮一档又落回，落回时已换状态｜揭晓、"一下子"；亮要有画内原因｜A（一个复合事件，不写 flash/glow/light 名词）：`the whole canvas brightens one step for an instant and settles back, and as it settles, dozens of small white snow dots are already scattered across the sky above the skyline; the skyline itself remains exactly unchanged`｜B：`a camera flash bursts white across the frame and, as it fades, the shot transitions to …`｜代码：全屏白层 opacity 0→0.35→0 共 6 帧，第 3 帧换底层｜推（待 T5）

**C17 同位置不同时代**｜构图全锁只换状态｜一画布最自然的时间转场｜A：`every window in the dark-grey skyline instantly switches from warm yellow to cold white, and three slender towers appear between the old buildings; the skyline's outline and position remain exactly unchanged`｜代码：同一底图两态，可配 D34｜推

**E31 母题换义回归 / X08 首尾回扣**｜同一物多次回来，意思变｜系列和整片的收束｜A：每次用同一个英文名字点名；回扣保持可认的主体/关系锚，明确本期已改变的结果，不要求全文复刻，`the whole canvas instantly recomposes into the opening picture: …; this time …`｜代码：同一组件 props 只改一项｜实（P-004、C-001）

### 4.3 遮罩与枢纽类

**D35 全屏枢纽（含黑场借位、色彩泛滥）**｜一种材质先铺满，在全屏态里换身份，再收成新画面｜两侧完全不同、又要连续；枢纽要空｜A 三拍：铺满 `a still field of grey-white static grain instantly covers the whole canvas …; the grain stays perfectly still` → 变 `large blue and orange blotches emerge across the whole grey static field until …, the first color in the film` → 收 `the full-canvas pattern shrinks evenly toward the center until it is a single horizontal oval …`｜B：`the camera pushes in until the dark back of his coat fills the entire frame. [Shot 2] … the shot transitions out of the same darkness …`｜代码：全屏噪声 shader / 纯色层，`clipPath: ellipse()` 收缩｜推（待 T4）

**D25 遮罩揭示 / 物体当 iris**｜遮罩形状本身有意义；本场最亮最大的物胀满成下一场底｜月亮胀满成白、峰冲脸铺白；几何 iris/星形＝黑名单｜A：`the full moon at the center swells evenly until it fills the entire canvas with its pale white, and nothing else remains`（until 0.85）｜代码：`clipPath: circle(r)` r 插值到对角线｜推

**G21 字形取景窗**｜大字当常驻窗，窗里按拍换｜窗里正是这个字所指（年份里放那年的作品）｜A（单张，≤4 字）：`four huge white serif numerals "一〇八二" stand across the black canvas; at the beat their strokes turn into windows showing a sheet of dark ink calligraphy inside, while the black canvas around them stays unchanged`；窗内按 0.4 s 换 → 代码｜代码：SVG `<text>` 当 `mask`，窗内放 H3 素材序列｜推（H3 易画出形外）

**D36 实体遮挡擦除**｜画里的实体掠过，切口藏在遮蔽最满处｜B 线主力；擦除者要有来路方向｜B·段界：段 N 末镜 `a dark bamboo-ribbed sail glides from right to left close in front of the lens, filling the entire frame by the end of the shot`；段 N+1 `[Shot 1]` 帆仍满屏继续滑，`[Shot 2] At 00:01.217, the cut hides inside the passing sail: … as its trailing edge clears frame-left, it reveals …`｜A（待测）：块面滑入盖住、停死，再在下一句换底下的画面（写法见 flow.md §四.2（画内转场））；不写 sweep / swipe——带 until 的"一抹铺满"在草稿里被画成刷子笔触（h3-production-lessons P-011）｜代码：前景层 x 平移，下层在遮蔽满帧时切换｜线 / A 推

### 4.4 镜头穿越与尺度跳跃

**F05/F23 镜头穿越（推穿）**｜进入一个东西的内部成为新世界｜内动词就是"进入"、门是语义上的门（年份里的"〇"＝进入那年）；否则是黑名单 zoom-through｜A（单独一句，until 0.9）：`the small amber window at the center of the dark-grey house expands evenly from its center until its edges pass beyond all four edges of the canvas, so that its plain amber interior now fills the entire frame`；下一句才往空的琥珀里放东西｜B：`The camera pushes in with large amplitude at fast speed through the round lit window, and the shot continues inside …`（一镜内完成）｜代码：three.js 相机沿 z 穿过开口，或 2D 整层 `scale` 以窗心为原点｜推（待 T3）

**B17/B18 尺度跳跃 / 德罗斯特**｜局部↔整体，收缩到最小才认出；推一轮回到起始构图｜从细胞到人体、从像素到画面；回到起始＝X08｜A：收缩 `… shrinks evenly toward the center until it is …`；德罗斯特在放大后另一句 `at the exact center of the amber field, a small window identical to the first one instantly appears`｜B：`the camera pulls out with large amplitude …`｜代码：嵌套组件递归 + 对数缩放（`Math.exp(t)`）保持匀速感｜推

**F26 甩镜（B only）**｜横摇进拖影，下一镜同向同速落定｜甩向一个视线或声音｜A 转译成内容整排平移（§3）｜B：`the camera pans right with large amplitude at fast speed into a streaked blur— [Shot 2] At 00:04.000, the camera cuts as the same rightward whip settles onto …`｜代码：整层 x 平移 + 方向模糊 filter，切点在模糊峰｜推

**F18 rack focus**｜焦点从一层移到另一层｜注意力本身要换对象时（catalog F18：一切虚化只剩一点）；景深层至少两层｜A 写成明度层切换：`the grey foreground grid instantly turns the same pale grey as the canvas, and the black silhouette behind it instantly becomes solid black; every other element remains exactly unchanged`｜B：`the focus racks from … to …`｜代码：两层 `blur()` 互换｜推

**F21/D04 运动矢量延续、出画入画**｜方向与速度跨缝一致｜两场之间有同一个方向的运动（catalog F21：屏幕边缘是舞台口；D04 动作匹配）；方向变化需给可读线索，不禁止有理由的反向｜A 两句两拍：`the seal-red arrow slides right and out past the right edge` → `a seal-red paper boat slides in from the left edge, continuing the same rightward motion, and stops dead at the center`｜B：`the camera's slow rightward drift continues at the same speed across the cut`｜代码：共用速度常量｜A 推 / B 线

### 4.5 2D / 3D 结合

**B32 页面倒地**｜立着的一页向后倒成地面，下一件事在地面上发生｜字墙→文字大地；必须"倒下之后在上面发生下一件事"｜A：`the upright page of tiny black characters tips backward, pivoting on its bottom edge, and lands flat as a floor stretching to the horizon, settling with one small bounce`（锁机位由 motion_rule 写；不写 `like a …` 比喻，P-002）｜B 可续 `then the camera glides low along the blank path in the middle of the text floor`｜代码：three.js 平面 `rotation.x` 0→−π/2，字纹理为可读字｜推

**B31 两视图双读**｜正看 A 侧看 B，转四分之一圈就是论证｜"视角决定结论"的文本；转一次停住｜A（物转镜头锁，until）：`the long ridge of grey ink dots turns a quarter turn in place around its vertical axis and stops dead, now seen end-on as one sharp peak; only the ridge turns, and every other element remains exactly unchanged`｜代码：点云 `rotation.y` 0→π/2，正交相机｜推

**D12/B01 侧转成线、3D→2D**｜3D 物侧转薄成一条线，这条线是下一画面的第一笔｜从体积回到讲述｜A：`the red 3D word turns sideways until it is only a thin red line across the canvas`｜代码：`scaleZ`→0 后换 2D 线组件｜推

**B02 2D→3D 挤出**｜外轮廓连续只变厚度｜简单几何｜A：`the flat seal-red square at the center instantly extrudes into a seal-red cube seen from slightly above, its front face exactly where the square was`｜代码：`ExtrudeGeometry` depth 插值｜推（简单几何才稳）

**I21 二维画、三维光**｜平面形接受同一盏灯｜剪影人站进 3D 雨雾｜A/B：`a flat hand-drawn ink silhouette …, lit from the upper left by one soft light: a thin pale rim along his left edge and a soft contact shadow on the wet ground, while his body stays perfectly flat`（不写 glow，不写 `like paper` 这类比喻，P-002）｜代码：sprite + 法线贴图或手画亮边层｜推

### 4.6 字当演员与信息动画（多数归代码层）

**G23 场景物质成字**｜字由本场物质凝成，按它的物理还回去｜一次一字；离黑名单最近，粒子必须叫得出名字｜A：`the falling rain in front of the bamboo gathers mid-air into one large white character "莫" made of raindrops, holds for a breath, then its lower strokes run down and fall away as ordinary rain`｜代码：字形采样点做粒子目标，叠在 H3 的雨上（推荐）｜推

**G22 字号即刻度**｜字号＝量｜里程、人口；与 Q01 互斥｜A：相对大小 `"惠州" snaps in to its right at twice its height`｜代码：`fontSize = k * value`，精确比例｜推

**O19 大字归档**｜大字砸下→缩进清单｜结尾要收藏物；一段只用一次｜A：H3 只出世界并留空 `the upper left quarter of the night sky stays empty and dark`｜代码：FLIP 缩放平移入列｜—

**O20 参数扫动**｜可见手柄拨动、世界按规律变｜文本里真实的变量，一片一个｜B / A（until）：`a thin white slider handle below the flame glides from the left end to the right end, and as it moves the flame grows from a small round flame into a tall narrow flame, stopping exactly when the handle stops`（只写火焰本身的形状，不写 bead / tongue 这类喻体名词，P-003）｜代码：滑杆值驱动参数，刻度数字代码出｜推

**C26 冲击帧**｜最重的字前 1–3 帧反色闪｜一片一次、反拍｜H3 不写（24 fps、≲1.2 s 合并）｜代码：`<Sequence from={hit-2} durationInFrames={2}>`｜—

### 4.7 声音接缝（B / 后期）

**H21 声音匹配**｜前一声化成后一声跨过切口｜两侧有音色或音高相近的声音（catalog H21：尖叫→汽笛、吊扇→旋翼）｜B：`the kettle's whistle continues seamlessly across the cut and becomes the train's long whistle`｜A：只能让两个事件的音效押韵（同一音色、同一音高走向）｜代码 / 后期：两段音轨在切点交叉淡化，音高对齐｜推

**H22 声音桥 / J-L 切**｜声音先于画面进入，或拖进下一场｜下一场的声音要先把观众带过去（catalog H22）｜B：下一场声音在切点前写出；跨段每段 `non_diegetic_music` 逐字一致｜A：装配时挪音轨（A 线提示词里不写配乐）｜代码 / 后期：音轨前移或后拖，跨过一个或多个切口｜推

## 5. 失败模式与对策

| 症状 | 原因 | 对策 |
|---|---|---|
| morph 被画成叠化（两个半透明形） | 写了两个物；写了 `morphs … finishing by`（P-016） | 一个主语 + 轮廓动词 + `one single shape changing continuously in place` + `until it has become`；不写 morph/dissolve；不需要看过程就写瞬变 `instantly changes into …`（P-016 实测干净） |
| morph 被压成瞬换 | 默认 motion_rule 是瞬变 | 给 until（0.8–0.9）、用 continuously；仍瞬换→本期 motion_rule 加句（问用户） |
| 匹配被画成同屏两物 | 写了"A 和 B"；B 线后镜点了前镜物名 | A：`replaced in place … no longer exists anywhere`；B：只写 `same position and scale` |
| 镜头动了 | 写了 zoom/pan/camera/推近 | §3 五种转译 |
| 容器挪不动或拖走内容 | 框离开内容（P-005，换种子没用） | 容器原地，只换里面；要挪写成边线动作（P-005 有效写法） |
| 转场退成硬切 / 软件味 | 只写 `transitions to`，没写材料动作；写了 wipe/iris | 每个 transition 后跟一句材料/实体动作 + 一个跨场锚 |
| 跨段漂移 | 长变化跨段；段 ≥2 未点名（C-001） | 在稳定中间态切开（最简形状）；段 ≥2 点名全部在场元素，段首写开场清单（C-005） |
| 整屏重构走样 | 大段重述 | 只放段首；回扣保身份与结果锚，勿重置剧情 |
| 光脉冲画成发光物 | 写了 flash/glow/light/highlight（P-013） | "整张画布亮一档又落回"，无光源名词 |
| 颜色抢跑 | 前面没约束（P-007） | 上色前写 `nothing on the canvas has any color yet` 或只约束那片 |
| 文字转场糊字 | 文字形变 | 只做整词出现/换色，字形变形交代码 |
| 长段后半冒东西 | ≥12 s 段不稳（C-002，换种子有用） | 大形变段 ≤12 s、形变放前半；先换种子 |
| 旧元素在续接开头或新元素出现时晃一下 | 写了否定句 `nothing else moves`（C-005） | 写正面持续状态 `every other element remains exactly unchanged`；段首开场清单 |

## 6. 自测

静音看接缝 · 逐帧看中间态（有没有两个半透明形）· 首尾帧并排（认得出吗）· 换文测（换一句旁白这个转场还成立＝装饰）· 说出锚与画内原因。

## 7. 待测（占 GPU 前先问用户）

T1 形变一个形（部分实测：瞬变 `instantly changes into` 干净、`morphs … finishing by` 叠成两个半透明形，P-016；形变歪一两帧，P-009；边数不稳，P-015；过程版 `changing continuously … until it has become` 未测）· T2 原位替换只剩一个物（近似实测：原地换形 `instantly changes, in place, into` 稳定，P-005 / P-016；`X no longer exists anywhere` 点名招回的风险未测，§3）· T3 子框放大时外部一起出画 · T4 全屏枢纽→色彩泛滥→收成椭圆 · T5 光脉冲 · T6 首尾回扣 · T7 B 线图形+声音匹配与段界遮挡。方法与过线标准见工作区文档 `一些最近的想法\10\高级转场研究\03_并入skill的建议.md` §9。T3–T7 在 h3-production-lessons 里还没有结论（10-01 查）。

2026-10-01 增（世界级层，world-class.md §五；起因 h3-production-lessons F-007）。每项先出两段草稿，过了再上 768 复核一段：

- **T8 活层**（本期确实需要时）：motion_rule 写一处小面积、恒定、不载信息的小动静（h3-storyboard-writing §6 活层写法），信息元素照样死停。待测：看片确认活层用途和焦点，再评估 h3_align 是否适用；持续运动导致误检/漏检时要报告指标局限，不能单凭几何面积保证通过。
- **T9 视差横移**（§3 第六种）：前景层滑出画面、中景只挪一小步。过线：两层速度看得出不同；中景没被拖走、没变形；对齐只检到一个起点。
- **T10 R3 档位块首测**（锁定风格 skill 里的 R3 档位块，或开放媒介的同类块）：剪影演员换姿势用"瞬间换成"。过线：演员不长五官和手指、不走路；每件东西的扁平影子成形且朝同一方向；成片读数的色面仍落在强调色上（底色族没被算成颜色）；段 ≥2 演员不走样。

测完按 h3-production-lessons 的模板记进 P- / F- 条目，复现两次再改正式写法。
