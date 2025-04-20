    • In the same workspace i made another package called ‘edge_cam_pkg’.
    • Then i made a publisher node. This node will capture frames using OpenCV, and convert the processed frame (edge-detected) into a ROS message.
    • I also used grayscale detection as itsimplifies the image before edge detection since color is not needed for detecting edges.
    • Next i created a subscriber node to receive the edge-detected image and display it in an OpenCV window for visual feedback.
    • The publisher node processes the camera frames by applying edge detection, while the subscriber node displays the resulting edge-detected image.
    • Basically, Q2 was an extention of the Q1 pipeline by applying edge detection on the camera frames and then publishing the processed frames to a new ROS topic.
