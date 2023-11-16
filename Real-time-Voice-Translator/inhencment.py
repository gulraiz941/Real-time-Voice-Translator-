from gtts import gTTS
from googletrans import Translator
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
from flask import Flask, render_template, request, jsonify
import SpeechTranslationApp


translator = Translator()

# Language dictionary to map language names to language codes
language_codes = {
    'english': 'en',
    'french': 'fr',
    'danish': 'da',
    'arabic': 'ar',
    'chinese': 'zh-CN'
}

class SpeechTranslationApp:
    def __init__(self):
        self.translated_text = None
        self.recognized_text = None
        self.recognizer = sr.Recognizer()

    def translator_fun(self, text, src_lang, dest_lang):
        return translator.translate(text, src=src_lang, dest=dest_lang).text

    def text_to_voice(self, text_data, lang_code):
        tts = gTTS(text=text_data, lang=lang_code, slow=False)
        audio = AudioSegment.from_mp3(tts.save("D:\\MP3\\audio.mp3"))
        play(audio)

    def process_input(self, audio):
        print("Select Input Language:")
        print("1. Urdu")
        input_lang_choice = input("Enter the number for your choice: ")

        input_lang = 'ur'  # Default is Urdu
        if input_lang_choice == '1':
            print("Select Output Language:")
            for index, (lang_name, lang_code) in enumerate(language_codes.items(), start=2):
                print(f"{index}. {lang_name.capitalize()}")
            output_lang_choice = input("Enter the number for your choice: ")

            if output_lang_choice in map(str, range(2, len(language_codes) + 2)):
                output_lang = list(language_codes.values())[int(output_lang_choice) - 2]

                print("Processing...")
                self.recognized_text = self.recognize_audio(audio, language=input_lang)
                self.translated_text = self.translator_fun(self.recognized_text, src_lang=input_lang, dest_lang=output_lang)
            else:
                print("Invalid choice for the output language.")
        else:
            print("Processing...")
            self.recognized_text = self.recognize_audio(audio, language=input_lang)

            # Select Arabic as the output language
            output_lang = 'ar'

            self.translated_text = self.translator_fun(self.recognized_text, src_lang=input_lang, dest_lang=output_lang)

        print(f"Translated to {output_lang}: {self.translated_text}")
        print(f"Text to Speech in {output_lang} (Man's voice)...")
        self.text_to_voice(self.translated_text, lang_code=output_lang)

    def recognize_audio(self, audio, language):
        return self.recognizer.recognize_google(audio, language=language)

    def run(self):
        while True:
            audio = self.listen_to_audio()
            self.process_input(audio)

    def listen_to_audio(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source, phrase_time_limit=13)
        return audio

from your_backend_script import SpeechTranslationApp

app = Flask(__name__)

# Initialize the SpeechTranslationApp
translation_app = SpeechTranslationApp()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    try:
        audio_file = request.files['audio_data']
        input_lang = request.form['input_lang']
        output_lang = request.form['output_lang']

        # Process the audio using the SpeechTranslationApp
        result, audio_filename = translation_app.process_audio(audio_file, input_lang, output_lang)

        return jsonify(result=result, audio_file=audio_filename)
    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run();