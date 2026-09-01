<div align="center">

<img src="assets/social-preview.png" alt="de-ai-writing：自然的中英文写作，保留证据，删掉模板感" width="100%">

# de-ai-writing

**面向自然、具体、有作者感的中英文写作；不改坏事实和证据。**

[English](README.md) · [完整案例](examples/README.md) · [安装](docs/installation.md) · [隐私](docs/privacy.md) · [使用条款](docs/terms.md) · [问题反馈](https://github.com/qiyanghong2020/de-ai-writing/issues)

[![GitHub stars](https://img.shields.io/github/stars/qiyanghong2020/de-ai-writing?style=social)](https://github.com/qiyanghong2020/de-ai-writing/stargazers)
[![Release](https://img.shields.io/github/v/release/qiyanghong2020/de-ai-writing?display_name=tag)](https://github.com/qiyanghong2020/de-ai-writing/releases)
[![Validate](https://github.com/qiyanghong2020/de-ai-writing/actions/workflows/validate.yml/badge.svg)](https://github.com/qiyanghong2020/de-ai-writing/actions/workflows/validate.yml)
[![skills.sh](https://skills.sh/b/qiyanghong2020/de-ai-writing)](https://skills.sh/qiyanghong2020/de-ai-writing)
[![MIT License](https://img.shields.io/github/license/qiyanghong2020/de-ai-writing)](LICENSE)

</div>

`de-ai-writing` 用于修改过度结构化、空泛、重复、翻译腔明显或被模型“磨得太平”的中英文文字，覆盖论文、医学稿件、学位论文、邮件、申请材料、报告、产品文档和长篇概念性文章。

它不是 AI 检测绕过工具，也不靠机械替换同义词。修改过程中，事实、数字、引用、不确定性、文体和作者意图都属于受保护内容。

## 30 秒看懂工作流

<div align="center">
<img src="assets/demo.gif" alt="约30秒演示：锁定证据、诊断重复、完成改写并审计长篇论文结构" width="900">
</div>

演示使用合成材料，没有上传任何真实稿件。

## 它与普通 humanizer 有什么不同

| 常见处理方式 | `de-ai-writing` |
| --- | --- |
| 删除所谓 AI 高频词和连接词 | 结合上下文判断词汇、结构、语气和证据问题 |
| 输出一种通用的“人类语气” | 中英文分通道，并保留合理的 World English |
| 追求 AI detector 分数 | 保留结论与不确定性，不承诺绕过检测 |
| 只处理句子和段落 | 检查跨章节语义重复、重复收束和低分析增量 |
| 把整齐框架都视为 AI 腔 | 只要分类改变解释、评价或行动，就保留 taxonomy |

## 快速安装

使用开源的 `skills` CLI：

```bash
npx skills add qiyanghong2020/de-ai-writing -g
```

也可以一次安装到 Codex、Claude Code 和 Cursor：

```bash
npx skills add qiyanghong2020/de-ai-writing \
  -g -a codex -a claude-code -a cursor -y
```

手动路径、项目级安装、更新和各客户端调用方式见[跨 Agent 安装说明](docs/installation.md)。

## 使用方法

### 一般改写

```text
请使用 de-ai-writing 修改下面的内容，使表达自然、具体，同时保留全部事实、引用、数字和限制条件。
```

### 中文论文或医学写作

```text
请使用 de-ai-writing 修改这段中文讨论。减少翻译腔、抽象套话和模板化连接词，但不要改变证据强度、统计量和医学术语。
```

### 英文学术稿件

```text
Use de-ai-writing to edit this manuscript paragraph for natural academic English. Preserve the author's World English register and do not strengthen the claims.
```

### 长篇 Viewpoint 或 framework paper

```text
请使用 de-ai-writing 先对这篇完整 Viewpoint 做全文结构审计。梳理中心命题在各章节的复现，盘点 gate、state、tier 和 framework 等标签，识别分析增量不足的段落并提出压缩方案；不得误删必要的 Methods、Results、定义、限制或 Introduction–Conclusion 呼应。
```

在 Codex 中可用 `$de-ai-writing`，在 Claude Code 和 Cursor 中可用 `/de-ai-writing`。当任务与技能描述吻合时，各客户端也可以自动调用。

## 完整案例

全部案例均为合成材料，并展示受保护信息、问题诊断、修改结果以及有意保留的内容。

| 案例 | 展示的关键判断 |
| --- | --- |
| [英文学术段落](examples/01-english-academic.md) | 不把观察性相关改写成因果结论 |
| [英文工作邮件](examples/02-english-email.md) | 让请求和截止时间清楚，同时保持礼貌 |
| [中文医学讨论](examples/03-chinese-medical.md) | 保留样本量、效应量、区间和研究设计边界 |
| [中文工作邮件](examples/04-chinese-workplace-email.md) | 删去程序化铺垫，不牺牲职业语气 |
| [30页 Viewpoint 审计](examples/05-viewpoint-structural-audit.md) | 建立命题复现图，合并装饰性概念标签 |
| [taxonomy 反例](examples/06-taxonomy-preservation.md) | 保留具有独立决策后果的分类 |
| [World English 保留](examples/07-world-english.md) | 提高清晰度，但不抹去场景化语域 |

## 工作方式

1. **锁定意义。** 先保护结论、数字、来源、比较方向和不确定性。
2. **选择通道。** 只在任务需要时加载中文、英文、医学/论文或长文规则。
3. **先诊断，再改写。** 区分词汇、结构、语气、证据和作者声音问题。
4. **在合适尺度上修改。** 处理局部段落；只有得到授权时，才先压缩全文重复再做句级润色。
5. **进行人工式复核。** 确认结果符合文体，没有新增事实，也没有强化结论。

详细规则放在 `references/` 中，Agent 按需读取，不会把大教程全部塞进入口文件。

## 长篇论文的结构级审计

对于已授权的全文任务，技能可以：

- 用一句话概括中心命题；
- 建立跨章节的 thesis-recurrence map；
- 判断每次复现是否增加证据、限定条件、反例、操作后果、新推论或失效边界；
- 盘点 `framework`、`boundary`、`gate`、`tier`、`state`、`class`、`level`、`matrix` 和 `model` 等标签；
- 为每个章节确定一个独立任务；
- 先压缩没有分析增量的重复，再进入句级润色。

技能不会机械删除 taxonomy、定义、Methods、Results、限制，也不会把正常的 Abstract–Introduction–Conclusion 呼应当成冗余。可查看[完整 Viewpoint 案例](examples/05-viewpoint-structural-audit.md)和[应保留 taxonomy 的反例](examples/06-taxonomy-preservation.md)。

## 隐私

这个仓库只是本地指令与参考文件，不提供托管改写服务，也不会自行收集稿件内容。你选择的 Agent 和模型仍可能按照各自政策处理输入文本。

不要把未发表论文、患者身份信息、保密审稿材料、凭据或法律敏感内容粘贴到未经审查的第三方在线 Demo。只有在服务运营方、模型与子处理方、数据留存、训练用途、删除渠道和事故责任均有明确说明后，仓库才适合接入这类入口。详见[隐私说明](docs/privacy.md)。

## 验证

运行仓库契约测试：

```bash
python -m unittest discover -s tests -v
```

只检查 Agent Skills 发现结果、不执行安装：

```bash
npx skills add . --list
```

测试覆盖前置 YAML、引用路径、核心边界、案例类型、全文审计能力、本地链接和机器可读的行为预期；不调用 AI detector，也不修改用户文档。

## 仓库结构

```text
de-ai-writing/
├── SKILL.md                 # 路由和核心边界
├── references/              # 中英文、医学和长文规则
├── examples/                # 七个完整案例
├── tests/                   # 契约测试和行为预期
├── docs/                    # 安装与隐私说明
├── assets/                  # 社交预览和演示素材
└── agents/openai.yaml       # Codex 界面元数据
```

## 使用边界

- 最终文风不能证明某一段由人或 AI 创作。
- AI detector 结果不能作为确定性证据。
- AI 使用披露应根据真实工作流程和目标期刊或机构政策判断。
- 用户只要求修改一段时，不擅自重构全文。
- 投稿或发布前，用户仍需核对修改后的内容。

## 参与改进

欢迎提交 issue 或 pull request，尤其欢迎：

- 事实不变、表达更自然的中英文案例；
- 学术、医学、技术或职业写作中的领域特异性误判；
- 应当保留的必要重复或有效分类框架；
- 可复现的长文边界案例和行为测试。

请不要提交以操纵 AI detector 分数为唯一目标的规则。早期参考和明确拒绝的处理方式见[设计来源说明](UPSTREAM.md)。

## 许可证

本项目采用 [MIT License](LICENSE)。

---

如果这个技能帮你保住了内容、删掉了模板感，欢迎为[仓库点一个 Star](https://github.com/qiyanghong2020/de-ai-writing)，也欢迎分享一个真正难处理的案例。
