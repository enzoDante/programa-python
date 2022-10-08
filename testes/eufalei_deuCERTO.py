import speech_recognition as sr

#Habilita o microfone para ouvir o usuario
microfone = sr.Recognizer()
with sr.Microphone() as source:
    #Chama a funcao de reducao de ruido disponivel na speech_recognition
    microfone.adjust_for_ambient_noise(source)
    #Avisa ao usuario que esta pronto para ouvir
    print("Diga alguma coisa: ")
    #Armazena a informacao de audio na variavel
    audio = microfone.listen(source)
try:
    #Passa o audio para o reconhecedor de padroes do speech_recognition
    frase = microfone.recognize_google(audio,language='pt-BR')
    #Após alguns segundos, retorna a frase falada
    print("Você disse: " + frase)
 #Se nao reconheceu o padrao de fala, exibe a mensagem
except sr.UnknownValueError:
    print("Não entendi :(")

x = 'olá'
y = 'https//:'+frase
#print(y)
#print(x.upper())
#if frase == 'olá' or frase == 'Olá':
    #print("deu certo") #muhauauauauu deu certooooo xD
#else:
    #print('n deu certo :(')