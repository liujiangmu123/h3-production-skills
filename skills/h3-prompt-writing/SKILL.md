---
name: h3-prompt-writing
description: Write and compile MiniMax H3 prompts for T2VA, I2VA, FL2VA, L2VA and Ref2VA. Preserve the official fields and translate a decided creative-animation-treatment handoff into concrete actions, episode style text and transitions without losing its causal mechanism or motion evidence. Use for H3 field grammar, 创意编译, 本期风格块 and segment continuity. A-line Chinese picture lines and visual_en/beat placement belong to h3-storyboard-writing; choosing the idea belongs to creative-animation-treatment; known generation failures belong to h3-production-lessons.
compatibility: Portable to any agent that can read local files — no external API calls, MiniMax Hub tools, or proprietary runtime required. The agents/openai.yaml file only adds optional ChatGPT/Codex UI metadata; it does not restrict the skill to OpenAI agents.
metadata:
  kind: global
  version: "1.7.0"
  source: "github.com/MiniMax-AI/MiniMax-H3/skills/h3-prompt-writing — 官方 Workflow 至 Tips 与 base-en.txt/ref-en.txt 保持原文；本地创意编译及 creative-compile.md 于2026-10-03修订，保留因果骨架与动作证据。配音先行逐句落实见 h3-storyboard-writing"
---

# H3 Prompt Writing

## Workflow

1. Identify the input mode: T2VA, I2VA, FL2VA, L2VA, or full-reference Ref2VA.
2. For base text/keyframe modes, read `references/base-en.txt` and follow its final prompt structure.
3. For full-reference mode, read `references/ref-en.txt` and follow its six-section rewrite format.
4. Preserve the exact field names, section order, labels, and timing notation from the selected guide.

## Base Modes

- T2VA: build the full audiovisual timeline from text.
- I2VA: start from the first frame and develop forward from it.
- FL2VA: describe the continuous path between the first and last frames.
- L2VA: infer a plausible opening and converge to the supplied last frame.

Use `integrated_multimodal_description`, `overall_soundscape`, and `non_diegetic_music` in the order shown in `references/base-en.txt`.

## Full-Reference Mode

Ref2VA rewrites use `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, and `non_diegetic_music` in that order. Reference labels stay consistent across all sections.

Read `references/ref-en.txt` for label rules, retention analysis, and complete examples.

## Output Rules

- Write rewrite sections in English; preserve dialogue, lyrics, and visible scene text in their original language.
- Describe each shot by composition, subjects, environment, actions, camera, sound, and the exact point where referenced content appears.
- Avoid plot summaries, unresolved reference labels, and timing that does not match the requested duration.
## Tips for Better Results
- Always match the total duration of the description to the requested video length (4–15 seconds).
- Keep reference labels consistent (e.g. `<Picture 1>`, `<Video 1>`, `<Audio 1>`) across every section.
- Prefer concrete visual and audio details over abstract words like "cinematic" or "beautiful".
- When using keyframes (I2VA / FL2VA / L2VA), clearly state how the first and/or last frame connects to the timeline.

---

## 本地：创意编译（creative-animation-treatment → H3 提示词）

> 以上为上游原文；以下为本库新增。上游语法与本节冲突时，字段名、顺序、时间写法以上游为准；本库产线约束（镜头锁死、段长、续接、补偿）以 `h3-storyboard-writing` §0 / §3 / §6 / §9 与 `h3-director`「多镜头线出片」为准。

**一句话关系：** `creative-animation-treatment` 决定**想法、路由与转场**；本 skill 把它**编译**成 H3 能执行的英文；A 线的逐句中文画面与 visual_en 落位交 `h3-storyboard-writing`；写完交 `h3-production-lessons` 预检。有了新的创意动画处理，先从交接单重写受影响的段，再检查全片衔接；不要在旧提示词中追加一个效果名就算完成。全库调用顺序见工作区文档 `G:\AI\视频分析\skill\_skill关系图.md`（文档，不是 skill）。

**编译保真：** 锁定风格与用户选择 → 因果骨架 → 不可丢的动作证据 → 真实产线约束 → 英文措辞。把“接触后沿纤维渗开”写成“瞬间变黑”，即使语法正确，也丢掉了创意。工具装不下时指出具体冲突，交回 treatment 调整动作跨度或制作路线；不要悄悄改成图标出现、统一弹出或逐句配图。

### 分工（不重叠）

| 问题 | 归谁 |
|---|---|
| 这段做成什么样子、用哪种转场、哪层做 | creative-animation-treatment |
| 把交接单变成 H3 句式：保住动作证据、写清适用的世界信息、本期风格块英文全文、长效果分段与段间交接 | **本 skill** |
| H3 字段语法（三字段、[Shot N]、运镜三维、Ref2VA 六节） | **本 skill**（上游原文） |
| A 线：原稿中文画面 §0、visual_en / beats / until / still 落位、风格块怎么设进工具（action=style、运动模式、补偿、目标键）、时间码拼装 | h3-storyboard-writing |
| 某种写法 H3 以前画错过、该怎么改 | h3-production-lessons |
| 旁白、钩子、配色推导 | 风格 skill |
| 观众在哪一刻做什么（等待物、留白、揭晓、命名的位置） | participation-design 定，经交接单「参与位」带进来；编译时当固定约束 |

**具体描述原则：** 本地产线把 `h3_timecode` 拼好的文本直接送进 H3-Base。写清观众需要看见的主体、空间关系、材料、动作过程和结果；§7 的八槽是适用信息检查，不是加景物或凑词数的配额。简洁风格照样可以有清楚的因果与有力的运动，不能靠堆世界细节替代动画设计。

### 编译八步（细则、模板与示例在 [references/creative-compile.md](references/creative-compile.md)）

1. **收单**：读创意交接单（creative-compile.md §1），先提取「因果骨架」「不可丢的动作证据」「动作设计表」。旧单可从内动词、中文画面与动量链提取，无法确定的核心动作退回 treatment；无住户、无活层、无转场是合法选择。缺非核心装饰不阻断简单任务，也不自己补想法。
2. **分线**：A 线（配音先行时间码）→ 产出逐拍"编译稿"交 `h3-storyboard-writing` 落位；B 线（多镜头 T2VA）→ 直接产出整段三字段。
3. **剥层**：路由给代码层的字、数、遮罩、冲击帧，从 H3 文本里删掉，只写 H3 要生成的空间与状态（P-003：提到的名词会出现）。代码层事件留在交接表，未实现、未装配时标为待办，不能当已经画出来。
4. **写清状态**：按八槽检查适用信息（§7.1）。A 线共用的风格、媒介与身份进本期风格块；随剧情变化的位置、姿态、明暗进对应事件与段首状态。B 线进 `[Shot 1]` 与每镜的空间锚。不强加住户、景深层、颗粒或活层。
5. **词译**：将动作表译成**起态 / 触发 → 可见过程 → 终态 / 反应 → 保持**。瞬变只用于结果本来就是瞬变的动作；因果靠过程成立的动作保留路径、速度关系与材料反应，A 线给 `until`。效果名要落成可见动作，风格名与真实光源照常保留；详见 §2、§7.2。
6. **转场编译**：转场清单逐行套模板（creative-compile.md §3；手法卡与 H3 落法见 `creative-animation-treatment/references/transitions.md`）。A 线只用画内转译；B 线用 `[Shot N] At …, the camera cuts to …` 并写画内原因与跨场锚。
7. **切段与衔接**：在动作允许的稳定中间态切开；跨句不停的长动作先查 A 线 `until` 与句尾保持的限制（`h3-storyboard-writing/references/animation-intent.md`）。段 ≥2 首拍点名上一段终态，新事件晚于首事件下限；续接重放头不能承载新动作，揭晓安排在重放之后（§4、§7.3）。
8. **保真复核**：把动作证据逐条指向编译稿中的具体句：谁触发、怎么变化、旧物怎样留在结果里、下一拍承接什么。停顿、迟到、首次上色与招牌动作按交接位置保留，不额外强加前一拍 still。再过 §6 与 §7.6，交 production-lessons。

### 产出格式

- **B 线**：`### 第 N 段 · 标题（T2VA，秒数s）` + 一个代码块（三字段，按 base-en §2）。
- **A 线**：先交**本期风格块**（现有六个文本键英文全文，按 §7.1 适用项），再交编译稿表 `句序 · 原句 · 中文画面 · visual_en 草案 · until · sfx_en · still · 转场编号 · 代码层事件` 与简短「动作证据 → 对应句」对照。交 `h3-storyboard-writing` §1–7 落位；这些说明是交接文本，不是新增工具字段；时间码由 `h3_timecode` 生成，本 skill 不写秒。
