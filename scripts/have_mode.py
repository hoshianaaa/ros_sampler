#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *

import os
sys.path.append(os.path.join(os.path.dirname(__file__), './python_utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), './python_ros_utils'))

from python_utils import *
from python_ros_utils import *

mode_list = ["mode1","mode2","mode3"]
mode = "mode1"

def callback(msg):
  global mode, node_name
  d = msg.data
  if d in mode_list:
    mode = d
    rosparam.set_param("/node_name/mode",mode)

node_name = "have_mode"
rospy.init_node(node_name)

pub_topic_name = rospy.get_param("~pub", "mode_list")
sub_topic_name = rospy.get_param("~sub", "mode")

print("pub:",pub_topic_name)
print("sub:",sub_topic_name)

pub = rospy.Publisher(pub_topic_name, String, queue_size=10)
rospy.Subscriber(sub_topic_name, String, callback)

r = rospy.Rate(10)

while not rospy.is_shutdown():
  pub.publish(String(list2string(mode_list)))
  print(mode)
  r.sleep()

'''
- example run command
rosrun ros_sampler have_mode.py _pub:=aaa _sub:=aaa
'''

