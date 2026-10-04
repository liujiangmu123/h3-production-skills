---
name: participation-design
description: |
  Designs viewer participation for a science/explainer video or a selected beat: prediction, estimation, comparison, self-experiment, reflection or hand-back, chosen for the content, duration and locked style. Use for 参与式/互动感/引导观众/让观众自己想/填空开场/留白, a participation beat sheet, or an audit of passive explaining. Produces the viewer task, clues, required think-time, visible feedback and implementation risks; supports short clips and local script edits without imposing a full-film structure. Does not write final narration in a locked style's voice, H3 prompts or timecodes.
metadata:
  kind: global
  version: "1.2.0"
  source: "G:/AI/视频分析/一些最近的想法/15/电子智人_无旁白参与式科普/视频分析/05、06、07"
---

# Participation Design 参与引导设计

**目标**：让观众做一件与本期内容有关的事（猜 / 估 / 读 / 比 / 试），给足线索与思考时间，再让画面的反馈帮助他理解。先定义这一处参与的用途，选合适装置；一支短片可以只有一个参与点，也可以只审现成稿的一拍。

装置库来自参与式参考分析；其中双实验开场、多章递进、光揭晓、约 70% 翻转、个人反省与交还是**一种可选长片组合**（见 beat-templates），不成为任何风格的必守配方。章数、高潮位置、揭晓手段和结尾听用户意图与锁定风格。

## 设计底线
1. **失败有解释**：装置可必中、失败即答案，或由片子陪观众完成；答错/答不出时有公平的反馈，不能羞辱观众。条件实验要写成功条件与兜底。
2. **出力有用**：每一处参与帮助理解或情绪推进；剂量按时长和观众负担决定，不逐章硬凑。
3. **时间真的留出来**：需要思考就给可辨认的题面/待完成动作，旁白和画面不抢答；可用静止物、悬而未决的姿态、空位或轻微过程等待，不强制发光。时长按实际阅读/尝试量估，并由下游实测复核。
   已验证的 H3 A 线冻结块用静止等待物。持续闪烁/呼吸会干扰 `h3_align` 的整帧差起点检测；本期运动块需要活层时，交动画设计与分镜标明执行风险和人工核看的动作证据，不能靠帧差结果否决其意义。精确倒计时仍交代码/后期层，不声称当前已接入。

## 工作流
1. **读入**：选题或现成稿 + 风格线（有/无旁白、产线：H3 / 代码动画 / 混合）。
2. **找入口**：为需要参与的概念想几个可当场完成的入口；没有合适入口就直接讲清，不为了覆盖每个概念强塞问题。
3. **选装置**：从 `references/device-library.md` 按目标、时长、知识门槛与路线选。L0–L8 是参与功能标签，可重复、跳过、并行；不要求递增或以 L8 收尾。
4. **排 beat**：按 `references/beat-templates.md` 选局部/短片/长片组合，写参与 beat 表；反馈可以是动作结果、形变、比较、遮挡解除、光/色或声音，按风格决定。
5. **自检**：过 `references/self-check.md` 的通用项，所选装置才查对应项；不适用标 N/A 与理由。
6. **交接**：时长只给“最少思考/读字秒建议”，不排时间码。与 `creative-animation-treatment` 一起定观众何时期待、何时看见动作证据；配音实测后可调整位置，但保留参与目的、先做后反馈的次序和必要等待。A 线留白实现由分镜/配音层承接；句末 MiniMax `<#秒#>` 当前会被剪静音、标记还会进字幕（总指导 §13 第 10 条，未修），不能把该标记当已可用的时长实现。

## 输出格式
```
## 参与 beat 表 · <片名>
用途：<这处参与帮助理解什么>    回扣物/仪表：<有才写>
| # | 段/章 | 观众要做什么 | 装置ID | 题面/旁白 | 等待状态 | 最少留白s | 反馈/动作证据 | 命名（如需） | 实现层与待验证风险 |
自检：通用项 ✓/✗；装置条件项 ✓/✗/N/A + 修改说明
```

## 有旁白时的改写（配音先行线）
- 旁白念完问题就停；**画面先揭晓、旁白后半拍确认**，禁止抢答。
- 填空/自体实验材料**只在屏上**，旁白不念（念了实验就没了）；旁白只说"读一下这句"。
- 与锁定风格冲突时，改选兼容装置或减少参与位，不改风格规则；用户明确要求偏离时才讨论其创新范围，记录在本期交接。

## 与其他 skill 的关系
| skill | 关系 |
|---|---|
| 锁定的风格 skill（任意 `<风格>-style-explainer`） | **上游/并行**：风格 skill 锁定旁白口吻、画面默认与哲学，也登记这个作者自己的参与读数（问号个数、留白秒、口吻）；写稿时参与层用本 skill 的方法、用该风格的读数，冲突时该风格赢；本 skill 只往里插参与 beat，不改其口吻 |
| `style-foundations` 的参与尺子 | **分析侧的镜像**：分析一支片"作者怎么让观众参与"用那把尺子量；本 skill 管生成侧"这一期怎么让观众参与" |
| `creative-animation-treatment` | **下游/并行**：本 skill 定参与目的、必要等待和反馈次序；它设计可见过程与动作证据，将所选参与位并入普通 MD 交接（装置 ID · 等待状态 · 最少思考秒 · 反馈 · 命名）。配音实测后协同调位置，不抢答 |
| `h3-storyboard-writing` | **下游**：接 beat 表，把每个参与 beat 写成逐句分镜（含留白段与等待物的画面行） |
| `h3-prompt-writing` | **更下游**：编译 H3 能画好的层（氛围、实体、可控反馈动作）；精确中文/数字/仪表交可用代码或后期层，未接入的标待实现 |
| `style-foundations` | 通用尺子；本 skill 不存风格结论，只存跨风格的参与方法 |

## 产线拆层（通用）
- H3：底图、氛围、实体与可控反馈动作；A 线按本期运动块写等待状态和过程风险。
- 代码动画（Remotion / ffmpeg drawtext / ASS）：空格、候选滚动、仪表、计数器、公式、乱序/遮挡文字、字幕。
- 合成：代码层叠在 H3 上，揭晓时码对齐。无旁白片的时钟 = 读字时长 + 留白。

## References
- `references/device-library.md` — 32 种参与装置（触发心理、屏上写法、时长、题材、实现要点、反例）
- `references/beat-templates.md` — 全片/章/单 beat 模板与模板句
- `references/self-check.md` — 写稿与成片自检清单
