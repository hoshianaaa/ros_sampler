#include"ros/ros.h"
#include"sensor_msgs/JointState.h"
#include"std_msgs/String.h"
#include <iostream>

class MyNode
{
    public:
        MyNode(ros::NodeHandle *nodehandle):nh_(*nodehandle)
         {
            pub = nh_.advertise<std_msgs::String>("/data", 5);
            sub = nh_.subscribe("/data", 1000, &MyNode::callback, this);
            timer = nh_.createTimer(ros::Duration(0.1), &MyNode::main_loop, this);
         }

          void callback(const std_msgs::String& msg)
         {

           std::cout << msg.data << std::endl;

         }

         void main_loop(const ros::TimerEvent &)
         {
            // implement the state machine here
             std_msgs::String msg;
             msg.data = "bbb";
             pub.publish(msg);
         }

    private:
        ros::NodeHandle nh_;
        ros::Publisher pub;
        ros::Subscriber sub;
        ros::Timer timer;
};

int main(int argc, char * argv[])
{
    ros::init(argc, argv, "nodename");
    ros::NodeHandle nh;
    MyNode node = MyNode(&nh);
    ros::spin();
    return 0;
}
