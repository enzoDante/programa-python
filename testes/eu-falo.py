import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print('Diga algo...')
    audio = r.listen(source)
print(r.recognizer_google(audio))