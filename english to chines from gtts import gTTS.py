from gtts import gTTS
import speech_recognition as sr
from googletrans import Translator
import playsound
import os

translator = Translator()

def translator_fun(text, src_lang, dest_lang):
    return translator.translate(text, src=src_lang, dest=dest_lang)

def text_to_voice(text_data, lang_code):
    myobj = gTTS(text=text_data, lang=lang_code, slow=False)
    myobj.save("D:\\MP3\\audio.mp3")
    playsound.playsound("D:\\MP3\\audio.mp3")
    
while True:
    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold = 1
        audio = rec.listen(source, phrase_time_limit=13)
    try:
        print("Processing...")
        spoken_text = rec.recognize_google(audio, language='en')  # Recognize speech in English
        
        print("Translating to Chinese...")
        chinese_version = translator_fun(spoken_text, src_lang='en', dest_lang='zh-CN')
        
        print("Text to Speech in Chinese...")
        text_to_voice(chinese_version.text, lang_code='zh-CN')
   
    except Exception as e:
        print(e)