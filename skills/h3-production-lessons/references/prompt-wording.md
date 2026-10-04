# 物件与措辞（P-）

> P-001/002/003/013 的已见风险：平面画布提示词中的比喻、排除物件名与光感词可能引入非预期实体或光。需要的主体/实景光源照常写清形状、状态与事件；排除不需要的东西优先写正面的持续状态。风险按条目已测范围判断，不宣称所有名词必被画出，也不禁止题材所需的光。

### P-001 发光物件（路灯、屏幕、光锥）照常写，写清亮灭和什么时候亮（复现）
- 症状：09-30 画框 v2 草稿第 1、2 轮，背景里的路灯被画成亮的、带光锥，琥珀色提前出现。
- 失败写法：路灯只是背景道具 `a plain grey street lamp whose lamp head is unlit grey`，没有亮起事件，且画布句里有比喻 `like a single lamp aimed at the middle of a wall`（第 1 轮：被画亮）；`there are no lamps, lights or glowing things anywhere`（第 2 轮：仍画出亮灯）。
- 有效写法（10-01 草稿三组都成功，暗底琥珀风格块）：
  - 一直亮：`a flat street lamp instantly appears at the center of the empty canvas, already lit: a thin straight grey pole standing on a thin grey ground line, its lamp head a small solid warm amber disc, and directly beneath the head a flat triangular cone of amber light with crisp straight edges that lands on the ground as a flat amber ellipse; the light is drawn only as these flat shapes, with no halo, no bloom and no soft glow around them`
  - 先灭后亮（亮起是剧情）：先写 `a flat grey street lamp … switched off: a thin straight grey pole … topped by a small flat grey lamp head; it gives no light at all and the canvas has no color at all yet`，亮起另写一个时间码事件 `the street lamp switches on: its small grey head instantly turns solid warm amber and a flat triangular cone of amber light with crisp straight edges appears beneath it, landing on the ground as a flat amber ellipse, with no halo and no bloom`。灭的状态一直保持到事件；亮起约 0.3 s 完成。
  - 只写形状、事件时才叫它路灯（`a thin straight grey pole … topped by a small flat grey disc` → `the small grey disc … turns solid warm amber, becoming a lit street lamp`）同样成功，H3 自己画出路灯外形。
- 原因：一个默认会亮的东西，如果提示词没说它灭着、也没说它什么时候亮，H3 会按常识让它亮；画布句里的"灯"会被当成要画的物体（P-002）；否定句同样会招来它（P-003）。
- 光锥会带一点竖向渐变（H3 自带），写 `no gradient` 也去不干净；扁平风格里可接受。
- 证据：画框 v2 草稿 r1、r2（09-30，失败）；灯测试 A/B/C 草稿 896×512 段 1（10-01，成功）。
- 范围：暗底 + 单一暖强调色风格块、草稿档。768 未单独测。
- 推翻：`h3-storyboard-writing` 1.3.2 写的"会发光的东西连名字都别写"是错的，1.3.3 已删。
- 已升级 → `h3-storyboard-writing` §2 表「画面里的实景光源」行（注明 768 未单独测）。

### P-002 画布句里的比喻名词会被画出来（复现）
- 症状：画布写成某个地方的比喻，H3 就画出那个地方或那个物件。
- 失败写法：`on a flat near-black canvas (#141414) like a darkened cinema`（画框 v1 段 1 开头 0.4 s 闪出放映机和夜街，09-30）；`lit by a soft central light pool … like a single lamp aimed at the middle of a wall`（画框 v2 草稿 r1 冒出亮着的路灯）。
- 有效写法：直接写光的样子，不写它像什么：`with a soft, perfectly steady pool of light in the middle that falls off into darker corners and a barely visible fine grain`。
- 注意：风格 skill 里"画布是一个地方"这类说法（例（仅示格式）：某风格推导画布时先问"这块画布是哪里"）是**推导画布用的想法**，写进提示词时只写推导出的光和质感，不写那个地方的名字。
- 已升级 → `h3-storyboard-writing` §6（画布句只写光和质感，不写比喻）。
- 证据：画框 v1 768 段 1（09-30）；画框 v2 草稿 r1（09-30）；r4 起去掉 lamp 比喻后路灯消失。

### P-003 肯定/否定中点名非预期物件，可能把它引入画面（复现，范围见证据）
- 症状：为了"排除"或"允许"某样东西而提到它，它反而出现了。
- 失败写法：`there are no lamps, lights or glowing things anywhere`（出现亮灯，画框 v2 草稿 r2）；收尾句里写允许 `flat faceless figure icons`（段 1 框里多出三个人形图标，画框 v1 768，09-30）。
- 有效写法：不想要的东西干脆不提；需要排除时用描述画面的正句（`everything is grey and white only, with no color at all`、`nothing else stands on the ground line`），不点物件名。
- 例外：`no halo, no bloom`、`no gradient` 这类排除**效果**的否定没观察到反作用。
- 证据：画框 v1 768 段 1（09-30）、v2 草稿 r2（09-30）。
- 已升级 → `h3-storyboard-writing` §2 表「不要的东西写成正句」行、§6 `no_voice_en`（放开住户的句子只在真登记了住户的期用）。

### P-004 小物件的数量和位置要写死（复现）
- 症状：续接段里小物件多出一个、两个合成一个、被拖着走或变大。
- 失败写法：`two small white circles side by side`（768 段 4 亮回时多出一个圆；段 2 两个圆合成一个）。
- 有效写法：`two small white circles standing on the ground at about one third and two fifths of the canvas width with a clear gap between them`；后续每拍点名 `exactly two small white circles … in their exact original places and sizes, with nothing added`；场景只有这几样时加 `nothing else stands on the ground line`。
- 证据：画框 v2 768 段 2、段 4，r1–r3（09-30）。
- 已升级 → `h3-storyboard-writing` §0「写清主体、位置、颜色」、§2 表第一行。

### P-005 框类元素（画框、取景框、选框）不要让它离开框里的主体（复现，换种子没用）
- 症状：要画框"挪到空地上"，H3 不是框不动，就是把框里的东西一起拖走或弄没。
- 试过都失败（768）：`jumps to an empty patch of ground`；`disappears … and an identical frame instantly appears further right`；`shifts further to the right … until its left edge sits just right of the right circle`；`slides … and stops dead on the empty ground`（带 until）；外加换种子 307970。草稿 r5 曾经成功，768 上不成立（见 C-004）。
- 有效写法：
  - 第一次挪框写成边线动作：`the left edge of the amber frame instantly snaps inward to the gap between the two white circles while its right edge stays exactly where it is`——H3 执行成等宽右移，结果正确。
  - 框原地变形成另一种框：`the amber frame instantly changes, in place, … into a tall upright phone-camera viewfinder`——稳定。
- 绕法：演示非要空框，就让框留在主体上，换成别的手段（另起一只新框、或用明暗把主体压掉）；或者用关键帧锚定（引擎 `MiniMaxH3AddGuide` 能把指定画面钉在任意帧，产线还没接）。
- 证据：画框 v2 768 段 3 四次（09-30）。
- 已升级 → `h3-storyboard-writing` §2 表「画框 / 取景框 / 选框」行。

### P-006 要一直留在画面上的标记，写"留到最后"（单次）
- 症状：弧线（声波）出现后几秒内自己消失了。
- 失败写法：原句没留档。
- 有效写法：`three thin white curved arcs … instantly appear one after another, the last arc a hair late, and then stay on the door, unchanged, until the end`。
- 证据：画框 v2 草稿 r4 → r5（09-30）；段号没留档。

### P-007 强调色第一次出现之前，写明"还没有颜色"（单次）
- 症状：强调色计划在第 4 句才第一次出现，结果段 1 框里的两个白圆就变成了琥珀色。
- 失败写法：原句没留档。
- 有效写法：上色之前的拍写 `both circles stay pure white, nothing on the canvas has any color yet`；上色那拍写 `… turns saturated warm amber, the first color in the film`。
- 证据：画框 v2 768 段 1，r1 → r2（09-30）。

### P-008 同一种强调色要说"和某某一样的颜色"（单次）
- 症状：快门键 `fills solid amber` 时变成了红色。
- 有效写法：`fills solid with the same warm amber as the viewfinder outline`。
- 证据：画框 v2 768 段 5 r1 → r2（09-30）。

### P-009 形变时元素会歪一两帧（单次，未解决）
- 症状：宽银幕画框变成竖的手机取景框时，有一两帧是斜的。
- 试过：`staying perfectly upright and never tilting`——减轻，没去掉。
- 证据：画框 v2 768 段 5（09-30）。

### P-010 "框外的东西褪成浅灰"做不出来，改成"框外变虚线"（复现）
- 症状：要画框外的东西变淡，H3 只把整张纸调亮一档，框外的鸟和屋檐照样是黑的；整幅亮度变化还会让帧差把它当成一次全屏事件。
- 失败写法：`everything outside the frame, the wire beyond its edges, the right bird and the roof eave, turns a very pale grey, while the left bird and the wire inside the frame stay ink-black`（瞬现、滑动两种写法都失败）。
- 有效写法（待 768 复核）：`the right bird and the roof eave, which are outside the frame, instantly turn into thin dashed grey outlines with no fill, while the left bird inside the frame and the wire stay solid ink-black`；之后被框进来的写 `the moment the right bird is inside the frame it turns from a dashed outline back into a solid ink-black silhouette`。虚线在草稿里一直很稳（P-005 之外的虚线轮廓、P-006）。
- 证据：画框 v3 草稿段 1（10-01，滑动与瞬现两版）。
- 复核（10-01 第二轮草稿）：虚线写法生效，框外的鸟和电线变虚线；但屋檐仍是实线，电线左侧框外也还是实线——每个要变虚的元素都要点名，"框外的东西"这种统称不够。
- 第三轮（10-01 13:05 草稿段 1）：屋檐在同一句里点名（`the right bird and the roof edge, which are outside the frame, turn into thin dashed grey outlines with no fill`）后，屋檐、右鸟和框两侧的电线都变成了虚线（电线没点名也跟着变了）。点名有效；草稿成立，768 未测。

### P-011 滑动写法下"一抹铺满"会被画成刷子笔触（单次）
- 症状：`fills the whole inside of the wide frame in one swipe from left to right`（带 until）→ 框外先出现一大片灰色干刷笔触，两三帧后才消失。
- 有效写法：本次亮纸平涂的同稿对照中，瞬现填色避免了 swipe 的刷子笔触；需要材料涂抹过程的拍保留其过程目标，另选可控写法并标待测，不据本条把所有填色都改成瞬现。
- 注意：这里原先记的有效句以 `… Kodak-yellow highlight` 结尾，v3 第二轮草稿里 `highlight` 招来整幅偏黄和光锥，**改用 P-013 的写法**。
- 证据：画框 v3 草稿段 2，滑动版有、瞬现版无（10-01）。

### P-012 画框拉宽（左边线不动、右边线滑开）可以做出来，带 until 有完整过程（单次）
- 有效写法：`the frame's left edge stays exactly where it is while its right edge slides steadily to the right, stretching the frame from 4:3 into a wide 2.39:1 cinema frame of the same height until it also encloses the right bird; … the label below changes to "2.39 : 1" …`，until = 句末。滑动版能看到拉宽的过程（读数中途出现过「4:39」一帧），瞬现版一下跳到位。
- 对比：P-005（让画框离开框里的主体）做不出来；**让画框长大把新东西包进来**做得出来。
- 证据：画框 v3 草稿段 2（10-01）。

### P-013 `highlight` 会被当成光：整幅偏色 + 框下冒光锥（单次）
- 症状：框内填黄后，整张纸染上暖黄，框下方多出一个放映机式梯形光锥；色面读数虚高，下一段对齐也被干扰（段 3 零匹配）。
- 失败写法：`the whole inside of the wide frame instantly fills with a flat, fully saturated Kodak-yellow highlight`
- 有效写法（待草稿复核）：写成颜料/色块并锁住周围：`the inside of the wide frame is instantly painted solid flat Kodak yellow, like an opaque paper cut-out, while the paper around the frame keeps exactly the same pale warm grey; there is no light and no beam`；风格块加一句纸色永远不变。
- 原因：highlight / glow / light 类词带"光源"语义，和 P-001 同机制。
- 适用：亮纸 + 单一黄色强调风格块，草稿。
- 证据：画框 v3 草稿第二轮段 2（10-01，会话 2663c48f）。
- 复核（10-01 13:05 草稿段 1）：不写 highlight，写 `fills with flat, opaque, fully saturated Kodak yellow, the first color in the film … the cream paper outside the frame keeps exactly its color`，风格块加 `the paper is the same color everywhere on the canvas and keeps exactly this color for the whole shot` → 黄色是干净的平涂，纸色没变，没有光锥。草稿成立，768 未测。

### P-014 "按快门后框外全部消失"做不出来，改成"框外变虚线"（复现，换写法没用）
- 症状：要手机框外的东西全部清空，H3 在鸟后面冒出一团黄色，整幅再次偏黄，之前已隐藏的虚线猫和屋檐又回来了。
- 第二次（10-01 13:11 草稿段 4）换写法：`the round shutter button instantly turns solid yellow, and at the same instant everything outside the phone is erased, the dashed roof edge, the dashed cat, the ends of the wire outside the phone and the part of the tail outside the phone, leaving blank cream paper all around the phone; the phone and everything inside it stay exactly as they are` → 更糟：写在 7.371 s 的快门，6.25 s 时快门键已经实心（至少早 1 s）；6.9 s 时手机外框和快门键一起被抹掉，框里的黄色变成两块房子形的乱形；伸进框里的猫尾在这之前已变成一个倒挂的黑块。逐项点名"要抹掉什么"也不行。
- 有效写法（待复核）：沿用本期"框外 = 虚线"的语法：快门那拍写框外的电线、房子、屋檐 `instantly turn into thin dashed grey outlines with no fill`，纸色不变；变形另起一拍。
- 原因：大面积"消失"H3 倾向于用整幅亮度/颜色变化去做；和 P-010 一样，用局部的"实 → 虚"代替。
- 证据：画框 v3 草稿段 4 第一轮（10-01 10:26）、第二轮（10-01 13:11）；Kiro 会话 10-01 抽帧。

### P-015 精确数量与多边形边数：写数字不够（复现，未解决）
- 症状：六边形画成七八边形（E2E 冰为什么浮，09-27）；稿子 6 支箭头画成 8 支（画框 v1 段 3，09-30）。2K 照样放大（G-004）。
- 试过：写 `six`、`a hexagon`——不稳。
- 可试：P-004 的写死位置法（每个元素给位置）、数量 ≤3 的分组（`two rows of three arrows`）；或走关键帧锚定（P-005 绕法）。都未测。
- 证据：E2E（09-27）、画框 v1 768（09-30）。

### P-016 容器换形写成 `morphs … finishing by`：叠化成两个半透明形，一格变两格（单次）
- 症状：手机框变成一格胶片画格。第二轮写成 morphs + until，出片时旧形（P-014 留下的黄色乱形）和新胶片同时半透明地叠在一起（7.9 s 前后，写的是 9.121 s，早约 1.2 s），落定成**两格**胶片（要的是一格）。同段 3.75 s 鸟旁还冒出一个没写的四角星。
- 失败写法：`the phone outline morphs in place into a single frame of motion-picture film of the same size: a black film-strip frame with one row of small square sprocket holes along its top edge and one along its bottom edge, still holding the same picture of the two birds, the wire, the yellow and the tail; the "16 : 9" label disappears and nothing else is on the paper with a soft film-reel tick, finishing by 00:10.150`
- 有效写法：`the phone outline instantly changes into a single frame of motion-picture film: a black film-strip frame of the same size with one row of small square sprocket holes along its top edge and one along its bottom edge, holding the same picture of the two birds, the yellow and the tail`（第一轮：一格，干净）
- 原因：两件事叠在一起，没拆开测——同段上一拍"清空框外"已经把手机外框抹掉，形变的起点不在了（P-014）；`morphs` + until 让 H3 去画中间态，它用叠化来画。印证 `creative-animation-treatment` transitions.md §5 第一行：形变不写 morph，写一个主语 + `changes into`（要过程时写 `one single shape changing continuously in place, until it has become …`）。
- 适用：亮纸 + 单一黄色强调风格块，草稿 896×512；768 未测。
- 证据：画框 v3 段 4 第一轮（10-01 10:26）对第二轮（10-01 13:11）；Kiro 会话 10-01 抽帧。
