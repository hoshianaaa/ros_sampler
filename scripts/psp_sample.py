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
  psp_num = 3

  for i in range(psp_num):
    psp_list.append(PSP(node_name + "/param" + str(i)))

  psp_str = PSP(node_name + "/mode", "String")

  r = rospy.Rate(100)
  while not rospy.is_shutdown():
    for i in range(psp_num):
      print(psp_list[i].process())
    print(psp_str.process())
    r.sleep()

