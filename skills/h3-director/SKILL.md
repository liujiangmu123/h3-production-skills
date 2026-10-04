---
name: h3-director
description: 生产线导演（H3 视频量产，Pi 工具版）。用户给选题 / 原稿 / 口令要拍某一期时用本技能：配音先行四步（分镜→MiniMax 配音反推段长→时间码提示词→渲染质检）或多镜头线（模式 A 整段提示词）→验收迭代→768→2K→交付。涵盖开工清单、人工停点、档位决策、级联语义、验收双模式、风格包路由、素材库直连、多期管理。学新视频、找方向选题、创新风格不在这里（那是 h3-research-director）。
metadata:
  kind: core
  version: "1.6.0"
---

# H3 导演手册（Pi 工具版）

> **工作室两条线**：研发线 `h3-research-director`（学风格 → 找方向选题 → 创新风格 → 产出风格 skill 与任务消息）；**生产线 = 本技能**（拿到选题 / 任务消息后，一期一期出片）。生产线用到的：风格 skill `<风格>-style-explainer`（写稿：哲学、画面、节奏、旁白写法、作者感觉、产线路线；方向选题在它配对的选题 skill `<风格>-series-planner`）、`h3-storyboard-writing`（配音先行线的分镜、本期风格块怎么设、时间码规则）、`h3-prompt-writing`（官方字段语法 + 本地创意编译：多镜头线整段提示词、A 线所需风格与动作信息）、`h3-production-lessons`（H3 画错过的写法）、`creative-animation-treatment`（写稿前的动画设计及已有稿的动作审查，按需要用整片或局部模式）、`participation-design`（参与式期的拍表）。

> 全链路口径：`G:\AI\H3动画量产_AI总指导.md`（§4 写稿与原稿格式、§8 档位/步数/耗时、§9 改词后从段 1 重建、§10 2K、§13 已知问题、§15 每期清单）；为什么这么定看 `G:\AI\H3_测试与提速记录.md`。

> 你是导演。工具是你的手：42 个 h3_* 工具 + 技能库。用户只说话，你排一切。
> **铁律：H3 任务一律调 h3_* 工具，禁止 bash/curl 直连 ComfyUI、禁止手改 JSON。**
> **铁律二：配音定时钟，画面跟时间码，字幕不在本流程生成（用户后期语音转文字）。H3 不听音频、不说话、不画字幕。**
> **定稿配置（2026-09-27 实测）**：Turbo v1.1 6 步出 draft/768（1344×768 = 1MP）→ 2K 走 3D latent 超分 ×2 + H3 逐块 1 步重绘细节（不用像素超分，RTX VSR 已放弃；2K 超分词由产线自动取本段原提示词，`upscale.prompt_source=segment`，**不要另写 2K 提示词**）；补偿缺省 +0.2（本机 ComfyUI 0.37.4 上偏早，新风格线第一期两段草稿定一次，`h3-storyboard-writing` §6）；改词/改段长一律从段 1 作废重建。耗时：768 ≈ 42+0.0029·F² 秒/段、2K ≈ 35+0.66·F 秒/段（F=渲染帧数；12 秒续接段实测 768 4.9 + 2K 3.9 分钟；150 秒成片约 1.9 小时；前提 ComfyUI 0.37.4 + int8 VAE + `--reserve-vram 5 --vram-headroom 2`，`run_h3.bat` 已设，变慢先查 `http://127.0.0.1:8188/system_stats` 的版本与 argv；12 秒段的 2K 超过 8 分钟多半是显存溢出，让用户关掉占显存的程序）。段长常用 12 秒左右，12 秒以内每秒成本几乎一样，15 秒起变贵。
> **配音只用 MiniMax 网页（Credible Alex，扣声贝）**；登录过期要用户扫码（`h3_voices action=web_login`），这是除验收外唯一需要人手的环节。字幕、BGM 都不生成，用户后期自己做；要 1080 就出 2K 后缩放（总指导 §12）。

## 人工停点（只有这几处停下来等用户，其余一路推进）

| 停点 | 为什么 | 你做什么 |
|---|---|---|
| 原稿写完 | 词和段长在草稿阶段定死，768 开跑后改一个字 = 全部重跑 | 把原稿给用户过目，得到"可以"再建期 |
| `h3_plan_durations` 真跑前 | 首次合成扣声贝；有产物时会级联作废 | 报 dry_run 的段长表（或"需真合成"）+ 作废范围，得到同意 |
| 每个 `h3_batch` 真跑前 | 占 GPU（12 秒段 768 约 5 分钟/段） | 报 dry_run 的段数与 ETA，得到同意再 `confirmed=true` |
| 验收 | F1：只有用户说"段 N 过 / 全部过"才 `h3_approve segment_index=N confirmed=true note="用户原话"` | 给粗剪路径和 align/seam 结果，等口令 |
| 会作废产物的落盘 | 改词/改段长/重摇 768 | 复述"将作废…"，同意后 `confirmed=true` |
| MiniMax 登录失效 | 要扫码 | `h3_voices action=web_login`，请用户扫码 |
| 原稿句末有停顿标记 `<#秒#>` | 配音层会剪掉句末静音、标记还会进字幕（总指导 §13 第 10 条，未修） | 修好前不真跑 `h3_plan_durations` / `h3_narrate`；分镜写完就停，告诉用户在等修复 |

用户说"一路跑完 / 跑完叫我"时，停点合并成一次确认：先把后面要跑的全部档位、段数、ETA 一次报清，同意后按序跑，只在失败或验收时停。

## 开工检查（每次会话第一件事）

1. `h3_doctor`（新机器 / 久未用 / 报错时）—— 逐项红绿，红项带修复命令（ComfyUI、模板、模型等）；MiniMax 配音服务与登录态用 `h3_voices action=status` 查。
2. `h3_status` —— 引擎在线才生成；离线就告诉用户先开 ComfyUI（8188，`run_h3.bat`）。
3. `h3_list_episodes` —— 多期盘点（每期三档进度+验收数）；用户没指名时用它找期。
4. `h3_get_wall` —— 看当前期进度（project 参数直接传期名）。
5. 渲染前 `h3_pipeline_get` 核一次定稿配置：`tiers.draft.steps` / `tiers.768.steps` = 6、视频 VAE = int8_convrot、2K 超分词来源 = 每段自动（segment）。不对先告诉用户，别直接改（改步数 = 该档从段 1 重跑）。
6. 写任何字之前（包括写原稿的中文画面）：`h3_get_skill("h3-storyboard-writing")`（§0 中文画面约束 + 分镜英文写法）+ 风格包；`h3_get_narration` 读旁白。

## 主流程：选题 → 动画设计 → 写稿 → 配音先行四步（新期默认，docs/26、docs/27）

建期前完成所需**写字的活**（技能，不动 GPU）：没有 MD 先选题、设计、写稿；已有 MD 先检查动画设计与可编译性，再补缺件：
- **0 选题**：`h3_get_skill("<系列配对里的选题 skill>")`（`h3_series action=get` 看 style；缺省 `shenhai-series-planner`）——找方向 → 评级 → 开工种子包 → 选题池 → 任务消息，产物写到系列根 `_选题/`；已有选题库直接 `h3_library` 挑一期（工作区是系列文件夹时它列的就是 `<根>/_原稿/`）。
- **0.5 动画设计**：先读风格包锁定已有规则。新片写中文画面前、已有稿需要动画化，或用户反馈“中等 / 像幻灯片 / 不连贯 / 没创意”时，`h3_get_skill("creative-animation-treatment")`：常规期也做所需的局部设计与动作审查，C 档才需要整片形式发明，不由 A/B/C 决定是否读创意技能。风格要求或用户要求参与时，先读 `participation-design` 出所需参与拍表，再交给动画设计。
  创意交接的普通 MD 保留「因果骨架」「不可丢的动作证据」「动作设计表」（主体起态 / 目标触发 / 可见过程 / 终态继承 / 焦点镜头 / 路线风险），附在原稿的独立章，**不塞进工具 JSON，也不放进解析器的 ② 章**。先决定观众看见哪个变化、为何发生、留下什么给下一拍，再写句子。
- **1 写稿**：`h3_get_skill("<系列配对里的风格 skill>")`（缺省 `shenhai-style-explainer`；它写着多镜头线的，改走下文「多镜头线出片」）+ `h3_get_skill("h3-storyboard-writing")` + `h3_get_skill("h3-production-lessons")`（按本期物件和动作查已测范围），一起用：旁白听风格 skill，中文画面按动画设计交接展开，同时守 storyboard-writing §0 的可编译要求。固定机位、瞬现、冻结与事件预算按所选风格和本期运动块决定；深海默认块不推广为通用美学。补英文是编译，需保住关键动作的过程、起停、反应和终态，不能把它们统一译成 appears instantly（F-006）。
  出 md 原稿写到 `<根>/_原稿/第NNN期_题名.md`：分段旁白（一句一行）+ 每句中文画面描述 + 动作旁的音效；**不写秒、不写段长**（时长由配音反推）。字数按**目标秒数 × 3.5**（150 秒 ≈ 550 字；参考片的 ×5 会写长 30%）。格式必须是总指导 §4.3：`## ② 长版旁白时间轴` / `【第 N 段 | … | 拍型：…】` / `整句 → 视觉：中文画面`；画面该静止的句子写 `→ 视觉：（静止）`，建期后自动标 still。旧格式原稿先按 `h3-storyboard-writing` 转换节改好再建期。
  写完按风格 skill 自检与**作者感觉对照**过一遍：想法 / 画面 / 节奏 / 旁白 / 声音逐项问“作者本人会不会这样做”。创新 B/C 新的是内容，做法、分寸、口吻仍听已锁定风格；某项不像，先改做法，不砍点子。参与拍表不抢答，配音实测后可在保持参与目的与次序的前提下调位置。风格 skill 的「产线路线」写着 A + B 混排、歌先行或代码层的，看下文「混合路线」。
"配音先行"指配音先于**画面生成**（配音定时钟），不是先于选题写稿。

**系列 = 一个文件夹**（工作区任选，见导则"当前系列"行）：根下 `系列.json` 记作者 / 系列名 / 风格配对 / 默认声线 / 下一期号，`_选题/ _原稿/ _素材/` 三个子目录放写字阶段的产物，期目录与它们并列。新文件夹第一次用先问清作者、系列名、风格，`h3_series action=init`（`h3_new_episode` 不传 parent 也会自动建，缺省作者"设计师深海"、系列名=文件夹名、风格配对=深海那对；新风格的系列要在 init 时写明 style 配对：风格 skill + 选题 skill 的名字）；`h3_series action=get/set` 看改。有清单时 `h3_new_episode` 的 author/domain/version 缺省取清单，期名没有 `第NNN期_` 前缀会按下一期号自动补；声线顺序：期 `配音/voice.json` > 系列 `tts.voice` > 全局。

```
① 选题 → 分镜：h3_library 选题或用户给 MD → h3_new_episode 模式 C（分镜建期）
      触发：storyboard=true；或不给 storyboard 时自动——给了 narration 纯文本 / MD 只有 ② 旁白章没有 ③ 提示词章
      （MD 同时有 ②③ 章想走时间码法必须显式 storyboard=true，否则落到模式 A；storyboard 与 segments 词表互斥）
      建出 分镜_长版.json（旁白句 + 每句中文画面描述 visual_zh，不写秒）+ 旁白脚本_长版.txt（一句一行）+ 占位快照
      **快照里是占位词（"Placeholder — pending h3_timecode"）+ 字数估算段长，不能拿去渲染**——真词由 h3_timecode 写、真段长由 h3_plan_durations 反推
      → h3_storyboard action=style 设本期风格块（写法按 h3-storyboard-writing §6：档位 / 画布 / 强调色按 交接单 → 原稿 ① 章或任务消息 → 风格 skill 推导法 的顺序取，英文按 h3-prompt-writing 创意编译 §7 补所需信息，不按八槽数量凑角色/景物/活层；有住户或过程时核对 no_voice_en / hold_en / closing_en / sound_suffix 是否冲突。不设就是默认深海米白+印章红，只适合采用该默认的符号期）
      → h3_storyboard action=set 逐句补英文画面 visual_en（动作短语）与音效 sfx_en；一句多拍用 beats=[{at,until?,visual_en,sfx_en?}]；
        这句画面该静止就 still=true（不写画面、不出时间码）；写法按 h3-storyboard-writing
      逐笔描画/渐变这类长动作必须给 until（→ "finishing by"），否则 H3 会一直做下去把后面的事件全推迟
      → h3_storyboard action=view 确认"缺英文画面 0 句"
② 旁白 → 音频 → 段长：h3_plan_durations（dry_run 先看表）
      MiniMax 首次没有缓存时 dry_run 只会说"需真合成"（不扣费）——向用户说明会扣声贝，同意后真跑，别跳去 h3_timecode
      TTS 原速试算每段语音长度，段长 = grid(speech + gapSegment) 写回快照，再真跑配音出 wav / timing.json / srt
      真跑后逐段看 fit：ok / tight 正常；compressed / stretched / overflow = 段长没跟上，重跑 h3_plan_durations，不压配音
③ 时间码提示词 → 渲染 → 质检：h3_timecode preview=true 看词 → 落盘（门禁见下）
      → h3_batch tier="draft" → h3_align（帧差动作起点 vs 时间码；中位 ≤0.2s、单点 ≤0.3s 过）
      超差：先看 h3_align 有没有给 suggest_compensation_s，再决定改补偿量还是改分镜那一拍（见「质检迭代」）
④ 装配：看片用 h3_assemble mode="rough"（缺省 audio=mix：配音主轨 + H3 音效）；交付用 h3_deliver tier="2k"（缺省 audio=narration；subtitles 默认 none，不烧字幕）。h3_assemble 不写 mode 是 delivery（要全段 2K + 全验收）
```

**②③ 落盘门禁（三道，口径相同）**：扩展 `index.ts` 的 `CONFIRM_POLICY` 集中策略表在 `tool_call` 上先拦，工具内 `guardCascade` 再拦，桥层 `_require_cascade_confirmed` 兜底（直调桥 CLI 也拦）。三层都是——
**会作废产物（草稿/正片、2K、已验收）才要 `confirmed=true`；当前无产物直接放行，不必 confirmed**。
所以建期阶段 ①②③ 一路走下来不需要任何确认；一旦出过片，落盘前先跑 `h3_plan_durations dry_run=true` / `h3_timecode preview=true`，
返回里会明说"真跑将作废：草稿/正片 段…、2K 段…、撤销验收 段…"和下一步（"带 confirmed=true" 或 "无产物，不必 confirmed"）——
**先看这句，再照它向用户复述范围**，用户同意后才带 `confirmed=true`。没带就调会被拒并附范围（不是 bug，是提醒你先复述）。
注意 `h3_plan_durations` 和 `h3_timecode` 的守卫都按"从段 1 起"算范围（不管传了哪些 segments；冻结指纹覆盖全片），只要期里有产物就要 confirmed。
`h3_storyboard` 也在门禁里，但**只有 `action="init"` + `overwrite=true` 要 `confirmed=true`**（重建分镜会把手填的英文画面/音效和旁白 txt 覆盖掉）；`view / set / style` 与不覆盖的 init 是纯增量，随便调。
**被拒时先读拒绝理由再决定动作**：说"期不存在 / 期名匹配多个"的是期参数写错了，去 `h3_list_episodes` 查期名，**别加 `confirmed` 重试**（门禁对期名解析失败一律放行，所以这条错是工具给的真错，不是确认问题）。

**version=抖音版**：`h3_plan_durations` / `h3_timecode` 只能 `dry_run=true` / `preview=true`——定稿快照只有长版一份，抖音版写进去会把长版顶掉，工具会拒。落盘只认长版；抖音版要配音走 `h3_narrate`。

**质检迭代（h3_align 之后怎么走）**：
- 先判问题在哪一层：因果/演出设计不成立 → 回 `creative-animation-treatment` 改动作结构；交接有过程而词里只剩出现/消失 → 修编译；设计和词都清楚而 H3 未执行 → 查经验库、改可控实现；只有时机偏移 → 校准；持续活层/细线导致帧差误判 → 人看动作证据。不要把每种失败都归为补偿或换种子。
- 对照原稿 MD 的三项交接：不可丢的动作是否看得见，起态→过程→终态是否完整，上拍的结果是否被下拍继承。用户说“动画中等”时先改这一层，不能只加修饰词、音效或装饰凑读数（F-007）。
- 有 `suggest_compensation_s` 且核看片段确有系统性偏移 → `h3_storyboard action=style style={"compensation_s": …}` → `h3_timecode` 重写（有产物带 confirmed，落盘从段 1 起作废全部草稿/正片——冻结指纹覆盖全片，只重跑变动段必被引擎拦）→ `h3_batch tier="draft"` 从段 1 重建 → 再 `h3_align`。活层、错误匹配或旧段长片干扰时不直接应用建议。
- **fail/check 但没给 suggest** → 先查匹配和画面，不代表已排除补偿问题：
  - 有“未检到动作”：看片判断未执行、太轻或连续运动让起点漏测；确认未执行才改可控动作/终点/相邻拍，`h3_timecode` 落盘后按作废范围重建；测量漏检保留人工动作证据，不为检测强行改设计。
  - 全部匹配且核看设计/执行正常，仅离散偏差：可同 seed 重跑该段一次查复现，`h3_reroll segment_index=N tier="draft"`（只作废旧 take、撤销该段验收，不渲染）→ `h3_generate tier="draft" segment_index=N`；复现后按原因处理，不循环同种子重摇。
- **"同 seed 重跑"两种写法，按词有没有改选**：段 seed 由段号派生，两条路都不换种子。
  - 词改过（`h3_timecode` 落盘级联，该段草稿已作废）→ `h3_batch tier="draft"`，它只补缺草稿的段，天然就是"只重跑改过的段"。`h3_batch` 的 Pi 工具**没有 `segments` 参数**（只有 tier / dry_run / confirmed / detach / max_segments / max_retries / project），`h3_batch … segments=[N]` 一律是错写法——要指定单段只能走 `h3_reroll` / `h3_generate`。
  - 词没变、草稿还在（`h3_batch` 会跳过它）→ `h3_reroll segment_index=N tier="draft"` → `h3_generate tier="draft" segment_index=N`；`seed` 缺省保留原种子（画面可能不变），要换画面才显式给 `seed`。
- 每段可能带 warning **"试片 …s 与当前段长 …s 不符——这片是旧段长出的"**：说明这条试片是改段长前渲染的，时间码对不上是必然的，**先重跑草稿再看**，不要据它改补偿量。
- `h3_align` 缺省取 2k→768→draft 首个**未作废**的 take；指定 `tier` 时会连作废档一起查，结果只供参考（advice 里会标）。

**写拍的约束（h3_storyboard action=set / h3_timecode 会校验）**：
- 写入时间 = 句起点 + at×句长 + compensation_s(默认 +0.2，配锁死/瞬现式 motion_rule；渐进描画类风格约 −0.5)，段 ≥2 再加 continuation_head_s 0.917，带 until 的拍再加 until_lead_s（缺省 0，`h3-storyboard-writing` §6），且**不早于 head + min_first_s(0.3)**：
  段 1 首事件下限 0.3s；段 ≥2 首事件下限 0.917+0.3 = **1.217s**。句首动作靠前的要接受这个下限，或与下一拍合并——
  两拍被抬平到同一时间码时 h3_timecode 会 warning"合并成一拍或把 at 往后挪"。
- `beats` **不要给空表 `[]`**——空表和缺省一样走单拍路径，此时 `visual_en` 为空会被拒（"visual_en 不能为空……要写多拍请给非空 beats"）；走单拍就直接给 `visual_en`。
- `at ∈ [0,1)`、`until ∈ (at,1]`，越界被拒。`until` **不要晚于下一拍起点**——会 warning"H3 可能把两拍并成一个动作"，要么缩 until 要么把下一拍 at 往后挪。
- 快照段长与配音 target 差 >0.05s 时 h3_timecode 视同 lint error 拒写（"先重跑 h3_plan_durations"），`force=true` 才放行——别用 force 绕，段长没跟上就回②。
- **时间码 ≥ 段长是 error（`timecode_past_end`），不是提醒**：那一拍根本不在片子里（`head_s` / 补偿量写错，或段长换了没重算），落盘会被拒、`preview` 进 `lint_blocked`。只有"最后一拍离段尾不足 0.5s"（`timecode_overflow`）才是 warn，可以放过。两者互斥，同一段不会同时出现。
- `h3_timecode preview=true` 的返回里，没过的质检项是逐条 `✗` 行——**照着 `✗` 改分镜英文（`h3_storyboard action=set`）再 preview**，不要直接 `force`。带了 `force` 时头行会写"落盘会照写"，那是最后手段。
- 段长必须在 **0.2~60 秒**内（引擎硬区间）。`h3_plan_durations` 反推越界时真跑会在**写任何文件之前**拒掉（返回 `out_of_range` 段号，没有 .bak、没有级联），`dry_run` 只给 warning——办法是把那段旁白拆成两段（`h3_storyboard action=init` 重切）或改短旁白。

**占位词会被拒**：分镜建期后、`h3_timecode` 落盘前，快照里每段都是 `Placeholder — pending h3_timecode`。这时 `h3_batch`（**连 dry_run 也拦**）、`h3_generate`、`h3_reroll` 会直接报"段 … 的提示词还是占位词……先 h3_timecode preview=true 看词、落盘后再渲染"，`h3_production_plan` 出 blocker。这不是引擎故障，是守卫——回到 ③ 把词落盘（有产物带 confirmed），不要换段号、换档位重试。

**桌面用户的对应操作（pi-desktop 段墙面板「配音先行」页签，只对时间码法的期出现）**：用户在面板点的按钮分两类——直连只读探测（毫秒级、不经你）和"交给 Agent"（会以指令形式发到会话里，由你执行）。你收到的指令文案是面板生成的，照它做即可：
- 三环没走完时，状态头与动作条主按钮显示当前环节（⓪ 分镜 / ① 段长与配音 / ② 时间码词），点击跳到该页，不会出现"批量草稿"。
- ⓪ 分镜卡：缺英文画面的句子列表；**「让 AI 补 N 句英文画面」→ 发给你**（文案要求你先 `h3_get_skill` 拿写词技能与风格包，再 `h3_storyboard action="set" items=[…]` 批量补，补完报 `action="view"` 的缺口数）。面板 `fs.watch` 监听 `分镜_*.json`，你每写一句用户立刻看到。
- ① 段长与配音卡：「试算段长」直连 `h3_plan_durations dry_run=true`（用户已经看过段长表与"真跑将作废…"）；**「交给 Agent 真跑段长 + 配音」→ 发给你**，文案里已带作废范围——仍按门禁复述一次，用户同意再 `confirmed=true` 真跑。
- ② 时间码词卡：「预览词」直连 `h3_timecode preview=true`（用户可临时填补偿量只看效果，不写分镜）；`✗` 行是 lint error；**「交给 Agent 落盘时间码」→ 发给你**，有 `lint_blocked` 时文案会写"先改分镜那几拍，别用 force 绕"。
- ③ 音画对齐卡：「跑质检」直连 `h3_align`；**「应用建议补偿」直接写分镜 `style.compensation_s`（纯文本，不经你，不作废产物）**——之后用户通常会点「交给 Agent 按质检结果修」，你按「质检迭代」一节走：有建议就 `h3_timecode` 重写（复述范围 + confirmed）→ `h3_batch tier="draft"` 补作废段 → `h3_align`；没建议且有未匹配事件就改分镜那一拍；都没有就 `h3_reroll` 同 seed 重跑一次。
- 面板直连**没有**真跑段长、落盘时间码、渲染这三个动作——凡是会级联作废产物或上 GPU 的，一律经你，门禁照旧。

之后：验收（用户说「段N过」→ h3_approve segment_index=N confirmed=true）→ h3_batch tier="768"（全部段；此后词与段长不再改，抽查 h3_align / h3_seam_check）→ h3_batch tier="2k"（全部 768 通过后再批量，逐段 1→N；**两者之间不要清 ComfyUI `input\`**，768 latent 只在那里）→ h3_deliver tier="2k" → ffprobe 核"视频时长 = 配音时长" → h3_archive。草稿档可选：新风格/新题材先跑草稿定节奏和补偿，风格成熟直接 768。

**任何阶段用户想"看看整体"** → `h3_assemble mode="rough"`（见下节），不必等全片跑完。

### 兼容旧期（MD ③ 章直出提示词）

老期的 MD 自带「分段提示词」章节：`h3_new_episode(md_path)` 模式 A 直接建快照，`h3_narrate` 配音，改词走 `h3_write_segment` / 对照层。这条路仍可用，但**配音先行风格（深海）的新期不要走**——旧词让 H3 自己念 `<d>` 台词并画字幕条，配音后画面必然对不上（docs/26「为什么要换」）。多镜头线的新期正是走模式 A，见下一节。

## 多镜头线出片（风格 skill 写着「产线归属：不是配音先行」的，如诗词长卷、木刻拼贴）

这类风格的朗诵、字幕、配乐是提示词里的设计，画面跟诗句 / 音乐走，不跟外配旁白走。**不用** `h3_storyboard` / `h3_plan_durations` / `h3_timecode` / `h3_align` / `h3_narrate`。

1. **写稿**：`h3_get_skill("<风格 skill>")` + `h3_get_skill("h3-prompt-writing")`（官方字段语法；有创意交接单时照它的「本地：创意编译」）+ `h3_get_skill("h3-production-lessons")`。原稿写到 `<根>/_原稿/第NNN期_题名.md`，格式：
   ````markdown
   ## 长版 · H3 分段提示词

   ### 第 1 段 · 起势（T2VA，12s）
   ```
   integrated_multimodal_description: …
   overall_soundscape: …
   non_diegetic_music: …
   ```
   ````
   解析器（`workbench_core.parse_segments`）只认这几条，写稿前看一遍：
   - **章**：`##` 级、标题含「分段提示词」（含「抖音」的是抖音版，否则长版）；下一个 `##` 标题就是章尾。
   - **章内只放三样**：段头 `### 第 N 段 · 标题（T2VA，秒数s）`（N 从 1 连续）、段头后的**第一个**代码块（= 这段提示词，三字段原样送 H3）、`>` 引用行（进段备注）。分镜表、朗诵稿、拼装说明、查证放别的 `##` 章：放在章内不报错，但每段只取第一个代码块，排在提示词前面的说明块会被当成提示词，后面的被静默丢掉。
   - **秒数**：建议 4–15（引擎硬区间 0.2–60），可写小数（`10.5s`）。建期**向上**吸附到 17k+5 帧 @24fps（12s → 12.25s，15s → 15.083s，`h3_lint` 的 `grid_snap` 会报）。提示词里最后一个 `At MM:SS.mmm` 按写的秒数算（不按吸附后的）：离段尾不足 0.5 s 是 warn，到或超过段尾是 error。
   - **段 ≥2 的开头是重放**：段 N（N ≥2）从段 N−1 的末 22 帧（0.917 s）续写，这 0.917 s 在组装时剥掉，画面和声音都不留。所以段 ≥2 的 `[Shot 1]` 写"上一段最后一镜的延续"（同主体、同景别、同光，动作接着走），换景 / 新镜头 / 新的一句朗诵从 `At 00:01.217` 起；段内时间码从重放头算起。风格 skill 若写"每组 [Shot 1] 开新景、时间从 00:00.000 起"，风格声明句照写，新景顺延到 `[Shot 2]`。
   - 只做 T2VA：段间走 latent 续接，不能用 `<Picture N>`。
2. **建期**：`h3_new_episode md_path=…`（不带 storyboard，自动走模式 A）→ `h3_lint`（全期）。这条线的 `<d>` 朗诵、画面字幕、voice-over 是风格设计，`dialogue_tag` / `subtitle_bar` / `no_voice_missing` / `narration_in_prompt` 这几条提醒向用户说明后可以不改；error 级照样要改。**风格 skill 里的旧样例和工具规则冲突时以工具为准**：样例里有 `<Picture N>`、`near-silent`（改写成具体的低响度环境声，如 faint wind over the reeds）、段 ≥2 开头就换景的，照上面改，不照抄样例。
3. **出片**：`h3_batch tier="draft" dry_run=true` → 用户同意 → 跑 → `h3_assemble mode="rough" audio="segment"`（听 H3 自己的朗诵和配乐）→ 用户验收 → `h3_batch tier="768"` → `h3_batch tier="2k"` → **`h3_deliver tier="2k" audio="segment"`**（缺省的 narration 会找外配旁白，找不到就出无声片）→ `h3_archive`。
4. **注意**：段间续接按第 1 步"段 ≥2 的开头是重放"写。这条线在 H3-pi-agent 里**还没做过端到端实测**：第一期先只跑前两段草稿，看段间衔接和朗诵音质，再决定整期。用户自带配音时按风格 skill 里的"配音卡点"写，仍是模式 A。

### 混合路线（风格 skill 的「产线路线」写着 A + B、歌先行或代码层时）

以风格 skill 的「产线路线」为准，这里只写怎么落到工具上。**一期只有一种建期模式**（模式 A 整段词表 / 模式 C 分镜），工具不支持一期里混用。
- **A 线主体 + B 线插段**（如冷开场、蒙太奇脉冲）：主体按主流程建一期；插段按「多镜头线出片」另建一期（同系列文件夹，期名标"插段"）；两期各自出片、交付。跨期拼接没有工具：把两期成片路径和插入位置（主体第几段后）交给用户在剪辑软件里拼。
- **B 线 + 歌先行**（画面跟歌词走）：按「多镜头线出片」；段长和段内 `At` 按歌词时间手写（`h3_lint` 照样查 `timecode_order` / `timecode_past_end` / `grid_snap`）；交付 `audio="segment"`，歌曲由用户后期铺。想先对着歌看节奏，可试 `h3_assemble mode="rough" audio="mix" narration_wav=<歌曲 wav>`（没实测过，先跟用户说明）。
- **字幕版、无旁白**（字幕当旁白句，配音只当时钟）：按主流程；交付 `h3_deliver tier="2k" audio="segment" subtitles="burn"`。原稿有句末停顿标记的，先看人工停点表最后一行。
- **代码层**（会被观众读的字、数、仪表、公式、外框）：H3 那句写（静止）或只写留空区的光；代码层没有承接 skill，Remotion / HyperFrames 的 Node 依赖也没装（装要联网，先问用户）。交付时告诉用户哪几处的字要后期叠。

### 老期迁到时间码法

已经建好（甚至出过片）的模式 A 老期也能切到配音先行，步骤：

1. `h3_storyboard action=init md_path=<原稿 MD>`（原稿在 `<期>/原稿/`）——解析 ② 旁白章拿到全部段/句/visual_zh，建 分镜_长版.json。纯文本、不碰快照与段墙，零代价。
   没有 MD 时不给 md_path 也行：init 会兜底回读 `旁白脚本_长版.txt`（只有句子，没有 visual_zh）。分镜已存在要重建带 `overwrite=true` + `confirmed=true`（已填的英文拍会丢，先向用户说明；留 .bak + 回退点）。
2. 人工只补 `visual_en` / `sfx_en` / `until`（`h3_storyboard action=set`；中文画面 visual_zh 已从 MD 带过来）。
3. `h3_plan_durations dry_run=true` 看段长变化表：老期段长是手填的，几乎每段都会变。
4. **真跑的代价**：会改全部变动段的段长并从段 1 起级联——等于**作废该期所有草稿/正片/2K 与验收**
   （例：001 期 16 段，段 1/2 已有 768 + 2K、段 1 已验收 → 段 1/2 的 768 与 2K、段 1 验收全废）。
   dry_run 返回里的"真跑将作废：…"就是这份清单——**必须先向用户逐项复述代价并得到明确同意，再带 `confirmed=true` 真跑**。之后 `h3_timecode preview=true` → 落盘（同样要 confirmed）→ 重跑草稿。
5. 后悔：段长与词都各存了回退点（`plan_durations` / `timecode_seg…`），`h3_undo action="list"` 能回。

## 粗剪：看整片节奏的唯一手段

逐段看片看不出整片顺不顺——旁白铺满 4 分钟，画面只出了 3 段，导演最想知道的"整体感觉"恰恰看不到。

```
h3_assemble mode="rough"
```

它做的事：按**剧本全长**拼一条片子——每段取当前最佳可用档（2k>768>draft），还没生成的段放
**等长占位板**（写着段号与时长）。占位板时长严格等于脚本时长，所以**旁白全程对得上**，
你能听着完整旁白看现有画面，直接听出哪段跟不上、哪段时长不对。

- **哪怕只出了 1 段也能出全长片子**，随时可跑，不需要验收、不需要引擎在线
- 音轨默认 `mix` = 旁白 + 段内音效/配乐（H3 出片自带音效，这样一起听）
- 默认在角上烧「段号·档位·时长」，边看边记哪段要改
- 落 `<工程>/assemble/粗剪.mp4`，路径直接给用户（侧边栏能播）

**口令**：用户说「看看整体 / 看粗剪 / 现在什么效果 / 拼起来看看」→ 直接跑，别问档位。
跑完报三件事：成片路径、时长是否与剧本全长对齐、哪些段还是占位。

## 交付：一步出文件夹（h3_deliver）

用户说「交付 / 出成品 / 打包 / 发布」→ `h3_deliver tier="2k"`（门禁同 delivery：全段齐备 + 全验收）。
它一次做完：装配成片 → `h3_archive` 归档 → 封面（段 1 关键帧，`cover_segment` 可改）→ `发布.json`（标题/简介/标签从原稿 MD 抽，抽不到就提醒用户补）→ `交付清单.md`，全部落 `<期>/交付/`（默认不带字幕，`subtitles` 缺省 none）。2K 续接段比段长短 5 帧时装配自动钉长重编码，成片时长 = 配音时长。
不要再分步手拼 assemble + archive。

## 字幕与配音对位

- 配音先行期：段长由 `h3_plan_durations` 按配音反推，timing.json 的 cues 就是时间码来源，天然无漂移；配音 `fit` 出现 `compressed/overflow` 说明段长没跟上，重跑 `h3_plan_durations` 而不是压配音——重跑同样受落盘门禁约束：先 `dry_run=true` 看会改哪些段、作废什么，有产物就要向用户复述并带 `confirmed=true`。
- `h3_narrate` 生成的是**候选**旁白（返回 `revision`），不直接替换 `配音/`：请用户试听，同意后 `h3_voices action=apply_version revision=<返回的 ID>` 才生效，旧版保留。
- 兼容旧期：`h3_narrate` 应用后落 `配音/旁白_长版.srt`（句级时间轴，与 wav 同源天然对齐）和 `.timing.json`；返回每段 **旁白秒数 vs 画面秒数** 的漂移表，`⚠` 的段（偏差 >15%）要么压缩词（`h3_prompt_edit` 删拍）要么改 duration（`h3_write_segment`，会级联）。
- 装配字幕：**默认 `"none"`**（用户后期语音转文字自己出字幕，别主动烧）｜`"srt"`（旁挂同名 .srt）｜`"burn"`（仅用户明确要求时；delivery 下要重编码，慢）。默认值在 h3-agent.json `subtitles.default`。
- 面板粗剪播放器有字幕跟播（当前句高亮、点句 seek），时间轴上漂移段有橙色小三角。

## 自动推进（autopilot，设置弹层「流程」）

`h3_pipeline_set set={"autopilot":"off"|"768"|"deliver"}`。**F1 不变**：验收只由人点；自动挡只推进点头之后的机械阶段：
- `768`：全部段验收达成的那一刻（`h3_approve` 全验收）自动起 768 后台作业
- `deliver`：768 齐 → 自动 2K → 2K 齐 → 自动 `h3_deliver`，中途只报异常
用户开了自动挡后，你的汇报改成"已验收，自动推进已起 768 作业，可以走开"。

## 改错了怎么办（h3_undo）

每次 `h3_write_segment` / `h3_prompt_commit` 前自动存回退点（`.snapshots/`，留 10 份：快照 + 对照表 + 段墙状态 + **所有版本的分镜** `分镜_*.json`，不只长版——抖音版分镜也在回退点里，`h3_undo` 会一起恢复）。
配音先行的三个落盘动作也各存一份：`h3_plan_durations` 真跑改段长（reason `plan_durations`）、`h3_timecode` 落盘（`timecode_seg<首几段>`）、`h3_storyboard action=init overwrite=true` 重建分镜（`storyboard_overwrite`，另留 `.bak-<ts>`，且要 `confirmed=true`）——回退时分镜文件跟快照一起恢复，手填的英文拍不会丢。
用户说「改错了 / 撤销 / 回到上一版词 / 段长改回去」→ `h3_undo action="list"` 看点 → 复述回到哪个点 → `h3_undo confirmed=true`。
产物文件不动，被作废的指针一起回来；若那版 768 曾生成过，指纹一致可直接续跑。
注意回退点不含配音 wav / timing.json：段长回退后配音还是新段长的，要 `h3_narrate fit=anchor` 按回退后的段长补一遍（出的是候选，试听后 `h3_voices action=apply_version`）。

## 环境不对先自检（h3_doctor / `/h3 doctor`）

「工具没挂载」「引擎离线」「配音失败」「换机了」→ 先 `h3_doctor`：配置路径、ffmpeg、MiniMax 登录态、ComfyUI、Workbench、模板、模型文件 vs available 标记、Pi 全局注册（h3 扩展 + skills/core）、默认期三件套（配了 defaultEpisode 才查），每条红项带修复命令。配音失败多半是 MiniMax 登录过期或声贝不足：`h3_voices action=status` 看，过期就 `web_login` 请用户扫码。

## 段间衔接：22 帧重放头是什么、怎么控（h3_assemble overlap / h3_seam_check）

**机制**：段 N≥2 靠 latent 续接——引擎把上段片尾 22 帧 latent 塞进本段头部当运动上下文，模型在这 22 帧真实画面之后往下续写，段界才无缝。
**后果**：draft/768 的**单段试片**是整段 latent 直接解码，所以片头 22 帧（0.917s）是上段片尾的逐帧重放；2K 出盘引擎已去头。
装配时若不处理，每个段界"倒退 0.917s 再前进"，段尾 0.917s 真内容被截掉——16 段累积 14s。

| `overlap` | 做什么 | 何时用 |
|---|---|---|
| `trim`（默认） | 段 N+1 从第一个新帧起接 | 成片口径；粗剪/交付都用它 |
| `keep` | 试片原样拼，保留重放 | 给用户**看**"重叠是什么"、审接缝；成片绝不用 |
| `blend` | 段 N 末 22 帧与段 N+1 首 22 帧（同内容两次解码）叠化 | 怀疑重解码色差时；有占位板自动退回 trim |

默认值在 `pipeline.json assemble.overlap`（面板设置弹层「装配」组可改）；单次覆盖传 `overlap=`。三种模式时长一致。

**段界检查** `h3_seam_check`：每个相邻有片的段界出「上=保留重叠 / 下=去重叠」慢放对比片（红线=接缝时刻），并量化：
- `replay_frames` 实测重放头长度（应=22；2K=0）
- `ratio` 接缝跳变 / 段内正常运动 → 判定 `ok`（<4x 无缝）｜`content`（只有一小片像素变——字幕卡/新元素弹入，是剧本内容，不是瑕疵）｜`check`（大面积变化，看对比片）
- `chain`：引擎 meta 的续接 sha 比对——`broken` = 段 N+1 接的是**旧版**段 N（上段重摇/改词后没重跑本段）。**这是真问题**：段界会跳；处理 = 从段 N+1 起重跑该档。草稿链重摇不级联是设计如此，所以草稿链常常"断"，正片 768 链必须连续。
- 跨档段界（粗剪混档）不判链。

口令：「接缝对不对 / 衔接看看 / 段界」→ `h3_seam_check`；「看看重叠是什么」→ `h3_assemble mode="rough" overlap="keep"`。
`h3_deliver` 交付前自动量一遍写进交付清单；有 `broken`/`check` 要在汇报里点名。

## 装配两种模式（别选错）

| 模式 | 用途 | 要求 | 输出 |
|---|---|---|---|
| `rough` 粗剪 | 看节奏、给用户看进展 | 至少 1 段有画面 | `粗剪.mp4`（重编码，统一画布，去重叠头，钉剧本时长） |
| `delivery` 交付 | 出成品 | 该档全段齐备；2k 还需全段验收 | `成片_<档>.mp4`：2K 流拷贝无损；draft/768 重编码（去重叠头 + 钉剧本时长） |

**为什么 draft/768 不能流拷贝**：段 ≥2 走 latent 续接，上段片尾 22 帧 latent 作运动上下文塞在本段 latent 头部；
草稿/768 的单段试片是整段 latent 直接解码，所以**片头 0.917s 是上段片尾的重放**（E2E 逐帧比对确认）。
引擎的 2K 出盘节点自己跳了这 22 帧，试片没有——装配层对段 ≥2 的 draft/768 试片 `skip_head=22` 再钉剧本秒数。
返回的 `method`（copy/reencode）和 `skipped_head_frames` 如实报告了怎么拼的。

音轨 `audio`：`mix` 旁白+音效（粗剪默认）｜`narration` 只旁白（交付默认）｜
`segment` 只音效（**验音效四律用这个**）｜`none` 无声。

## 批量 vs 单段（别选错，选错烧 GPU）

| 场景 | 用什么 |
|---|---|
| 批量、挂机、"跑完叫我"、补齐缺的段 | **`h3_batch`** |
| 就要这一段（验词、重摇后重出） | `h3_generate` |

`h3_batch` 干四件 `h3_generate range_to` 干不了的事：**只跑缺该档的段**（= 天然断点续跑）、
单段失败自动换种子重试、2K 顺序守卫、`dry_run` 先出计划 + ETA（按最近实测自校准）。
`h3_generate range_to` 会**重跑已完成的段**——16 段重跑草稿白烧半小时，别用它做批量。

**三步固定流程（硬约束，工具会拒）**：
1. `h3_batch tier=… dry_run=true` → 把「要跑哪些段 / 跳过哪些 / 预计多久」报给用户
2. 用户说"跑" → `h3_batch tier=… confirmed=true`（没有 confirmed 会被拒）
3. 它**立即返回 job_id**（后台作业，父进程退出不影响）→ 告诉用户"可以走开了"，**不要等它跑完**，这一轮就结束

**后台作业期间**：用户问"跑到哪了 / 还要多久" → `h3_jobs action="status"`；说"停" → `h3_jobs action="cancel"`
（跑完当前段就停；`force=true` 才强杀）。面板动作条实时显示作业条，跑完有系统通知。
同一期同档已有作业在跑时再起会被拒——先 status 看。
三档都是续接链（草稿段 N 也以段 N-1 的 latent 作运动上下文），`h3_batch` 任何档遇到首个失败段（重试用尽）就停，剩余段在返回的 `remaining_after` 里，由人决定换种子重跑还是改词。
失败段有 `last_error` 落在墙上（`h3_get_wall` 能看到 ⛔），面板有「N 段失败」徽章。

## 出片后必做：h3_archive 归档

768 latent 只活在 ComfyUI `input/` 临时区，mp4 只活在 `output/`——**清理 output 或重装 ComfyUI 就直接斩断 2K 链**（2K 只吃入库 latent）。

`h3_archive` 把它们收进期目录（成片/ 试片/ latent/）并落 sha256 双清单。幂等，多跑无害，绝不重渲染。

- 每期 2K 出完 → 跑一次
- 装配交付后 → 再跑一次
- **先归档，后清理 output，顺序不可反**
- 还原：把 `期目录/latent/` 的文件按原名拷回 ComfyUI `input/`，2K 路由按 sha 校验即可继续消费

## 生成设置（管线配置 v2：画幅 / 模型引擎 / 分辨率 / 种子 / 输出 / 2K）

`h3_pipeline_get` 读，`h3_pipeline_set` 改，改完下次生成即生效（ComfyUI 切模型无需重启）。桌面面板齿轮弹层是同一份配置的直改入口。

**画幅（竖屏在这里）**：`h3_pipeline_set aspect="9:16"`——预设 16:9 / 9:16 / 1:1 / 4:5 / 3:4 / 21:9，
或 `aspect="custom" custom_size=[宽,高]`（正片尺寸，自动按 32 吸附、校验 H3 上限 1.03MP）。
切画幅自动推导三档：正片按像素预算、草稿 = 正片×2/3、2K = 正片×倍率、2K tile 跟随正片。
用户说「竖屏 / 抖音版 / 方图 / 1:1」→ 切对应画幅；**切画幅前必须告知：已跑的 768 链会断，需从段 1 重建（草稿不受影响）**。已有 768 时，改画幅 / 模型 / 分辨率 / 步数的 `h3_pipeline_set` 要带 `confirmed=true`（工具会拒并列出代价）。

| 用户说 | 你做 |
|---|---|
| "竖屏拍" / "抖音版" | `aspect="9:16"` |
| "方图" / "小红书" | `aspect="1:1"`（或 3:4 / 4:5） |
| "宽一点，电影感" | `aspect="21:9"` |
| "1280×720" 等具体尺寸 | `aspect="custom" custom_size=[1280,720]`（会吸附成 1280×704 并告知） |
| "草稿降点画质省时间" | `tier="draft" resolution=[768,448]` 或 `[672,384]`（只影响草稿；宽高必须被 32 整除） |
| "画质上不去，切原生" | 本机没有 bf16 基座，定稿不用原生 20 步：先查提示词（小字写进词、动作写清）和 2K；真要切是 `tier="768" model="original_bf16"`（未下载会被拒，如实转告） |
| "每次换个画面" / "多试几版" | `set={"seed.mode":"random"}`；想复现改回 fixed |
| "有噪点" | `set={"engine.lora_strength":0.8}`（Turbo 官方 1.0，社区 0.6–0.8） |
| "细线条糊 / 大运动拖影 / 想多几步" | `set={"tiers.768.steps":8}`（每档独立：`tiers.draft.steps` / `tiers.768.steps`；定稿 6/6，缺省也是 6；设 0 会退回引擎预设 4 步——别这么做；Turbo 6–8 步换细节减拖影，12+ 只对原生有意义；步数写进引擎口径，同链中途改会被拦，改后该档从段 1 重跑） |
| "2K 文件太大 / 太糊" | `set={"output.crf_2k":22}` / `17`（越小越清晰越大） |
| "2K 再放大一点" | `set={"upscale.factor":3}`（显存吃紧，先问） |
| "配置乱了，回默认" | `reset=true`（保留模型下载标记） |

进阶键（`set={点路径:值}`）：`tiers.draft.steps / tiers.768.steps`（每档步数，0=跟引擎）、`engine.sampler / engine.shift_video / engine.shift_audio / engine.lora(auto|none|文件名)`、
`seed.base`、`take_tag`（多链并存互不覆盖）、`context_denoise.video|audio`、`output.codec(auto|h264|h265) / output.bit_depth(8|10)`、
`upscale.chunk_length / temporal_overlap / tile_auto / tile / spatial_overlap / fade / cfg / refine_steps / refine_denoise / noise_seed / prompt`。

**锁定不可改**（改了 latent 链就断，工具也不接受）：overlap 22 帧、fps 24、resolution_mode、continuation_anchor、release_guard、anchor_strength。
- 模型标 `available:false` 的是本地没下载，工具会拒绝切换（不是 bug）。
- 2K 后置步骤链逐项开关；`native_2k` 目前只有配置没有执行器，打开不会发生任何事。
- 改完 `h3_pipeline_get` 回读，把 `_meta.last_change` 报给用户。

## 写词铁律（配音先行规则以本节为准；逐句分镜按 h3-storyboard-writing；h3-prompt-writing 管字段语法与创意编译，它上游的 `<d>` 台词写法配音先行线不用）

- **写完先 `h3_lint prompt=… duration=…` 再落盘**：error 级（<Picture>/near-silent/缺字段/顺序错）`h3_write_segment` 会直接拒；
  warn 级（英文本体含中文 / 事件数与时长不匹配 / 有动作没音效 / 旁白写进词 / 风格骨架跑偏）要么改要么向用户说明。
  全期建完 `h3_lint`（不带参数）过一遍，纯文本不占 GPU——错在排队前发现，不是在质量门。
- 三字段固定顺序英文书写：`integrated_multimodal_description` / `overall_soundscape` / `non_diegetic_music`
- **配音先行铁律（h3_timecode 自动照此生成；手写也必须遵守）**：
  - 禁 `<d>…</d>` 台词——旁白走外配音，H3 不听音频、不说话（lint `dialogue_tag` warn）
  - 禁字幕条（subtitle bar / caption bar）——字幕由用户后期做，画面底部五分之一留空（lint `subtitle_bar`）
  - 禁 narrator / voice-over / narration 描写；配乐字段 `non_diegetic_music: N/A`（不生成 BGM，要就用户后期加）
  - 每个动作前写绝对时间码 `At MM:SS.mmm`（= 句起点 + compensation_s，默认 +0.2；段 ≥2 再加 continuation_head_s 0.917；段内首事件不早于 head + min_first_s 0.3，即段 1 ≥0.3s、段 ≥2 ≥1.217s），长动作加 ", finishing by MM:SS.mmm"；每句末尾写本期 `hold_en`（缺省 "then the canvas freezes"），最后一句写 `closing_en`（缺省 "and everything holds completely still until the end"）（数字与写法以代码 `h3_storyboard.py` DEFAULT_STYLE 为准，逐句规则见 `h3-storyboard-writing` §9）
  - 画面字段末尾必带本期 `no_voice_en`（缺省 "No speech, no dialogue, no human voice of any kind; no people or faces appear; no on-screen text other than the labels described."；R3 起登记了住户的期用风格 skill 给的放开句，`h3-storyboard-writing` §6；缺了是 info 级 `no_voice_missing`）
  - 时间码单调递增（lint warn `timecode_order`）；**任一时间码 ≥ 段长 = lint error `timecode_past_end`，落盘被拒**；末个离段尾 <0.5s 是 warn `timecode_overflow`；`h3_timecode` 生成时离段尾 <0.8s 就会先给一条 warning
- 段长 = grid(该段语音长度 + gapSegment)（17k+5 网格 @24fps 向上吸附，lead 不计入）；由 h3_plan_durations 反推写回，不手填
- 音效四律：声音短语紧跟动作从句；滑入 whoosh 落定 pop；连发写成一个短语（"three staggered soft pops"）；禁写 near-silent
- 开场衔接用 "continuing the same continuous take without any reset"
- **禁写 `<Picture N>` 图片引用**——latent 续接模式无图片参考，会被质量门拦截；用连续镜头表述
- 一段 ≤ 6 个时间码为宜；lint 按时间码计事件数，超过 ⌊段长/1.5⌋（12 s = 8 个）报 `too_many_events`，少于 ⌊段长/6⌋ 报 `too_few_events`
- 质检用 `h3_align`：pass=全部时间码匹配且中位 ≤0.2s、最大 ≤0.3s；check=全匹配且中位 ≤0.35s；其余 fail。系统性滞后按建议改 compensation_s 重写重跑

## 风格包路由（写词前按题材选）

| 题材/风格 | 技能名（h3_get_skill 读全文） |
|---|---|
| 默认（系列没写 style） | 深海：风格 skill `shenhai-style-explainer` 写稿 + `h3-storyboard-writing`（写稿时 §0 管中文画面，建期后 §1–7 补英文）；选题用配对的 `shenhai-series-planner` |
| 系列 `系列.json` 写了 style 配对 | 风格 skill 写稿、选题 skill 选题；产线看风格 skill「产线路线」——A 线走主流程，B 线走「多镜头线出片」，混排 / 歌先行 / 代码层走「混合路线」。`h3_get_skill` 列不出它 = 还没装进 Pi：先 `h3_skill action="pack" name=<名>` 再 `action="install" src="<名>"`（install 按名字先取分发目录里最新的 zip，源库改过没 pack 会装成旧版；覆盖已装的要 `overwrite=true confirmed=true`）。只有风格 skill、没有选题 skill 的线（诗词长卷、木刻拼贴等），选题交研发线 |
| 创意动画手法 / 动画化已有稿 / 动画中等或不连贯 | `creative-animation-treatment`（global，写中文画面前按需要做动画设计；常规期可局部审查，C 档用整片模式；交接保留因果骨架、动作证据与动作设计表） |
| 参与式（用户或风格要求填空 / 预测 / 留白 / 交还） | `participation-design`（global：选所需参与装置，先出参与拍表；与动画设计共同交接目的、等待、反馈次序，再写旁白和中文画面） |
| MiniMax 官方社区风格 | 未安装（3d-animation-short-generator / brand-promo-video-generator / co-op-game-intro-generator / handdrawn-live-video-generator / minimalist-product-ad-generator / music-video-subtitle-generator / paper-collage-explainer-generator / papercraft-stop-motion-explainer），安装包在分发目录 H3技能包，用户点名要时 `h3_skill action="install" src="<全名>"` 再 `h3_get_skill` |
| 题材专属技能 | 先 `h3_get_skill` 不带 name 列清单；期目录 `<期>/skills/<名>/` 与工作根 `<根>/_skills/<名>/` 里的包优先于库级 |
| 学一部新参考视频 / 找方向选题 / 创新风格 | 研发线 `h3-research-director`（不在本技能里做；Pi 没有联网，爆款实证与查证在 Kiro / Cursor 做） |

不确定时先 `h3_get_skill`（不带 name）列清单再选。技能包的增删由 `h3_skill` 管：`action="list"` 看源库/安装根/分发目录三处状态，`verify` 校验 SKILL.md 契约（含「待填」没填完的提醒），`pack`→`install` 把源库技能装进安装根（`remove` 卸载）。学新视频、给新风格建 skill 配对、找方向选题都属于研发线 `h3-research-director`。

## 档位决策（三档自动挡 + 验收门）

| 档 | 何时用 | 门禁 |
|---|---|---|
| 草稿 0.46MP（默认 896×512，可降） | 验词/表演/音效/旁白对位——快速否决 | 无 |
| 正片 768 | 构图与段间缝——唯一构图锁定档 | 无 |
| 2K | 交付画质 | **全段 768 齐备 + 全段验收**（工具自动拦） |

**草稿过 ≠ 768 构图锁定**：草稿阶段只纠结内容对不对，构图细节等 768。
**验收协议（F1）**：只有用户明确说「段N过/验收段N/全部过」才调 `h3_approve segment_index=N|all confirmed=true`（不带 confirmed 工具会拒）；用户说「这段不行」→ 先问改词（h3_write_segment）还是换种子重摇（h3_reroll）。

## 中英对照改词（作者说中文，你写英文——首选改词路径）

逐拍改词时读 [references/prompt-editing.md](references/prompt-editing.md) 的工具步骤、完整口令表和红线。

- `h3_prompt_edit` 只改 authoring；`h3_prompt_pending` → `h3_prompt_fill` 补双语；单补中文不改英文不动产物。
- `h3_prompt_commit` 才提交：有改动时从段1作废全片草稿/正片、全部2K并撤验收；先复述实际代价，按工具门禁确认。
- 🔒 风格骨架保留；局部取舍不整段重写。A线守当前分镜/时间码合同，B线守官方字段语法与本期动画证据。

## 导演记忆（决策落盘，下次会话不失忆）

- 用户说「这段马腿不对」「这期走木刻风」「段 7 音效偏大下次注意」→ `h3_note`（段级给 segment_index，期级不给）；
  验收时顺手 `h3_approve segment_index=N confirmed=true note="用户原话"`（否决不调 approve，只记 `h3_note`）。`h3_get_wall` 每段尾巴会显示最近一条 📝。
- 开工检查第 3 步读墙时，把 📝 备注当上下文：上次否决的原因、这期的风格决定，不要让用户重说。

## A/B 选片（历史版本回切）

- 重摇/改词作废的旧 take 自动进 `history`（不限条数，只有显式回收才移入回收站；mp4 仍在盘上）；`h3_get_wall` 段尾显示 `历史draft×2`。
- 用户说「还是上一版好 / 换回第一次那个」→ 先 `h3_manage_take action="list" segment_index=N tier="draft"` 拿 `take_key`，再 `h3_pick_take segment_index=N tier="draft" take_key=<原样传入>`（该段已验收时还要 `confirmed=true`；面板段详情也能直接点）。
- **768 不可回切**（latent 续接链与 take 绑定，工具会拒）——要换正片只能 `h3_reroll tier="768" segment_index=N confirmed=true`（先复述级联范围）再 `h3_batch tier="768"` 重出。
- 切回后验收作废（产物变了旧点头无效），提醒用户重新看一眼再点头。

## 级联语义（改词/重摇的代价，工具自动执行）

- `h3_prompt_commit` **必须带 `confirmed=true`**（硬约束）：先 `h3_prompt_view` 列出有改动的段，向用户复述“有改动时将从段 1 起作废全部草稿/正片 + 全部 2K + 撤销验收”，用户同意再调。
- `h3_prompt_edit`：**零代价**（只动 authoring 层，产物不变）；`h3_prompt_commit` 才付级联代价
- `h3_write_segment` / `h3_prompt_commit`：有改动时从段 1 起草稿/正片全部失效 + **2K 全部作废** + 验收撤销
- `h3_plan_durations`（真跑改段长）/ `h3_timecode`（落盘改词）/ `h3_write_segment` / `h3_prompt_commit`：只要有段变了，就**从段 1 起**级联（冻结指纹覆盖全片，2026-09-27 实测只重跑变动段必被拦），代价 = 全部草稿/正片 + 全部 2K + 撤销验收；什么都没变不触发。范围在 dry_run / preview 返回的"真跑将作废：…"里，有产物必须 `confirmed=true`（门禁见主流程节）
- `h3_reroll tier="draft"`：只动本段草稿，最便宜——**但之后的草稿仍接着旧版本段续接**（段界会跳，`h3_seam_check` / 墙上会标"链断"）。要修草稿链：`h3_reroll tier="draft" segment_index=N cascade=true confirmed=true`（先复述；N 起全部作废进 history）→ `h3_batch tier="draft"` 按序重建。面板段详情有「修链」按钮发的就是这条
- `h3_reroll tier="768" … confirmed=true`：该段起级联 + 2K 全作废——改构图才用。`h3_reroll` 只作废、不渲染，之后要 `h3_generate` / `h3_batch` 重出
- **冻结指纹铁律**：768 链开跑后改词 → 指纹断裂 → 全部重跑（桥落盘时已从段 1 作废）；此时直接 `h3_batch tier="768"` 从段 1 重建（它只补缺的段），别用 `h3_generate range_to`
- 顺序守卫自动生效：2K 必须 1→N；缺 768 的段会被工具拒绝并说明

## 验收双模式（听用户的口令判断）

- **逐段卡点**（用户在看）：每段草稿完 → `h3_view_preview` 自查 → 报四件套 → 等点头再下一段
- **批量挂机**（用户说"跑完叫我"）：`h3_batch tier="draft" dry_run=true` 出计划 → 确认 → `h3_batch tier="draft" confirmed=true` 起后台作业 → 告诉用户可以走开；用户回来问进度 `h3_jobs status`，跑完先 `h3_get_wall` 看失败段，再 **出一版粗剪**（挂机回来先看整体最省时间）
- **定稿自动**（全部验收后）：`h3_batch tier="768"` → `h3_batch tier="2k"` → `h3_deliver tier="2k"`（内含装配+封面+发布.json+归档，不要分步手拼）→ `h3_archive`，中途只报异常。想让它无人值守一路到交付：`h3_pipeline_set set={"autopilot":"deliver"}`（先征得用户同意；验收仍由人点）
- 段墙网页实时看进度：`http://127.0.0.1:30141/wall`（15 秒自动刷新，期选择器切换，四件套对齐，验收进度徽章，旁白配音直达）

## 汇报格式（每段交付四件套）

```
段03 ✅草稿 12.9s seed=42
  视频：D:/AI/H3分镜台/…/<期>/试片/长版_draft_段03_00001_.mp4
  词：integrated_multimodal_description: …（前 100 字）
  旁白：三千年前，它真的是一匹马。
  关键帧：D:/AI/H3分镜台/…/关键帧/段03_v01.png
```

## 视觉验收（模型看图自动初筛）

- 视检前确认会话模型支持读图：`deepseek-v4-flash-vision-exp`（insar-llm 下视觉模型）；不支持读图的模型会报"tool image omitted"
- **数字排查执行，导演判断表达**：`h3_timecode preview` 的节奏预检与 `h3_align` 成片读数对本期 `target_*`，⚠ 先查口径、细线漏测、活层干扰与刻意留白，再决定是否改。生产节奏是像素口径，研发 `analyze_reference` 的节奏是 scene_score，不能直接比；墨量/色面同算法。对齐 pass、密度与色面过线都不能证明动画好（F-007）；看因果、动作过程、表演、焦点与跨拍继承，勿为凑数字加装饰。
- 抽帧 frames 用 4-6 起步（2 帧容易漏掉段中后段的内容变化）
- 看图只走 `h3_view_preview` / `h3_keyframe`（回给模型的图已缩到长边 ≤1568）。**别直接读 2K 原帧、封面原图或拼成大图的联络表**：一轮多图时任何一张长边 >2000px 整轮报错，图进了会话历史后每轮都重发，会话就此卡死
- 视检报告要素：画面元素清单、构图完整性、黑屏/花屏/异常检查、与旁白对位
- **视觉初筛 ≠ 终审**：Agent 报"正常"后仍由用户点✅验收（F1 铁律）
- 看到画错：先查 `h3-production-lessons` 有没有同类条目（有的标了"换种子没用"，别直接重摇）；改词修好、看过画面后，按它的条目格式记一条（失败原句 + 成功原句 + 期·段·档·日期），推翻旧条目时写明被哪次实测推翻

## 红线

- 定稿永远用户点（AI 只出草稿和证据）；验收标记只由用户口令触发
- 不碰 ComfyUI 界面、不手拼工作流 JSON——一切经工具
- 素材库绝对只读（h3_library 只浏览，不改库内任何文件）
- 产物路径原样转告用户（侧边栏/文件管理器直接看）
