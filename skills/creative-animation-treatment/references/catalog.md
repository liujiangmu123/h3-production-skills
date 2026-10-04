# 使用边界（2.2.0）

本目录保留旧编号以兼容已有研究。历史配方中的固定层数、数量、均匀节拍禁令和默认 A 线限制不自动成为通用要求；以新版 SKILL、animation-design.md、当前风格和实际工具合同为准。未验证的制作路线/能力须标待测。

# Operator catalog

按已设计的动作机制查少量手法。编号是索引，不是镜头；不强制跨轴凑 2–3 项。先读 animation-design.md，按选定媒介原生演绎。

Numbering is stable. Total: **526** (A–O 371 + P–S 74 + T–W 65 + X 16; 2026-10 并入 08 动画手法研究 11 条、10 高级转场研究 10 条), of which **13 are retired** (tagged inline, listed at the end; numbers are kept so old treatments still resolve). Seven non-operator sections follow the axes: the **native-render cheat sheet**, the **转场语法速查**, the **制作路由判据**, the **combination recipe**, the **cliché blacklist** (截至 2026-09; objects *and* motion habits), the **feasibility flags**, and the **retired operators** — consult the last three before scoring.

This catalog is the **idea layer** (what to do). How the chosen operators must *feel* — anticipation, settle, uneven offsets, the hold, color as relationship — lives in [feel.md](feel.md) and is applied in SKILL Step 7. 运动是否有效由意义、材料和实际样片判断，不由编号或统一缓动禁令打分。

---

## 快速入口（只是索引，编号不变；先按 SKILL Step 3 比较不同动作机制，再按需找轴）

**按内动词**。表里混着动词位和扭转位：动词只从 B / D / E 动词 / L / M / P / U / W 里挑一个（见 Combination recipe），其余当扭转。

| 内动词 | 先看 |
|---|---|
| 变成 / 换身份 | D01 D02 D10 D24 · L15 · M03 M09；各媒介怎么演查 Native-render cheat sheet |
| 冻住 / 定格成符号 | E01 · E16 · M01 M10 · S05；cheat sheet「凝固」行 |
| 出现 / 消失 / 换位 | L01 L02 L03 L09 · E02 |
| 进入 / 打开内部 | F05 F17 F23 · B10 B12 B28（门要是语义上的门，见「转场语法速查」后的补充写法） |
| 累积 / 增殖 / 计数 | D16 · L07 · J12 · H04 · Q01（数量是论点 → 制作路由判据走代码） |
| 删减 / 只剩一个 | J11 · T03 · E14 · W12 |
| 分开 / 合上 | D15 · W01 W02 · B11 · U06 · R19 |
| 毁掉 / 无常 / 复原 | P01 P06 · D17 · L04 |
| 回到 / 循环 / 回扣 | X08 · E31 · D32 · C07 C08 · B18 |
| 弄错再纠正 / 反着来 | E13 · E23 · D28 · C04 · E30 |
| 生长 / 衰败 | D14 · E04 · N05 N14 · W 轴 |
| 时间流过 | C17 · C09 C10 · F09 · M20 · S01 S03 |
| 让规则 / 力被看见 | E17 E18 · N / Q / S / V 轴 |
| 对比 / 并行 | C28 · C20 · Q19 · I16 · S08 · B31 |
| 尺度 | B17 B18 · E24 · S15 · X16 |
| 换视角 / 谁在看 | F02 F07 F22 · R21 · B31 |

**按问题**（用户这样说时先开哪里）

| 问题 | 先开 | catalog 里看 |
|---|---|---|
| 画面太简单 / 像信息图 / 像剪贴画 | world-class.md §一（档位低于知识）、§二.1（住户圣经）；不靠加图标、加标签 | 换 Axis A 媒介 · B13 B21（景深层）· I21（二维画、三维光） |
| 像 PPT / 一句一张图 | flow.md §一（动量链）与 animation-design.md | D01 D33 D35 · C17 ·「转场语法速查」 |
| 要转场 / 接缝 | transitions.md §1 五步；A 线只用 §3 | 「转场语法速查」· D03 D05 D25 D34–D36 · F05 F26 F27 |
| 2D 3D 结合 / 换维度 | feel.md §七；transitions.md §4.5 | B 轴维度切换族（B01–B03、B24–B25、B28、B30–B32）· D33 跨维度锚 · I03 I04 I15 I21 |
| 要留人（钩子、收藏、回看、评论） | SKILL Step 8；观众参与交 `participation-design` | X01 X05 X07 X08 X09 X13（X 不单用，要配 A / B / D 动词） |
| 太抽象 / 看不懂 | SKILL「When the user rejects the winner」 | E12 · E03 |
| 太冷 / 没感觉 | feel.md §一 | K02 · K05 · E26 |
| 像 AI 做的 / 见过 | feel.md §四 | cliché blacklist · 退役条目 · 换 Axis A · Step 3 Invert（E13 E23 D28 C04）/ Let the medium fail（I11 K10 R15 E27） |
| 做不出来 | — | feasibility flags · 制作路由判据 |
| 字和数要准 | 制作路由判据（字与数走代码） | G22 · Q01 · O20 · X16 · feasibility flags「A36 / G-axis」行 |
| 声音单薄 | feel.md §三 | H16–H20（声音设计）· H21 H22（接缝） |

---

## Axis A — Material / medium (what the world is made of) · A01–A45

A01 Cel / 赛璐璐分层  
A02 2D digital paint  
A03 Limited animation (口型动、身体冻)  
A04 Rotoscope  
A05 3D CGI realistic  
A06 3D stylized (Pixar-like)  
A07 NPR / toon shader  
A08 Voxel / Minecraft cubes  
A09 Low-poly  
A10 Claymation  
A11 Puppet + armature  
A12 Replacement faces (3D-printed plates)  
A13 Object animation (everyday things)  
A14 Pixilation (真人当定格)  
A15 Paper cutout  
A16 Silhouette / 剪影 (Reiniger)  
A17 皮影  
A18 剪纸 / 窗花  
A19 折纸 / 立体书 pop-up  
A20 Sand on lightbox  
A21 Paint-on-glass  
A22 Clay painting (Joan Gratz)  
A23 Pinscreen  
A24 Charcoal erase-rebuild (Kentridge)  
A25 Drawn-on-film / scratch (McLaren, Lye)  
A26 水墨宣纸  
A27 工笔重彩  
A28 敦煌壁画动起来  
A29 木版年画 / 浮世绘  
A30 Collage / photocollage (Gilliam)  
A31 Embroidery / felt / wool  
A32 针孔 / 蓝晒 cyanotype 逐帧  
A33 Risograph / 网点印刷  
A34 Pixel art / dither  
A35 ASCII / terminal  
A36 Kinetic type as the only actor  
A37 Data viz (axes, particles, charts)  
A38 Volume render / MRI-CT 切片  
A39 Architectural BIM / exploded CAD  
A40 UI / diegetic HUD 世界  
A41 Game engine cinematic (Unreal NPR)  
A42 Photogrammetry / Gaussian splat  
A43 Light painting / long exposure  
A44 Projection mapping onto objects  
A45 Mixed live-action + animation composite  

---

## Axis B — Space / dimension · B01–B32

B01 3D 压扁成 2D（透视塌缩、角色变成贴纸）  
B02 2D 鼓成 3D（纸片充气、线稿挤出厚度）  
B03 正交投影 ↔ 透视来回切  
B04 等轴测 isometric 世界  
B05 一点透视走廊隧道 — 退役 2026-09-05（装饰无动词；仅当它本身就是文本的内动词时可用，见文末「退役条目」）  
B06 鱼眼 / 超广角几何夸张  
B07 反透视 / 不可能建筑 (Escher)  
B08 展平：球面世界摊成地图  
B09 折叠：地图折回地球  
B10 剖视 cross-section  
B11 爆炸图 exploded view  
B12 透视穿墙 / x-ray  
B13 多层玻璃 / 多平面 (Disney multiplane)  
B14 舞台侧翼 / Forced perspective 微缩  
B15 倾斜地平线 Dutch  
B16 环形城市围住主体（Spider-Verse 坠楼）  
B17 尺度跳：微距 ↔ 行星 (Powers of Ten)  
B18 Droste / 画中画无限嵌套  
B19 镜像世界对折  
B20 莫比乌斯 / 克莱因瓶空间  
B21 2.5D 纸剧院（层间视差）  
B22 正反面：翻面看到另一套空间  
B23 重力方向改写（墙变地板）  
B24 景深塌成一张剪纸  
B25 立体变成阴影再变成立体  
B26 Z-depth 切片像 CT 扫过  
B27 全景 360 被裁成一条胶片  
B28 屏幕是窗户，镜头穿过去换维度  
B29 角色存在于 UI 层，背景是 3D  
B30 角色是 3D，特效是手绘 2D（Spider-Verse FX）  
B31 两视图双读：同一三维体正看读作 A、侧看读作 B，原地转四分之一圈就是论证（横看成岭侧成峰；转一次、停住，不来回转）  
B32 页面倒地：正对观众的一页（字墙、图表、地图）以底边为轴向后倒成地面，下一件事在这片地面上发生（内容倒、镜头锁死，A 线可用；F19 的锁机位版）  

> 维度切换族：B01–B03、B24–B25、B28、B30–B32。维度切换必须有跨维度锚（D33），见 feel.md §七；转场用法见 [transitions.md](transitions.md)。

---

## Axis C — Time · C01–C28

C01 实时  
C02 升格慢动作  
C03 降格快放 / 延时  
C04 倒放  
C05 子弹时间 / time-slice 环绕冻结  
C06 一帧里叠多种速度（有的人冻、有的人走）  
C07 循环 loop / GIF 逻辑  
C08 回文 palindrome（正放接倒放无缝）  
C09 时间层叠：过去残影留在现在  
C10 时间卷轴：横移等于年代  
C11 一镜到底（空间连续假装时间连续）  
C12 跳切 jump cut 当呼吸  
C13 动画在 2s（每帧持两格，漫画感）  
C14 动画在 1s（全流畅）  
C15 定格步进 vs 补间突然切换  
C16 时间冻结，镜头仍绕  
C17 时间流逝，构图钉死（同一机位早餐蒙太奇）  
C18 预知：未来残影先到，现在才跟上  
C19 记忆擦除：Kentridge 式残炭  
C20 时间晶体：同一动作不同年代并置  
C21 节拍即时间（每一拍生成一个物体，Gondry）  
C22 丢帧 / 胶片卡顿当风格 — 退役 2026-09-05（装饰无动词；仅当它本身就是文本的内动词时可用，见文末「退役条目」）  
C23 可变帧率：情绪高就掉到 8fps  
C24 昼夜在一拍里转完  
C25 年龄：同一主体连着长老再缩回  
C26 冲击帧：全片最重的字落地前插 1–3 帧反色/撞色全屏字形当视觉鼓点；一片一次、落反拍（H3 不写，合成层插帧）  
C27 反差硬切 smash cut：高点或长静之后一次改完所有大变量（一画布风格写成段首整屏重构，一片一次）  
C28 交叉剪辑 / 双栏交替：两个同时进行的过程来回切、越切越快（一画布风格写成左右两栏一次只动一栏）  

---

## Axis D — Transform / continuity · D01–D36

D01 连续形变 morph（轮廓插值）  
D02 拆成基本几何再重组成下一物  
D03 匹配剪辑 match cut（形/色/运动押韵）  
D04 动作匹配：手势跨镜头完成  
D05 图形匹配：圆硬币=圆月亮  
D06 颜色当向导（一条色带变成拉链）  
D07 替换 substitution（山=努力）  
D08 组合 combination（钟表眼）  
D09 运动即意义（下落=坠落感）  
D10 物体交换：A 的部件变成 B  
D11 液体 ↔ 固体（要原生演，见 SKILL）  
D12 线 ↔ 面 ↔ 体  
D13 正负形反转（Rubin vase）  
D14 生长 / 凋谢  
D15 分裂 / 融合  
D16 复制增殖（每一拍多一个鼓，Gondry）  
D17 侵蚀 / 风化  
D18 缝合 / 拆线  
D19 折叠纸艺变换  
D20 像素化 / 反像素化  
D21 矢量变照片再变矢量  
D22 文字变成它所表示的物  
D23 物变成它的名字  
D24 轮廓描一遍就换身份  
D25 遮罩揭示（iris, wipe, 墨晕开）  
D26 映射：把 A 的运动贴到 B 上  
D27 拓扑不变的形变（咖啡杯=甜甜圈）  
D28 误匹配：形似但意义相反，再纠正  
D29 渐变材质，形体不动  
D30 形体变，材质不动（同一木纹贯穿）  
D31 因果链：一倒全倒（牛顿摆式）  
D32 无缝循环变形回自身  
D33 同一身份重排：两状态之间相同元素保持身份滑到新位置，只有不同部分消失或长出；可跨维度（3D 字块→纸上扁平字块）。每次只一处，观众说得出"哪个没变"  
D34 光脉冲换态：整屏亮一档又落回，落回时已换状态、构图不动；亮必须有画内原因（揭晓、闪光、闪电）  
D35 全屏枢纽：一种材质或纯色先铺满整屏（雪花、雾、墨、暗面），在全屏态里换身份再收成新画面；枢纽要空  
D36 实体遮挡擦除：画里的实体掠过画面（前景物、船帆、笔刷、纸条），切口藏在遮蔽最满处；擦除者要有来路和方向  

---

## Axis E — Rhetoric / meaning · E01–E31

E01 可逆生命：活一下再冻成符号（icon→symbol）  
E02 迟到的容器：原子先出现，笼子后扣上  
E03 事物自己说话：不要激光笔，让它变色/变形  
E04 母题衰变：同一动作一次比一次残  
E05 字面化成语 / 歇后语  
E06 拟人，但只用领域零件当身体  
E07 换喻：工具代表制度（印章=帝国）  
E08 提喻：局部当整体  
E09 反讽：画面做旁白的反面  
E10 双关：一个形两读  
E11 证明式动画：画面让论点无法不信  
E12 延迟命名：先看见，后出现标签  
E13 错误预期再纠正  
E14 缺席：该在的东西不在，空位说话  
E15 幽灵叠加：起源轮廓半透明对齐  
E16 标本针 / 辅助线把活物钉死  
E17 规则显现：网格、五线谱、坐标轴长出来  
E18 规则崩塌：那些线自己折断  
E19 通感：把声音画成形状，把味道画成运动  
E20 寓言动物，但立刻回收成概念  
E21 过程当身份（不是「是什么」是「正在变成」）  
E22 不可逆：这一变回不去（隶变级）  
E23 可逆玩笑：变了又弹回  
E24 尺度幽默：大事用小道具演  
E25 神圣感：对称、慢、留白  
E26 滑稽感：弹性过冲、失误、自我修复  
E27 恐怖感：正确的形略错一点  
E28 信息图表逻辑（对比、因果、分层）当诗来用  
E29 标题序列逻辑：用一个符号概括整段（Saul Bass）  
E30 不可靠视觉叙述者：画面撒谎，后一秒招认  
E31 母题换义回归：同一物件多次回来，每次意思变，最后一次交给观众（区别于 E04 衰变、X08 只管结尾）  

---

## Axis F — Camera / viewpoint · F01–F27

F01 几乎静止，只呼吸式微推  
F02 主观镜头 POV  
F03 上帝正交俯视  
F04 虫视微距  
F05 一镜穿墙穿物  
F06 镜头是角色的眼睛，眨眼=切  
F07 镜头钉在物体上（object-locked）  
F08 环绕 orbit — 退役 2026-09-05（装饰无动词；仅当它本身就是文本的内动词时可用，见文末「退役条目」）  
F09 横移等同时间  
F10 竖移等同社会等级  
F11 变焦 vs 推轨冲突（Hitchcock dolly zoom）  
F12 手持不稳当纪录片  
F13 锁死三脚架，只有物在动  
F14 多机位同时（split 成漫画格）  
F15 画中画监控  
F16 穿过印刷网点进入照片世界  
F17 从截面滑进内部  
F18 镜头焦距当武器（一切虚化只剩一点）  
F19 倾斜直到墙变成路  
F20 摄影机在 2D 纸面滑动，突然有了视差  
F21 屏幕边缘是舞台口，入画出画  
F22 反打：我们发现自己在被看  
F23 无限推进直到质地变成另一套世界  
F24 固定机位长镜头，只靠调度  
F25 摄像机故障：过曝、滚轮快门、对焦呼吸当语言 — 退役 2026-09-05（装饰无动词；仅当它本身就是文本的内动词时可用，见文末「退役条目」）  
F26 甩镜接力 whip pan：快速横摇进拖影，下一镜同向同速落定；甩向一个视线或声音原因（B 线专用；A 线转译成内容整排平移）  
F27 视线切 eyeline cut：看 → 所看之物，方向一致、守轴线（一画布风格写成"朝向 → 所指处出现变化"）  

---

## Axis G — Graphic / print / type · G01–G23

G01 漫画分格长出来再溶解成连续时空  
G02 速度线 / 残影肢 / smear  
G03 网点 / 半色调  
G04 剖面线 hatching 自己在动  
G05 文字是建筑  
G06 文字是流体  
G07 字幕不是贴片，是场景里的物体  
G08 手写正在被写，写错，划掉  
G09 铅字印刷一格一格砸上  
G10 印章 / 邮戳 / 打孔  
G11 蓝图 / 工程图线自己装配  
G12 乐谱线变成地平线  
G13 地图图例变成真的地形  
G14 UI 组件拟物化成道具  
G15 图标演化（线性→面性→像素→emoji）  
G16 二维码 / 条码当纹理再解码成画面  
G17 报纸折叠露出下一版新闻（时间）  
G18 贴纸、胶带、修正液的物理层  
G19 徽章、纹章解体重组  
G20 字幕卡拉OK 变成切开世界的光  
G21 字形取景窗：一个大字/剪影当常驻的窗，窗外不动，窗里的世界按拍换；合法条件 = 窗里的东西正是这个字所指  
G22 字号即刻度：字的大小直接等于它代表的量（里程、人口、分量），全片同一换算；与 Q01 Isotype 互斥  
G23 场景物质成字：字由本场已有、叫得出名字的物质凝成（雨、雪、浪光、墨尘），读完按那种物质的物理还回去；通用发光粒子仍按黑名单  

---

## Axis H — Sound-image coupling · H01–H22

H01 口型同步对白  
H02 音画对位：声音说A画面做B  
H03 视觉音乐（Fischinger）：形状即旋律  
H04 每一鼓点增殖一个物体  
H05 音高=高度，响度=尺度  
H06 无声：突然抽走声音，画面继续  
H07 拟音可见（脚步砸出波纹）  
H08 歌词文字当角色演戏  
H09 声画错位：延迟 3 秒再对上  
H10 合成声刻在胶片齿孔上（McLaren）  
H11 环境声是唯一叙事  
H12 心跳/节拍器可见  
H13 噪声纹理=失真声音  
H14 对话变成字幕块碰撞  
H15 音乐结构当剪辑结构（主歌切镜，副歌一镜）  
H16 材质即音色：世界由什么做成，就发什么声（纸世界=笔纸摩擦，发光世界=电子嗡迹；换媒介=换整套音色板）  
H17 三层一件事：瞬态定帧 + 音色本体 + 短尾巴，听感仍是一个事件（元素落地=click+thump+微室内尾）  
H18 连发防机枪：同类事件重复时错拍/渐弱/微变调（七个格子=七声 staggered 渐弱，不是同一声×7）  
H19 静默当标点：关键定格前抽走所有 SFX，让旁白裸奔一句（对比即强调；深 boom 全片只许一次）  
H20 riser 预告 payoff：结论落地前 0.5-1 秒起一条上升音，正好在结论帧上解决（期待感的声学形状）  
H21 声音匹配：前一声化成后一声跨过切口（尖叫→汽笛、吊扇→旋翼），音色或音高相近（B 线 / 后期）  
H22 声音桥 / J-L 切：声音先于画面进入或拖进下一场，跨过一个或多个切口（B 线写进提示词；A 线只能装配时挪音轨）  

---

## Axis I — Hybrid / style-shift · I01–I21

I01 整段一种媒介，绝不换  
I02 情绪一变，画风突变（Yuasa / Mind Game）  
I03 现实层 2D，回忆层 3D，或反过来  
I04 手绘特效盖在 3D 上  
I05 实拍人物，世界是动画  
I06 动画人物，世界是实拍  
I07 油画逐帧（Loving Vincent）  
I08 胶片颗粒 / 超 8 / VHS 作为时代开关 — 退役 2026-09-05（装饰无动词；仅当它本身就是文本的内动词时可用，见文末「退役条目」）  
I09 Glitch / datamosh 当维度撕裂 — 退役 2026-09-05（装饰无动词；仅当它本身就是文本的内动词时可用，见文末「退役条目」）  
I10 Pixel-sort / RGB split 当冲击 — 退役 2026-09-05（装饰无动词；仅当它本身就是文本的内动词时可用，见文末「退役条目」）  
I11 漫画印刷出错：套准不准、漏色  
I12 游戏 HUD 死机，露出引擎线框  
I13 从故事板线稿「未完成」直接开演，再慢慢上色  
I14 风格按年代滤镜演进 — 退役 2026-09-05（装饰无动词；仅当它本身就是文本的内动词时可用，见文末「退役条目」）  
I15 每个角色一种媒介（人是剪纸，城是 3D）  
I16 同一镜头里左右两半不同媒介  
I17 AI latent walk 当融化 — 退役 2026-09-05（装饰无动词；仅当它本身就是文本的内动词时可用，见文末「退役条目」）  
I18 实拍定格 + CG 清理（Laika 式）  
I19 舞台纪录：能看见操作者的手  
I20 假纪录片访谈切开动画  
I21 二维画、三维光（Klaus 法）：形保持手绘平面，但接受同一盏灯的细亮边、接触阴影、环境遮蔽；一层统一颗粒跟着物体走（亮边写"细亮边"，不写 glow）  

---

## Axis J — Constraint games · J01–J16

J01 单色+一枚强调色  
J02 只有圆形  
J03 只有直线  
J04 机位永不移动  
J05 主体永不离开画面中心  
J06 十秒一镜零切  
J07 全片一个循环动作  
J08 只能用文字，不许画物  
J09 只能用物，不许出现文字  
J10 每句旁白只允许一个新元素  
J11 倒计时：元素被删到只剩一个  
J12 加法：每秒多一样，直到崩塌  
J13 对称强制  
J14 画框就是舞台，出画即死亡  
J15 全黑场，只靠光扫出形  
J16 全白纸，只靠折痕存在  

---

## Axis K — Motion craft used as meaning (Disney 12, inverted) · K01–K12

Not "animate correctly". Use the principle as the *idea*.

K01 Squash & stretch = 身份软硬（制度让它再也不能压扁）  
K02 Anticipation = 谎报：蓄力很久，结果没发生  
K03 Staging = 聚光只打在不该看的地方，再纠正  
K04 Straight-ahead vs pose-to-pose = 即兴 vs 被关键帧（命运）锁死  
K05 Follow-through = 身体停了，制度还在晃  
K06 Slow in/out = 开头结尾被拉长成仪式  
K07 Arcs =  mechanized 直线打破弧线（工业化）  
K08 Secondary action = 主论点不动，小东西把秘密说完  
K09 Timing = 同一动作三种时值=三种性格  
K10 Exaggeration = 真实世界做不到的一次形变，然后弹回可信  
K11 Solid drawing / volume = 2D 角色突然获得真实体积再被抽走  
K12 Appeal = 故意取消可爱，变成图示，再决定要不要还给它  

---

## Axis L — Magic effects (state-change grammar) · L01–L16

From Sharpe / Fitzkee / 52Kards: what the audience *thinks* happened. Native-render; do not film a magician unless the text is about magic.

L01 Production 从无到有  
L02 Vanish 从有到无  
L03 Transposition 两物互换位置  
L04 Restoration 毁了再完好（撕卡复原）  
L05 Levitation / 反重力  
L06 Penetration 穿过固体  
L07 Multiplication 一个变一群  
L08 Inanimate animation 死物自己动  
L09 Teleportation 这里消失、那里完整出现  
L10 Prediction 预言被画面兑现  
L11 Signed identity 被标记的那个回来了（不是仿品）  
L12 Saw-in-half 切开仍活 / 仍工作  
L13 Escape 从锁死的系统里出来  
L14 Misdirection 镜头/色/动把注意领走，真正的变在别处完成  
L15 Transformation-as-effect 变的是身份不是形状（和 D01 不同）  
L16 Will-bends-matter 意志改物（弯曲、折断、听话）  

---

## Axis M — Stage / performance traditions · M01–M20

M01 歌舞伎「见得」：动作冻成一张浮世绘  
M02 睨み：冻住时能量集中到眼睛  
M03 早替：一闪之间换装/换身份  
M04 黑衣 kurogo：约定「看见但不存在」的操作者  
M05 花道：主体从观众席里走出来  
M06 旋转舞台：世界转，人几乎不走  
M07 宙乘：吊威亚当公开的不可能  
M08 隈取：把怒、义、鬼画成脸上的血流方向  
M09 川剧变脸：内心状态瞬间换皮  
M10 京剧亮相：亮相=论证落地的一帧  
M11 水袖：情绪外化成长布，布就是运动  
M12 文乐：三个人操作一个偶，操作者在场且被当成空气  
M13 越南水傀儡：水面既是舞台又是遮挡  
M14 Wayang 影戏：只认影子，偶本身不可见  
M15 布拉格黑光剧：UV 下物体自己飞，人隐身  
M16 能剧面具：微转改变悲喜  
M17 提线外露：让线成为主题（控制可见）  
M18 对象剧场：椅子、鞋、灯自己演完一场戏  
M19 纸芝居：翻牌讲故事，翻本身是剪辑  
M20 长卷 / 手卷 cinema：横移等于读一段历史  

---

## Axis N — Physical / generative phenomena as look · N01–N22

N01 Cymatics / 克拉尼图形：声音站成立体几何  
N02 Ferrofluid：磁场长刺  
N03 Schlieren：空气被看见  
N04 Reaction-diffusion / 图灵斑：斑点自己长出来  
N05 L-system：规则递归成树  
N06 Physarum 黏菌：用时间寻路  
N07 Boids 集群  
N08 Cellular automata / 生命游戏  
N09 万花筒对称折叠  
N10 李萨如 / 示波器纯向量  
N11 频谱当地形  
N12 浑仪 / orrery：制度是一套齿轮天空  
N13 磁力线显形  
N14 晶体生长  
N15 金缮：裂痕用强调色修，伤变成纹样  
N16 锈/包浆：时间是一层材质  
N17 非牛顿流体 / 水冠慢镜  
N18 焦散 caustics 当建筑  
N19 生物发光  
N20 Cloud tank 染料云  
N21 频闪：连续运动被切成姿势雕塑  
N22 连续摄影叠印（Marey）：一条动作同时存在  

---

## Axis O — Info-objects, paper machines, object-pun · O01–O20

O01 Split-flap 机场翻牌：信息有重量和噪声  
O02 Cartogram：面积=数据，地图自己变形  
O03 Gapminder 气泡国：国家当会呼吸的点  
O04 Telestrator：解说线画在活的影像上  
O05 Variable font：字重/宽度轴=情绪轴  
O06 Slit-scan：把时间涂抹成一条空间（2001 星门）  
O07 终点线相机 photo-finish：胜负是一条时间切片  
O08 3D 西洋镜：雕塑被频闪唤醒  
O09 Volvelle 转盘书：旋转对齐才读得懂  
O10 Tunnel book：一层层透视的纸舞台  
O11 Rube Goldberg：因果被故意做得太机械  
O12 PES 物件双关：手榴弹切开是牛油果（形似+语义）  
O13 数据当角色（Rosling）：曲线有性格  
O14 机械跳表 / 计数翻页  
O15 算盘珠当粒子  
O16 八音盒滚筒：凸点=将发生的事件  
O17 战术回放：冻结、画线、再放行  
O18 即时代入：AR 越位线、球路迹变成世界里的真线  
O19 大字归档：每个关键项先整屏大字砸下，下一拍缩小飞进一侧清单成为一行；结尾清单本身就是收藏物（X06+X07 的连续动作；精确清单交代码）  
O20 参数扫动：画里一个看得见的参数手柄被拨动，世界连续按规律跟着变，拨到某点出现拐点；滑杆必须是文本里真实的变量，一片一个  

---

## Axis P — Make then unmake (ephemeral drawing) · P01–P12

Grammar: the picture's meaning includes its destruction. Do not copy sacred designs; steal only the *rule*.

P01 完成即销毁：最密的图案被一扫而空（沙坛城式无常，用抽象几何）  
P02 日日重画：同一门口每天新的一张，旧的被脚带走  
P03 一笔画闭合成环：不许抬笔，环=循环  
P04 点阵约束：只能绕点走线，点是法律  
P05 画给非人类看：米粒图案是给蚂蚁的路（功能先于观赏）  
P06 扫向中心：世界收成一撮灰，倒进流动的水里才算完  
P07 故意画错的商品版：真的那张不许被观看  
P08 从中心向外长，销毁时按相反顺序拆神名  
P09 对称是吉，破对称是事件  
P10 粉末介质：风/喷嚏是合法的结局  
P11 临时性是功德：保存下来反而失败  
P12 观看者必须踩过它才能进门  

---

## Axis Q — Notation that becomes the world · Q01–Q20

The score/diagram is not a caption. It *is* what happens.

Q01 Isotype：多=同一图标重复计数，禁止放大图标  
Q02 奥运 pictogram 网格：四肢只许 45°/90°  
Q03 IKEA 说明书：爆炸步骤是唯一语言，不许英雄透视  
Q04 Minard 拿破仑图：路径粗细=人数，地理服从损失  
Q05 Sankey：流量是有宽度的河  
Q06 图形乐谱（Cardew Treatise）：形状被演奏，每次演出不同  
Q07 Siteswap：数字就是抛接，数字对了球才合法  
Q08 Jacquard 穿孔卡：孔先于布，布是孔的兑现  
Q09 钢琴纸卷：未来是迎面而来的一排孔  
Q10 费曼图：粒子是线，相遇是顶点  
Q11 句法树：句子自己长出树枝  
Q12 进化支序图：分歧是时间  
Q13 安全须知卡片：最坏情况用最简人形演一遍  
Q14 棋盘评估条：谁要赢，条就倾斜  
Q15 Nightingale 玫瑰图：楔形面积=代价，一年围成一圈  
Q16 乐谱生命线：一条贯穿全书的横线是读者的命  
Q17 地图不是地形而是力：棍=涌浪，壳=岛（stick chart 语法）  
Q18 装配动画：零件按编号自己找到孔  
Q19 小多图 small multiples：同一构图邮票阵列，只改一个变量  
Q20 Sparkline：词级小图嵌在句子里呼吸  

---

## Axis R — Perception, darkroom, analog program · R01–R24

R01 Ames 屋：走几步人就巨/矮，地位是透视谎言  
R02 Troxler：盯着不动，周围的论点自己消失  
R03 中空面具错觉：凹的脸看起来是凸的  
R04 视差消失 / 变化盲：变了你没看见  
R05 太阳化 solarization：曝光过头，边缘镶银，正负颠倒  
R06 物影摄影 rayograph：没有相机，东西自己印在光里  
R07 拍立得显影：意义在两分钟里从灰雾里长出来  
R08 接触印样 / contact sheet：时间铺成格子，红圈才是被选中的命运  
R09 胶片倒计时 leader：电影还没开始，倒计时就是主体  
R10 SMPTE 彩条 / 测试卡：校准失败变成美学  
R11 Lumia / Clavilux：无声的光当第八艺术，不是 MV 可视化  
R12 水印：对着光才出现的第二套图像  
R13 防伪微缩文字：放大才承认还有一层法律  
R14 Auxetic：越拉越宽（负泊松比，反 Disney 压扁）  
R15 形状记忆：加热/冷却，它自己回到上一身份  
R16 Demoscene plasma：色彩场自己呼吸 — 退役 2026-09-05（装饰无动词；仅当它本身就是文本的内动词时可用，见文末「退役条目」）  
R17 Rotozoomer：一张贴图旋转缩放成隧道 — 退役 2026-09-05（装饰无动词；仅当它本身就是文本的内动词时可用，见文末「退役条目」）  
R18 伪 3D 地砖：只有透视网格在跑 — 退役 2026-09-05（装饰无动词；仅当它本身就是文本的内动词时可用，见文末「退役条目」）  
R19 Metaball：圆融合成一滩活的体积  
R20 铜栏 raster bars：扫描线本身是角色 — 退役 2026-09-05（装饰无动词；仅当它本身就是文本的内动词时可用，见文末「退役条目」）  
R21 变形透视 anamorphosis：只有一个站位画面才合法  
R22 Pepper's ghost：45°玻璃里的人是反射，不是实体  
R23 暗箱 camera obscura：房间自己是相机，世界倒立进来  
R24 无限镜：两面镜子把一次复制成深度

---

## Axis S — Time as matter, body as timeline · S01–S18

S01 年轮：时间是一圈圈的物质  
S02 冰芯：气候被冻成一条透明柱  
S03 地层：上下=古今，断层=事件  
S04 化石压扁：活的 3D 被地质压成 2D（字面维度损失）  
S05 琥珀：运动被树液暂停  
S06 等高线起立：地图长出真的山  
S07 日晷表针：影子是唯一的演员  
S08 时区切开屏幕：同一动作在相邻格里差几小时  
S09 时装自行演化：一件衣服当众走过一百年（Chalayan 语法）  
S10 记忆合金裙撑：温度一变，廓形换年代  
S11 日界线：跨过一条经线，日期被加一天或删一天  
S12 物候钟：先开花的树比日历更准  
S13 年号改元：墙上的纪年突然换一套，人还在走  
S14 影调分离 / 多重点测：一张脸里有好几个时代的光  
S15 航拍变倾斜移：巨物变模型，模型变巨物  
S16 树被锯开才读得懂它的一生  
S17 潮汐：建筑的脚被周期性删掉  
S18 日食：世界被咬一口，咬痕移动  

---

## Axis T — Writing that is not yet language · T01–T19

Marks, codes, and anti-writing. Do not fake sacred scripts; steal the *rule*.

T01 无语义书写 asemic：姿态是字，字读不出  
T02 复写本 palimpsest：刮掉仍透出上一层法律  
T03 涂黑诗 blackout：删到只剩一句真话  
T04 图形诗 calligram：字排成它所写的物  
T05 牛耕式 boustrophedon：一行往右一行往左，方向=劳作  
T06 谚文拼装：零件是音素，拼合才发声  
T07 楔形按进泥：意义是凹进去的，凸出来是假的  
T08 甲骨裂纹：问的问题被火回答成缝  
T09 结绳：结的位置和方向是数，剪断=删档  
T10 盲文凸起：必须摸，看是作弊  
T11 旗语 / 灯语：身体角度才是字母  
T12 莫尔斯：亮灭的时间就是字  
T13 速记：只留下骨架，元音是空气  
T14 隐写：加热或紫外才现形（和透光水印不是同一件事）  
T15 活字排队：每个字是一块铅，句子是队列  
T16 红笔审稿：删除线比正文更有权  
T17 暗号轮：对齐才可读，错一格全是噪声  
T18 夹注造反：行间小字自己长成主文  
T19 字出列：一行字（字块、活字、卡片）里一个字离队独自演剧情，句子留下空位仍可读；一行只许一个、且是承载转折的那个  

---

## Axis U — Craft grammar (textile, wood, kitchen) · U01–U16

Process as transform. Native-render the *rule*, not the factory tour.

U01 扎经：图案在织之前就染，错位是风格  
U02 绞缬：捆住的地方拒绝颜色  
U03 蜡防：蜡是暂时的法律，煮掉才完成  
U04 刺子绣：补丁的针脚变成纹样  
U05 条纹叙事：每条织带一种句子，缝合才成篇  
U06 榫卯：无钉，凹凸互为句子  
U07 千层折叠：折叠次数=体积，偷懒就塌  
U08 调温曲线：错一度表面就起霜  
U09 褐变：时间把颜色烤进结构里  
U10 薄膜包住液体：软的东西穿上固体的戏服  
U11 发酵：看不见的群体把面举起  
U12 烟熏沉积：气味变成一层颜色  
U13 木拼花：碎片拼回一个假的整体  
U14 缺席当模具：走掉的形状把空腔留给下一物质  
U15 铅条强迫：碎片被线框强制成为一幅画  
U16 窑变：同一配方，火给不同的脸  

---

## Axis V — Play / rule systems as space · V01–V16

The rules *are* the set. Not HUD decoration.

V01 围空：不占格子，占被围住的气  
V02 精妙尸体：每人只看见接口，整体事后才合法  
V03 事件谱：一句话指令=整场动画  
V04 缺字母：全世界不许出现某一个形  
V05 心情漫游：地图服从心情，不服从街道  
V06 全景敞视：一个人看见所有格子，格子互相看不见  
V07 洗牌成句法：随机顺序变成命运的语法  
V08 禁手：同一点不能立刻回去  
V09 棋钟：思考消耗物质化的时间  
V10 残局：只剩几子，规则变得更残酷  
V11 规则可改：玩家改规则的那一步才是高潮  
V12 错位拼图：块是对的，图是错的  
V13 多米诺：倒下是唯一被允许的动词  
V14 魔方：表面乱了，群还在  
V15 弹珠台：倾斜和弹性是法律  
V16 纸上建筑：画出来的房子比盖出来的更真  

---

## Axis W — Life process as clock · W01–W14

Biological verbs as animation grammar. Not lab footage.

W01 对齐再一分为二：信息均分，两份都完整  
W02 故意不均：拆牌产生多样性  
W03 自我拆包：整齐收成可回收的小包，不是爆炸  
W04 自噬：饿的时候吃掉自己的旧零件  
W05 光校准：光一来，整座城的钟对准  
W06 物候：花开顺序就是日历  
W07 蜕皮：旧身份成了一张透明的壳  
W08 共生：两种完全不像的东西共用一套循环  
W09 趋性：没有脑子，只有朝光/朝糖的斜率  
W10 瘢痕地图：修的时候写下不可逆的路  
W11 通行证：自己的形状放行，异己被贴标签  
W12 突触修剪：用得少的连接被删，剩下的变粗  
W13 冬眠：代谢降到几乎静止，外面的时间飞  
W14 回声定位：世界是反弹回来的形状

---

## Axis X — Attention / retention grammar · X01–X16

Structural operators for series knowledge video. They shape *when* things happen, never *what the look is* — always combine with a real A/B/D verb, never ship X alone. 以下是观众结构的可选方法；旧版平台权重/阈值无一手核实依据，已撤回，不能作为创作要求。

X01 钩子帧：第 1 秒的画面自己就是一个问题（悬空的半个字、没有影子的物体、多出一格的表格）  
X02 认知反差开场：先演"你以为的"，1 秒内画面自己反驳（你以为横是平的——放大镜下它在爬坡）  
X03 好奇心缺口：先给结果后给原因（先看到七个"马"字打架，再解释战国异形）  
X04 结论先行：金句第一句就说完，正片是"为什么这句话是真的"的证明过程  
X05 微高潮节拍：每 15-20 秒一次小 payoff（一次变形完成、一次对比揭晓、一枚印章落地）  
X06 进度锚点：画面里有一条可感知的进度线（演变链、倒计时、填充中的容器），观众知道"还剩多少"  
X07 收藏物：片中生成一件值得存下来的东西——规则卡、对照表、口诀、清单；它在结尾完整亮相一次  
X08 回环收束：结尾画面回到钩子帧，但已被正片改写（同一格子，字已换代）  
X09 评论钩子：片尾留一个可辩论的开放题或二选一（"你的名字里有生僻字吗"）——诚实的，不是标题党  
X10 系列缺口：本期结尾露出下期钩子帧的 1 秒残影（追剧机制）  
X11 搜索词可视化：把观众会搜的那句话变成片中实物（概念卡=可搜索的词条）  
X12 参与感：让观众的手进入画面逻辑（长按点赞图标会变形、暂停找茬）  
X13 峰终定律：最强的一次画面放在结尾前一拍，最后一拍安静收束（观众记住峰值和结尾）  
X14 信息差递进：每回答一个问题就抛出一个更深的问题，答案永远比问题慢半拍  
X15 时间承诺：开场画面暗示"这只要一分钟"（进度环、倒计时），降低划走冲动  
X16 具身比例尺：把抽象数字换算成观众身体能感受的量（心脏一生跳动次数=一条从北京到上海的点线）

---

## Native-render cheat sheet

Same inner verb, different Axis A. Never shoot the industrial literal unless the text is about that industry.

| Inner verb | MG / 矢量 | 定格黏土 | 水墨 | 3D CGI | 文字运动 |
|---|---|---|---|---|---|
| 凝固 / 冻住 | 填色拍实、描边锁死、过冲回弹停止 | 黏土变硬、指纹冻在表面 | 晕染停、水干、焦墨定 | motion blur 消失、拓扑冻结 | 字母对齐基线，不再跳 |
| 熔化 | 色块塌成圆角，锚点减少 | 黏土塌、失去骨架 | 墨再次化开 | 布料/软体解算 | 字失核，成一滩 |
| 3D→2D | 透视线收成正交，厚度变描边 | 偶被压成剪纸 | 皴法变平涂 | 法线拍平，变成 sprite | 立体字压成铅字 |
| 铸造 | 色块「浇」进轮廓，冷却=填充完成 | 按进模具再揭开 | 一笔填满空心描 | 布尔并集，接缝消失 | 字从模具铅块里弹出 |
| 生长 | 路径 trim 画出 | 逐帧加泥 | 浓破淡、加叶 | 置换/生长着色器 | 字重从 Thin 到 Black |
| 撕裂 | 形状路径裂开 | 真的撕纸 | 纸纹裂 | 布料撕裂解算 | 字被字距撑破 |
| 消失 | 锚点收到零，不淡出 | 被手盖住揭开已空 | 化进纸里 | 缩成一点光 | 字距收到叠成一条 |
| 变脸 | 色块瞬间换填，轮廓不动 | 替换脸片 | 同一轮廓换皴 | blendshape 或材质拍换 | 字重/字形轴跳一档 |
| 时间涂抹 | 物体按扫描线错帧 | 黏土被拉成条 | 墨被刮出彗星尾 | 顶点按 Y 取不同时间 | 字母上下半截来自不同字 |
| 完成即毁 | 图案 trim 画完立刻 reverse 擦掉 | 沙盘一刷 | 水洗宣纸 | 粒子收进一点 | 字逐个退格 |
| 多=重复 | 图标复制，尺寸锁死 | 同一件小物摆一排 | 同一印章盖 n 次 | instance 阵列 | 同一字复制 n 个 |
| 越拉越宽 | 描边外扩，面积增加 | 泡沫黏土横胀 | 墨晕横向吃纸 | 负泊松比材质 | 字距和字重同时加大 |
| 删到一句 | 遮罩吃掉图形只留路径 | 泥被刮走只剩轮廓 | 淡墨被浓墨盖死 | 布尔差集 | 涂黑诗只留关键词 |
| 无钉咬合 | 路径布尔互锁 | 两块泥凹凸对上 | 飞白与浓墨嵌合 | 布尔并集无缝 | 偏旁互锁成字 |
| 对齐再分 | 锚点对中再复制 | 一块泥被刀均分 | 一墨点裂成两滴 | 网格对称切开 | 一个字拆成两个偏旁 |
| 换场 | 原位替换 / 全屏枢纽 | 手盖住再揭开 | 墨晕满再收 | 子框推穿 | 字成为新画面的结构 |

---

## 转场语法速查（按机制索引；整片模式 A.5 / B.7 定 transition grammar 时用；写法与判据见 [transitions.md](transitions.md)）

| 机制 | 什么在换 | 编号 | A 线（锁机位、零剪辑） |
|---|---|---|---|
| 物质接力 | 同一种物质换形成下一物 | D01 D02 G06 G23 | 能 |
| 平面翻成空间 | 页倒成地、平面鼓起 | B32 B02 F19 | B32 能，F19 不能 |
| 空间压成平面或线 | 侧转成线、透视塌缩 | D12 B01 B31 | 能 |
| 字形 / 轮廓当门 | 穿过一个字进入下一世界 | B28 F05 G21 | 改成"子框放大吞没画面"才能 |
| 形状押韵 | 圆→圆、白球→月 | D03 D05 | 同画布原位替换能；跨画面要剪辑（B） |
| 物体当 iris | 本场最大的物胀满成下一场底色 | D25 | 能 |
| 全屏枢纽 | 铺满→在全屏态换身份→收成新形 | D35 | 能（推断，待测） |
| 光态 / 光脉冲 | 同一布景，光一拍变 | C24 K03 D34 | 能（块面事件） |
| 身份重排 | 同一组元素换位、换维度 | D33 I03 | 能（字面交代码） |
| 尺度连续 | 局部↔整体、收缩后才认出 | B17 B18 F23 | 能（内容缩放） |
| 拍点蒙太奇 | 容器不动，内容按拍换 | G21 H15 C21 | 换得比 1.2 s 快就交代码 |
| 反差 / 并行 | 撞击、两线交替 | C27 C28 | 段首整屏重构 / 双栏 |
| 运镜类 | 甩、推穿、rack focus、视线切 | F26 F05 F18 F27 | 转译（内容平移 / 子框放大 / 明度层切换 / 朝向→所指处） |
| 声音类 | 声音匹配、声音桥、静音后硬落 | H21 H22 H19 C26 | B 线或后期 |

**已有编号的转场补充写法（2026-10）：** D01 当转场＝背景不变、特征点对齐，两个半透明形同时在＝失败 · D03 含"概念押韵"，判据是不靠字幕也补得出 · D04 动作中段切、下一镜从下一帧接；旋转对位属此 · D05 匹配要被准备（物先变状态才成匹配形：剥开才是白球）；A 线写原位替换 · D06 向导物是块面点，细线测不到 · D12 侧转成线当转场：这条线是下一画面的第一笔 · D22 当转场只做整词出现/换色，字形变形交代码；"字走痕在" · D25 收窄：遮罩形状本身要有意义，几何 iris/星形只是换场（归黑名单）；物体本身当 iris · C11 藏切四法：暗、糊、遮、同框 · C12 一画布：原位跳位 · C17 同位置不同时代是一画布最自然的转场 · C24 换光不换景当段落分界 · B02 外轮廓连续只变厚度 · B17 揭示型：收缩到最小才认出 · B18 推进一轮回到起始构图＝X08 · B28/F05 门必须是语义上的门，否则是黑名单 zoom-through；A 线写子框放大 · E15 匹配叠化在 A 线写成原位换态 · F18 平面媒介等价物＝明度层级切换 · F21 跨接缝方向与速度一致 · F23 推进到的子框内部要空 · G13 图表几何是场景骨架，数值不许改 · D16 计数曲线先慢后快、刹停、最后一个数停最长 · H19 重音按本片需要，不强制三次或三幕位置 · X08 A 线回扣保留身份与动作锚，写明结果改变。

---

## 制作路由判据（H3 / 代码 / 混合；Step 4 选路由时用）

| 判据 | 走代码（Remotion / three.js / CSS） | 走 H3 | 混合怎么拼 |
|---|---|---|---|
| 画面上的字与数 | 准确中文、>2 个文字对象、小字、会变的数 | 大字标签 ≤2、每个 ≤4 字；伪字纹理 | H3 出伪字纹理，代码叠可读字 |
| 时间精度 / 密度 | 帧级事件（冲击帧）、间隔 <1.2 s、>1 个 / 1.5 s | 间隔 ≥1.2 s、每段 ≤6 个时间码 | 密集事件放代码层，H3 对应句写（静止） |
| 有机材质（雨雾水墨云光毛发） | 要写着色器，易廉价 | **舒适区** | H3 出底片，代码只加字与遮罩 |
| 大量刚体与计数 | 物理离线烘焙，数量精确 | 数量读不清时可 | 数量是论点 → 代码 |
| 相机 | 任意 | A 线锁死；B 线可动 | 混合段只有一个相机 |
| 遮罩 / 布尔转场（字形窗、穿〇） | 精确 | 单张静态可 | 代码遮罩，窗里放 H3 素材 |
| 跨段一致性（同一字块、累计读数） | 天然一致 | 跨段会漂（P-004） | 要"认出来"的东西交代码 |
| 改一个字的成本 | 秒级重渲 | 一段 768 + 2K 约 9 min | 易改的东西放代码 |

合成六条：只有一个相机 · 字只在一层（代码出字时 H3 提示词一个字名都不提，只描述留空区的光与质感）· 一条时钟（A 线 timing.json；无旁白线拍网格）· 对齐点写进交接（误差让代码去追 H3）· 底部五分之一留字幕 · 强调色同源（同一个值进 H3 风格块与代码主题，第一次出现两层同步）。本库（截至 2026-10-01）**没有承接代码层的 skill**，Remotion / HyperFrames 的 Node 依赖也没装（装要联网，先问用户）：代码层写到 treatment「制作路由与分层」块为止，由人或后续 skill 实现。

---

## Combination recipe

`Look = A (medium) + (B or D or E-verb or L or M or P or U or W) (the verb) + (C or F or G or H or I or J or K or N or O or Q or R or S or T or V, or E when it is not already the verb) (the twist)`

E-verbs are the rhetoric operators that *are* an action: E01 可逆生命, E02 迟到的容器, E04 母题衰变, E14 缺席, E21 过程当身份, E22 不可逆. The rest of Axis E and all of Axis K are twists.

For series knowledge video, add one structural pass: `+ X (when things happen)`. X never replaces the verb.

Examples of legal mixes:

- A26 水墨 + B10 剖视 + C19 残炭记忆  
- A36 纯文字 + D22 字成物 + J08 不许画物  
- A06 风格化 3D + B01 压扁 2D + I04 手绘特效  
- A15 剪纸 + D01 形变 + F13 锁机位  
- A09 低面 + D02 拆几何重组 + H05 音高=高度（原 I09 datamosh 已退役；撕裂改为几何面片按音高拆开）  
- A36 纯文字 + T03 涂黑诗 + J08 不许画物  
- A10 黏土 + U06 榫卯 + F13 锁机位（原 C16 时间冻结镜头仍绕与退役 F08 环绕同类，已换）  
- A26 水墨 + P01 完成即毁 + W03 自我拆包  
- A02 2D + E01 可逆生命（verb）+ E02 迟到的容器（twist）— 汉字象形马  
- A37 数据粒子 + J12 加法直到崩塌 + K01 squash 当价值被压扁  
- 锁定风格（A 锁定，例：深海 MG）+ D01 形变链 + X03 好奇心缺口 + X08 回环收束（结构以该风格 skill 的骨架与 hit-mechanics 为准）  
- A37 数据粒子 + Q05 Sankey + X16 具身比例尺（把流量河换算成人行道人流）

Illegal: A01+A10+A26 in one shot with no textual reason to hybridize. Also illegal: X01+X05+X07 alone with no A/B/D — retention grammar without a look is a listicle, not a film.

---

## Cliché blacklist（历史装饰症状表；有观看意义或风格依据时可用）

旧版新鲜度分数不再使用。下表用于追问“是不是未经选择的装饰”，不能只因某物/某运动在表中就禁止它。

| Family | Items |
|---|---|
| Idea / growth / connection | 灯泡=想法；火箭=增长；拼图块=整合；齿轮咬合=协作；握手；桥=连接；台阶/山峰=进步；钥匙开锁=解决 |
| Tech default（暗底发光家族） | 漂浮粒子；发光网络节点+连线；霓虹线条在黑底上生长；线框地球+弧线；数据隧道穿越；矩阵数字雨；HUD 悬浮 UI；电路板线路"长出来"；大脑+电路；DNA 双螺旋；光束扫描 |
| Logo / reveal | 粒子汇聚成 logo；粒子爆散；蓝图线稿"自己装配"成产品（除非 Q18 是内动词）；等轴测城市从地面升起 |
| Time / process | 沙漏；时钟指针飞转；日历翻页；打字机逐字；白板手绘的手；地图上插图钉+连线；多米诺当装饰（V13 当内动词除外） |
| Liquid / abstract | 墨滴入水（除非媒介是水墨且动词是化开）；金属液浇铸=历史；纸飞机=消息；折纸鸟=自由 |
| Camera default | 无理由的缓慢环绕；无理由的推进；镜头飞进瞳孔/钥匙孔换场景（Vox zoom-through，已饱和） |
| Motion habit（运动层陈词滥调，2026-09-05 增） | 所有元素同一缓动；等距级联入场（0.1 s 一个）；一直有东西在漂浮/呼吸的空闲循环；淡入淡出当转场；文字逐字打出或逐词弹跳；每个动作都回弹；随机微抖当手持；运动模糊当兴奋；bloom/glow 当光；音乐渐强宣告情绪；慢动作+逆光+剪影；几何 wipe / iris / 星形遮罩 / 百叶窗 / 翻页 / 相册滑动当转场；无画内原因的闪白闪黑；每拍都切每拍都闪；无锚的 2D↔3D 切换；3D 字无理由自转 |
| Look-as-filter（滤镜当意义） | glitch/datamosh/pixel-sort 当冲击；VHS/胶片颗粒当年代；风格按年代换滤镜；demoscene 效果（plasma、rotozoomer、伪 3D 地砖、raster bars）当视觉；AI latent walk 当融化；摄像机故障当语言 |

检查名词和动作是否提供观看证据。命中上表时追问用途；没有题意/风格依据才替换，不因不是原文字面名词或命中某运动就强制删除。

---

## Feasibility flags（AI 视频为主，2026-09 口径；命中 ≠ 禁用，命中 = 写对策）

历史风险索引来自本地普查与接缝研究，未在本轮重新运行对应模型。下表“强/可靠/便宜”与具体数字是旧样本/建议，不是当前工作流保证；需要准确事实、字形、数量、口型或身份时按当前工具与样片确认。

| Family | Flag | Mitigation |
|---|---|---|
| A36 / G-axis 文字当演员 | Text renders well (中文/假名/logo 可读) **if** explicitly asked for sharp edges; long text sequences drift between generations | Ask for 清晰锐利 in the style's own type / color rule (白字黑边、无衬线 only when the style is silent); ≤ 2 text objects per clip; lock exact strings; never rely on page numbers / small labels |
| Q01 Isotype / any exact count, Q02 grid pictograms, N08 automata | Counts and lattice regularity drift over 4–6 s | Keep count ≤ 7 or make the count *unreadable-by-design*; freeze the grid as a locked plate, animate only the delta |
| D01 morph, D27 topology | Silhouette-to-silhouette morph is strong; face / hand / text morph smears | Morph simple silhouettes; for faces use D24 (re-outline) or replacement (A12) instead of interpolation |
| C11 一镜到底 / F24 long take | Outdoor long takes and 8-shot single-prompt workflows lose precision after ~4 shots | Prefer indoor + locked camera; ≤ 4 shots per segment; chain segments by latent continuation (segment ≥2 `[Shot 1]` continues the last shot, new shot from 00:01.217); no `<Picture N>` / FL2VA on the H3 lines |
| H01 lip-sync, multi-speaker dialogue | Lip-sync desyncs after ~8–10 s; > 2 speakers scramble voice assignment | ≤ 2 speakers, ≤ 8 s of dialogue per clip, or no on-screen speech (narration with 嘴闭着) |
| B01/B02 dimension change, B10 cross-section, B17 scale jump | Reliable when the geometry is simple; hollow-object interiors invent detail | Describe the interior explicitly; cut the section as a single plane, not a bite |
| L-axis vanish / production / teleport | Strong when staged as hard state changes on a beat | Give it a transient (H17) and a frozen frame before and after; never a slow fade |
| I09 datamosh (retired — only when it is the text's inner verb, see 退役条目), R05 solarization, I11 misregistration | Models render "glitch" as decorative noise | Write it as a *physical* event (blocks hold, then smear along motion vectors), tie to a sound transient, one occurrence only |
| K-axis weight & timing, C13 on-twos | Default output is constant-velocity glide | Write anticipation → action → settle as shapes and relative speeds ("first quarter barely moves, then snaps"); durations only on non-timecode lines; "uneven beats, never a metronome"; ask for 2s stepping explicitly |
| Any operator on the H3 timecode / voice-first line | Locked camera; events ≲1.2 s apart merge; ≤15 s and ≤6 timecodes per segment; rich envelopes shift the timing compensation | See SKILL Step 7b (A line) / 7c (B line) (world-class.md §五); the rules and numbers are owned by `h3-storyboard-writing` §0 / §3 / §6 / §9 and `h3-director`「多镜头线出片」 |
| A20 sand / A21 paint-on-glass / A24 charcoal | Textures shimmer frame to frame | Accept shimmer as the medium *only if* the text is about impermanence; otherwise lock the substrate as a still plate |
| Photoreal A05 + one impossible thing | The impossible thing must obey light, shadow, grain, focus **more strictly** than its surroundings | Name the light source, contact shadow, focal plane and grain for the added element |
| Any join on the A line | Camera / cut words collide with the locked motion_rule | Only in-frame translations (原位替换、容器换内容、内容平移、子框放大、全屏枢纽); long changes split at stable intermediate forms; full-canvas recomposition at segment start (transitions.md §3; per-operator A-line wording in the §4 cards) |
| F26 / F27-B / H21 / H22 | No A-line equivalent | B line or post (装配挪音轨) |
| 代码动画（Remotion / three.js） | 有机材质要写着色器易廉价；物理须烘焙 | 有机材质交 H3；代码只做字、数、遮罩、刚体 |
| 混合合成（H3 底片 + 代码层） | 两个相机会漂；两层都画字会重复；两条时钟错位 | 一个相机、字只在一层、一条时钟；交接写对齐点与留空区（「制作路由判据」） |
| Any operator + "keep subject in frame" | Intent language is ignored | Use composition language (全身中景，脚在画面底部 10%) |

Non-AI production (2D / 3D / stop-motion) inverts several of these: text, counts and long takes are cheap; morphs and physics simulations cost time. 先确定实际制作路线，再记录能力依据、风险与待测，不做旧版可行性自评分。

---

## 退役条目 Retired operators（2026-09-05；编号保留，默认不选）

Retired because they are **decoration without a verb**: each is a *look* the generator or a plugin produces by itself, and (as of 2026-09) audiences read it as "an effect was applied", not "something happened". They are retired, not deleted — old treatments still resolve, and 可在有题意、观看任务或锁定风格依据时使用，尤其当 **operator 本身承担内动词** (a rap about tearing a label may still datamosh; a horror beat about "almost right" may still refuse to focus — examples 4 and 10 in examples.md are those literal cases).

| # | Operator | Why retired | Replace with |
|---|---|---|---|
| B05 | 一点透视走廊隧道 | AI 默认空间；隧道本身不做任何事 | B10 剖视 / B12 x-ray / F17 滑进内部 — 让空间被打开而不是被穿过 |
| C22 | 丢帧 / 胶片卡顿当风格 | 滤镜当年代或情绪 | C19 记忆残炭 / P 轴 make-then-unmake — 让时间在材料上留下痕迹 |
| F08 | 环绕 orbit | 镜头替内容制造动感 | F13 锁机位；或一次有原因的移动（craft pass Camera 行） |
| F25 | 摄像机故障当语言 | 故障是插件，不是表达 | E27 almost-correct / K02 犹豫 — 让"看不清"由物体的行为而非镜头产生 |
| I08 | 胶片颗粒 / VHS 作为时代开关 | 滤镜当年代 | 换材料而非换滤镜：A 轴内的纸种、墨种、印刷方式变化（G 轴） |
| I09 | Glitch / datamosh 当维度撕裂 | 生成器最爱的"冲击" | D02 拆几何重组 / L 轴状态变化 — 撕裂要有撕裂者 |
| I10 | Pixel-sort / RGB split 当冲击 | 纯装饰 | J01 单色事件 / 一次破色（feel.md §二） |
| I14 | 风格按年代滤镜演进 | 滤镜当叙事 | I01–I03 媒介真的更替（同一物在不同材料里重演） |
| I17 | AI latent walk 当融化 | 生成器副产品当风格 | D01 形变链（有起点、有终点、有原因的融化） |
| R16 | Demoscene plasma | 屏保 | N 轴真实物理现象（对流、扩散）作为色彩场的原因 |
| R17 | Rotozoomer | 屏保 | B17 尺度跳 / F23 无限推进（有嵌套逻辑的推进） |
| R18 | 伪 3D 地砖 | 屏保 | B04 等轴测 / Q 轴 notation-as-world（网格得是某种东西的网格） |
| R20 | 铜栏 raster bars | 屏保 | G 轴 print grammar（条纹得是印刷或织物的条纹，U 轴） |

Rule of thumb for future retirements: if an operator can be described entirely as "apply X" with no subject that does something, it belongs here.
