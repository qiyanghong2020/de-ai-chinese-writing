<div align="center">

# de-ai-writing

**面向中英文论文的双语学术 humanizer。**

**保留证据，审计完整论证，不只替换几个词。**

[English](README.md) · [完整案例](examples/README.md) · [安装](docs/installation.md) · [隐私](docs/privacy.md) · [使用条款](docs/terms.md) · [问题反馈](https://github.com/qiyanghong2020/de-ai-writing/issues)

[![GitHub stars](https://img.shields.io/github/stars/qiyanghong2020/de-ai-writing?style=social)](https://github.com/qiyanghong2020/de-ai-writing/stargazers)
[![Release](https://img.shields.io/github/v/release/qiyanghong2020/de-ai-writing?display_name=tag)](https://github.com/qiyanghong2020/de-ai-writing/releases)
[![Validate](https://github.com/qiyanghong2020/de-ai-writing/actions/workflows/validate.yml/badge.svg)](https://github.com/qiyanghong2020/de-ai-writing/actions/workflows/validate.yml)
[![skills.sh](https://skills.sh/b/qiyanghong2020/de-ai-writing)](https://skills.sh/qiyanghong2020/de-ai-writing)
[![MIT License](https://img.shields.io/github/license/qiyanghong2020/de-ai-writing)](LICENSE)

</div>

`de-ai-writing` 是面向中文与英文稿件的双语学术写作润色工具，覆盖英文学术论文、中文稿件、医学写作、学位论文、邮件、申请材料和技术文档。它会保留事实、数字、引用、比较方向、证据强度、不确定性和作者语域，不会把不同作者的表达抹成同一种声音。

在用户明确授权全文处理时，它还可以审计长篇论文的结构：梳理中心命题在不同章节中的复现，识别概念换名和装饰性 taxonomy，并判断篇幅是否与证据和分析贡献相称。

它不是同义词替换器、AI 作者身份鉴定工具或 detector 绕过工具。

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

Claude Code 还可以通过插件市场安装：

```text
/plugin marketplace add qiyanghong2020/de-ai-writing
/plugin install de-ai-writing@de-ai-writing
/reload-plugins
```

运行重载命令后，技能会在当前会话中生效；也可以重启 Claude Code。

手动路径、项目级安装、更新和各客户端调用方式见[跨 Agent 安装说明](docs/installation.md)。

## 共同基线

可靠的写作技能应当保留原意、不编造细节、尊重作者声音、结合上下文判断问题，也不能把最终文风当成 AI 作者身份的证据。`de-ai-writing` 以这些要求为起点。

## de-ai-writing 增加了什么

| 增量能力 | 实际作用 |
| --- | --- |
| 中英文独立通道 | 按语言加载规则，不用同一套风格处理两种语言 |
| 学术与医学证据边界 | 保护统计量、因果上限、领域术语和各类论文章节的语域 |
| World English 保留 | 提高清晰度，但不把合理的本地或非母语语域抹成企业式美式英语 |
| 全文命题复现图 | 检查同一命题在不同章节的功能，不只数相邻段落中的重复词 |
| 框架与术语盘点 | 只有新标签没有改变解释或行动时才合并概念 |
| taxonomy 误判保护 | 分类会改变证据、决策或允许声称的内容时予以保留 |
| 贡献与篇幅审计 | 压缩没有分析增量的重复，不机械追求最短文本 |
| 作者身份与披露边界 | 将文风诊断与“谁写的”“披露是否充分”分开处理 |

## 30 秒看懂工作流

<div align="center">
<img src="assets/social-preview.png" alt="de-ai-writing：自然的中英文写作，保留证据，删掉模板感" width="100%">
</div>

<div align="center">
<img src="assets/demo.gif" alt="约30秒演示：锁定证据、诊断重复、完成改写并审计长篇论文结构" width="900">
</div>

演示使用合成材料，没有上传任何真实稿件。

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

普通技能安装后，在 Codex 中可用 `$de-ai-writing`，在 Claude Code 和 Cursor 中可用 `/de-ai-writing`。通过 Claude Code 插件安装后使用 `/de-ai-writing:de-ai-writing`。当任务与技能描述吻合时，各客户端也可以自动调用。

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

### 两个结构判断速览

**一篇重复的 30 页 Viewpoint。** 同一临床有效性命题出现在摘要、引言、局限、gate、evidence state、治理和结论中。审计保留必要的首尾呼应和具有操作意义的两个 gate，删除重复的 state 层，并合并两个功能重叠的治理分类。[查看命题复现图和压缩方案。](examples/05-viewpoint-structural-audit.md)

**一套应该保留的整齐 taxonomy。** technical、retrospective clinical 和 prospective clinical 三种状态分别允许不同的后续行动和声称范围。技能保留全部分类，只删除重复列举分类名称、没有新增后果的末句。[查看 taxonomy 反例。](examples/06-taxonomy-preservation.md)

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

## 实际验证了什么

运行仓库契约测试：

```bash
python3 -m unittest discover -s tests -v
```

只检查 Agent Skills 发现结果、不执行安装：

```bash
npx skills add . --list
```

仓库区分三种验证层级：

- **仓库契约测试**检查前置 YAML、版本一致性、引用路径、核心边界、插件清单、案例覆盖、本地链接和 fixture 结构。
- **行为/评估 fixtures**为合成案例记录受保护信息、预期判断、禁止结果和输出形式，可供人工或未来自动化前向测试使用。
- **这些测试没有执行模型端到端评估。** 测试通过不能证明所有 Agent 或模型都一定给出正确改写。

测试不调用 AI detector、付费 API 或外部改写服务，也不修改用户文档。详见[评估规范](evals/README.md)。

## 仓库结构

```text
de-ai-writing/
├── .claude-plugin/          # Claude Code 插件和市场元数据
├── SKILL.md                 # 路由和核心边界
├── references/              # 中英文、医学和长文规则
├── examples/                # 七个完整案例
├── evals/                   # 合成行为 fixtures，不是模型结果
├── tests/                   # 确定性的仓库契约测试
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

- **误判（false positive）：** 合理的表达、taxonomy、引用或必要重复被删改。请提供文体、原文、预期判断和实际结果。
- **意义丢失（meaning loss）：** 改写遗漏或改变事实、排名、同时性、效应方向、不确定性、限制、引用关系或适用范围。
- **长文案例（long-document case）：** 可复现的跨章节重复、概念换名、装饰性框架或贡献与篇幅失衡。请使用合成或可公开材料，并指出不同章节各自应承担的任务。

请不要提交以操纵 AI detector 分数为唯一目标的规则。早期参考和明确拒绝的处理方式见[设计来源说明](UPSTREAM.md)。

## 许可证

本项目采用 [MIT License](LICENSE)。

---

如果这个技能帮你保住了内容、删掉了模板感，欢迎为[仓库点一个 Star](https://github.com/qiyanghong2020/de-ai-writing)，也欢迎分享一个真正难处理的案例。
