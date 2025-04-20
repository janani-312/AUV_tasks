#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from q3.msg import bot_pose

directions = ["north", "east", "south", "west"]
x, y = 0, 0
facing_idx = 0  # Initially facing north

def callback(command):
    global x, y, facing_idx

    if command.data == "forward":
        if directions[facing_idx] == "north":
            y += 1
        elif directions[facing_idx] == "east":
            x += 1
        elif directions[facing_idx] == "south":
            y -= 1
        elif directions[facing_idx] == "west":
            x -= 1

    elif command.data == "turn left":
        facing_idx = (facing_idx - 1) % 4

    elif command.data == "turn right":
        facing_idx = (facing_idx + 1) % 4

    elif command.data == "stop":
        rospy.loginfo("Bot stopped.")
        return

    pose = bot_pose()
    pose.x = x
    pose.y = y
    pose.direction = directions[facing_idx]
    pub.publish(pose)

    rospy.loginfo(f"Current Position → x: {pose.x}, y: {pose.y}, direction: {pose.direction}")


def subscriber_node():
    global pub
    rospy.init_node('pose_subscriber', anonymous=True)
    pub = rospy.Publisher('bot_pose_info', bot_pose, queue_size=10)
    rospy.Subscriber('bot_commands', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass

