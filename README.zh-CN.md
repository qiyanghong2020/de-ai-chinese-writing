<div align="center">

<h1>de-ai-writing</h1>

<p><strong>面向中英文写作的 Codex 技能：减少模板味和机器抛光感，同时保留事实、证据与作者语气。</strong></p>

<p>
  <a href="README.md">English</a>
  ·
  <a href="https://github.com/qiyanghong2020/de-ai-writing/issues">问题反馈</a>
  ·
  <a href="#安装">安装</a>
</p>

<p>
  <a href="https://github.com/qiyanghong2020/de-ai-writing/stargazers"><img src="https://img.shields.io/github/stars/qiyanghong2020/de-ai-writing?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/qiyanghong2020/de-ai-writing/commits/main"><img src="https://img.shields.io/github/last-commit/qiyanghong2020/de-ai-writing" alt="Last commit"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/qiyanghong2020/de-ai-writing" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/Codex-skill-111827" alt="Codex skill">
  <img src="https://img.shields.io/badge/languages-English%20%7C%20中文-2563EB" alt="中英文">
</p>

</div>

`de-ai-writing` 是一个面向 Codex 的中英文去 AI 腔技能，用于处理过度结构化、空泛、重复、翻译腔明显或被模型“磨得太平”的文字。它适用于中英文论文、医学稿件、学位论文、邮件、申请材料、报告、产品文档和长篇概念性文章。

它不是 AI 检测绕过工具，也不靠机械替换同义词。技能会在保留事实、数字、引用、不确定性、文体和作者意图的前提下，处理真正造成模板感的表达与结构问题。

## 它能识别什么

- 模板化连接词和解释过满的脚手架
- 重复句式、对称修辞和过于均匀的节奏
- 缺少明确主体、动作、条件或后果的抽象表达
- 被抹平的作者语气，以及中英文翻译腔
- 表达很顺、但强度超过证据的学术措辞
- 长篇论文中的跨章节语义重复
- 没有分析功能的装饰性分类和概念换名
- Word 或其他长文流程中的结构敏感问题

## 修改示例

### English

> **Before:** Importantly, it is worth noting that self-verification plays a crucial role in enhancing trustworthiness; however, it cannot fully replace external validation.

> **After:** Self-verification can catch internal inconsistencies, but it does not establish external validity.

### 中文

> **修改前：** 值得注意的是，该结果进一步凸显了在实际应用场景中持续优化相关机制的重要性。

> **修改后：** 该结果说明，相关机制在实际应用前仍需继续优化。

目标不是把文字改得口语化或故意留下错误，而是删除没有信息增量的包装，同时保留原来的结论和证据边界。

## 安装

### 让 Codex 安装

向 Codex 发送：

```text
请使用 $skill-installer 安装这个技能：https://github.com/qiyanghong2020/de-ai-writing
```

安装完成后，该技能会在下一轮 Codex 对话中可用。

### 手动安装

macOS 或 Linux：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/qiyanghong2020/de-ai-writing.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/de-ai-writing"
```

如果同名目录已经存在，请先检查或更新现有版本，不要直接覆盖。

## 使用方法

通过 `$de-ai-writing` 显式调用技能。

### 一般改写

```text
请使用 $de-ai-writing 改写下面的内容，使表达自然、具体，同时保留全部事实、引用、数字和限制条件。
```

### 中文论文或医学写作

```text
请使用 $de-ai-writing 修改这段中文讨论。减少翻译腔、抽象套话和模板化连接词，但不要改变证据强度和医学术语。
```

### 英文学术稿件

```text
Use $de-ai-writing to edit this manuscript paragraph for natural academic English. Preserve the author's World English register and do not strengthen the claims.
```

### 长篇 Viewpoint 或 framework paper

```text
请使用 $de-ai-writing 先对这篇完整 Viewpoint 做全文结构审计。梳理中心命题在各章节的复现，列出 gate、state、tier 和 framework 等自创标签，识别分析增量不足的段落并提出压缩方案；不得误删必要的 Methods、Results、定义、限制或 Introduction–Conclusion 呼应。
```

## 长篇论文的结构级审计

有些 AI 腔不在单句，而在全文结构。对于用户明确授权的整篇稿件，技能可以：

1. 用一句话概括全文核心命题；
2. 建立跨章节的 thesis-recurrence map；
3. 检查每次复现是否增加了证据、限定条件、反例、操作后果或新推论；
4. 盘点 `framework`、`boundary`、`gate`、`tier`、`state`、`class`、`level`、`matrix` 和 `model` 等概念标签；
5. 为每个章节确定一个独立任务；
6. 先压缩没有分析增量的重复，再进入局部改写。

技能不会机械删除所有 taxonomy，也不会把正常的 Introduction–Conclusion 呼应当成冗余。只要一个分类确实改变解释、评价、决策或行动，就应当保留。

## 设计原则

- **先保意义。** 事实、引用、数字、比较方向、限制条件和不确定性不能被改坏。
- **尊重文体。** 医学讨论、产品 README 和工作邮件不应共享一种通用的“人类语气”。
- **中英文分开处理。** 不把英文写作习惯强行移植到中文里。
- **具体性优先。** 不靠错别字、俚语、轶事或虚构例子伪装成人工写作。
- **不承诺检测结果。** 文风不能可靠证明作者身份，AI detector 分数也不是优化目标。
- **不扩大授权范围。** 用户只要求修改一段时，不擅自重构全文。

## 仓库结构

```text
de-ai-writing/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── chinese.md
    ├── english.md
    ├── execution-patterns.md
    ├── markers.md
    ├── rewrite_patterns.md
    ├── risk_words_quicklist.md
    └── thesis-medical.md
```

`SKILL.md` 只保留路由和核心边界，具体的中英文规则与长文执行流程放在 references 中，使技能只加载当前任务真正需要的内容。

## 使用边界

- 不能根据最终文风确定某一段必然由人或 AI 创作。
- AI detector 结果不能作为确定性证据。
- AI 使用披露应根据真实工作流程和目标期刊或机构政策判断。
- 投稿或发布前，用户仍需核对修改后的内容。

## 许可证

本项目采用 [MIT License](LICENSE)。

## 参与改进

欢迎提交 issue 或 pull request。尤其欢迎以下内容：

- 事实不变、但表达明显更自然的中英文修改案例；
- 学术、医学、技术或职业写作中的领域特异性误判；
- 应当保留的必要重复或有效分类框架；
- 可以复现的长文处理边界案例。

请不要提交以操纵 AI detector 分数为唯一目的的规则。

---

如果这个技能帮你保住了内容、删掉了模板感，欢迎为[仓库点一个 Star](https://github.com/qiyanghong2020/de-ai-writing)。
