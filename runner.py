import requests

def send_audio():
    #print('attempting to send audio')
    # url = 'http://127.0.0.1:5000/theseSpecialHands/upload'
    url = 'http://35.167.91.182:8080/theseSpecialHands/upload'

    with open('test2.wav', 'rb') as file:
        data = {}
        files = {'messageFile': file}
        req = requests.post(url, files=files, json=data)
        print(req.status_code)
        print(req.text)

send_audio()