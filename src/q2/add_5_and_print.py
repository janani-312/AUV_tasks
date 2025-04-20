#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def callback(data):
    final_result = data.data + 5
    rospy.loginfo(f"Final Result: {final_result}")

def subscriber():
    rospy.init_node('final_node', anonymous=True)
    rospy.Subscriber('multiplied_by_10', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass

