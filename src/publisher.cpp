#include "ros/ros.h"
#include <std_msgs/String.h>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "pub_sample");

  ros::NodeHandle n;

  ros::Publisher pub = n.advertise<std_msgs::String>("/data", 1);

  double param = 0;
  n.setParam("/param", 11.11);
  n.getParam("/param", param);
  std::cout << "param:" << param << std::endl;


  ros::Rate loop_rate(1);

  std_msgs::String msg;

  while (ros::ok())
  {
    msg.data = "aaa";
    pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
  }
  return 0;
}
