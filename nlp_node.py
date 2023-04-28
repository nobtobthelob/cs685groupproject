import rospy
from std_msgs.msg import String

def nlp_callback(data):
    print("message Received @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    d = data.data
    label = d[0]
    amount = d[1]

    # Update the relevant ROS parameters
    # For example, you might use the following syntax to set the max_vel_x parameter for the TrajectoryPlannerROS plugin:
    # rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_x', 0.5)

    local_parameter_path = "cs685groupproject/jackal_helper/configs/params/base_local_planner_params.yaml"

    # relative parameters
    if(amount == -1):
        if label == 0:
            max_vel_x = rospy.get_param(local_parameter_path + '/max_vel_x')
            # Increase the max_vel_x parameter by 20%
            new_max_vel_x = max_vel_x * 1.2
            rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_x', new_max_vel_x)
            rospy.loginfo("max_vel_x increased from %f to %f", max_vel_x, new_max_vel_x)
            max_vel_x = rospy.get_param(local_parameter_path + '/min_vel_x')
            # Increase the max_vel_x parameter by 20%
            new_max_vel_x = max_vel_x * 1.2
            rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_x', new_max_vel_x)
            rospy.loginfo("max_vel_x increased from %f to %f", max_vel_x, new_max_vel_x)

    # absolute parameters
    #else:

    


def nlp_listener():
    rospy.init_node('nlp_listener', anonymous=True)
    rospy.Subscriber('nlp_input', String, nlp_callback)
    rospy.spin()

if __name__ == '__main__':
    nlp_listener()