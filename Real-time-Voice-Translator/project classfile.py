from gtts import gTTS
import speech_recognition as sr
from googletrans import Translator
from pydub import AudioSegment
from pydub.playback import play

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
        self.recognizer = sr.Recognizer()
        self.rec = sr.Recognizer()

    def translator_fun(self, text, src_lang, dest_lang):
        return translator.translate(text, src=src_lang, dest=dest_lang)

    def text_to_voice(self, text_data, lang_code):
        tts = gTTS(text=text_data, lang=lang_code, slow=False)
        audio = AudioSegment.from_mp3(tts.save("D:\\MP3\\audio.mp3"))
        play(audio)

    def run(self):
        while True:
            with sr.Microphone() as source:
                print("Listening...")
                self.rec.pause_threshold = 1
                audio = self.rec.listen(source, phrase_time_limit=13)
            try:
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
                        spoken_text = self.recognizer.recognize_google(audio, language=input_lang)

                        print(f"Translating to {output_lang}...")
                        translated_version = self.translator_fun(spoken_text, src_lang=input_lang, dest_lang=output_lang)

                        print(f"Text to Speech in {output_lang} (Man's voice)...")
                        self.text_to_voice(translated_version.text, lang_code=output_lang)
                    else:
                        print("Invalid choice for output language.")
                else:
                    print("Processing...")
                    spoken_text = self.recognizer.recognize_google(audio, language=input_lang)

                    # Select Arabic as the output language
                    output_lang = 'ar'

                    print(f"Translating to Arabic...")
                    self.text_to_voice(spoken_text, lang_code=output_lang)

            except Exception as e:
                print(e)

if __name__ == "__main__":
    app = SpeechTranslationApp()
    app.run()