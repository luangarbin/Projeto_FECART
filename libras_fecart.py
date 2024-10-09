import cv2
import mediapipe as mp
from keras.models import load_model
import numpy as np
import h5py
import time
import threading

#Usando webcam
cap = cv2.VideoCapture(0)

#Carregamento do modelo
f = h5py.File("keras_model.h5", mode="r+")
model_config_string = f.attrs.get("model_config")
if model_config_string.find('"groups": 1,') != -1:
    model_config_string = model_config_string.replace('"groups": 1,', '')
    f.attrs.modify('model_config', model_config_string)
    f.flush()
    model_config_string = f.attrs.get("model_config")
    assert model_config_string.find('"groups": 1,') == -1
f.close()

model = load_model('keras_model.h5')

classes = ['A', 'B', 'C', 'D', 'E', 'F']

# senhas e mensagens
senha = "ECA"  
indice_senha = 0  
mensagem = "" 
mensagem_completa = "" 

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

#reconhecendo as maos
hands = mp.solutions.hands.Hands(max_num_hands=1)


tempo_ultima_verificacao = time.time()
intervalo_verificacao = 2  
tempo_mensagem_completa = 0  
mensagem_exibida = False  

def verificar_senha(letra_reconhecida):
    global indice_senha, mensagem, mensagem_completa, tempo_ultima_verificacao, tempo_mensagem_completa, mensagem_exibida
    
    tempo_atual = time.time()
    
    if letra_reconhecida == senha[indice_senha]:
        mensagem = f"Acertou: {letra_reconhecida}!"
        indice_senha += 1  
        
        # verificação das senhas
        if indice_senha == len(senha):
            mensagem_completa = 'Liberou!! A senha:   !'
            tempo_mensagem_completa = time.time()  # tempo de exibição
            mensagem_exibida = True
            time.sleep(15)

            indice_senha = 0  
        if indice_senha == 0: 
            mensagem_completa = ''
            
    else:
        mensagem = f"Aguardando a próxima letra: {senha[indice_senha]}"
    
    tempo_ultima_verificacao = tempo_atual  

# loop principal de captura da imagem e reconhecimento
while True:
    success, img = cap.read()
    frameRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)
    handsPoints = results.multi_hand_landmarks
    h, w, _ = img.shape

    if handsPoints is not None:
        for hand in handsPoints:
            x_max, y_max, x_min, y_min = 0, 0, w, h
            for lm in hand.landmark:
                x, y = int(lm.x * w), int(lm.y * h)
                x_max = max(x, x_max)
                x_min = min(x, x_min)
                y_max = max(y, y_max)
                y_min = min(y, y_min)

            cv2.rectangle(img, (x_min - 50, y_min - 50), (x_max + 50, y_max + 50), (0, 255, 0), 2)

            try:
                # Prepara a imagem recortada e normalizada
                imgCrop = img[y_min - 50:y_max + 50, x_min - 50:x_max + 50]
                imgCrop = cv2.resize(imgCrop, (224, 224))
                imgArray = np.asarray(imgCrop)
                normalized_image_array = (imgArray.astype(np.float32) / 127.0) - 1
                data[0] = normalized_image_array
                
                # Faz a predição da letra
                prediction = model.predict(data)
                indexVal = np.argmax(prediction)
                letra_reconhecida = classes[indexVal]

                # Exibe a letra reconhecida na imagem
                cv2.putText(img, letra_reconhecida, (x_min - 50, y_min - 65), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 5)

                if (time.time() - tempo_ultima_verificacao) >= intervalo_verificacao:
                    threading.Thread(target=verificar_senha, args=(letra_reconhecida,)).start()

            except Exception as e:
                print(f"Erro no reconhecimento: {e}")
                continue

    # mensagens na imagem da camera
    cv2.putText(img, mensagem, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    if mensagem_exibida:
        # Verifica o tempo
        if time.time() - tempo_mensagem_completa < 25:
            cv2.putText(img, mensagem_completa, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            mensagem_exibida = False 
    cv2.imshow('Imagem', img)

    # encerra o programa se for pressionado o 'Esc'
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
