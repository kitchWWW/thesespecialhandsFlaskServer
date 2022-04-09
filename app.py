from flask import Flask
from flask import request
import time

def current_milli_time():
    return round(time.time() * 1000)


app = Flask(__name__)

def run():
    app.run()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/theseSpecialHands/audio', methods=['GET', 'POST'])
def doUploadAudio():
    if request.method == 'POST':
        file = request.files['messageFile']
        file.save('./uploads/'+str(current_milli_time())+".wav")
    return "success"


if __name__ == "__main__":
    app.run()