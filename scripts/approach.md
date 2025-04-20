    • First we need to create a ROS workspace. Ive created one and named it ‘depthai_ws’ and then i made a file called  ‘camera_stream.py’. This is where i wrote the code.
    • Here, this file creates a simulated DepthAI pipeline using OpenCV. It does not use a real DepthAI device as i was having issues connecting my laptop camera. Therefore i downloaded a video called ‘sample.mp4’.
    • The code uses cv2 for video capture and GUI. It initializes the video source, loops through video frames and then displays them using OpenCV.
    • In the output, we’ll see a pop-up window titled: ‘simulated depthai output’ which plays the videoin real time.
