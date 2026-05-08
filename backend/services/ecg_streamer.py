import time
import threading


class ECGStreamer:

    def __init__(self, socketio):
        self.socketio = socketio
        self.data = [0.1, 0.2, 0.3]  # na test
        self.running = False

    def start(self):
        self.running = True
        thread = threading.Thread(target=self.stream)
        thread.start()

    def stop(self):
        self.running = False

    def stream(self):
        i = 0

        while self.running:

            value = self.data[i % len(self.data)]

            self.socketio.emit("ecg", {"value": value})

            i += 1
            time.sleep(0.01)