import cv2
import numpy as np

# Carregar o modelo YOLO pré-treinado
net = cv2.dnn.readNet("D:\codigo-vsCode\ARQUIVOS_SECUNDARIOS\yolov3.weights", "D:\codigo-vsCode\ARQUIVOS_SECUNDARIOS\yolov3.cfg")

# Carregar os nomes das classes
with open("D:\codigo-vsCode\ARQUIVOS_SECUNDARIOS\coco.names", "r") as f:
    classes = f.read().strip().split("\n")

# Definir cores para cada classe
colors = np.random.randint(0, 255, size=(len(classes), 3), dtype="uint8")

# Inicializar a captura de vídeo
cap = cv2.VideoCapture(0)

while True:
    # Capturar o frame da câmera
    ret, frame = cap.read()
    if not ret:
        break
    
    # Passar o frame pelo modelo
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    outputs = net.forward(output_layers)

    # Processar as detecções
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and class_id == 0:  # 0 é o ID da classe "pessoa"
                box = detection[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                (center_x, center_y, width, height) = box.astype("int")
                x = int(center_x - (width / 2))
                y = int(center_y - (height / 2))
                cv2.rectangle(frame, (x, y), (x + width, y + height), colors[class_id], 2)
                text = f"{classes[class_id]}: {confidence:.2f}"
                cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[class_id], 2)

    # Mostrar o frame com as detecções
    cv2.imshow("Camera", frame)

    # Parar o loop quando pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()