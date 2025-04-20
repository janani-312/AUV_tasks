#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def command_publisher():
    pub = rospy.Publisher('bot_commands', String, queue_size=10)
    rospy.init_node('command_publisher', anonymous=True)
    rate = rospy.Rate(1)

    print("Enter commands: forward | turn left | turn right | stop")

    while not rospy.is_shutdown():
        command = input(">> ").strip().lower()
        if command in ['forward', 'turn left', 'turn right', 'stop']:
            pub.publish(command)
        else:
            print("Invalid command. Use: forward, turn left, turn right, stop")
        rate.sleep()

if __name__ == '__main__':
    try:
        command_publisher()
    except rospy.ROSInterruptException:
        pass

