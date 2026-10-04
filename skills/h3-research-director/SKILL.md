---
name: h3-research-director
description: |
  Research-line director of the H3 animation studio (研发线总入口). Learns a reference video or written source such as a WeChat 公众号 (measure → reports → philosophy, animation mechanism, master recipe, three-tier table, author feel), finds fitting directions and topics, develops derived styles, and produces paired style/topic skills with production task messages. Use for 分析这个视频 / 分析这个公众号 / 学习风格 / 找方向选题 / 创新风格 / 做成 skill, or corrections supported by new measurements. Separates observed source behavior, controllable production rewrites and untested actions. Episode production belongs to h3-director; this skill does not render or run paid voice by itself.
metadata:
  kind: core
  role: research-director
  version: "2.9.0"
  source: "G:/AI/视频分析/跨风格文档"
---

# 研发线导演：学风格 → 找方向选题 → 创新风格 → 产出 skill

工作室只有两条线。**本 skill 管研发线**；每一期怎么出片归生产线 `h3-director`。

```
研发线（本 skill）                                   生产线（h3-director）
① 量 → ② 判 → ③ 定产线 → ④ 方向与选题 → ⑤ 风格创新
      → ⑥ 产出 skill → ⑦ 验证 + 任务消息  ──────────▶  一期一期出片
产物：风格 skill <风格>-style-explainer                读风格 skill 写旁白和画面，
        （哲学、画面、节奏、旁白写法、作者感觉）         A 线同时守 h3-storyboard-writing §0，
      选题 skill <风格>-series-planner（方向、选题）    工具出片
      选题库 / 路线图 / 任务消息
```

一个风格 = 画面 + 画面节奏 + 旁白 + 声音，外加把它们串起来的哲学。四样都要分析、都要进风格 skill；只学了画面，做出来的片子"长得像"但"不像他说话"。

**学习对象不限于视频。** 公众号文章、专栏、书都走同一条线、同样七步，只有两处不同：① 怎么采集和量（见 ①「文章来源」），③ 要先给它配一个画面语言（原文没有画面）。其余 ②④⑤⑥⑦ 照常。

**铁律**：先量后判；数字描述原片、注来源片；风格与爆点分开建档；skill 只存读数、取舍和发明（通识留在 `style-foundations`）；走哪条产线由测量决定；本线不渲染、不真跑配音，要做先问用户。

## 用到的模块（都按需读）

| 步骤 | 模块 |
|---|---|
| ① ② 量与判 | 本 skill `references/evidence-ledger.md`（证据台账、含义对齐、边界复核）；`style-foundations`（六把尺子含旁白与文案、参与 `participation-rulers.md`；测量口径 `measurement-protocol.md`，暗场小字 / 无旁白片按其 7b 分带量；哲学读法、三层分离法、作者感觉与作者感觉对照）；本 skill `references/report-outlines.md` |
| ④ 方向与选题 | 本 skill `references/planning-method.md`（通用方法）+ 各风格自己的 `*-series-planner`（专有判据与数据）；完整实例 `shenhai-series-planner` |
| ⑤ 风格创新 | 本 skill `references/style-innovation.md` + `creative-animation-treatment`（想法层操作子库）+ `participation-design`（参与装置库：给变体换一种让观众参与的做法时用） |
| ⑥ 产出 skill | `h3_skill scaffold / verify / pack / install`；完整实例 `shenhai-style-explainer` |
| ⑥ ⑦ 写风格 skill 的交付格式、验证 | `h3-storyboard-writing`（A 线；§0 是写中文画面时就要守的 H3 约束，§6 是本期风格块，风格 skill 的画面规则要和它对齐）或 `h3-prompt-writing`（官方语法 + 创意编译）+ `h3-director`「多镜头线出片」（B 线）；混排、歌先行、代码层见 `h3-director`「混合路线」；+ 生产线工具的免费步骤 |

## 在哪做

- **Kiro / Cursor**：有子代理和联网搜索。报告并行写、④ 的爆款实证与事实查证只能在这里做。
- **Pi（H3-pi-agent）**：能跑脚本和 `h3_*` 工具（量化、scaffold、免费验证），**没有联网搜索**；④ 里要联网的项标"待联网查证"，留给 Kiro / Cursor。
- 开工前：`h3_skill list` 查这个风格有没有 skill。没有 → 从 ① 走。有 → 先看 ② 末段：缺哲学 / 主配方 / 三层表 / 作者感觉 / 选题 skill 就按"缺件"补；只有新测量推翻了旧条目才走 ⑥ 升级模式。

## ① 建档与量

```
G:\AI\视频分析\<题材>_<风格短语>\          一个参考源一个文件夹，下面四样按顺序放
  原始视频\                               原片只读（文章来源叫 原始素材\）
  视频分析\{01–04 报告, 分析素材\}         ① ② 的产物
  skill\{1_风格skill_<slug>-style-explainer\, 2_选题skill_<slug>-series-planner\}   ⑥ 的产物（实体）
  风格量产\{00_领域总览.md（评级总表 + 否决清单）, <方向>\_开工种子包.md, <方向>\_选题路线图.md, _风格创新_变体卡.md, 任务消息\}
  目录说明.md                             这条线走到第几步、结论、两个 skill 的版本
```

某一条线的结论只写在这条线的文件夹里；不属于任何一条线的内容才放 `G:\AI\视频分析\跨风格文档\`。一次性脚本、临时抽帧用完就清。

环境：`G:\AI\视频分析\.venv`（缺了：`uv venv --python 3.12 .venv` → `uv pip install --python .venv\Scripts\python.exe -r requirements-analysis.txt`）；ffmpeg 在 `C:\Tools\ffmpeg\bin`；转写模型 `G:\AI\hf-cache\faster-whisper-small`。

```powershell
cd G:\AI\视频分析
.venv\Scripts\python.exe -X utf8 scripts\analyze_reference.py --video "<片1>" --id V01 --video "<片2>" --id V02 --out "<风格线>\视频分析\分析素材"
```

`--crop-bottom 0.16`（底部字幕带；无字幕给 0）、`--move-thr 0.004`（颗粒底 / 实拍先量噪声底再调高）、`--no-asr`（纯音乐）。输出每片一个子目录 + 汇总 `analysis_report.md`（每片末尾有帧号 → 秒的换算）；有旁白的片子目录里有 `transcript.json`（ASR 分句 + 时码），03 旁白写法靠它，要逐字听校。

**文章来源（公众号等）**：`原始视频\` 换成 `原始素材\`，每篇一个 `.md`（标题、发布日期、链接、能看到的阅读 / 在看 / 转发数，正文原样）。选 ≥5 篇：数据最好的代表作 + 普通的几篇（看作者的常态）。公众号链接先用网页抓取，抓不到就请用户粘贴全文。不跑 `analyze_reference.py`；字数、段长、句长、小标题数、引语与数字密度、转折和高潮落在全文百分之几，直接从原文数（口径写在报告里）。只学方法：原文放在风格线文件夹里，不进 skill（`narration.md` 的逐字样例只摘短句）；要把他的某篇文章直接改编成视频，先有授权。

脚本之后必须人看：逐张看 `sheets/` 联络表；0.10–0.30 的单帧跳变用 `ffmpeg -i <片> -ss <t−0.5> -t 1 -vf fps=10 x_%02d.png` 核对是不是整屏重构图（加 `--evidence` 脚本直接抽好首帧、最后一帧、最后 1 秒和切点 / 快速动作前后 1 秒的 10 fps 条，放 `evidence/`）；多片报范围（最小–最大 + 中位）。

**事实先于理解**（细则 `references/evidence-ledger.md`）：每支片一份 `证据台账.md`——五遍看法（全片 → 真实切镜 → 时间线无空洞 → 快速动作 / 接触 / 遮挡加密 → 倒查结尾），外观 / 道具 / 动作 / 镜头 / 声音分开记，每条标已见 / 待定 / 用户设定；单张截图不推整段动作，结尾不补。然后做**含义对齐**：中文复述"谁在做什么 → 期待什么 → 转折 → 最后状态"+ 我理解的笑点 / 落差，不确定的说出来，问一次等用户确认；用户补充的设定和画面事实分开存。确认后才写 ② 的报告。

## ② 判：四份报告 → 哲学 + 主配方 + 三层表 + 作者感觉

提纲、必填数、子代理提示词骨架在 `references/report-outlines.md`：01 视觉美学、02 节奏与剪辑（画面节奏 + 旁白节奏 + 声画咬合）、03 旁白写法（句式、修辞、结构、口吻、从不说的话、≥15 句逐字样例、写稿公式；无旁白风格写朗诵 / 字幕 / 音乐）、04 风格解构（最后写）。01–03 在 Kiro / Cursor 可并行派子代理，主对话核对。04 必须产出四样东西，后面每一步都靠它们：

1. **哲学**（读法见 `style-foundations`「哲学怎么读出来」）：3–7 条"作者相信 X → 所以 Y"，合成一句话，导出 2–4 道选题门。先写草稿，第 3 项三层表写完后回头逐条核对：每条对不上两条规则的删。
2. **主配方**：一条可复述的时序主线（动作链 + 硬指标 + 变量分配），写清核心动画机制：主体从什么状态出发，什么触发或阻力使它发生可见变化，结果怎样留下来推动下一拍。材质、色彩与出现/消失清单不能代替动作链。非叙事片按“规则/演示对象 → 可见过程 → 认知结果”提取；证据不足就回查关键片段，不补不存在的意图。
3. **三层表**（方法见 `style-foundations` 三层分离法）：本质 / 作者默认 / 每期自由，**画面、画面节奏、旁白、声音四个维度都要有**。④ 的契合判据来自本质和选题门，⑤ 的创新只动作者默认与每期自由。
4. **作者感觉**：哲学 + 本质压成"他怎么想、怎么看、怎么动、怎么说"，按想法 / 画面 / 节奏 / 旁白 / 声音五项各 1–3 条，每条写成"他会……，不会……"；再写本风格的作者感觉对照（这五项各问什么）。判断标准是"作者本人拿到这个新点子会不会就这样做"，不是"观众认不认得出"。每一期、每个创新都拿它对照。

爆点机制（前 3 秒给什么、揭示时刻、记忆点、收尾）单独一章，不混进风格。含义层（笑点、落差、情绪转折）写在这一章，引用用户确认过的复述；动作都对、含义丢了的样例段不算合格。报告里的数字和描述都能追到证据台账 ID；交报告前过 `evidence-ledger.md` 第四节边界复核清单。

**风格已有 skill、但缺哲学 / 主配方 / 三层表 / 作者感觉 / `hit-mechanics.md` / 选题 skill（早期做的 skill 常见）**：不用重新量，也不先改风格 skill。按 `style-foundations` 的哲学读法和三层分离法从它现有的规则里拆出来，整理爆点机制，写进这个风格的选题 skill `fit-criteria.md`（没有选题 skill 先按 ⑥ 第 1 步只补它）。缺的是旁白写法（没有 `narration.md`）：要做选题时不影响；要升级风格 skill 时按 03 提纲补一份报告，走 ⑥ 升级模式。缺件清单和写法见 `planning-method.md` 第三节"基线缺件"。之后 ④ ⑤ 都按这份走。

## ③ 定产线路线

| 看什么 | A 配音先行时间码线 | B 多镜头线 |
|---|---|---|
| 画面跟谁走 | 旁白句子 | 音乐拍点、诗句或镜头节奏 |
| 切换 / 镜头 | 硬切≈0，镜头可锁 | 直切换景、运镜是风格本身 |
| 已有例子 | 深海 | 望海潮、唐伯虎 |
| 生产线怎么做 | 原稿 ② 章 → 分镜 → 配音 → `h3_timecode` | 原稿 `## 长版 · H3 分段提示词` 每段一个代码块 → 模式 A 建期（`h3-director`「多镜头线」） |

**文章来源先配画面**：原文没有画面、画面节奏和声音，先定画面语言——借一个已有风格 skill 的画面（它的三层表画面 / 画面节奏 / 声音三行照搬），或用 `creative-animation-treatment` 整片模式按这位作者的哲学发明一个（让画面也像他会做的）；再按上表选 A / B 线。写法和想法照学，篇幅、铺垫、信息密度不照搬：压到视频时长，最强的反转或细节前置到前 3 秒，一句一个看得见的变化。结果按 ⑤ 的"杂交"记（作者的写法 × 配的画面），新主配方要写得出来。

A 线指配音定时钟、时间码编译，不把固定机位/瞬现自动当成所有风格的原片规则。交接区分**原片动画机制、当前可控实现、尚待验证的动作**；可控降级也要保住关键动作证据，丢了核心过程就需重做实现设计，不能记成风格本质。
A 线的默认 motion_rule 与补偿缺省 +0.2 是 09-27 在"镜头锁死、四分之一秒瞬现"上实测的，本机 ComfyUI 0.37.4 上偏早（`h3-storyboard-writing` §6）：新风格第一期都要用两段草稿标定一次；要渐进动作就得先改 motion_rule 再标定（占 GPU，须用户同意）。一种风格需要 A 线主体加 B 线插段、歌先行或代码层时，「产线路线」写清楚，生产线按 `h3-director`「混合路线」落（一期只有一种建期模式）。

## ④ 找方向与选题

按 `references/planning-method.md` 六阶走：候选 ≥25 个且有意外跨度 → 三个一票否决（H3 可生产性 / 合规 / 池深）→ 风格契合（先过哲学导出的选题门，再用三层表的本质逐条问"这个领域能不能兑现"）+ 爆火六力 → 定星 → 五星方向写开工种子包（≥15 条联网爆款实证）→ 选题池、撞题扫描、路线图 → 任务消息。每期标创新档：A 按配方直走 / B 母题创新 / C 形式即内容。

迁移盲测：挑一个 TOP 方向，按主配方写一张纯文字节拍表，**时长按本风格原生时长**（深海类讲解写 30 秒一段；15 秒单段的风格就写 15 秒，不要把拍子放大到段界上），节拍表里旁白按 03 的写稿公式写几句原文，逐项过作者感觉对照：新领域的东西，他会不会就这样拍、这样讲。哪项答不上来 → 回 ② 补配方、旁白写法或作者感觉。

## ⑤ 风格创新：在这个风格上能不能长出新风格

按 `references/style-innovation.md`。目标是**创新之后还有作者的感觉**：新的是做什么、用什么，守的是他怎么想、怎么做。程度 1、2 的哲学和本质一条不动，作者感觉对照五项都要答得出"他会这样做"；程度 3 是有意离开原作者，要写出新的哲学和主配方。三种程度，结论写清是哪一种：

1. **期级创新**：只动每期自由层，或带理由偏离一两条作者默认 → 不是新风格。母题登记进选题 skill「创新档与母题库」的 B 档母题库；偏离作者默认的登记进风格 skill「创新档怎么执行」的允许的偏离（见 ⑥ 表）；C 档每期现场做，不登记。
2. **风格变体**：哲学与本质全保留，换一组作者默认（画布、材质、运动质感、镜头、声音层、旁白的作者默认中的 2–4 项）→ 过五问后立一对变体 skill。
3. **杂交 / 新风格**：改动了某条本质，或把两个风格的本质拼起来 → 必须写得出新的哲学和主配方，再按新风格从 ③ 走起。

每个候选写一张变体卡（保留什么、改什么、为什么、最适合哪些方向、H3 能不能做、按原生时长的节拍盲测），存 `<风格线>\风格量产\_风格创新_变体卡.md`。

## ⑥ 产出 skill

1. 骨架：`h3_skill action=scaffold video=<slug> title=<中文名> source=<风格线路径> skills_source=<风格线路径>\skill`（Kiro / Cursor 里在 `G:\AI\h3-pi-agent` 下：`'{"action":"scaffold","video":"<slug>","title":"<中文名>","source":"<风格线路径>","skills_source":"<风格线路径>/skill"}' | G:\AI\envs\minimax-h3\python.exe bridge\h3_tool.py h3_skill`，先 `$env:PYTHONIOENCODING='utf-8'; $OutputEncoding = New-Object System.Text.UTF8Encoding($false)`——管道带 BOM 时桥会报"Unexpected UTF-8 BOM"）。生成风格 skill `<slug>-style-explainer` + 选题 skill `<slug>-series-planner`（英文名是工具和 Pi 的命名规则，只能小写字母、数字、连字符；中文名写在标题和 description 里），各处留「待填」占位。
   - 见名知意：把两个文件夹改名为 `1_风格skill_<slug>-style-explainer`、`2_选题skill_<slug>-series-planner`（前缀只给人看，工具认 SKILL.md 里的 name，不改 name）。
   - 接到工具上：在 `G:\AI\视频分析` 下跑 `.venv\Scripts\python.exe -X utf8 scripts\link_skills.py`，它给 h3_skill、Cursor、Kiro 建指向实体的链接；`--check` 只查不改。之后 verify / pack / install 照常。风格变体用 `video=<原slug>-<变体短名>`。已有风格 skill、只缺选题 skill：`video=<它 metadata.video> explainer_name=<已有风格 skill 名>`，只生成选题 skill；工具会自动在已有风格 skill 的 metadata 补 `pair`（不动正文），返回 `paired_existing=true` 即成功。
2. 按下表填：

| 报告 / 步骤里的 | 填到 |
|---|---|
| 04 哲学 | 风格 skill「哲学」（一句话 + 3–7 条）+ `style-dna.md`「哲学（证据版）」 |
| 04 主配方、三层表（四维度） | 风格 skill「主配方」「三层表」+ `style-dna.md` 三层表 |
| 04 作者感觉与作者感觉对照 | 风格 skill「作者感觉」+ 自检表最后一条 |
| 01 画布 / 色彩 / 构图读数、04 通用尺子取舍表 | `style-dna.md` Part A（取舍表进 A0；写区间和预算，不写 hex） |
| 02 画面节奏、声画咬合 | `style-dna.md` Part A 画面节奏 / 声画咬合 + `beat-templates.md`（节奏型、拍型）+ 风格 skill「节奏」。读数写明口径：`analyze_reference.py` 的事件、静止、运动占比是 scene_score 口径，产线 `target_*` 是像素口径，不能直接填（`style-foundations` measurement-protocol §8） |
| 02 旁白节奏 + 03 旁白写法 | `narration.md`（旁白节奏、句式、口吻、修辞、结构、从不说的话、写稿公式、逐字样例）+ 风格 skill「旁白写法」 |
| 03 参与层读数（参与类型表、思考留白、命名先后、交还） | `narration.md`「参与」一节 + `beat-templates.md` 的拍型（出题、留白、揭晓各是哪一拍）；本风格的读数写在这里，通用装置写法引用 `participation-design`，不复制 |
| 原片读数怎么翻成 H3 提示词 | `style-dna.md` Part A′（例：原片偶有推镜 → A 线镜头锁死）；旁白的产线写法在 `narration.md` 末节 |
| 代表镜头 / 爆点机制 | `example-aperture.md` / `hit-mechanics.md` |
| ③ 的路线 | 风格 skill「产线路线」与「交付格式」 |
| 04 选题门、④ 的契合判据、领域套件、台账 | 选题 skill `fit-criteria.md`、`domain-kits.md`、SKILL.md 台账 |
| ⑤ 的期级创新 | 选题 skill「创新档与母题库」的 B 档母题库 / 风格 skill「创新档怎么执行」的允许的偏离 |
| ⑤ 每个候选的结论（立 / 暂不立 / 降为期级） | 选题 skill「创新档与母题库」的变体与杂交登记；立了的变体 / 新风格另起一对 skill |

3. 写法：数字注来源片与日期；description 第三人称、写清做什么 + 何时用、≤1024 字符；正文 ≤500 行，细节放 references（一层）；正文不写源库路径，引用写技能名。
4. `h3_skill verify` 0 error 且无「待填」提醒 → `pack` → `install`（覆盖带 `overwrite=true confirmed=true`）→ `verify where=installed`。顺序不能省 pack：`install src=<名>` 先取分发目录里最新的 zip，源库改过没 pack 会装成旧版。
5. **升级模式**（已有 skill）：只改被新测量推翻的条目；差异清单（原文 / 实测 / 证据 / P0–P3）先给用户看，同意后改。版本：改规则、加章节升次位（x.Y.0），只补证据、改错字升末位。往风格 skill「允许的偏离」加一行也算改风格 skill：先给用户看，同意后写，升末位。

## ⑦ 验证与交接

1. 免费行为验证：派一个没看过报告的子代理只读新 skill，为一个种子题写 2 段原稿。
   - A 线：临时系列里 `h3_new_episode storyboard=true` → `h3_storyboard action=style`（新风格 skill 给的本期风格块）→ `h3_storyboard action=set` → `h3_plan_durations dry_run=true`（不扣声贝；首次没有缓存时只回"需真合成"，到此为止，不真跑）。
   - B 线：临时系列里 `h3_new_episode md_path=…`（模式 A）→ `h3_lint`。
   写不出、解析报错、lint 报错的地方，就是 skill 没讲清的地方，回 ⑥ 改。免费步骤只证明原稿可解析、分镜可编译，**不证明 H3 已能画出**；运行时长、动作执行与画面品质保留“待出片验证”。对照普通 MD 创意交接的「因果骨架」「不可丢的动作证据」「动作设计表」（主体起态 / 目标触发 / 可见过程 / 终态继承 / 焦点镜头 / 路线风险），看编译后是否仍有核心过程；这些字段不进入工具 JSON。讲解类用了参与装置时，再查 `participation-design` 通用项和所选装置条件项，不强制改成多章参与式。文章来源另加一条：拿作者写过的一个题改写成一期原稿，和原文并排对照——想法、切入角度、口吻要是他的，长度和顺序要是视频的。再拿写出来的 2 段逐项过作者感觉对照（旁白念出来和原片逐字样例并排看：口吻、句式、先后顺序是不是他的），不是他的做法的地方回 ⑥ 补旁白写法或作者感觉。
2. 真配音、草稿、补偿标定：只在用户同意后做。
3. 交接前再过一遍边界复核清单（`evidence-ledger.md` 第四节）；源事实变过（换片、改切点、改结尾），受影响的结论与样例重核，旧勾选作废。
4. 删临时期；结论写进风格线 `目录说明.md`；给每个方向写任务消息（模板见 `planning-method.md`），交给生产线 `h3-director`。

## Reference Files

- `references/report-outlines.md` — 四份报告（视觉 / 节奏 / 旁白写法 / 风格解构）提纲与必填数、各报告进风格 skill 的哪里、子代理提示词骨架、`目录说明.md` 模板
- `references/evidence-ledger.md` — 证据台账（五遍看法、五类分记、三档状态、结尾四档）、含义对齐确认步、同一组事实投影多条路线、边界复核清单
- `references/planning-method.md` — 通用找方向 / 选题方法：六阶、否决、契合、六力、星级、钩子类型、池深、撞题、种子包 / 路线图 / 任务消息骨架、合规红线
- `references/style-innovation.md` — 风格创新：三种程度、变体生成、杂交、变体卡、五问筛选、立项与验证
