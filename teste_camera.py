from picamera import PiCamera
from time import sleep

cam = PiCamera()


cam.start_preview()

sleep(5)


cam.capture('/home/pi/Desktop/milagre/foto.jpg')

cam.stop_preview()
