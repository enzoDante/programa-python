import cv2
import numpy as np

# Carregar os arquivos de configuração e pesos pré-treinados do YOLO
net = cv2.dnn.readNet("D:\codigo-vsCode\ARQUIVOS_SECUNDARIOS\yolov3.weights", "D:\codigo-vsCode\ARQUIVOS_SECUNDARIOS\yolov3.cfg")
classes = []
with open("D:\codigo-vsCode\ARQUIVOS_SECUNDARIOS\coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Inicializar a captura de vídeo da webcam
cap = cv2.VideoCapture(0)

while True:
    # Ler um frame do vídeo
    ret, frame = cap.read()
    height, width, channels = frame.shape

    # Detectar objetos no frame
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Processar as saídas da rede neural
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and class_id == 0:  # 0 é o índice da classe pessoa
                # Pessoa detectada
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Remover redundâncias com a supressão não máxima
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Desenhar retângulos ao redor das pessoas detectadas
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = "Pessoa"
            color = colors[0]  # Cor para pessoa é index 0
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y + 30), font, 3, color, 3)

    # Mostrar o frame resultante
    cv2.imshow("Detecção de Pessoas", frame)

    # Esperar por uma tecla e sair se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()