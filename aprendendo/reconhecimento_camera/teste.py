#pip install opencv-python
import cv2

def contar_pessoas():
    # Carregar o classificador para detecção de rostos
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Inicializar a captura de vídeo
    cap = cv2.VideoCapture(0)  # 0 para a câmera padrão

    while True:
        # Capturar o frame
        ret, frame = cap.read()
        if not ret:
            break

        # Converter o frame para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostos na imagem
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Mostrar a quantidade de pessoas detectadas
        print("Pessoas na sala:", len(faces))

        # Desenhar retângulos ao redor dos rostos detectados
        for (x, y, w, h) in faces:
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