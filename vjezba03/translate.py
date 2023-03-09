#!python.exe
from http import cookies
import os


translations = {
    "eng":{'home':'home', 'articles':'articles', 'cart':'cart', 'contact':'contact'},
    "hr":{'home':'pocetna', 'articles':'artikli', 'cart':'kosarica', 'contact':'kontakt'},
    "de":{'home':'Haus', 'articles':'Artikeln', 'cart':'Verkaufstasche', 'contact':'Kontakt'},
    "es":{'home':'Casa', 'articles':'Arti', 'cart':'Bolsa', 'contact':'Kontacto'}
}

def decide_language(lang=None):
    cookies_string = os.environ.get('HTTP_COOKIE', '')
    all_cookies_object = cookies.SimpleCookie(cookies_string)
    if lang is not None:
        cookie = cookies.SimpleCookie()
        cookie['lang'] = lang
        print (cookie.output())
    elif all_cookies_object.get('lang'):
        lang = all_cookies_object.get('lang').value
    else:
        lang = 'eng'
    return lang




def display_language():
    for key in translations:
        print ('<a href="?lang=' + key + '">' + key +'</a>')


def make_translations(language, key):
    return translations.get(language, translations['eng']).get(key, 'prazno')

