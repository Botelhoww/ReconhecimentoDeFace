import cv2
import mediapipe as mp
import requests
from requests.structures import CaseInsensitiveDict

webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils


url = "https://localhost:7152/api/job-vacancies"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

data = """
{
 "Title": "ACHOU UM CARA",
 "Description": "ACHOU UM CARA",
 "Company":"ACHADOS",
 "SalaryRange": "0"
}
"""

# DAR GET
# url = "https://localhost:7152/api/job-vacancies"
# resp = requests.get(url, verify=False)
# conteudp = resp.content
# texto = resp.text

while True:
    verificador, frame = webcam.read()

    if not verificador:
        break

    lista_rostos = reconhecedor_rostos.process(frame)

    qtd = 0
    #se existe algum rosto
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            qtd + 1
            desenho.draw_detection(frame, rosto)
            resp = requests.post(url, headers=headers, data=data, verify=False)
            print('passou: ', qtd, 'x')

    cv2.imshow("Detecção Facial", frame)

    if cv2.waitKey(5) == 27:
        break

webcam.release()