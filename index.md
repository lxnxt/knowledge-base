---
layout: home
title: 知识库
---

# 知识库 📚

> 记录学习、沉淀知识、积累成长

## 最近文章

{% for post in site.posts limit:5 %}
- [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%Y-%m-%d" }}
{% empty %}
- 暂无文章，写一篇吧！
{% endfor %}

---

## 关于这个知识库

这是一个基于 **Obsidian + GitHub Pages** 的个人知识库。

### 使用方法

1. 在 Obsidian 中用 Markdown 写文章
2. 通过 Obsidian Git 插件同步到 GitHub
3. GitHub Pages 自动渲染，生成永久链接

### 文章格式

文章文件命名格式：`YYYY-MM-DD-文章标题.md`

示例：`2026-05-10-AI学习笔记.md`

文件开头加上：

```yaml
---
title: 文章标题
date: 2026-05-10
tags: [AI, 学习]
---
```

---

## 标签分类

{% for tag in site.tags %}
- [{{ tag[0] }}]({{ site.baseurl }}/tags.html#{{ tag[0] }})
{% endfor %}
