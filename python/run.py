#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import codecs
import datetime
import markdown
import time
from bs4 import BeautifulSoup

def write(path,content):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
    with codecs.open(path, "w", "utf-8") as f:
        f.write(content)
        f.close()
        
def get_content_from_source_file(path):
    if os.path.isdir(path):
        md_file = os.path.join(path,'README.md')
        if not os.path.exists(md_file):
            basename = os.path.basename(path)
            return '# ' + basename[3:]
    else :
        md_file = path
    with open(md_file,'r',encoding='utf-8') as f:
        content = f.read()
        return content
        
def get_key_workds_from_source_file(path):
    if os.path.isdir(path):
        md_file = os.path.join(path,'README.md')
        if not os.path.exists(md_file):
            return ''
    else :
        md_file = path
    with open(md_file,'r',encoding='utf-8') as f:
        f.readline()
        keywords = f.readline().strip().lstrip('-')
        return keywords
        
def path_to_html_path(path):
    #print('path_to_html_path ' + path)
    if path == '../content/':
        return '../html/index.html'
    if os.path.isdir(path):
        return '../html' + path[10:] + '/index.html'
    else:
        return '../html' + path[10:-2] + 'html'
        
def remove_tags(text):
    return BeautifulSoup(text, "lxml").text
        
def write_article_to_file(article):
    article_content = markdown.markdown(article['content'])
    local_path = article['target']
    #print(article_content)
    article['description'] = remove_tags(article_content)[:100].replace('\n','')
    #article['keywords'] = ''
    article['content'] = article_content
    #print(local_path)
    template = '''
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="renderer" content="webkit">
    <meta http-equiv="Cache-Control" content="no-siteapp" />
    <meta name ="viewport" content ="initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no">
    <link href="/css/bootstrap.min.css" rel="stylesheet" media="screen">
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <meta name="theme-color" content="#337ab7">
    <title>{article[title]} :: Binkery 技术博客</title>
    <meta name="keywords" content="{article[keywords]}">
    <meta name="description" content="{article[description]}">
    <script>
    var _hmt = _hmt || [];
        (function() {{
          var hm = document.createElement("script");
          hm.src = "https://hm.baidu.com/hm.js?1258cd282e3e864279d9edd53837183b";
          var s = document.getElementsByTagName("script")[0]; 
          s.parentNode.insertBefore(hm, s);
        }})();
    </script>
</head>
<body>
    <div  class="row-fluid">
    <div class="span8 offset2">
        <header>
            <a href="{app[link]}">{app[name]}</a>
        </header>
    </div>
    </div>
    
    <div class="row-fluid">
        <div class="span8 offset2">
            <nav>
	            <ul class="nav nav-pills">
                    {app[nav]}
                </ul>
            </nav>
        </div>
    </div>
    <div class="row-fluid">
        <div class="span8 offset2">
            <div class="span8">
                 <article>
                     {article[content]}
                     <P> - EOF - </P>
                     <p> 本文链接 <a href="{article[link]}"> {article[link]}</a>，欢迎转载，转载请注明出处。</p>
                </article>
            </div>
            <div class="span4">
                <ul>{app[sidebar]}</ul>
            </div>
        </div>
        
    </div>
    <div class="row-fluid">
        <div class="span8 offset2">
            <footer>
                 <p>网站更新时间:{app[last_modify_time]}</p>
                 <p>CopyRight &copy; <a href="{app[link]}">BETA.binkery.com</a></p>
            </footer>
        </div>
    </div>
</body>
</html>
'''.format(article=article,app=app)
    #print(local_path)
    write(local_path,template)
    
def path_to_link(path):
    #print('===== ' + path)
    if path == '../content/':
       #print('=======')
       return '/index.html'
    if os.path.isdir(path):
        return path[10:] + '/index.html'
    else:
        return path[10:-2] + 'html'
        
        
def get_title_from_source_file(path):
    if os.path.isdir(path):
        md_file = os.path.join(path,'README.md')
        if not os.path.exists(md_file):
            #print(os.path.basename(path))
            basename = os.path.basename(path)
            return basename[3:]
    else:
        md_file = path
    with open(md_file,'r',encoding='utf-8') as f:
        _title = f.readline().strip().lstrip('#')
    return _title

def toInt(path):
    try:
        return str(int(path))
    except (TypeError,ValueError):
        return path
    
def dispatch_path(parent,file):
    node = {}
    if file == '.' :
        node['source'] = parent['source']
        node['target'] = app['target'] + 'index.html'
        node['link'] = app['link'] + 'index.html'
    else :
        node['source'] = os.path.join(parent['source'],file)
        if os.path.isdir(node['source']):
            node['target'] = app['target'] + 'category/' + toInt(file[3:7]) + '.html'
            node['link'] = app['link'] + 'category/' + toInt(file[3:7]) + '.html'
        else:
            node['target'] = app['target'] + 'archives/' + toInt(file[3:10]) + '.html'
            node['link'] = app['link'] + 'archives/' + toInt(file[3:10]) + '.html'
    node['title'] = get_title_from_source_file(node['source'])
    node['content'] = get_content_from_source_file(node['source'])
    node['keywords'] = get_key_workds_from_source_file(node['source'])
    if os.path.isdir(node['source']):
        files = sorted(os.listdir(node['source']),reverse=False)
        node['content'] += '\n## 文章列表 \n'
        for f in files:
            if f == 'README.md':
                continue
            child_file = os.path.join(node['source'],f)
            child_title = get_title_from_source_file(child_file)
            if os.path.isdir(child_file):
                child_link = app['link'] + 'category/' + toInt(f[3:7]) + '.html'
            else:
                child_link = app['link'] + 'archives/' + toInt(f[3:10]) + '.html' 
            node['content'] += '- [' + child_title + '](' + child_link + ')\n'
    write_article_to_file(node)

    if os.path.isdir(node['source']):
        files = sorted(os.listdir(node['source']),reverse=False)
        for f in files :
            if f == 'README.md':
                continue
            # 最后需要递归一下
            dispatch_path(node,f)
          
def get_nav():
    nav = '<li><a href="/">主页</a></li>'
    files = sorted(os.listdir(app['source']),reverse=False)
    for f in files:
        if f == 'README.md':
            continue
        path = os.path.join(app['source'],f)
        title = get_title_from_source_file(path)
        if os.path.isdir(path):
            nav += '<li><a href="{link}">{title}</a></li>\n'.format(link=app['link'] + 'category/' + toInt(f[3:7]) + '.html',title=title)
    return nav
    
def get_sidebar():
    nav = '<ul>'
    files = sorted(os.listdir(app['source']),reverse=False)
    for f in files:
        if f == 'README.md':
            continue
        path = os.path.join(app['source'],f)
        title = get_title_from_source_file(path)
        if os.path.isdir(path):
            nav += '<li><a href="{link}">{title}</a></li>\n'.format(link=app['link'] + 'category/' + toInt(f[3:7]) + '.html',title=title)
            children = sorted(os.listdir(path),reverse=False)
            nav += '<ul>'
            for child in children:
                if child == 'README.md':
                    continue
                child_path = os.path.join(path,child)
                child_title = get_title_from_source_file(child_path)
                if os.path.isdir(child_path):
                    nav += '<li><a href="{link}">{title}</a></li>\n'.format(link=app['link'] + 'category/' + toInt(child[3:7]) + '.html',title=child_title)
            nav += '</ul>'
    nav += '</ul>'
    return nav
    
def date_from(y,m,d):
    d1 = datetime.date.today()
    d2 = datetime.date(y,m,d)
    return (d1-d2).days

def date_to(y,m,d):
    d1 = datetime.date.today()
    d2 = datetime.date(y,m,d)
    return (d2-d1).days

cst_tz = datetime.timezone(datetime.timedelta(hours=8))

app = {
    'source':'../content/',
    'target':'../html/',
    'link':'http://beta.binkery.com/',
    'last_modify_time':datetime.datetime.now(tz=cst_tz).strftime("%Y-%m-%d %H:%M:%S"),
    'name':'Binkery技术博客'
}
app['nav'] = get_nav()
app['sidebar'] = get_sidebar()

root = {
    'source':app['source'],
    'link':app['link'],
    'target':app['target'],
    'content':''
}
dispatch_path(root,'.')
