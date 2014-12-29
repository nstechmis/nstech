#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'nstech'
SITENAME = u'Nung Sian Tech.'
SITEURL = ''
MAINSITEURL = SITEURL

PATH = 'content'

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
TESTIMGPATH = '/theme/images/public-domain-images-free-stock-photos-high-quality-resolution-downloads-public-domain-archive-19-1000x667.jpg'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
  'zh': {
    'SITENAME': '穠纖科技',
  }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
