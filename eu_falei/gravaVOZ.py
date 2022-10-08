import speech_recognition as sr

microfone = sr.Recognizer()
with sr.Microphone() as source:
    microfone.adjust_for_ambient_noise(source)
    print("Teste de voz de vídeos!!!\n")
    audio = microfone.listen(source)
try:
    frase = microfone.recognize_google(audio,language="pt-BR")
    print("Você disse: "+frase)
except sr.UnknownValueError:
    print("Não entendi :(\n")
