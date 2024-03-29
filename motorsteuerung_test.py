import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

uhrzeigersinn = GPIO.PWM(21, 50)
gegen_uhrzeigersinn = GPIO.PWM(25, 50)

uhrzeigersinn.start(0)
gegen_uhrzeigersinn.start(0)
while True:
    uhrzeigersinn.ChangeDutyCycle(100)
    time.sleep(2)
    uhrzeigersinn.stop()
    gegen_uhrzeigersinn.ChangeDutyCycle(100)
    time.sleep(2)
    gegen_uhrzeigersinn.stop()