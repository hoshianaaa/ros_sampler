#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *

import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), './python_utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), './python_ros_utils'))

from python_utils import *
from python_ros_utils import *

from data_controller import DataController

if __name__ == '__main__':

  node_name = "data_controller_sample"
  init(node_name)

  dc = DataController("data")
  dc.debug_on()
  dc.send(100)
  dc.wait()

