---
title: SenseNova-U1 原生多模态统一架构开源模型
date: 2026-05-10
tags: [AI, 多模态, 开源模型]
platform: github
source: https://github.com/OpenSenseNova/SenseNova-U1
---

# SenseNova-U1：基于 NEO-unify 架构统一多模态理解与生成

**机构：** OpenSenseNova

**开源协议：** Apache 2.0

**相关链接：**
- GitHub: https://github.com/OpenSenseNova/SenseNova-U1
- HuggingFace: https://huggingface.co/collections/sensenova/sensenova-u1
- ModelScope: https://modelscope.cn/collections/SenseNova/SenseNova-U1
- 技术报告: https://github.com/OpenSenseNova/SenseNova-U1/blob/main/docs/pdf/SenseNOVA_U1.pdf

## 概述

🚀 **SenseNova U1** 是全新一代原生多模态模型系列，在单一架构中统一了多模态理解、推理与生成。它代表着多模态 AI 的根本性范式转变：**从模态集成走向真正的统一**。SenseNova U1 不再依赖适配器在不同模态之间进行翻译，而是以原生方式跨语言与视觉进行思考与行动。

视觉理解与生成的统一开启了巨大的可能性。SenseNova U1 立足于**数据驱动学习阶段**（如 ChatGPT），并指向下一阶段——**智能体学习阶段**（如 OpenClaw），以原生多模态的方式进行学习、思考和行动。

## 核心架构：NEO-unify

SenseNova U1 的核心是 **[NEO-unify](https://huggingface.co/blog/sensenova/neo-unify)** —— 一个为多模态 AI 而设计、从第一性原理出发的全新架构：*它彻底摒弃了视觉编码器（VE）与变分自编码器（VAE）*，因为像素与文字信息在本质上是深度相关的。

主要特性：
- 🔗 端到端地将语言与视觉信息建模为统一整体
- 🖼️ 在保留语义丰富度的同时，维持像素级的视觉保真度
- 🧠 通过原生 MoT 实现跨模态推理，效率高、冲突少

## 模型库

本次开源为 SenseNova U1 Lite 系列，共两个规格：

| 模型 | 参数量 | HF 权重 |
| :---- | :------- | :--------- |
| SenseNova-U1-8B-MoT-SFT | 8B MoT | [🤗 链接](https://huggingface.co/sensenova/SenseNova-U1-8B-MoT-SFT) |
| SenseNova-U1-8B-MoT | 8B MoT | [🤗 链接](https://huggingface.co/sensenova/SenseNova-U1-8B-MoT) |
| SenseNova-U1-8B-MoT-LoRA-8step-V1.0 | 0.4B | [🤗 链接](https://huggingface.co/sensenova/SenseNova-U1-8B-MoT-LoRAs/blob/main/SenseNova-U1-8B-MoT-LoRA-8step-V1.0.safetensors) |
| SenseNova-U1-A3B-MoT-SFT | A3B MoT | [🤗 链接](https://huggingface.co/sensenova/SenseNova-U1-A3B-MoT-SFT) |
| SenseNova-U1-A3B-MoT | A3B MoT | [🤗 链接](https://huggingface.co/sensenova/SenseNova-U1-A3B-MoT) |

> 💡 `SenseNova-U1-8B-MoT` 中的 `8B-MoT` 指的是 ~8B 理解参数**与** ~8B 生成参数。

## 能力亮点

- 🏆 **开源 SoTA** — 统一多模态理解与生成上树立新标杆，在多种理解、推理与生成基准上均达开源最优
- 📖 **原生图文交错生成** — 单一模型单次生成连贯图文内容，支持生活指南、旅行日记等场景
- 📰 **高密度信息呈现** — 生成知识图解、海报、PPT、漫画、简历等复杂内容
- 🤖 **VLA + 世界建模** — 未来方向指向 AI Agent

## 能力示例

### 文生图（推理）

| 原始文本 | 推理过程 | 生成图像 |
| :--- | :--- | :--- |
| A male peacock trying to attract a female | 孔雀开屏求偶的完整思维链推理 | 生成的图像 |
| A small piece of dry wood and a dense iron block in a transparent water tank | 木头浮水面、铁块沉底，基于密度的物理推理 | 生成的图像 |

### 图像编辑（推理）

支持因果推理、物理变化、生物变化等复杂编辑任务，如：
- "Draw what it will look like one hour later" — 茶水氧化变深
- "Change the water to high-concentration saltwater" — 鸡蛋在高浓度盐水中上浮

### 图文交错生成

单一模型单次生成连贯的图文内容，支持生活指南、旅行日记等富叙事性与表现力的场景。

## 技术报告

- `[2026.05.10]` 发布技术报告并开源 A3B-MoT-SFT 与 A3B-MoT 模型权重
- `[2026.05.08]` 新增 GGUF 量化权重与分层加载 VRAM 模式，便于单卡低显存推理
- `[2026.05.06]` 发布 8 步推理 LoRA 模型
- `[2026.04.30]` 发布 8 步推理预览版
- `[2026.04.27]` 首发基础模型权重与推理代码

## 后续计划

- [ ] SenseNova-U1 训练代码
- [x] SenseNova-U1 最终版权重与技术报告 ✅
