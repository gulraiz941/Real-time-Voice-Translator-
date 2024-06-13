from flask import Flask, render_template, request, jsonify
import os
import speech_recognition as sr
from googletrans import Translator
import pyttsx3
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
    # Add more languages as needed
}

class SpeechTranslationApp:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.rec = sr.Recognizer()
        self.input_lang = None
        self.output_lang = None
        self.engine = pyttsx3.init()

    def setup_languages(self):
        print("Select Input Language:")
        for index, (lang_name, lang_code) in enumerate(language_codes.items(), start=1):
            print(f"{index}. {lang_name.capitalize()}")
        input_lang_choice = input("Enter the number for your choice: ")

        if input_lang_choice in map(str, range(1, len(language_codes) + 1)):
            self.input_lang = list(language_codes.values())[int(input_lang_choice) - 1]
        else:
            print("Invalid choice for input language.")

        print("Select Output Language:")
        for index, (lang_name, lang_code) in enumerate(language_codes.items(), start=1):
            print(f"{index}. {lang_name.capitalize()}")
        output_lang_choice = input("Enter the number for your choice: ")

        if output_lang_choice in map(str, range(1, len(language_codes) + 1)):
            self.output_lang = list(language_codes.values())[int(output_lang_choice) - 1]
        else:
            print("Invalid choice for output language.")

    def translator_fun(self, text, src_lang, dest_lang):
        return translator.translate(text, src=src_lang, dest=dest_lang)

    def text_to_voice(self, text_data):
        self.engine.say(text_data)
        self.engine.runAndWait()

    def run(self):
        if self.input_lang is None or self.output_lang is None:
            self.setup_languages()

        while True:
            with sr.Microphone() as source:
                print("Listening...")
                self.rec.pause_threshold = 1
                audio = self.rec.listen(source, phrase_time_limit=13)
            try:
                print("Processing...")
                spoken_text = self.recognizer.recognize_google(audio, language=self.input_lang)

                print(f"Translating to {self.output_lang}...")
                translated_version = self.translator_fun(spoken_text, src_lang=self.input_lang, dest_lang=self.output_lang)

                print(f"Text to Speech in {self.output_lang} (Man's voice)...")
                self.text_to_voice(translated_version.text)

            except Exception as e:
                print(e)

if __name__ == "__main__":
    app = SpeechTranslationApp()
    app.run()
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    input_lang = request.form['input_lang']
    output_lang = request.form['output_lang']
    audio_file = request.files['audio_data']

    # Save the uploaded audio file temporarily
    audio_file_path = 'temp_audio.wav'
    audio_file.save(audio_file_path)

    translation_app = SpeechTranslationApp()
    translation_app.process_audio(input_lang, output_lang, audio_file_path)

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/signin", methods=["POST"])
def signin():
    # Handle the sign-in/sign-up form submission
    # Check if the username and password are correct
    # If they are correct, save the user data in a session or a cookie
    # If they are not correct, return an error message

    # Example:
    username = request.form["username"]
    password = request.form["password"]

    if username == "user" and password == "password":
        # Save user data in a session or a cookie
        return jsonify({"success": True})
    else:
        return jsonify({"error": "Invalid username or password"})

@app.route("/process_audio", methods=["POST"])
def process_audio():
    # Handle the voice translation process
    # Get theinput and output languages and the audio file from the form data
    # Process the audio file using a speech recognition and translation API
    # Return the translation result and the accuracy score

    # Example:
    input_lang = request.form["input_lang"]
    output_lang = request.form["output_lang"]
    audio_data = request.files["audio_data"]

    # Process the audio file using a speech recognition and translation API
    # Example:
    translation_result = "This is the translation result"
    accuracy_score = 0.95

    return jsonify({"result": translation_result, "accuracy": accuracy_score})

if __name__ == "_main_":
    app.run(debug=True)