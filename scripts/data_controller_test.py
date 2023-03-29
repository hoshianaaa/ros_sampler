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

rospy.init_node("data_controller_test")

pub_topic_name = rospy.get_param("~pub", "data")
sub_topic_name = rospy.get_param("~sub", "data")

print("pub:",pub_topic_name)
print("sub:",sub_topic_name)

pub = rospy.Publisher(pub_topic_name, Float64, queue_size=10)
rospy.Subscriber(sub_topic_name, Float64, callback)

r = rospy.Rate(10)

while not rospy.is_shutdown():
  pub.publish(Float64(0))
  r.sleep()

'''
- example run command
rosrun ros_sampler data_controller_test.py _pub:=aaa _sub:=aaa
'''

