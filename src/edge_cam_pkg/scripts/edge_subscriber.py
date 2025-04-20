#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def callback(msg):
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(msg, desired_encoding="mono8")
    cv2.imshow("Edge Detection Output", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        rospy.signal_shutdown("Quit requested")

def main():
    rospy.init_node('edge_subscriber', anonymous=True)
    rospy.Subscriber('/edge_image', Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

