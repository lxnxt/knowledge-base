---
title: "爬虫天花板！网站改版不用改代码！智能自愈+隐身反爬，网页提取比BS4快784倍"
created: 2026-05-10
updated: 2026-05-10
type: article
tags: [web scraping, Python, AI, 爬虫]
sources: [raw/articles/scrapling-wechat.md]
original_url: https://mp.weixin.qq.com/s/Jmpp2O3taqyFZ2U1d1EreA
author: 程序员慢祥
domain: mp.weixin.qq.com
---

# 爬虫天花板！网站改版不用改代码！智能自愈+隐身反爬，网页提取比BS4快784倍

> 来源：**程序员慢祥**
> 原文链接：[点击查看](https://mp.weixin.qq.com/s/Jmpp2O3taqyFZ2U1d1EreA)

# 基础安装pip&nbsp;install scrapling# 安装反爬/浏览器依赖pip install&nbsp;"scrapling[fetchers]"scrapling install# 全功能安装（含AI/Shell）pip install&nbsp;"scrapling[all]"补充说明：基础安装仅包含解析器引擎及核心依赖，无 Fetcher 和 CLI 相关功能；安装 `scrapling[fetchers]` 后，需执行 `scrapling install` 下载浏览器及系统依赖、指纹操作依赖，也可通过代码调用 `from scrapling.cli import install` 完成安装（支持强制重装）；`scrapling[ai]` 可单独安装 MCP 服务器功能，`scrapling[shell]` 可单独安装交互式 Shell 和 CLI 提取功能。Docker 安装：可直接拉取包含所有功能和浏览器的镜像，无需手动配置环境，命令如下：从 DockerHub 拉取：`docker pull pyd4vinci/scrapling`从 GitHub 注册表拉取：`docker pull ghcr.io/d4vinci/scrapling:latest`该镜像通过 GitHub Actions 自动构建推送，与项目主分支同步更新。2. 基础示例：抓取名言网站注意：经测试，目标网站 `https://quotes.toscrape.com/` 目前存在解析失败问题，报错信息为“网页解析失败，可能是不支持的网页类型，请检查网页或稍后重试”，该网站本身包含多条名言及标签内容（如“‘The world as we have created it is a process of our thinking...’”），可更换其他可正常访问的目标网站测试该代码逻辑。from&nbsp;scrapling.fetchers&nbsp;import&nbsp;Fetcher# 发起请求（若该网站解析失败，可替换为其他可正常访问的网页URL）page = Fetcher.get("https://quotes.toscrape.com/")# 提取数据quotes = page.css(".quote .text::text").getall()authors = page.css(".quote .author::text").getall()print(list(zip(quotes, authors)))3. 隐身模式：绕过 Cloudflare注意：经测试，目标网站 `https://nopecha.com/demo/cloudflare` 目前存在解析失败问题，报错信息为“网页解析失败，可能是不支持的网页类型，请检查网页或稍后重试”。该网站为 Cloudflare 验证演示页面，包含 reCAPTCHA、hCAPTCHA、funcaptcha、textcaptcha、awscaptcha 等多种验证类型，正常情况下 Scrapling 的 `StealthyFetcher` 可自动绕过这些验证，提取页面中的验证相关数据及服务信息。from&nbsp;scrapling.fetchers&nbsp;import&nbsp;StealthyFetcher# 自动绕过各类验证（该网站正常访问时支持验证绕过测试，解析失败可稍后重试）page = StealthyFetcher.fetch("https://nopecha.com/demo/cloudflare")data = page.css("#padded_content a").getall()print(data)4. 完整爬虫：并发 + 翻页注意：该示例基于 `https://quotes.toscrape.com/` 编写，若该网站无法解析，可将 `start_urls` 替换为其他支持翻页的可正常访问网页URL，爬虫逻辑保持不变。from&nbsp;scrapling.spiders import Spider,&nbsp;Responseclass&nbsp;QuotesSpider(Spider):name =&nbsp;"quotes"start_urls = ["https://quotes.toscrape.com/"] &nbsp;# 解析失败时可替换URLasync&nbsp;def&nbsp;parse(self, response: Response):for&nbsp;quote&nbsp;in&nbsp;response.css(".quote"):yield&nbsp;{"text": quote.css(".text::text").get(),"author": quote.css(".author::text").get()}# 自动翻页next_page = response.css(".next a::attr(href)").get()if&nbsp;next_page:yield&nbsp;response.follow(next_page)# 启动爬虫result = QuotesSpider().start()result.items.to_json("quotes.json")5. 多会话混合爬虫示例补充 README 中重点提及的多会话使用场景，可在单个爬虫中搭配不同类型 Session，适配不同请求需求：from&nbsp;scrapling.spiders&nbsp;import&nbsp;Spider, Request, Responsefrom&nbsp;scrapling.fetchers&nbsp;import&nbsp;FetcherSession, AsyncStealthySessionclass&nbsp;MultiSessionSpider(Spider):name =&nbsp;"multi"start_urls = ["https://example.com/"] &nbsp;# 该URL解析失败，替换为可正常访问的URLdef&nbsp;configure_sessions(self, manager):# 配置两种Session：快速HTTP请求（fast）、隐身绕过（stealth）manager.add("fast", FetcherSession(impersonate="chrome"))manager.add("stealth", AsyncStealthySession(headless=True), lazy=True)async&nbsp;def&nbsp;parse(self, response: Response):for&nbsp;link&nbsp;in&nbsp;response.css('a::attr(href)').getall():# 受保护页面路由到隐身Session，普通页面使用快速Sessionif&nbsp;"protected"&nbsp;in&nbsp;link:yield&nbsp;Request(link, sid="stealth")else:yield&nbsp;Request(link, sid="fast", callback=self.parse)6. Async Session 管理示例补充 README 中异步 Session 的使用方法，适配高并发场景：import&nbsp;asynciofrom&nbsp;scrapling.fetchers&nbsp;import&nbsp;FetcherSession, AsyncStealthySession, AsyncDynamicSession# FetcherSession 支持同步/异步两种模式async&nbsp;with&nbsp;FetcherSession(http3=True)&nbsp;as&nbsp;session:page1 = session.get('https://example.com/page1') &nbsp;# 该URL解析失败page2 = session.get('https://example.com/page2', impersonate='firefox135') &nbsp;# 该URL解析失败# 异步Session并发请求示例async&nbsp;with&nbsp;AsyncStealthySession(max_pages=2)&nbsp;as&nbsp;session:tasks = []urls = ['https://example.com/page1',&nbsp;'https://example.com/page2'] &nbsp;# 两个URL均解析失败，需替换为可正常访问URLfor&nbsp;url&nbsp;in&nbsp;urls:task = session.fetch(url)tasks.append(task)# 查看浏览器标签池状态（可选）print(session.get_pool_stats())results =&nbsp;await&nbsp;asyncio.gather(*tasks)print(session.get_pool_stats())7. CLI 命令使用示例补充 README 中 CLI 功能的使用方法，无需编写代码即可完成抓取，适配不同场景需求，结合工具特性补充完整示例：# 1. 启动交互式Web Scraping Shell（集成IPython，支持快捷操作）scrapling shell# 2. 基础提取：抓取网页内容并导出为指定格式（txt/md/html）# 示例1：提取网页全文，导出为md文件scrapling extract&nbsp;get&nbsp;'https://example.com'&nbsp;content.md# 示例2：指定CSS选择器提取目标内容，模拟Chrome浏览器请求scrapling extract&nbsp;get&nbsp;'https://example.com'&nbsp;content.txt --css-selector&nbsp;'#target-element'&nbsp;--impersonate&nbsp;'chrome'# 示例3：使用隐身模式，自动绕过Cloudflare等验证提取内容scrapling extract stealthy-fetch&nbsp;'https://example.com/protected-page'&nbsp;result.html --solve-cloudflare# 3. 动态渲染页面提取（适配JS渲染的动态内容）scrapling extract&nbsp;dynamic-fetch&nbsp;'https://example.com/dynamic-page'&nbsp;dynamic-result.txt --wait&nbsp;3&nbsp;&nbsp;# 等待3秒加载动态内容# 4. 查看CLI帮助文档，获取所有可用命令及参数scrapling --helpscrapling extract --help &nbsp;# 查看提取相关命令详情GitHub 项目地址：https://github.com/D4Vinci/Scrapling

终身学习，深耕AI领域

持续分享，优质AI开源

---

![性能对比](raw/assets/wechat-scrapling-01.jpg)

![架构图](raw/assets/wechat-scrapling-02.png)

![使用示例](raw/assets/wechat-scrapling-03.png)
