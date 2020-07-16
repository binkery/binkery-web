#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import codecs
import datetime
import markdown
import time
import html
from bs4 import BeautifulSoup

def write(path,content):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
    with codecs.open(path, "w", "utf-8") as f:
        f.write(content)
        f.close()
        

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
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="renderer" content="webkit">
    <meta http-equiv="Cache-Control" content="no-siteapp" />
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
    <meta name="theme-color" content="#337ab7">
    <title>{article[title]} | Binkery 技术博客</title>
    <meta name="keywords" content="{article[keywords]}">
    <meta name="description" content="{article[description]}">
    <meta name="baidu-site-verification" content="LgqE9vT9Dv" />
    <link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.css" rel="stylesheet" media="screen">
    <style type="text/css">
        pre{{
            background-color:#f8f9fa;
            border:1px solid rgba(0, 0, 0, 0.125);
            border-radius:0.25rem;
            background-clip: border-box;
            padding:1em;
        }}
        blockquote{{
            border-left:5px solid rgba(0, 0, 0, 0.125);
            padding:1em;
        }}
	.card-body ul{{
  		padding-inline-start:1rem;
	}}
    </style>
    <script>
        var _hmt = _hmt || [];
        (function() {{
            var hm = document.createElement("script");
            hm.src = "https://hm.baidu.com/hm.js?cceda2bd9bbe16209c98859a1cab0112";
            var s = document.getElementsByTagName("script")[0]; 
            s.parentNode.insertBefore(hm, s);
        }})();
    </script>
</head>
<body>
    <div class="container-fluid">

        <div  class="row mb-5">
            <div class="col"></div>
            <div class="col-sm-12 col-md-10 col-lg-10 col-xl-8">
                <nav class="navbar navbar-expand-lg navbar-light bg-light">
                    <a class="navbar-brand" href="{app[link]}">{app[name]}</a>
                    <ul class="nav nav-pills">{app[nav]}</ul>
                </nav>
            </div>
            <div class="col"></div>
        </div><!-- row nav -->

        <div class="row">
            <div class="col-md-1 col-lg-1 col-xl-2"></div>
            <div class="col-sm-12 col-md-10 col-lg-10 col-xl-6">
                
                <article>
                    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
                    <ins class="adsbygoogle"
                         style="display:block"
                         data-ad-format="fluid"
                         data-ad-layout-key="-gi-19+58-26-7b"
                         data-ad-client="ca-pub-5264794978178106"
                         data-ad-slot="8172112958"></ins>
                    <script>
                         (adsbygoogle = window.adsbygoogle || []).push({{}});
                    </script>
                </article>
                
                <nav><ol class="breadcrumb">{article[parent_path]}</ol></nav>
                <article>
                    {article[content]}
                    <p> - EOF - </p>
                    <blockquote>
                    <p>本站文章除注明转载外，均为本站原创或编译。欢迎任何形式的转载，但请务必注明出处，尊重他人劳动。<br/>
                    转载请注明：文章转载自 Binkery 技术博客 [<a href="https://binkery.com/">https://binkery.com</a>]<br/>
                    本文标题：{article[title]}<br/>
                    本文地址：<a href="{article[link]}"> {article[link]}</a></p>
                    </blockquote>
                </article>
                <article>
                    <ins class="adsbygoogle"
                         style="display:block"
                         data-ad-format="fluid"
                         data-ad-layout-key="-gi-19+58-26-7b"
                         data-ad-client="ca-pub-5264794978178106"
                         data-ad-slot="8172112958"></ins>
                    <script>
                         (adsbygoogle = window.adsbygoogle || []).push({{}});
                    </script>
                </article>
                <!--
                <div id="gitalk-container"></div>
                -->
            </div><!-- row content left -->

            <div class="col-sm-12 col-md-10 offset-md-1 col-lg-10 offset-lg-1 col-xl-2 offset-xl-0">
                <!-- 目录树 -->
                <div class="card mb-3">
                    <div class="card-header">目录树</div><div class="card-body"><ul>{app[sidebar]}</ul></div>
                </div><!--card -->
                <!-- 目录树 -->

                <!-- 赞助 -->
                <div class="card mb-3">
                    <div class="card-header">赞助商</div>
                    <div class="card-body">
                        <!-- binkery-sidebar -->
                        <ins class="adsbygoogle"
                             style="display:block"
                             data-ad-client="ca-pub-5264794978178106"
                             data-ad-slot="9371185226"
                             data-ad-format="auto"
                             data-full-width-responsive="true"></ins>
                        <script>
                             (adsbygoogle = window.adsbygoogle || []).push({{}});
                        </script>
                    </div>
                </div><!--card -->
                <!-- 赞助 -->
                
                <!-- 友情链接 -->
                <div class="card mb-3">
                    <div class="card-header">友情链接</div><div class="card-body">
                    <ul>
                    <li><a href="http://www.binkery.com/archives/1.html">友链申请</a></li>
			        <li><a href="http://xiaohost.com/" target="_blank">老牛博客</a></li>
			        <li><a href="https://www.xiaoz.me/" target="_blank">小z博客</a></li>
			        <li><a href="https://www.oldpan.me/" target="_blank">Oldpan的个人博客</a></li>
			        <li><a href="https://www.oldking.net/" target="_blank">老鬼的博客</a></li>
                    <li><a href="https://spacepage.top" target="_blank">记录思考</a></li>
                    <li><a href="http://www.shanghai60.org.cn" target="_blank">电影天堂网</a></li>
                    </ul>
                    </div>
                </div>
                 <!-- 友情链接 -->
            </div>
        </div><!-- row content -->

        <div  class="row mt-5">
            <div class="col-sm-12 col-md-10 offset-md-1 col-lg-10 col-xl-8 offset-xl-2">
            <footer>
                <p class="text-center">CopyRight &copy; <a href="{app[link]}">binkery.com</a> ^_^ Last Build @ {app[last_modify_time]} </p>
                <p class="text-center"><a href="{app[link]}sitemap.txt">sitemap</a></p>
            </footer>
            </div>
        </div><!-- row footer -->
    </div><!-- container-fluid -->
</body>
</html>
'''.format(article=article,app=app)
    #print(local_path)
    write(local_path,template)
    
def get_title_from_source_file(path):
    if os.path.isdir(path):
        md_file = os.path.join(path,'README.md')
        if not os.path.exists(md_file):
            #print(os.path.basename(path))
            basename = os.path.basename(path)
            return basename
    else:
        md_file = path
    with open(md_file,'r',encoding='utf-8') as f:
        _title = f.readline().strip().lstrip('#')
    return _title
    
def get_content_from_source_file(path):
    if os.path.isdir(path):
        md_file = os.path.join(path,'README.md')
        if not os.path.exists(md_file):
            basename = os.path.basename(path)
            return '# ' + basename[4:]
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
    
    
def toInt(path):
    try:
        return str(int(path))
    except (TypeError,ValueError):
        return path
    
          
def get_nav():
    nav = ''
    files = sorted(os.listdir(app['source']),reverse=False)
    for f in files:
        if f == 'README.md':
            continue
        path = os.path.join(app['source'],f)
        title = get_title_from_source_file(path)
        if os.path.isdir(path):
            nav += '<li class="nav-item"><a class="nav-link" href="{link}">{title}</a></li>\n'.format(link=app['link'] + 'category/' + f + '.html',title=title)
    return nav
    
def get_sidebar():
    nav = ''
    files = sorted(os.listdir(app['source']),reverse=False)
    for f in files:
        if f == 'README.md':
            continue
        path = os.path.join(app['source'],f)
        title = get_title_from_source_file(path)
        if os.path.isdir(path):
            nav += '<li><a href="{link}">{title}</a>\n'.format(link=app['link'] + 'category/' + f + '.html',title=title)
            children = sorted(os.listdir(path),reverse=False)
            nav += '<ul>'
            for child in children:
                if child == 'README.md':
                    continue
                child_path = os.path.join(path,child)
                child_title = get_title_from_source_file(child_path)
                if os.path.isdir(child_path):
                    nav += '<li><a href="{link}">{title}</a></li>\n'.format(link=app['link'] + 'category/' + child + '.html',title=child_title)
            nav += '</ul></li>'
    nav += ''
    return nav
    
def date_from(y,m,d):
    d1 = datetime.date.today()
    d2 = datetime.date(y,m,d)
    return (d1-d2).days

def date_to(y,m,d):
    d1 = datetime.date.today()
    d2 = datetime.date(y,m,d)
    return (d2-d1).days

def dispatch_tree(parent):
    files = sorted(os.listdir(parent['source']),reverse=True)
    for file in files:
        if file == 'README.md':
            continue
        child = {}
        child['source'] = os.path.join(parent['source'],file)
        child['parent'] = parent
        child['title'] = get_title_from_source_file(child['source'])
        parent['children'].append(child)
        if os.path.isdir(child['source']):
            child['target'] = app['target'] + 'category/' + file + '.html'
            child['link'] = app['link'] + 'category/' + file + '.html'
            child['children'] = []
            dispatch_tree(child)
        else:
            child['target'] = app['target'] + 'archives/' + file[:-3] + '.html'
            child['link'] = app['link'] + 'archives/' + file[:-3] + '.html'
        #print(child['link'] + ","  + child['title'])
        
    
def out_put(node):
    node['content'] = get_content_from_source_file(node['source'])
    node['keywords'] = get_key_workds_from_source_file(node['source'])
    node['parent_path'] = get_parent_path(node)
    app['sitemap'].append(node['link'])
    if os.path.isdir(node['source']):
        node['content'] += '\n## 文章列表 \n'
        for child in node['children']:
            node['content'] += '- [' + child['title'] + '](' + child['link'] + ')\n'
            out_put(child)
    elif node['parent'] is not None:
    	node['content'] += '\n## 相关文章 \n'
    	for child in node['parent']['children']:
    	    #pass
    	    #print(child['link'])
    	    node['content'] += '- [' + child['title'] + '](' + child['link'] + ')\n'
    write_article_to_file(node)
    
def get_parent_path(node):
    if node == None:
        return ''
    return get_parent_path(node['parent']) + '<li class="breadcrumb-item"><a href="{link}">{title}</a></li>'.format(link=node['link'],title=html.escape(node['title'])) 
    
    
cst_tz = datetime.timezone(datetime.timedelta(hours=8))

app = {
    'source':'../content/',
    'target':'../html/',
    'link':'https://binkery.com/',
    'last_modify_time':datetime.datetime.now(tz=cst_tz).strftime("%Y-%m-%d %H:%M:%S"),
    'name':'Binkery技术博客'
}
app['nav'] = get_nav()
app['sidebar'] = get_sidebar()
app['sitemap'] = []

root = {
    'source':app['source'],
    'link':app['link'],
    'target':app['target'] + 'index.html',
    'content':'',
    'parent':None,
    'children':[],
    'title':'主页',
    'keywords':''
    
}
dispatch_tree(root)
out_put(root)
sitemap = ''
for link in app['sitemap']:
    sitemap += link + '\n'

write(app['target'] + 'sitemap.txt',sitemap)




