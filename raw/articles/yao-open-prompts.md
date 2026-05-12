---
title: "姚金刚提示词合集 yao-open-prompts"
slug: yao-open-prompts
date: 2025-05-12
tags: [提示词, AI, prompt, GEO营销, 开源]
source: https://github.com/yaojingang/yao-open-prompts
---

# 姚金刚提示词合集 yao-open-prompts

## 概述

姚金刚提示词合集的开源版，面向真实场景的中文 AI 提示词库。

- **Star**: 1.8k
- **Fork**: 276
- **提示词数量**: 116 个
- **分类**: 9 大类
- **许可**: CC BY 4.0（可商用，需署名）

## 9 大分类

| 分类 | 数量 | 代表提示词 |
|---|---|---|
| AI内容 | 49 | 写作、润色、标题、公众号 HTML、短视频、PPT |
| AI营销 | 28 | GEO 营销、SEO、信源建设、数据监测 |
| AI学习 | 11 | 费曼提问、批判思维、记忆术、学习助理 |
| AI工作 | 10 | 企业合同、产品原型、PPT、网页 |
| AI教育 | 4 | 儿童教育、互动学习页、小游戏 |
| AI方法 | 8 | 元提示词、网页逆向、RTF 框架 |
| AI思考 | 3 | 批判思维、记忆、思维类 |
| AI生活 | 2 | 健康、亲子歌曲 |
| AI编程 | 1 | 架构设计 |

## 核心亮点

### 智能元提示词系统

- **V0.6 / V0.8 两版**，基于 **RTF 框架**（Role-Task-Format）
- 把需求分析→角色→任务→格式→评估串成完整流程
- LISP 结构化版本更进阶，适合二次开发
- 用途：生成任何高质量提示词的"起点提示词"

### GEO 营销（当前热点）

- **25 个实战模板**，AI 搜索优化（Generative Engine Optimization）
- 覆盖：机会判断、内容工程、信源建设、数据监测、增长诊断

### 内容与运营（最大类，49 个）

- 短视频文案、钩子开场、高互动文案
- 公众号 HTML 排版
- B站UP主、抖音爆款策划
- 评论区运营、数据复盘诊断
- 各行业内容专家（教育、穿搭、健身、美食、家居）

## 目录结构

```
yao-open-prompts/
├── prompts/          # 中文提示词
├── prompts-en/       # 英文镜像
└── scripts/          # 目录生成 + 质检脚本
```

每个提示词有完整 frontmatter 规范：`title、category、author、version、status、tags`。

## 参考链接

- GitHub: https://github.com/yaojingang/yao-open-prompts
