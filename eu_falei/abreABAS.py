import speech_recognition as sr
import webbrowser

microfone = sr.Recognizer()
x = 1
while x == 1:
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Diga Abrir(Anime house, anime ups, lista animes)\n")
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio,language="pt-BR")
        print("Você disse: "+frase)
    except sr.UnknownValueError:
        print("Não entendi :(\n")

    if frase == "Abrir Anime House" or frase == "Abrir anime House":
        webbrowser.open('https://animeshouse.net')
    elif frase == "Abrir Anime Cima" or frase == "Abrir anime Cima" or frase == "Abrir anime cima":
        webbrowser.open('https://animesup.biz')
    elif frase == "Abrir Lista animes" or frase == "Abrir lista animes":
        webbrowser.open('https://docs.google.com/spreadsheets/d/1l1I4JTJ60KFCNdSAk6xM5eGMPAGhoHX8y17jW-Awbz4/edit?usp=sharing')
    x = int(input("fazer outra escolha? 1-sim/2-não\n"))
    while x < 1 or x > 2:
        x = int(input("1-sim/2-não\n"))
