#!/usr/bin/env python3

import cv2
import time

class SimulatedDepthAIPipeline:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)
        if not self.cap.isOpened():
            raise RuntimeError("Failed to open video source")

    def start(self):
        print("Simulated pipeline started. Press 'q' to quit.")
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("End of stream or cannot fetch frame.")
                break
            time.sleep(0.01)
            cv2.imshow("Simulated DepthAI Output", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    pipeline = SimulatedDepthAIPipeline("sample.mp4")
    pipeline.start()

