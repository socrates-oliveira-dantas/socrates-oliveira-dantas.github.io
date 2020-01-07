#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dr. S\xf3crates de Oliveira Dantas'
SITENAME = u'Conte\xfado geral de F\xedsica!'
SITEURL = ''

# Paths
PATH = 'content'
PAGE_PATHS = ['pages','codes']
ARTICLE_PATHS = ['posts']

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

PLUGIN_PATHS = ['pelican-plugins']

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.youtube',
    'liquid_tags.notebook',
    'liquid_tags.include_code',
    'render_math',
    'pelican-ipynb.markup',
    'tipue_search']

I18N_TEMPLATES_LANG = 'en'

CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'

STATIC_PATHS = [ 'extra' ]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}

DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')

# Top menus
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

MARKUP =('md', 'ipynb')
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_USE_METACELL = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('É possível modificar estes links no arquivo de configuração.', '#'),)

# Social widget
SOCIAL = (('É possível modificar estes links no arquivo de configuração.', '#'),
          ('Outro link social', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
