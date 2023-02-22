#!/usr/bin/env python

import rospy
import rosparam

node_name = "ros_param_sampler"
rospy.init_node(node_name)


r = rospy.Rate(10)

rospy.sleep(0.3)

print(node_name)
count = float(rospy.get_param(node_name + "/count", "0.0"))

while not rospy.is_shutdown():

  count = count + 1

  if count > 100:
    count = 0

  print("count:",count)
  rosparam.set_param(node_name + "/count", str(count))

  r.sleep()
