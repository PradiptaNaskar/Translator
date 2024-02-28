import speech_recognition as sr
# from google_trans_new import google_translator{not working}
from googletrans import Translator
# import pyttsx3{not working}
# import pyaudio{not working}
import os
from gtts import gTTS
# import google_tts{not working}
# from playsound import playsound{not working}
import threading
print(threading.active_count())
print(threading.enumerate())

r=sr.Recognizer()
while True:

    with sr.Microphone() as source:
        print("------Speek now!!------")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
        except sr.UnknownValueError:
            print(" could not understand audio")
        except sr.RequestError as e:
            print("Somthing error;")
    translator = Translator()
    translate_text = translator.translate(speech_text, dest='ja')
    te = translate_text.text
    print(te)
    # st=input("enter your word:")
    tts = gTTS(text=te, lang='jw')
    tts.save("good.mp3")
    os.system("good.mp3")
    # =============================================
    # voice = gTTS(text=translate_text,slow=False)
    # voice.save("voice.mp3")
    # playsound("voice.mp3")
    # =============================================
    # engine = pyttsx3.init()
    # engine.say(translate_text.text)
    # engine.runAndWait()
    # =============================================

    # engine = pyttsx3.init()
    #
    # engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
    # engine.say(te)
    # engine.runAndWait()
    # ============================================



    # os.remove("good.mp3")
    # playsound('C:\\Users\\Asus\\Desktop\\transletor\\good.mp3')
