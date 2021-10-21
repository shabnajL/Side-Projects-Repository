### importing required packages

from gtts import gTTS
import os
from playsound import playsound

### selecting target text to read and targetted language

text1 = "Language is the road map of a culture. It tells you where " \
        "its people come from and where they are going."
language1 = 'en'

### making request to google to get synthesis
### slow=false; to tell the module to convert the audio in high speed
myObj = gTTS(text=text1, lang=language1, slow=False)

### saving the audio file
myObj.save('language1.mp3')

### playing the audio file
### os.system works fine here
#os.system("language1.mp3")
print("Playing audio in ENGLISH now")
playsound("../text-to-speech_converter/language1.mp3")

text2 = "ভাষা একটি সংস্কৃতির রোড ম্যাপ। এটি আপনাকে বলে যে এর মানুষ কোথা থেকে আসে এবং কোথায় যাচ্ছে।"
language2 = 'bn'

myObj2 = gTTS(text=text2, lang=language2, slow=False)
myObj2.save('language2.mp3')
#os.system("language2.mp3")
print("Playing audio in BENGALI now")
playsound("../text-to-speech_converter/language2.mp3")

text3 = "El idioma es la hoja de ruta de una cultura." \
        "Te dice de dónde viene su gente y hacia dónde se dirige."
language3 = 'es'
myObj3 = gTTS(text=text3, lang=language3, slow=False)
myObj3.save('language3.mp3')
print("Playing audio in SPANISH now")
playsound("../text-to-speech_converter/language3.mp3")
print("Thank You")

