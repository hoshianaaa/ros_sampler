#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *

import os
sys.path.append(os.path.join(os.path.dirname(__file__), './python_utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), './python_ros_utils'))

from python_utils import *
from python_ros_utils import *

import threading
import multiprocessing
from multiprocessing import Process

thread_num = 8

def callback(msg):
  print(msg.data)

def proc():
  for i in range(1000000):
    a = 3^100

rospy.init_node("thread_sample")


r = rospy.Rate(10)
print(os.cpu_count())
t = Timer()

print("thread")
ths = []
for i in range(thread_num):
  ths.append(threading.Thread(target=proc))
  
for i in range(thread_num):
  ths[i].start()

for i in range(thread_num):
  ths[i].join()
print(t.dt())

print("normal")
for i in range(1000000*thread_num):
  a = 3^100
print(t.dt())

mths = []
print("multi process")
for i in range(thread_num):
  mths.append(Process(target=proc))

for i in range(thread_num):
  mths[i].start()

for i in range(thread_num):
  mths[i].join()
print(t.dt())
