from flask import Flask
from flask import request
import time
import os
from flask_cors import CORS
from flask import send_file


def current_milli_time():
    return round(time.time() * 1000)

def getAllNames():
    allFiles = os.listdir('./uploads')
    names = filter(lambda x: '.mp3' in x, allFiles)
    return sorted(names)

def deleteIfNeeded():
    while doDeleteFiles():
        os.system("rm ./uploads/"+getOldestFile())

def doDeleteFiles():
    names = getAllNames()
    if(len(names) > 10):
        return True
    return False

def getOldestFile():
    return getAllNames()[0]

def getLatestFile():
    return getAllNames()[-1]


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
        file.save('./uploads/'+str(current_milli_time())+".mp3")
        deleteIfNeeded()
    return "success"

@app.route('/theseSpecialHands/latest.mp3', methods=['GET'])
def doGetLatestAudio():
    try:
        return send_file('./uploads/'+getLatestFile(), attachment_filename='latest.mp3')
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run()


