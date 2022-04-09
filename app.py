from flask import Flask
from flask import request
import time
import os
from flask_cors import CORS

def current_milli_time():
    return round(time.time() * 1000)

def deleteIfNeeded():
    while doDeleteFiles():
        os.system("rm ./uploads/"+getOldestFile())

def doDeleteFiles():
    allFiles = os.listdir('./uploads')
    names = list(filter(lambda x: '.wav' in x, allFiles))
    if(len(names) > 10):
        return True
    return False

def getOldestFile():
    allFiles = os.listdir('./uploads')
    names = filter(lambda x: '.wav' in x, allFiles)
    snames = sorted(names)
    print(snames)
    return snames[0]


def getLatestFile():
    allFiles = os.listdir('./uploads')
    names = filter(lambda x: '.wav' in x, allFiles)
    snames = sorted(names)
    print(snames)
    return snames[-1]


app = Flask(__name__)
CORS(app)

def run():
    app.run()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/theseSpecialHands/upload', methods=['POST'])
def doUploadAudio():
    if request.method == 'POST':
        file = request.files['messageFile']
        file.save('./uploads/'+str(current_milli_time())+".wav")
        deleteIfNeeded()
    return "success"

@app.route('/theseSpecialHands/latest', methods=['GET'])
def doGetLatestAudio():
    try:
        return send_file('./uploads/'+getLatestFile(), attachment_filename='latest.wav')
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run()


