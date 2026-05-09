# 个人知识库

基于 Obsidian + GitHub Pages 构建。

## 本地开发

```bash
# 安装依赖
bundle install

# 本地预览
bundle exec jekyll serve

# 访问 http://localhost:4000
```

## 文章格式

文件放在 `_posts/` 目录，命名格式：`YYYY-MM-DD-标题.md`

```yaml
---
title: 文章标题
date: 2026-05-09
tags: [标签1, 标签2]
---

正文内容...
```

## 同步到 GitHub

安装 Obsidian Git 插件，配置仓库地址即可自动同步。
