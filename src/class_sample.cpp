#include"ros/ros.h"
#include"sensor_msgs/JointState.h"

class MyNode
{
    public:
        MyNode(ros::NodeHandle *nh):
            pub(nh->advertise<sensor_msgs::JointState>("js", 5)),
            sub(nh->subscribe("topic", 1000, &MyNode::callback, this)),
            timer(nh->createTimer(ros::Duration(0.1), &MyNode::main_loop, this))
         {

         }

         void callback(const sensor_msgs::JointState & js) const
         {

         }

         void main_loop(const ros::TimerEvent &) const
         {
            // implement the state machine here
             pub.publish(sensor_msgs::JointState{});
         }

    private:
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
