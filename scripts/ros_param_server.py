#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *

import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), './python_utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), './python_ros_utils'))

from python_utils import *
from python_ros_utils import *

def callback(msg):
  print(msg.data)

rospy.init_node("ros_param_server")

file_name = rospy.get_param("~file_name", "~/.ros/ros_param_server_test")
print("file_name:",file_name)

'''
pub_topic_name = rospy.get_param("~pub", "data")
sub_topic_name = rospy.get_param("~sub", "data")

print("pub:",pub_topic_name)
print("sub:",sub_topic_name)

pub = rospy.Publisher(pub_topic_name, Float64, queue_size=10)
rospy.Subscriber(sub_topic_name, Float64, callback)
'''

ret = isfile(file_name)
print(ret)
if ret:
  bash_cmd("rosparam load " + file_name)

rospy.sleep(1)

r = rospy.Rate(10)

while not rospy.is_shutdown():
  #pub.publish(Float64(0))
  bash_cmd("rosparam dump " + file_name)
  r.sleep()

'''
- example run command
rosrun ros_sampler ros_param_server.py _pub:=aaa _sub:=aaa
'''

