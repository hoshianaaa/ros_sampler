#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *

import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), './python_utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), './python_ros_utils'))

from python_utils import *
from python_ros_utils import *
from psp import PSP

if __name__ == '__main__':

  node_name = "param_sub_pub"
  init(node_name)

  psp_list = []

  for i in range(10):
    psp_list.append(PSP(node_name + "/test_data" + str(i), "String"))

  r = rospy.Rate(100)
  while not rospy.is_shutdown():
    for i in range(10):
      print(psp_list[i].process())
    r.sleep()

