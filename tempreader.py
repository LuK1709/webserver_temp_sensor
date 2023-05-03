import time
import requests
import RPi.GPIO as GPIO

#endPoint = "http://localhost/raumtemps"
endPoint = "http://172.20.125.200:8080/raumtemps"

def get_request(url):
        r = requests.get(url)
        result = r.json()
        return result

def start_Motor():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(21, GPIO.OUT)
        #GPIO.setup(25, GPIO.OUT)

        uhrzeigersinn = GPIO.PWM(21, 50)
        #gegen_uhrzeigersinn = GPIO.PWM(25, 50)

        
        #gegen_uhrzeigersinn.start(0)
        uhrzeigersinn.start(0)
        uhrzeigersinn.ChangeDutyCycle(100)
        #gegen_uhrzeigersinn.ChangeDutyCycle(100)
        # gegen_uhrzeigersinn.stop()

def stop_motor():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(21, GPIO.OUT)
        #GPIO.setup(25, GPIO.OUT)

        uhrzeigersinn = GPIO.PWM(21, 50)
        uhrzeigersinn.stop()

if __name__ == "__main__":        
        while True:
                result = get_request(url = endPoint)
                temp = result[0][0]
                temp2 = temp
                if float(temp) > 23:
                        start_Motor()
                else:
                        stop_motor()
                time.sleep(1)