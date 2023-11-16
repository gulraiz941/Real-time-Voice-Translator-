from pydub import AudioSegment
from pydub.playback import play

# Load the audio file
audio = AudioSegment.from_file("D:\\MP3\\audio.mp3")

# Play the audio
play(audio)