import cv2

from picamera import PiCamera
from time import sleep

cam = PiCamera()
cam.start_preview()
sleep(4)

cam.capture('/home/pi/Desktop/milagre/foto.jpg')
cam.stop_preview()


#Carrega a imagem tirada 
image = cv2.imread("foto.jpg", 1)

#Carrega arquivo do cascade para dectar faces e olhos
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#converte pra preto e branco
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#procura o rosto na imagem
faces = face_cascade.detectMultiScale(gray, 1.1, 5)



#identifica a face e olhos
if (len(faces) > 0):
    print "indentificado(s) "+str(len(faces))+" face(s)"
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
    
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
       
    #salva o resultado encontrado da imagem
    cv2.imwrite('result.jpg',image)
else:
    print 'não foi encontrado nenhuma face'
