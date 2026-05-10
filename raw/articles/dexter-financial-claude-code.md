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

## Dexter — 金融圈的第一个「靠谱AI助手」

最近 GitHub 上有个项目爆了，叫 **Dexter**，专门帮基金经理、散户、研究员做金融分析。三个月冲到 23.5K Star，连我朋友圈都在转。

## 它牛在哪？

现在你问 ChatGPT 「苹果今年为啥涨」，它能给你编一段分析，听着挺像那么回事，但数字可能是瞎编的。这种事放股市里是要亏钱的。

Dexter 不一样。你问它，它会真的去查财报、查数据、验证逻辑，确认没问题了才告诉你答案——就像一个认真做功课的新人，而不是嘴炮王者。

## 核心设计

**① 给AI写「灵魂文档」**

不是普通 prompt，而是一套投资价值观，告诉它「宁可不说，也不要说错」「不懂的就说不懂」。有点像在培养一个靠谱的同事，而不是调戏一个话痨。

**② 上下文管理**

查财报数据量很大，很多AI会「消化不良」context 爆掉。Dexter 做了三层保护：小的它自己压缩，大的它先存硬盘，实在不行再做摘要。保证了它能跑完一个完整的深度研究。

**③ 所有操作可审计**

每一步查了什么、返回什么、它怎么想的，全记下来。金融讲究合规，这个设计很加分。

**④ Skills 扩展**

相当于给它装插件。想加一个 DCF 估值能力？写个 SKILL.md 文件丢进去，它自动就能用。跟 Hermes 的 skill 机制一样。

## 装了啥依赖

装个 Bun，clone 项目，配两个 API key，30 分钟跑起来。支持 OpenAI / Anthropic / Google / Ollama 本地模型，随时切换。

## 一句话评价

不是又一个「能聊天的AI」，而是一个「真的会干活」的AI助手。工程哲学扎实，不堆功能，垂直做深，值得抄作业。

---

## 引用链接

- [GitHub 仓库](https://github.com/virattt/dexter)
- [FinancialDatasets API](https://financialdatasets.ai)
