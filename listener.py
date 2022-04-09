import pyaudio
import wave
import requests
import threading


def fire_and_forget(fileName):
    threading.Thread(target=send_audio, args=([fileName])).start()

def send_audio(fileName):
    #print('attempting to send audio')
    # url = 'http://127.0.0.1:5000/theseSpecialHands/upload'
    url = 'http://35.167.91.182:8080/theseSpecialHands/upload'
    os.system("ffmpeg -i "+fileName+".wav "+fileName+".mp3")
    with open(fileName+".mp3", 'rb') as file:
        data = {}
        files = {'messageFile': file}
        req = requests.post(url, files=files, json=data)
        print(req.status_code)
        print(req.text)



chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
filename = "output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

seconds = 1 # how long between writes and sends
z = 0
while(True):
    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk) # ,exception_on_overflow = False
        frames.append(data)
        print(len(frames))
        while(len(frames) > 700):
            frames.pop(0)
    # Save the recorded data as a WAV file
    audioFilePath = "./sending/o"+str(z)
    print(audioFilePath)
    wf = wave.open(audioFilePath+".wav", 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    fire_and_forget(audioFilePath)
    z+=1

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()