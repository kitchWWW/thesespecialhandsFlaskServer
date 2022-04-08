import requests

def send_audio():
    #print('attempting to send audio')
    url = 'http://127.0.0.1:5000/theseSpecialHands/audio'
    with open('test.wav', 'rb') as file:
        data = {}
        files = {'messageFile': file}
        req = requests.post(url, files=files, json=data)
        print(req.status_code)
        print(req.text)

send_audio()