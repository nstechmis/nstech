#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'nstech'
SITENAME = u'Nung Sian Technology LTD.'
SITEURL = ''

PATH = 'content'

STATIC_PATHS = ['extra', 'img']
EXTRA_PATH_METADATA = {'extra/BingSiteAuth.xml': {'path': 'BingSiteAuth.xml'},
                       'extra/google90dd5bde7765c78d': {'path': 'google90dd5bde7765c78d.html'},
                       'extra/CNAME': {'path': 'CNAME'},
					   'extra/sitemap.xml': {'path':'sitemap.xml'}}

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

THEME = 'theme'

# test image url: http://imgur.com/0ruqHmQ

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
  'zh': {
    'SITENAME': '穠纖科技股份有限公司',
  }
}

DIRECT_TEMPLATES = ['index']
PAGE_ORDER_BY = 'order'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
