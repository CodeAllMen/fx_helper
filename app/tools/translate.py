"""
Create by yy on 2020/6/9
"""
import html
import re
import sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser

from googletrans import Translator


class Translate(object):
    agent = {'User-Agent':
                 "Mozilla/4.0 (\
                 compatible;\
                 MSIE 6.0;\
                 Windows NT 5.1;\
                 SV1;\
                 .NET CLR 1.1.4322;\
                 .NET CLR 2.0.50727;\
                 .NET CLR 3.0.04506.30\
                 )"}

    def __init__(self):
        self.translator = Translator(service_urls=['translate.google.cn'])

    def translate(self, content, origin_language, aim_language):
        """
        :param content:
        :param origin_language:
        :param aim_language:
        :return:
        """
        data = self.translator.translate(content, src=origin_language, dest=aim_language).text
        return data

    @staticmethod
    def unescape(text):
        if sys.version_info[0] < 3:
            parser = HTMLParser.HTMLParser()
        else:
            parser = html.parser.HTMLParser()
        return parser.unescape(text)

    def start_translate(self, to_translate, to_language="auto", from_language="auto"):
        # type: (object, object, object) -> object
        # type: (object, object, object) -> object
        """Returns the translation using google translate
        you must shortcut the language you define
        (French = fr, English = en, Spanish = es, etc...)
        if not defined it will detect it or use english by default

        Example:
        print(translate("salut tu vas bien?", "en"))
        hello you alright?
        """
        base_link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s"
        if sys.version_info[0] < 3:
            to_translate = urllib.quote_plus(to_translate)
            link = base_link % (to_language, from_language, to_translate)
            request = urllib.Request(link, headers=self.agent)
            raw_data = urllib.urlopen(request).read()
        else:
            to_translate = urllib.parse.quote(to_translate)
            link = base_link % (to_language, from_language, to_translate)
            request = urllib.request.Request(link, headers=self.agent)
            raw_data = urllib.request.urlopen(request).read()
        data = raw_data.decode("utf-8")
        expr = r'class="t0">(.*?)<'
        re_result = re.findall(expr, data)
        if len(re_result) == 0:
            result = ""
        else:
            result = html.unescape(re_result[0])
        return result

    def translate_com(self, to_translate, from_lang, to_lang):
        result = self.start_translate(to_translate, to_lang, from_lang)
        return result
