import time
import requests
import RPi.GPIO as GPIO

#endPoint = "http://localhost/raumtemps"
endPoint = "http://172.20.125.200:8080/raumtemps"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
motor = GPIO.PWM(21, 50)

def get_request(url):
        r = requests.get(url)
        result = r.json()
        return result

def start_Motor():
        motor.start(0)
        motor.ChangeDutyCycle(100)

def stop_motor():
        motor.ChangeDutyCycle(0)
        motor.stop()

if __name__ == "__main__":                
        while True:
                result = get_request(url = endPoint)
                temp = result[0][0]
                temp2 = temp
                print(temp)
                if float(temp) > 24:
                        start_Motor()
                else:
                        stop_motor()
                time.sleep(1)