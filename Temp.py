import os
import glob
import time
import requests

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
endPoint = "http://172.20.125.200:8080/raumtemps"
def read_temp_raw():
	f = open(device_file, 'r')

	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()

	equals_pos = lines[1].find('t=')
	
	if equals_pos != 1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		#temp_f = temp_c * 9.0 / 5.0 + 32.0
		return temp_c
while True:
	temp = read_temp()
	data={"temp": temp,"ort":"3.10"}
	headers = {'Content-Type': 'application/json'}
	r = requests.post(url = endPoint, json = data,headers=headers)
	time.sleep(1)
