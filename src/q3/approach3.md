    • I began by creating a new ROS package called q3 within the existing workspace (chat_ws). It has two Python scripts, one for the publisher node (command_publisher.py) and one for the subscriber node (bot_movement_node.py). I also defined a custom message type named bot_pose.msg to communicate the robot's updated position and direction.
    • bot_pose.msg has 3 fields: 
    • int32 x =  x-coordinate of the bot
    • int32 y = y-coordinate of the bot
    • string direction = current direction the bot is facing (North, East, South, West)
    • Then the publisher node is created. It takes input from the user via the terminal. It reads commands like "forward", "turn left", "turn right", or "stop" and publishes them to a topic /bot_commands which is then sent to std_msgs/String messages. So it basically acts like a remote control for the bot.
    • The subscriber node listens to the /bot_commands topic. It starts at (0,0) facing North. It keeps track of its current orientation using a list of directions (["North", "East", "South", "West"]) and an index to simulate turning left or right.
