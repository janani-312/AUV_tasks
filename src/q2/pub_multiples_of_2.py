#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def publisher():
    pub = rospy.Publisher('multiples_of_2', Int32, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(1)
    num = 2
    while not rospy.is_shutdown():
        rospy.loginfo(f"Published: {num}")
        pub.publish(num)
        num += 2
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

