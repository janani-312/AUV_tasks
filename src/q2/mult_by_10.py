#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def callback(data):
    result = data.data * 10
    rospy.loginfo(f"Received: {data.data}, Multiplied: {result}")
    pub.publish(result)

def subscriber_publisher():
    global pub
    rospy.init_node('multiplier_node', anonymous=True)
    pub = rospy.Publisher('multiplied_by_10', Int32, queue_size=10)
    rospy.Subscriber('multiples_of_2', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber_publisher()
    except rospy.ROSInterruptException:
        pass

