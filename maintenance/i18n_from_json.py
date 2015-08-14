# -*- coding: utf-8  -*-
"""
Convert i18n json files inside i18n folder to i18n python files.

This script is needed for compat to convert the new json files to the old
python files used by compat.

This script understands the following command-line argument:
    -sort   Sort the message items. You should never need it.

Use it startting fom maintenance folder!

Usage: python.exe i18n_from_json.py [<folder>] [<options, >]

to convert all files:
python.exe i18n_from_json.py

to convert a single folder to a single file:
python.exe i18n_from_json.py <folder>
"""
# (C) Pywikibot team, 2015
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id$'
#

import sys
import codecs
import json
import os
import re
import pkgutil

sys.path.insert(1, '..')
import pywikibot

# replace dictionary format parameters with plain format
plain_format = (
    'unlink-unlinking',
)

# map the language code to the corresponding site code
codemap = {
    'be-tarask': 'be-x-old',
    'bho': 'bh',
    'gsw': 'als',
    'lzh': 'zh-classical',
    'nb': 'no',
    'nan': 'zh-min-nan',
    'rup': 'roa-rup',
    'sgs': 'bat-smg',
    'vro': 'fiu-vro',
    'yue': 'zh-yue',
    'zh-hans': 'zh',
}


class ConvertJsonBot(object):

    """i18n conversion bot"""

    def __init__(self, filename=None, sort=False):
        self.source = filename
        self.confirm = True
        self.sort = sort

    def run(self):
        """Run the script."""
        if self.source is None:
            self.confirm = False
            source = os.path.join('..', 'i18n')
            root, dirs, files = next(os.walk(source))
            for d in dirs:
                if not d.startswith('.'):
                    self.treat(d)
        else:
            self.treat(self.source)

    def treat(self, folder):
        """Treat a single folder..."""
        self.cache = {}
        self.langs = []
        self.source = folder
        pywikibot.output(u'Converting %s...' % folder)
        self.get_source()
        self.get_langs()
        self.get_dest()
        if self.sort:
            self.get_old_translation(folder)
        else:
            self.get_translation()
        self.get_authors()
        self.writefile()

    def get_source(self):
        """Get a single source to convert."""
        while True:
            if self.source is None:
                self.source = pywikibot.input(
                    'Please input the folder to convert '
                    '(no input to leave):')
            if not self.source:
                exit()
            self.source = os.path.join('..', 'i18n', self.source)
            if os.path.exists(self.source):
                break
            pywikibot.output(u'%s does not exist. Please retry.' % self.source)
            self.source = None

    def get_langs(self):
        """Read all languages."""
        for root, dirs, files in os.walk(self.source):
            for f in files:
                if f.endswith('.json'):
                    self.langs.append(f.split('.')[0])

    def get_dest(self):
        """Get the destination file and confirm it."""
        self.dest = self.source + '.py'
        if self.confirm and pywikibot.inputChoice(
                u'Destination file is %s.' % self.dest,
                answers=['yes', 'no'], hotkeys='yn', default='n') == 'n':
            pywikibot.output('Quitting...')
            exit()

    def get_translation(self):
        """Read translations into cache."""
        site = pywikibot.getSite()
        base = os.path.basename(self.source)
        for lang in self.langs:
            filename = "%s/%s.json" % (base, lang)
            try:
                trans_text = pkgutil.get_data('i18n', filename)
            except (OSError, IOError):  # file open can cause several exceptions
                continue
            if isinstance(trans_text, bytes):
                trans_text = trans_text.decode('utf-8')
            transdict = json.loads(trans_text, "utf-8")
            for key in transdict:
                if key not in self.cache:
                    self.cache[key] = {}
                item = transdict[key]
                self.cache[key][lang] = transdict[key]

    def get_old_translation(self, package):
        """Read translations from i18n file into cache.

        Used for sorting only.
        """
        msg = getattr(__import__('i18n', fromlist=[str(package)]),
                      package).msg
        for lang in msg:
            for key in msg[lang]:
                if not key in self.cache:
                    self.cache[key] = {}
                self.cache[key][lang] = msg[lang][key]

    def get_authors(self):
        """Read old authors from file."""
        self.authors = {}
        translators = []
        if not os.path.exists(self.dest):
            return
        f = codecs.open(self.dest, "r", "utf-8")
        findcode = False
        while True:
            line = f.readline().strip()
            if not line:
                break
            pattern = '# Author: '
            if line.startswith(pattern):
                author = line[len(pattern):]
                translators.append(author)
                findcode = True
            elif findcode:
                codelist = re.findall("'([a-z-]+?)': {", line)
                if codelist:
                    self.authors[codelist[0]] = translators[:]
                    translators = []
                    findcode = False
        f.close()

    def writefile(self):
        """Write the python i18n file."""
        lang_keys = set()
        for key in self.cache:
            lang_keys.update(self.cache[key].keys())
        has_qqq = 'qqq' in lang_keys
        has_en = 'en' in lang_keys
        if has_qqq:
            lang_keys.remove('qqq')
        if has_en:
            lang_keys.remove('en')
        lang_keys = list(lang_keys)
        lang_keys.sort()
        if has_qqq:
            lang_keys.insert(0, 'qqq')
        if has_en:
            lang_keys.insert(0, 'en')
        if self.sort:
            meta = {}
        else:
            meta = self.cache['@metadata']
        messages = self.cache.keys()
        if not self.sort:
            messages.remove('@metadata')
        g = codecs.open(self.dest, "w", "utf-8")
        g.write(u"# -*- coding: utf-8 -*-\r\n")
        g.write(u'"""i18n message bundle."""\r\n')
        g.write(u"msg = {\r\n")
        for code in lang_keys:
            if not messages:  # authors but no messages found
                continue
            authors = set()
            if code in meta and isinstance(meta[code], dict):
                # list may contain int
                authors.update(unicode(author)
                               for author in meta[code]['authors'])
            # recover old authors
            authors.update(self.authors.get(code, []))
            change_set = [('Rubin', 'Rubin16'),
                          ('Geoffrey "GEOFBOT" Mon', 'Sn1per'),
                          ('Hym411', 'Revi'),
                          ]
            for old, new in change_set:
                if old in authors:
                    authors.remove(old)
                    authors.add(new)
            for autor in sorted(authors):
                g.write(u"    # Author: %s\r\n" % autor)
            if code in codemap:
                lang = codemap[code]
            else:
                lang = code
            g.write("    '%s': {\r\n" % lang)
            for item in sorted(messages):
                if code in self.cache[item]:
                    msg = self.cache[item][code]
                    if item in plain_format:
                        msg = re.sub(r'%\([^)]*?\)s', '%s', msg)
                    msg = msg.replace('\n', r'\n').replace("'", r"\'")
                    g.write(u"        '%s': u'%s',\r\n"
                            % (item, msg))
            g.write("    },\r\n")
        g.write(u"};\r\n")
        g.close()


def main():
    filename = None
    sort = False
    for arg in pywikibot.handleArgs():
        if not arg.startswith('-'):
            filename = arg
        elif arg == '-sort':
            sort = True
        elif arg == '-help':
            pywikibot.showHelp()
        else:
            pywikibot.warning(arg + ' is not supported')
    bot = ConvertJsonBot(filename, sort)
    bot.run()


if __name__ == "__main__":
    pywikibot.stopme()  # we do not work on any site
    main()
