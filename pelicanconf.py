#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = "飞龙"
SITEURL = "https://feilong.me"
SITENAME = "飞龙札记"
SITETITLE = SITENAME
SITESUBTITLE = "Less is more"
SITEDESCRIPTION = "飞龙札记 - felinx's blog"
SITELOGO = '/static/feilong.jpg'
FAVICON = '/static/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'friendly'

ROBOTS = 'index, follow'

THEME = 'pelican-themes/Flex'
PATH = 'content'
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh_CN'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
    # "zh": "%Y-%m-%d %H:%M:%S"
}

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
ARCHIVES_SAVE_AS = ''  # disable ARCHIVES page

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True

# LINKS = (('About', '/about.html'),)

SOCIAL = (
    ('github', 'https://github.com/felinx'),
    ('rss', '/feeds/all.atom.xml'))


MENUITEMS = (('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'CC BY-SA',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 50

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'post_stats']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'weekly',
        'pages': 'monthly',
    }
}

DISQUS_SITENAME = "feilong"
GOOGLE_ANALYTICS = "UA-9694421-8"

STATIC_PATHS = ['static', 'CNAME', '.gitignore', 'robots.txt']

# EXTRA_PATH_METADATA = {
#     'extra/custom.css': {'path': 'static/custom.css'},
# }

# CUSTOM_CSS = 'static/custom.css'

USE_LESS = True
