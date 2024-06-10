# screen_recorder.py
import mss
import cv2
import numpy as np
import os
import time
import threading

# Configurações de gravação
screen_size = (1920, 1080)  # Substitua com a resolução da sua tela
fps = 20.0
output_path = "/caminho/para/o/projeto/output/"
output_file = os.path.join(output_path, "captura.mp4")

# Verifica se a pasta de saída existe, se não, cria
os.makedirs(output_path, exist_ok=True)

# Configuração do codec e do arquivo de saída
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_file, fourcc, fps, screen_size)

# Função para capturar a tela
def record_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Captura o primeiro monitor

        while True:
            img = sct.grab(monitor)
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            out.write(frame)
            
            # Mostra o vídeo em uma janela
            cv2.imshow("Captura da Tela", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    out.release()
    cv2.destroyAllWindows()

# Executa a gravação da tela em uma thread separada
threading.Thread(target=record_screen).start()

# Aguardar por 60 segundos antes de terminar o script
# Ajuste o tempo conforme necessário
time.sleep(60)

# Parar a captura de tela
cv2.destroyAllWindows()
out.release()
