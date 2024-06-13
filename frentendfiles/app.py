from flask import Flask, render_template, request, jsonify
import os
import speech_recognition as sr
from googletrans import Translator
import pyttsx3

app = Flask(__name__)
translator = Translator()

# Language dictionary to map language names to language codes
language_codes = {
   'english': 'en',
    'french': 'fr',
    'danish': 'da',
    'arabic': 'ar',
    'chinese': 'zh-CN',
    'spanish': 'es',
    'german': 'de',
    'italian': 'it',
    'japanese': 'ja',
    'korean': 'ko',
    'portuguese': 'pt',
    'russian': 'ru',
    'turkish': 'tr',
    'hindi': 'hi',
    'urdu': 'ur',
    'swedish': 'sv',
    'dutch': 'nl',
    'greek': 'el',
    'hebrew': 'he',
    'thai': 'th',
    'vietnamese': 'vi',
    'polish': 'pl',
    'norwegian': 'no',
    'finnish': 'fi',
    'czech': 'cs',
    'hungarian': 'hu',
    'romanian': 'ro',
    'indonesian': 'id',
    'malay': 'ms',
    'bulgarian': 'bg',
    'slovak': 'sk',
    'croatian': 'hr',
    'serbian': 'sr',
    'ukrainian': 'uk',
    'persian': 'fa',
    'bengali': 'bn',
    'tamil': 'ta',
    'telugu': 'te',
    'marathi': 'mr',
    'gujarati': 'gu',
    'punjabi': 'pa',
    'swahili': 'sw',
    'amharic': 'am',
    'somali': 'so',
    'zulu': 'zu',
    'afrikaans': 'af',
    'filipino': 'fil',
    'icelandic': 'is',
    'latvian': 'lv',
    'lithuanian': 'lt',
    'estonian': 'et',
    'slovenian': 'sl',
    'albanian': 'sq',
    'bosnian': 'bs',
    'macedonian': 'mk',
    'armenian': 'hy',
    'georgian': 'ka',
    'kazakh': 'kk',
    'mongolian': 'mn',
    'azerbaijani': 'az',
    'uzbek': 'uz',
    'malagasy': 'mg',
    'pashto': 'ps',
    'kurdish': 'ku',
    'tigrinya': 'ti',
    'kannada': 'kn',
    'malayalam': 'ml',
    'sinhalese': 'si',
    'lao': 'lo',
    'khmer': 'km',
    'myanmar': 'my',
    'nepali': 'ne',
}

class SpeechTranslationApp:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def translator_fun(self, text, src_lang, dest_lang):
        return translator.translate(text, src=src_lang, dest=dest_lang).text

    def text_to_voice(self, text_data):
        self.engine.say(text_data)
        self.engine.runAndWait()

    def process_audio(self, input_lang, output_lang, audio_file_path):
        with sr.Microphone() as source:
            # print("Listening...")
            self.recognizer.pause_threshold = 1
            audio = self.recognizer.listen(source, phrase_time_limit=5)

        # with sr.AudioFile(audio_file_path) as source:
        #     audio = self.recognizer.record(source)
        try:
            spoken_text = self.recognizer.recognize_google(audio, language=input_lang)
            translated_text = self.translator_fun(spoken_text, input_lang, output_lang)
            self.text_to_voice(translated_text)
            return translated_text
        except Exception as e:
            return str(e)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    input_lang = request.form['input_lang']
    output_lang = request.form['output_lang']
    audio_file = request.files['audio_data']

    audio_file_path = 'temp_audio.wav'
    audio_file.save(audio_file_path)

    translation_app = SpeechTranslationApp()
    translated_text = translation_app.process_audio(input_lang, output_lang, audio_file_path)

    os.remove(audio_file_path)

    return jsonify({'result': translated_text, 'accuracy': 0.95})  # Example accuracy score

if __name__ == '__main__':
    app.run(debug=True)