# 逐拍中英对照改词与口令表

仅在改词/取舍/提交 authoring 时读取；本文件从导演主技能移出，工具与级联规则未变。

## 中英对照改词（作者说中文，你写英文——首选改词路径）

H3 只吃英文三字段，但作者用中文取舍。对照层把每个字段切成**拍（beat）**，
一拍 = 一份中文 + 一份英文，删拍就中英同删。

```
h3_prompt_view(segment_index=N)   看拍：拍号 / 状态 / 中文 / 英文 / beat_id / 🔒
h3_prompt_edit(...)               机械改：删拍·清字段·改中文·插拍·换序（毫秒级，不花 token）
h3_prompt_pending()               取待办：need_en（作者改了中文）/ need_zh（有英文缺中文）
h3_prompt_fill(items=[…])         你动笔：批量回填英文或中文
h3_prompt_commit(segment_index=N) 应用：重组英文 → 引擎重建快照 → 级联失效
```

**四种状态**：`ok` 中英齐｜`need_zh` 有英文没中文（初次导入英文资料）｜
`need_en` 中文改过英文没跟上｜`zh_only` 新插的纯中文拍。

**口令映射（照这个走，别重写整段）**：

| 用户说 | 你做 |
|---|---|
| "不要音效" / "音效全删" | `h3_prompt_edit op="clear_field" field="sound"` |
| "第 3 句不要" / "删掉推镜头那拍" | `h3_prompt_view` 找 beat_id → `op="del"` |
| "这拍改成：马腿要四条" | `op="edit_zh"` 写中文 → `h3_prompt_pending` → `h3_prompt_fill` 补英文 |
| "加一拍：镜头缓慢拉远" | `op="insert"` 带 zh → 同上补英文 |
| "把英文资料翻成中文给我看" | `h3_prompt_pending` 取 need_zh → `h3_prompt_fill` 填 zh（不改英文=不动产物） |
| "改好了，应用" | `h3_prompt_commit` |
| "跑完叫我" / "批量" / "接着跑" | `h3_batch dry_run` 报计划 → 用户确认 → `h3_batch confirmed=true`（后台作业，立即返回） |
| "跑到哪了" / "还要多久" / "停下" | `h3_jobs action="status"` / `action="cancel"` |
| "还是上一版好" / "换回去" | `h3_pick_take`（draft/2k；768 不可） |
| "记一下：…" / 任何口味决定 | `h3_note`（段级或期级） |
| "查查词有没有问题" | `h3_lint`（全期或单段，不占 GPU） |
| "这句画面是…" / "补英文画面" | `h3_storyboard action="set" index=N n=M visual_en=…`（配音先行①） |
| "配音出来 / 段长按配音来" | `h3_plan_durations dry_run=true` 看表 → 不带 dry_run 写回并出配音（返回说"将作废"时先复述、再带 confirmed=true） |
| "出时间码词 / 生成提示词" | `h3_timecode preview=true` → 落盘（同上；抖音版只能 preview） |
| "老期改成配音先行 / 迁到时间码法" | `h3_storyboard action=init md_path=<原稿>` → 补 visual_en → `h3_plan_durations dry_run=true` → 复述代价 → confirmed 真跑（见「老期迁到时间码法」） |
| "动作对不对得上 / 同步查一下" | `h3_align`（帧差 vs 时间码，给 compensation_s 建议） |
| "交付 / 出成品 / 打包" | `h3_deliver tier="2k"`（装配→归档→封面→发布.json→清单，含接缝质检；默认不带字幕） |
| "接缝对不对 / 段界看看" | `h3_seam_check`（对比片 + 重放帧 / 跳变 / 链） |
| "看看重叠是什么" | `h3_assemble mode="rough" overlap="keep"` |
| "改错了 / 撤销 / 回上一版词" | `h3_undo action="list"` → 复述 → `h3_undo confirmed=true` |
| "工具没挂载 / 引擎不对 / 换机了" | `h3_doctor` |
| "验收完自动往下跑" | `h3_pipeline_set set={"autopilot":"768"}` 或 `"deliver"` |
| "看看整体" / "看粗剪" / "拼起来看看" | `h3_assemble mode="rough"`（随时可跑，缺段补占位） |
| "只听音效" / "音效对不对" | `h3_assemble mode="rough" audio="segment"` |
| "归档" / "出完了收一下" | `h3_archive` |
| "草稿画质降一点省时间" | `h3_pipeline_set tier="draft" resolution=[768,448]` |
| "竖屏 / 抖音版 / 方图 / 具体尺寸" | `h3_pipeline_set aspect=…`（见「生成设置」节；先告知 768 链会断） |

**红线**：
- 🔒 拍是全段共用的**风格骨架**（画面字段前缀，每段逐字节相同）——不要删，用户明确要删才带 `force=true`。
- 改英文前：配音先行期按本文件「写词铁律」+ `h3-storyboard-writing`，老期（非时间码词）才对照官方 `h3-prompt-writing` 的字段语法；**只写这一拍该说的事**，别顺手重写整个字段。
- 英文本体必须英文，中文只能出现在画面文字的 `"引号"` 里（如标签 "甲骨文"）；配音先行期禁 `<d>` 台词与字幕条（兼容旧期的老词除外）；禁 `<Picture N>`、禁 `near-silent`（工具会拒）。
- **只填 zh 不动 en ⇒ 产物不变、不级联**，所以"补中文"是零代价操作，随时可做。
- `h3_prompt_commit` 才真正改产物（有改动时从段 1 起级联作废草稿/正片 + 全部 2K + 撤销验收；桥 `CASCADE_FROM=1`）——提交前跟用户确认。
- 整段推倒重写才用 `h3_write_segment`；逐拍取舍一律走对照层。

