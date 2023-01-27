#include "./cpp_ros_utils/psp.h"

int main(int argc, char * argv[])
{
    std::string node_name = "psp_sample";
    ros::init(argc, argv, node_name);
    ros::NodeHandle nh;
    Basic node = Basic(&nh);
    PSP psp = PSP(&nh, "psp_sample/psp");

    std::vector<std::string> mode_list = {"mode1","mode2","mode3"};
    PSP_mode psp_mode = PSP_mode(&nh, "/sample/mode", mode_list);

    ros::Rate loop_rate(100);

    while (ros::ok())
    {
      std::cout << "psp val: " << psp.get_value() << std::endl;
      std::cout << "psp mode val: " << psp_mode.get_value() << std::endl;
      ros::spinOnce();
      loop_rate.sleep();
    }
    return 0;
}
