---
title: "金融界的 Claude Code 来了"
created: 2025-05-10
updated: 2025-05-10
type: article
tags: [AI Agent, 金融科技, Claude Code, TypeScript, Bun]
sources: [raw/articles/dexter-financial-claude-code.md]
original_url: https://mp.weixin.qq.com/s/k7TeuWzNtiaa9RjOoZlqEg
author: 高老三聊AI
domain: mp.weixin.qq.com
---

# 金融界的 Claude Code 来了

> 来源：**高老三聊AI**
> 原文链接：[点击查看](https://mp.weixin.qq.com/s/k7TeuWzNtiaa9RjOoZlqEg)

---

## 二、Dexter 是什么？先建立全局视角

在聊 Dexter 的技术细节之前，我们先搞清楚它到底在解决什么问题。

传统 AI 金融工具的痛点是这样的：

你问 ChatGPT「苹果公司 2024 年营收增长驱动因素是什么」，它能给你一段听起来头头是道的分析——但那些数字很可能是编的，或者是过时的训练数据。金融领域，幻觉是致命的。

Dexter 的解法是：不要让 AI 「凭感觉」回答，而是让它真正去「查」，查完再「想」，想完还要「验」。

这就是它的三层架构：

用个更好理解的类比：Dexter 就像一个有巴菲特思维框架的新入职实习生，你给他一个问题，他会先列研究计划，然后去图书馆（数据库）查资料，查完自己对一遍逻辑，确认没问题再来汇报。

项目的核心配置文件之一是 SOUL.md——没错，是给 AI 写的「灵魂文档」，里面明确写着 Dexter 的投资哲学：

这不是花哨的 prompt engineering，这是在给一个会「自主决策」的 Agent 设定价值观。

---

## 三、技术拆解：Agent 架构到底怎么运转的？

了解了 Dexter 的定位，我们进入最核心的部分——它的 Agent 架构。

### 3.1 整体结构

Dexter 用 TypeScript + Bun 开发，基于 LangChain 构建 Agent 核心，用 Ink（React for CLI）渲染终端 UI。项目结构清晰：

```
src/
├── agent/       # Agent 核心：循环逻辑、上下文压缩、Scratchpad
├── tools/       # 工具集：财报数据、网页搜索、浏览器
├── skills/      # 技能扩展：DCF 估值等 SKILL.md 工作流
├── model/       # 多 LLM 提供商抽象层
├── memory/      # 记忆管理
└── evals/       # 评估套件（LangSmith）
```

### 3.2 Agent 循环：比你想的复杂得多

核心的 Agent Loop 在 `src/agent/agent.ts` 里，680 行代码，但逻辑非常清晰。每一轮循环做以下事情：

最多跑 10 轮（可配置），内置循环检测，不会失控跑飞。

### 3.3 上下文管理是亮点

这里有个工程细节值得展开——Dexter 实现了三层上下文管理策略，从轻到重依次是：

```
Microcompact（每轮检查：工具结果 >8 条，或总 token 估算 >80,000 时触发）
    ↓ 整体上下文超阈值
Memory Flush（把工具结果摘要写入本地记忆文件）
    ↓ 继续超阈值
Full Compaction（调用 LLM 生成一段上下文摘要，替换掉全部历史消息）
    ↓ 压缩失败兜底
Message Truncation（强制裁掉最老的几轮对话）
```

微压缩（Microcompact）并不是每轮都清理，而是每轮检查、按需触发：满足可压缩工具结果超过 8 条或这些结果 token 估算超过 80,000 任一条件才触发。触发后保留最近 4 条工具结果，其余替换为 `[Old tool result content cleared]` 占位符，不调用 LLM，极其轻量。

这个设计思路直接借鉴了 Claude Code 的上下文压缩机制，但在金融场景做了定制——因为财报数据往往很大，所以加了「大结果持久化」的逻辑，把超大工具结果写到本地 `.dexter/` 目录，不占用 LLM 上下文。

### 3.4 Skills 扩展系统

Dexter 有一套和它自身 SOUL.md 一脉相承的扩展机制：Skills。

每个 Skill 就是一个 SKILL.md 文件，包含 YAML frontmatter（name、description）和 Markdown 格式的操作说明。Agent 启动时自动扫描 `src/skills/` 目录，把所有 Skill 的元信息注入系统 prompt。

内置了两个 Skill：

你完全可以自己写 SKILL.md 文件，扩展 Dexter 的分析能力——Dexter 会在合适的时候自动调用对应技能。

---

## 四、工具箱：它能拿到什么数据？

Agent 再强，工具不行也是白搭。Dexter 内置了一套相当完整的金融数据工具链：

**财务数据（来自 FinancialDatasets API）：**

**信息检索工具：**

**技能调用（skill 工具）：** 每个查询最多触发一次，不会重复执行

**支持的 LLM 提供商**（通过 `/model` 命令随时切换）：
OpenAI（默认 gpt-5.4）、Anthropic、Google、xAI（Grok）、OpenRouter、Ollama 本地模型

---

## 五、透明是 Dexter 的核心竞争力

金融 AI 最让人不放心的一点就是「黑盒」——它给出答案，你不知道它经历了什么。

Dexter 的解法是 Scratchpad（草稿本）。每一次查询，所有工具调用的入参、原始返回、LLM 摘要都会写到 `.dexter/scratchpad/` 下的 JSONL 文件里：

```json
{
  "type": "tool_result",
  "timestamp": "2026-01-30T11:14:05.123Z",
  "toolName": "get_financials",
  "args": { "ticker": "AAPL", "period": "annual", "limit": 5 },
  "result": { ... },
  "llmSummary": "获取了苹果 5 年年度收入表，营收从 2740 亿增长到 3940 亿"
}
```

你可以像审计师一样逐条复盘它的推理过程。这在金融这个容错率极低的领域，是建立信任的关键。

---

## 六、WhatsApp 接入：随时随地的财务助理

这个功能我觉得相当有意思——Dexter 可以绑定你的 WhatsApp 账号，直接在聊天界面问它金融问题。

```bash
# 扫码绑定 WhatsApp
bun run gateway:login

# 启动网关
bun run gateway
```

绑定完成后，给「自己」发消息，Dexter 会在边「思考」边回复。相当于随身带了一个 24 小时在线的、能查实时财报的投资研究员。

---

## 七、上手只需 30 分钟

```bash
# 1. 安装 Bun 运行时
curl -fsSL https://bun.com/install | bash

# 2. 克隆项目
git clone https://github.com/virattt/dexter.git
cd dexter

# 3. 安装依赖
bun install

# 4. 配置 API 密钥
cp env.example .env
# 编辑 .env，填入以下密钥：
# OPENAI_API_KEY（必填）
# FINANCIAL_DATASETS_API_KEY（财报数据）
# EXASEARCH_API_KEY（网页搜索，可选）

# 5. 启动
bun start
```

启动后直接用自然语言提问，比如：

---

## 八、我的一点看法

Dexter 让我感兴趣的地方，不只是它能做金融分析这件事本身，而是它的工程哲学。

SOUL.md 这个设计细节特别能说明问题——作者不是在给 AI 写提示词，而是在给一个「自主行动者」设定价值观和思维框架。这背后的假设是：一个好的 Agent，需要有稳定的「人格」，才能在复杂任务里做出一致的决策。

这和当前很多「大而全」的 AI 工具走的是完全不同的路：深度垂直 + 哲学自洽，比功能堆砌更难复制。

另外，它的三层上下文管理方案（微压缩 → 记忆写盘 → 全量压缩）是非常值得学习的工程模式，特别是对于那些需要处理大量工具调用结果的 Agent 项目，这套机制直接决定了它能不能跑完一个完整的深度研究任务。

如果你想上手试试，可以关注「高老三聊AI」。

---

## 引用链接

- [GitHub 仓库](https://github.com/virattt/dexter)
- [FinancialDatasets API](https://financialdatasets.ai)
