
import cv2

def contar_pessoas():
    # Carregar o classificador para detecção de corpos inteiros
    full_body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

    # Inicializar a captura de vídeo
    cap = cv2.VideoCapture(0)  # 0 para a câmera padrão

    while True:
        # Capturar o frame
        ret, frame = cap.read()
        if not ret:
            break

        # Converter o frame para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar corpos inteiros na imagem
        bodies = full_body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Mostrar a quantidade de pessoas detectadas
        print("Pessoas na sala:", len(bodies))

        # Desenhar retângulos ao redor dos corpos inteiros detectados
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Mostrar o frame com as detecções
        cv2.imshow('Frame', frame)

        # Parar o loop quando pressionar a tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar os recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    contar_pessoas()