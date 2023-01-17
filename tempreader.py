import time
import requests

#endPoint = "http://localhost/raumtemps"
endPoint = "http://172.20.125.200:8080/raumtemps"

def get_request(url):
        r = requests.get(url)
        result = r.json()
        return result
if __name__ == "__main__":        
        while True:
                result = get_request(url = endPoint)
                temp = result[0][0]
                temp2 = temp
                if float(temp) > 20:
                        print("Warm")
                time.sleep(1)