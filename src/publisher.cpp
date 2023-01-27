#include "ros/ros.h"
#include <std_msgs/String.h>
#include "./cpp_ros_utils/psp.h"

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

  std::vector<std::string> mode_list = {"mode1","mode2","mode3"};
  PSP_mode psp_mode = PSP_mode(&n,"psp_sample/mode", mode_list);

  while (ros::ok())
  {
    msg.data = "aaa";
    pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
  }
  return 0;
}
