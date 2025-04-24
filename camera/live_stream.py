from flask import Flask, Response
from picamera import PiCamera
from time import sleep
import io

app = Flask(__name__)
camera = PiCamera()

@app.route('/start-stream', methods=['GET'])
def start_stream():
    camera.start_preview()
    sleep(10)  # stream time
    camera.stop_preview()
    return {"status": "Stream started"}, 200

@app.route('/capture-image')
def capture_image():
    stream = io.BytesIO()
    camera.capture(stream, format='jpeg')
    stream.seek(0)
    return Response(stream.read(), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
