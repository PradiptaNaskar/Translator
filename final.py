from typing import Dict, Any

import speech_recognition as sr
from googletrans import Translator
import os
from gtts import gTTS
r = sr.Recognizer()

while True:

    caps = {'afrikaans': 'af',
    'albanian': 'sq',
    'amharic': 'am',
    'arabic': 'am',
    'armenian': 'hy',
    'azerbaijani': 'az',
    'basque': 'eu',
    'belarusian': 'be',
    'bengali': 'bn',
    'bosnian': 'bs',
    'bulgarian': 'bg',
    'catalan': 'ca',
    'cebuano': 'ceb',
    'chichewa': 'ny',
    'chinese (simplified)': 'zh-cn',
    'chinese (traditional)': 'zh-tw',
    'corsican': 'co',
    'croatian': 'hr',
    'czech': 'cs',
    'danish': 'da',
    'dutch': 'nl',
    'english': 'en',
    'esperanto': 'eo',
    'estonian': 'et',
    'filipino': 'tl',
    'finnish': 'fi',
    'french': 'fr',
    'frisian': 'fy',
    'galician': 'gl',
    'georgian': 'ka',
    'german': 'de',
    'greek': 'el',
    'gujarati': 'gu',
    'haitian creole': 'ht',
    'hausa': 'ha',
    'hawaiian': 'haw',
    'hebrew': 'he',
    'hindi': 'hi',
    'hmong': 'hmn',
    'hungarian': 'hu',
    'icelandic': 'is',
    'igbo': 'ig',
    'indonesian': 'id',
    'irish': 'ga',
    'italian': 'it',
    'japanese': 'ja',
    'javanese': 'jw',
    'kannada': 'kn',
    'kazakh': 'kk',
    'khmer': 'km',
    'korean': 'ko',
    'kurdish (kurmanji)': 'ku',
    'kyrgyz': 'ky',
    'lao': 'lo',
    'latin': 'la',
    'latvian': 'lv',
    'lithuanian': 'lt',
    'luxembourgish': 'lb',
    'macedonian': 'mk',
    'malay': 'ms',
    'malayalam': 'ml',
    'maltese': 'mt',
    'maori': 'mi',

    'nepali': 'ne',
    'norwegian': 'no',
    'odia': 'or',
    'pashto': 'ps',
    'persian': 'fa',
    'polish': 'pl',
    'portuguese': 'pt',

    'romanian': 'ro',
    'russian': 'ru',
    'swedish': 'sv',

    'tamil': 'ta',
    'telugu': 'te',
    'thai': 'th',
    'turkish': 'tr',
    'ukrainian': 'uk',
    'urdu': 'ur',
    'uyghur': 'ug',
    'uzbek': 'uz',
    'vietnamese': 'vi'

    }
    print(caps.keys())
    g=input("Enter your country:").lower()
    d=caps.get(g)
    print(d)








    st = input("Enter Your Choice --{Voice Or Text}:").lower()
    st = str(st)
    if st == "voice":
        with sr.Microphone() as source:
            print("-----Say something!!------")
            audio = r.listen(source)
            try:
                speech_text = r.recognize_google(audio)
                print(speech_text)
            except sr.UnknownValueError:
                print(" could not understand audio")
            except sr.RequestError as e:
                print("Somthing error;")
        translator = Translator()
        translate_text = translator.translate(speech_text, dest=d)
        te = translate_text.text
        print(te)

        tts = gTTS(text=te, lang='jw')
        tts.save("good.mp3")
        os.system("good.mp3")
    elif st == "text":

        s = input("enter your text:")
        translator = Translator()
        translate_text = translator.translate(s, dest=d)
        te = translate_text.text
        print(te)
        # s=input("enter your word:")
        tts = gTTS(text=s, lang='jw')
        tts.save("good.mp3")
        os.system("good.mp3")
    else:
        print("some thig wrong!!")
