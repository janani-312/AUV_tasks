#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import threading

name = input("Enter your name (Jolyne/Joestar): ")

def callback(msg):
    if not msg.data.startswith(name + ":"):
        print(f"\n{msg.data}")

def listener():
    rospy.Subscriber("chat_topic", String, callback)
    rospy.spin()

def talker():
    pub = rospy.Publisher("chat_topic", String, queue_size=10)
    rospy.init_node("chat_node", anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = input()
        pub.publish(f"{name}: {msg}")
        rate.sleep()

if __name__ == '__main__':
    try:
        threading.Thread(target=listener).start()
        talker()
    except rospy.ROSInterruptException:
        pass

