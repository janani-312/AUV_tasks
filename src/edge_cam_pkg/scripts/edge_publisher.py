#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    rospy.init_node('edge_publisher', anonymous=True)
    pub = rospy.Publisher('/edge_image', Image, queue_size=10)
    bridge = CvBridge()

    # Change to 'sample.mp4' to simulate camera with a video file
    cap = cv2.VideoCapture(2)

    if not cap.isOpened():
        rospy.logerr("Failed to open video source")
        return

    rate = rospy.Rate(30)

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.logwarn("Failed to grab frame")
            break

        # Run edge detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)

        # Convert to ROS Image message and publish
        msg = bridge.cv2_to_imgmsg(edges, encoding="mono8")
        pub.publish(msg)

        rate.sleep()

    cap.release()

if __name__ == '__main__':
    main()

