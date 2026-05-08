from flask import Flask, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

socketio = SocketIO(app, cors_allowed_origins="*")

# import DOPIERO po stworzeniu socketio
from services.ecg_streamer import ECGStreamer

streamer = ECGStreamer(socketio)


@app.route("/")
def home():
    return "ECG backend działa!"


@app.route("/start")
def start():
    streamer.start()
    return jsonify({"status": "started"})


@app.route("/stop")
def stop():
    streamer.stop()
    return jsonify({"status": "stopped"})


if __name__ == "__main__":
    socketio.run(app, debug=True)