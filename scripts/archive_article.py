#!/usr/bin/env python3
"""
archive_article.py
归档文章 + 配图到知识库，并自动更新 articles.json

用法:
  python3 archive_article.py <文章标题> <描述> <标签> <图标emoji> <图标颜色> [--has-ppt] [--asset <配图文件路径>]
"""
import json
import os
import sys
import re
import glob

KB = '/Users/lxnxt/Documents/knowledge-base'
ARTICLES_JSON = f'{KB}/_data/articles.json'
ASSETS_DIR = f'{KB}/raw/assets'
ARTICLES_DIR = f'{KB}/raw/articles'

def slugify(title):
    """把标题转为 URL slug"""
    s = title.replace(' ', '-')
    s = re.sub(r'[^\w\u4e00-\u9fff-]', '', s)
    return s

def load_articles():
    with open(ARTICLES_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_articles(articles):
    with open(ARTICLES_JSON, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

def add_article(title, desc, tag, icon, icon_bg, has_ppt=False, ppt_asset=None, ppt_pages=None):
    articles = load_articles()
    slug = slugify(title)
    
    # Check if already exists
    if any(a['slug'] == slug for a in articles):
        print(f'⚠️  Article {slug} already in articles.json, skipping')
        return slug
    
    entry = {
        'slug': slug,
        'title': title,
        'desc': desc,
        'tag': tag,
        'icon': icon,
        'icon_bg': icon_bg,
        'href': f'/knowledge-base/raw/articles/{slug}.html',
        'asset': None,
        'has_ppt': has_ppt
    }
    
    if has_ppt and ppt_asset:
        entry['asset'] = f'/knowledge-base/{ppt_asset}'
    
    articles.insert(0, entry)  # Add to top
    save_articles(articles)
    print(f'✅ Added to articles.json: {slug}')
    return slug

def copy_asset(src_path, dest_name=None):
    """Copy asset to KB assets dir, return relative path"""
    if not os.path.exists(src_path):
        print(f'⚠️  Asset not found: {src_path}')
        return None
    if dest_name is None:
        dest_name = os.path.basename(src_path)
    dest = f'{ASSETS_DIR}/{dest_name}'
    import shutil
    shutil.copy2(src_path, dest)
    print(f'✅ Copied asset: {src_path} → {dest}')
    return f'raw/assets/{dest_name}'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        # Demo: add Dexter PPT
        print('Demo run: adding Dexter PPT article entry...')
        add_article(
            title='金融界的 Claude Code 来了',
            desc='GitHub 23.5K Star 的金融 AI Agent，专攻金融研究，三层架构 + SOUL.md 投资哲学，拒绝幻觉。',
            tag='AI Agent',
            icon='💰',
            icon_bg='pink',
            has_ppt=True,
            ppt_asset='assets/dexter-ppt-contact.png'
        )
        print('Done!')
        sys.exit(0)
    
    args = sys.argv[1:]
    has_ppt = '--has-ppt' in args
    args = [a for a in args if a != '--has-ppt']
    
    asset_idx = None
    if '--asset' in args:
        asset_idx = args.index('--asset')
        asset_path = args[asset_idx + 1]
        args = args[:asset_idx] + args[asset_idx+2:]
    else:
        asset_path = None
    
    if len(args) < 5:
        print(__doc__)
        sys.exit(1)
    
    title, desc, tag, icon, icon_bg = args[0], args[1], args[2], args[3], args[4]
    slug = add_article(title, desc, tag, icon, icon_bg, has_ppt, asset_path)
    
    if has_ppt and asset_path:
        # Also update the entry with correct path
        articles = load_articles()
        for a in articles:
            if a['slug'] == slug:
                a['asset'] = f'/knowledge-base/{asset_path}'
                break
        save_articles(articles)
    
    print(f'🎉 Archive complete! slug={slug}')
