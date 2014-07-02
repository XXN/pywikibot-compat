# -*- coding: utf-8  -*-
import family

__version__ = '$Id$'


# The Wikimedia family that is known as Wikiquote
class Family(family.WikimediaFamily):
    def __init__(self):
        super(Family, self).__init__()
        self.name = 'wikiquote'

        self.languages_by_size = [
            'pl', 'en', 'it', 'ru', 'de', 'pt', 'es', 'fr', 'cs', 'sk', 'bg',
            'bs', 'tr', 'uk', 'sl', 'he', 'fa', 'lt', 'eo', 'el', 'ca', 'zh',
            'id', 'hu', 'fi', 'sv', 'li', 'nl', 'hr', 'nn', 'ja', 'no', 'az',
            'sa', 'hy', 'ar', 'et', 'ko', 'gl', 'ml', 'cy', 'ka', 'sr', 'ro',
            'ku', 'te', 'th', 'da', 'eu', 'is', 'ta', 'vi', 'af', 'sq', 'hi',
            'kn', 'la', 'be', 'br', 'mr', 'ur', 'uz', 'zh-min-nan', 'gu', 'su',
            'wo', 'ky', 'am',
        ]

        self.langs = dict([(lang, '%s.wikiquote.org' % lang)
                           for lang in self.languages_by_size])

        # Override defaults
        self.namespaces[2]['ca'] = [u'Usuari']
        self.namespaces[3]['ca'] = [u'Usuari Discussió']
        self.namespaces[2]['cs'] = [u'Uživatel', u'Uživatelka']
        self.namespaces[3]['cs'] = [u'Diskuse s uživatelem', u'Diskuse s uživatelkou', u'Uživatel diskuse', u'Uživatelka diskuse']
        self.namespaces[9]['da'] = [u'MediaWiki diskussion', u'MediaWiki-diskussion']
        self.namespaces[13]['da'] = [u'Hjælp diskussion', u'Hjælp-diskussion']
        self.namespaces[3]['de'] = [u'Benutzer Diskussion', u'BD', u'Benutzerin Diskussion']
        self.namespaces[2]['fa'] = [u'کاربر']
        self.namespaces[3]['fa'] = [u'بحث کاربر']
        self.namespaces[3]['fr'] = [u'Discussion utilisateur', u'Discussion Utilisateur', u'Discussion utilisatrice']
        self.namespaces[8]['hi'] = [u'मीडियाविकि']
        self.namespaces[9]['hi'] = [u'मीडियाविकि वार्ता']
        self.namespaces[10]['hi'] = [u'साँचा']
        self.namespaces[11]['hi'] = [u'साँचा वार्ता']
        self.namespaces[829]['ja'] = [u'モジュール・トーク']
        self.namespaces[2]['ko'] = [u'사용자']
        self.namespaces[3]['ko'] = [u'사용자토론']
        self.namespaces[2]['pl'] = [u'Użytkownik', u'Użytkowniczka']
        self.namespaces[3]['pl'] = [u'Dyskusja użytkownika', u'Dyskusja użytkowniczki']
        self.namespaces[2]['pt'] = [u'Utilizador', u'Usuário', u'Utilizadora']
        self.namespaces[3]['pt'] = [u'Utilizador Discussão', u'Usuário Discussão', u'Utilizadora Discussão']
        self.namespaces[9]['ro'] = [u'Discuție MediaWiki', u'Discuţie MediaWiki']
        self.namespaces[10]['zh'] = [u'Template', u'样板', u'模板', u'樣板']
        self.namespaces[12]['zh'] = [u'Help', u'使用說明', u'帮助', u'幫助']
        self.namespaces[14]['zh'] = [u'Category', u'分类', u'分類']

        # Most namespaces are inherited from family.Family.
        # Translation used on all wikis for the different namespaces.
        # (Please sort languages alphabetically)
        # You only need to enter translations that differ from _default.
        self.namespaces[4] = {
            '_default': self.namespaces[4]['_default'],
            'af': u'Wikiquote',
            'am': u'Wikiquote',
            'ang': u'Wikiquote',
            'ar': [u'ويكي الاقتباس', u'Wikiquote'],
            'az': [u'Vikisitat', u'Wikiquote'],
            'be': u'Wikiquote',
            'bg': [u'Уикицитат', u'Wikiquote'],
            'br': [u'Wikiarroud', u'Wikiquote'],
            'bs': [u'Wikicitati', u'Wikiquote'],
            'ca': [u'Viquidites', u'Wikiquote'],
            'co': u'Wikiquote',
            'cs': [u'Wikicitáty', u'WC', u'WQ', u'Wikiquote'],
            'cy': u'Wikiquote',
            'da': u'Wikiquote',
            'de': [u'Wikiquote', u'WQ'],
            'el': [u'Βικιφθέγματα', u'Wikiquote'],
            'en': u'Wikiquote',
            'eo': [u'Vikicitaro', u'Wikiquote'],
            'es': u'Wikiquote',
            'et': [u'Vikitsitaadid', u'Wikiquote'],
            'eu': u'Wikiquote',
            'fa': [u'ویکی‌گفتاورد', u'Wikiquote'],
            'fi': [u'Wikisitaatit', u'Wikiquote'],
            'fr': u'Wikiquote',
            'ga': u'Vicísliocht',
            'gl': u'Wikiquote',
            'gu': u'Wikiquote',
            'he': [u'ויקיציטוט', u'Wikiquote'],
            'hi': u'Wikiquote',
            'hr': [u'Wikicitat', u'Wikiquote'],
            'hu': [u'Wikidézet', u'Wikiquote'],
            'hy': [u'Վիքիքաղվածք', u'Wikiquote'],
            'id': u'Wikiquote',
            'is': [u'Wikivitnun', u'Wikiquote'],
            'it': u'Wikiquote',
            'ja': u'Wikiquote',
            'ka': [u'ვიკიციტატა', u'Wikiquote'],
            'kk': u'Уикидәйек',
            'kn': u'Wikiquote',
            'ko': [u'위키인용집', u'인', u'Wikiquote'],
            'ku': [u'Wîkîgotin', u'Wikiquote'],
            'ky': u'Wikiquote',
            'la': [u'Vicicitatio', u'Wikiquote'],
            'lb': u'Wikiquote',
            'li': u'Wikiquote',
            'lt': u'Wikiquote',
            'ml': [u'വിക്കിചൊല്ലുകൾ', u'വിക്കി ചൊല്ലുകൾ', u'Wikiquote'],
            'mr': u'Wikiquote',
            'nl': u'Wikiquote',
            'nn': u'Wikiquote',
            'no': u'Wikiquote',
            'pl': [u'Wikicytaty', u'Wikiquote'],
            'pt': u'Wikiquote',
            'ro': [u'Wikicitat', u'Wikiquote'],
            'ru': [u'Викицитатник', u'ВЦ'],
            'sa': [u'विकिसूक्तिः', u'Wikiquote'],
            'sk': [u'Wikicitáty', u'Wikiquote'],
            'sl': [u'Wikinavedek', u'Wikiquote'],
            'sq': u'Wikiquote',
            'sr': u'Wikiquote',
            'su': u'Wikiquote',
            'sv': u'Wikiquote',
            'ta': [u'விக்கிமேற்கோள்', u'Wikiquote', u'விக்கிபீடியா'],
            'te': u'Wikiquote',
            'th': [u'วิกิคำคม', u'Wikiquote'],
            'tr': [u'Vikisöz', u'Wikiquote'],
            'uk': [u'Вікіцитати', u'ВЦ', u'Wikiquote'],
            'ur': [u'وکی اقتباسات', u'Wikiquote'],
            'uz': [u'Vikiiqtibos', u'Wikiquote'],
            'vi': u'Wikiquote',
            'wo': u'Wikiquote',
            'zh': u'Wikiquote',
            'zh-min-nan': u'Wikiquote',
        }

        self.namespaces[5] = {
            '_default': self.namespaces[5]['_default'],
            'af': u'Wikiquotebespreking',
            'als': u'Wikiquote Diskussion',
            'am': u'Wikiquote ውይይት',
            'ang': u'Wikiquote talk',
            'ar': u'نقاش ويكي الاقتباس',
            'ast': u'Wikiquote alderique',
            'az': [u'Vikisitat müzakirəsi', u'Wikiquote talk'],
            'be': [u'Размовы пра Wikiquote', u'Wikiquote размовы'],
            'bg': u'Уикицитат беседа',
            'bm': u'Discussion Wikiquote',
            'br': u'Kaozeadenn Wikiarroud',
            'bs': u'Razgovor s Wikicitatima',
            'ca': u'Viquidites Discussió',
            'co': u'Wikiquote talk',
            'cs': [u'Diskuse k Wikicitátům', u'Wikiquote diskuse', u'Wikiquote talk', u'Wikicitáty diskuse'],
            'cy': u'Sgwrs Wikiquote',
            'da': [u'Wikiquote diskussion', u'Wikiquote-diskussion'],
            'de': u'Wikiquote Diskussion',
            'el': [u'Συζήτηση Βικιφθέγματα', u'Βικιφθέγματα συζήτηση'],
            'en': u'Wikiquote talk',
            'eo': [u'Vikicitaro-Diskuto', u'Vikicitaro diskuto'],
            'es': u'Wikiquote discusión',
            'et': [u'Vikitsitaatide arutelu', u'Vikitsitaadid arutelu'],
            'eu': u'Wikiquote eztabaida',
            'fa': u'بحث ویکی‌گفتاورد',
            'fi': u'Keskustelu Wikisitaateista',
            'fr': u'Discussion Wikiquote',
            'ga': u'Plé Vicísliocht',
            'gl': u'Conversa Wikiquote',
            'gu': u'Wikiquote ચર્ચા',
            'he': u'שיחת ויקיציטוט',
            'hi': u'Wikiquote वार्ता',
            'hr': u'Razgovor Wikicitat',
            'hu': [u'Wikidézet-vita', u'Wikidézet vita'],
            'hy': u'Վիքիքաղվածքի քննարկում',
            'id': u'Pembicaraan Wikiquote',
            'is': u'Wikivitnunspjall',
            'it': u'Discussioni Wikiquote',
            'ja': [u'Wikiquote・トーク', u'Wikiquote‐ノート'],
            'ka': [u'ვიკიციტატა განხილვა', u'Wikiquote განხილვა'],
            'kk': u'Уикидәйек талқылауы',
            'kn': u'Wikiquote ಚರ್ಚೆ',
            'ko': u'위키인용집토론',
            'ku': [u'Gotûbêja Wîkîgotinê', u'Wîkîgotin nîqaş'],
            'ky': u'Wikiquote баарлашуу',
            'la': u'Disputatio Vicicitationis',
            'lb': u'Wikiquote Diskussioun',
            'li': u'Euverlèk Wikiquote',
            'lt': u'Wikiquote aptarimas',
            'ml': [u'വിക്കിചൊല്ലുകൾ സംവാദം', u'വിക്കി ചൊല്ലുകൾ സംവാദം'],
            'mr': u'Wikiquote चर्चा',
            'nds': u'Wikiquote Diskuschoon',
            'nl': u'Overleg Wikiquote',
            'nn': u'Wikiquote-diskusjon',
            'no': u'Wikiquote-diskusjon',
            'pl': u'Dyskusja Wikicytatów',
            'pt': u'Wikiquote Discussão',
            'qu': u'Wikiquote rimanakuy',
            'ro': [u'Discuție Wikicitat', u'Discuţie Wikicitat'],
            'ru': u'Обсуждение Викицитатника',
            'sa': [u'विकिसूक्तिःसम्भाषणम्', u'विकिसूक्तिःसंभाषणं'],
            'sk': [u'Diskusia k Wikicitátom', u'Komentár k Wikipédii'],
            'sl': u'Pogovor o Wikinavedku',
            'sq': u'Wikiquote diskutim',
            'sr': [u'Разговор о Wikiquote', u'Razgovor o Wikiquote'],
            'su': u'Obrolan Wikiquote',
            'sv': u'Wikiquotediskussion',
            'ta': [u'விக்கிமேற்கோள் பேச்சு', u'விக்கிபீடியா பேச்சு'],
            'te': u'Wikiquote చర్చ',
            'th': u'คุยเรื่องวิกิคำคม',
            'tr': u'Vikisöz tartışma',
            'tt': u'Wikiquote bäxäse',
            'uk': u'Обговорення Вікіцитат',
            'ur': u'تبادلۂ خیال وکی اقتباسات',
            'uz': [u'Vikiiqtibos munozarasi', u'Vikiiqtibos talk'],
            'vi': u'Thảo luận Wikiquote',
            'vo': u'Bespik dö Wikiquote',
            'wo': [u'Wikiquote waxtaan', u'Discussion Wikiquote'],
            'zh': [u'Wikiquote talk', u'Wikiquote討論', u'Wikiquote讨论'],
            'zh-min-nan': u'Wikiquote討論',
        }

        self.namespaces[100] = {
            'cs': u'Dílo',
            'de': u'Portal',
            'fr': u'Portail',
            'he': u'פורטל',
            'li': u'Portaol',
            'sk': u'Deň',
            'zh': u'Transwiki',
        }

        self.namespaces[101] = {
            'cs': u'Diskuse k dílu',
            'de': u'Portal Diskussion',
            'fr': u'Discussion Portail',
            'he': u'שיחת פורטל',
            'li': u'Euverlèk portaol',
            'sk': u'Diskusia ku dňu',
            'zh': u'Transwiki talk',
        }

        self.namespaces[102] = {
            'fr': u'Projet',
            }

        self.namespaces[103] = {
            'fr': u'Discussion Projet',
            }

        self.namespaces[104] = {
            'fr': u'Référence',
            }

        self.namespaces[105] = {
            'fr': u'Discussion Référence',
            }

        self.namespaces[108] = {
            'fr': u'Transwiki',
            }

        self.namespaces[109] = {
            'fr': u'Discussion Transwiki',
            }

        # attop is a list of languages that prefer to have the interwiki
        # links at the top of the page.
        self.interwiki_attop = []

        # on_one_line is a list of languages that want the interwiki links
        # one-after-another on a single line
        self.interwiki_on_one_line = []

        # Similar for category
        self.category_attop = []

        # List of languages that want the category on_one_line.
        self.category_on_one_line = []

        # Global bot allowed languages on http://meta.wikimedia.org/wiki/Bot_policy/Implementation#Current_implementation
        self.cross_allowed = [
            'af', 'am', 'ar', 'az', 'be', 'bg', 'br', 'bs', 'ca', 'cs', 'da',
            'el', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'gl', 'he', 'hi',
            'hu', 'hy', 'id', 'is', 'it', 'ja', 'ka', 'kn', 'ku', 'ky', 'la',
            'li', 'lt', 'ml', 'mr', 'nl', 'nn', 'no', 'pt', 'ro', 'ru', 'sk',
            'sl', 'sq', 'sr', 'su', 'sv', 'ta', 'te', 'tr', 'uk', 'uz', 'vi',
            'wo', 'zh',
        ]

        # Which languages have a special order for putting interlanguage links,
        # and what order is it? If a language is not in interwiki_putfirst,
        # alphabetical order on language code is used. For languages that are in
        # interwiki_putfirst, interwiki_putfirst is checked first, and
        # languages are put in the order given there. All other languages are
        # put after those, in code-alphabetical order.
        self.interwiki_putfirst = {
            'en': self.alphabetic,
            'fi': self.alphabetic,
            'fr': self.alphabetic,
            'he': ['en'],
            'hu': ['en'],
            'pl': self.alphabetic,
            'simple': self.alphabetic,
            'pt': self.alphabetic,
        }

        self.obsolete = {
            'als': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Alemannic_Wikiquote
            'ang': None,  # https://bugzilla.wikimedia.org/show_bug.cgi?id=29150
            'ast': None,  # https://bugzilla.wikimedia.org/show_bug.cgi?id=28964
            'bm': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Bambara_Wikiquote
            'co': None,
            'cr': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Nehiyaw_Wikiquote
            'dk': 'da',
            'ga': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Gaeilge_Wikiquote
            'jp': 'ja',
            'kk': None,   # https://bugzilla.wikimedia.org/show_bug.cgi?id=20325
            'kr': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Kanuri_Wikiquote
            'ks': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Kashmiri_Wikiquote
            'kw': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Kernewek_Wikiquote
            'lb': None,
            'minnan': 'zh-min-nan',
            'na': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Nauruan_Wikiquote
            'nb': 'no',
            'nds': None,  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Low_Saxon_Wikiquote
            'qu': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Quechua_Wikiquote
            'simple': 'en',  # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Simple_English_(3)_Wikiquote
            'tk': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Turkmen_Wikiquote
            'tokipona': None,
            'tt': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Tatar_Wikiquote
            'ug': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Oyghurque_Wikiquote
            'vo': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Volapuk_Wikiquote
            'za': None,   # http://meta.wikimedia.org/wiki/Proposals_for_closing_projects/Closure_of_Zhuang_Wikiquote
            'zh-tw': 'zh',
            'zh-cn': 'zh'
        }

    def code2encodings(self, code):
        """
        Return a list of historical encodings for a specific language wikipedia
        """
        # Historic compatibility
        if code == 'pl':
            return 'utf-8', 'iso8859-2'
        if code == 'ru':
            return 'utf-8', 'iso8859-5'
        return self.code2encoding(code),
        
    def shared_data_repository(self, code, transcluded=False):
        return ('wikidata', 'wikidata')
