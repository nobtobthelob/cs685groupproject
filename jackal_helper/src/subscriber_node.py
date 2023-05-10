#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Received message: %s", data.data)
    value = int(data.data.split(",")[0])
    amount = float(data.data.split(",")[1])
    
    max_vel_x = rospy.get_param('/move_base/TrajectoryPlannerROS/max_vel_x')
    min_vel_x = rospy.get_param('/move_base/TrajectoryPlannerROS/min_vel_x')
    acc_lim_x = rospy.get_param('/move_base/TrajectoryPlannerROS/acc_lim_x')
    acc_lim_theta = rospy.get_param('/move_base/TrajectoryPlannerROS/acc_lim_theta')
    max_vel_theta = rospy.get_param('/move_base/TrajectoryPlannerROS/max_vel_theta')
    min_vel_theta = rospy.get_param('/move_base/TrajectoryPlannerROS/min_vel_theta')
    occdist_scale = rospy.get_param('/move_base/TrajectoryPlannerROS/occdist_scale')
    pdist_scale = rospy.get_param('/move_base/TrajectoryPlannerROS/pdist_scale')
    
    if value == 1:
        rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_x', max_vel_x * 1.2)
        rospy.loginfo(f'Updated parameter max_vel_x from {max_vel_x} to {max_vel_x * 1.2}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/min_vel_x', min_vel_x * 1.2)
        rospy.loginfo(f'Updated parameter min_vel_x from {min_vel_x} to {min_vel_x * 1.2}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/acc_lim_x', acc_lim_x * 1.2)
        rospy.loginfo(f'Updated parameter acc_lim_x from {acc_lim_x} to {acc_lim_x * 1.2}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/acc_lim_theta', acc_lim_theta * 1.2)
        rospy.loginfo(f'Updated parameter acc_lim_theta from {acc_lim_theta} to {acc_lim_theta * 1.2}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_theta', max_vel_theta * 1.2)
        rospy.loginfo(f'Updated parameter max_vel_theta from {max_vel_theta} to {max_vel_theta * 1.2}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/min_vel_theta', min_vel_theta * 1.2)
        rospy.loginfo(f'Updated parameter min_vel_theta from {min_vel_theta} to {min_vel_theta * 1.2}')
    elif value == 2:
        rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_x', max_vel_x * 1.4)
        rospy.loginfo(f'Updated parameter max_vel_x from {max_vel_x} to {max_vel_x * 1.4}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/min_vel_x', min_vel_x * 1.4)
        rospy.loginfo(f'Updated parameter min_vel_x from {min_vel_x} to {min_vel_x * 1.4}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/acc_lim_x', acc_lim_x * 1.4)
        rospy.loginfo(f'Updated parameter acc_lim_x from {acc_lim_x} to {acc_lim_x * 1.4}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/acc_lim_theta', acc_lim_theta * 1.4)
        rospy.loginfo(f'Updated parameter acc_lim_theta from {acc_lim_theta} to {acc_lim_theta * 1.4}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_theta', max_vel_theta * 1.4)
        rospy.loginfo(f'Updated parameter max_vel_theta from {max_vel_theta} to {max_vel_theta * 1.4}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/min_vel_theta', min_vel_theta * 1.4)
        rospy.loginfo(f'Updated parameter min_vel_theta from {min_vel_theta} to {min_vel_theta * 1.4}')
    elif value == 3:
        rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_x', max_vel_x * 0.8)
        rospy.loginfo(f'Updated parameter max_vel_x from {max_vel_x} to {max_vel_x * 0.8}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/min_vel_x', min_vel_x * 0.8)
        rospy.loginfo(f'Updated parameter min_vel_x from {min_vel_x} to {min_vel_x * 0.8}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/acc_lim_x', acc_lim_x * 0.8)
        rospy.loginfo(f'Updated parameter acc_lim_x from {acc_lim_x} to {acc_lim_x * 0.8}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/acc_lim_theta', acc_lim_theta * 0.8)
        rospy.loginfo(f'Updated parameter acc_lim_theta from {acc_lim_theta} to {acc_lim_theta * 0.8}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_theta', max_vel_theta * 0.8)
        rospy.loginfo(f'Updated parameter max_vel_theta from {max_vel_theta} to {max_vel_theta * 0.8}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/min_vel_theta', min_vel_theta * 0.8)
        rospy.loginfo(f'Updated parameter min_vel_theta from {min_vel_theta} to {min_vel_theta * 0.8}')
    elif value == 4:
        rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_x', max_vel_x * 0.6)
        rospy.loginfo(f'Updated parameter max_vel_x from {max_vel_x} to {max_vel_x * 0.6}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/min_vel_x', min_vel_x * 0.6)
        rospy.loginfo(f'Updated parameter min_vel_x from {min_vel_x} to {min_vel_x * 0.6}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/acc_lim_x', acc_lim_x * 0.6)
        rospy.loginfo(f'Updated parameter acc_lim_x from {acc_lim_x} to {acc_lim_x * 0.6}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/acc_lim_theta', acc_lim_theta * 0.6)
        rospy.loginfo(f'Updated parameter acc_lim_theta from {acc_lim_theta} to {acc_lim_theta * 0.6}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_theta', max_vel_theta * 0.6)
        rospy.loginfo(f'Updated parameter max_vel_theta from {max_vel_theta} to {max_vel_theta * 0.6}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/min_vel_theta', min_vel_theta * 0.6)
        rospy.loginfo(f'Updated parameter min_vel_theta from {min_vel_theta} to {min_vel_theta * 0.6}')
    elif value == 6:
        rospy.set_param('/move_base/TrajectoryPlannerROS/occdist_scale', occdist_scale * 1.5)
        rospy.loginfo(f'Updated parameter occdist_scale from {occdist_scale} to {occdist_scale * 1.5}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/pdist_scale', pdist_scale * 1.5)
        rospy.loginfo(f'Updated parameter pdist_scale from {pdist_scale} to {pdist_scale * 1.5}')
    elif value == 5:
        rospy.set_param('/move_base/TrajectoryPlannerROS/occdist_scale', occdist_scale * 0.5)
        rospy.loginfo(f'Updated parameter occdist_scale from {occdist_scale} to {occdist_scale * 0.5}')
        rospy.set_param('/move_base/TrajectoryPlannerROS/pdist_scale', pdist_scale * 0.5)
        rospy.loginfo(f'Updated parameter pdist_scale from {pdist_scale} to {pdist_scale * 0.5}')
    elif value == 7:
        rospy.set_param('/move_base/TrajectoryPlannerROS/occdist_scale', amount)
        rospy.loginfo(f'Updated parameter occdist_scale from {occdist_scale} to {amount}')
    elif value == 8:
        rospy.set_param('/move_base/TrajectoryPlannerROS/pdist_scale', amount)
        rospy.loginfo(f'Updated parameter pdist_scale from {pdist_scale} to {amount}')
    elif value == 9:
        rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_x', amount)
        rospy.loginfo(f'Updated parameter max_vel_x from {max_vel_x} to {amount}')
    elif value == 10:
        rospy.set_param('/move_base/TrajectoryPlannerROS/min_vel_x', amount)
        rospy.loginfo(f'Updated parameter min_vel_x from {min_vel_x} to {amount}')
    elif value == 11:
        rospy.set_param('/move_base/TrajectoryPlannerROS/acc_lim_x', amount)
        rospy.loginfo(f'Updated parameter acc_lim_x from {acc_lim_x} to {amount}')
    elif value == 12:
        rospy.set_param('/move_base/TrajectoryPlannerROS/acc_lim_theta', amount)
        rospy.loginfo(f'Updated parameter acc_lim_theta from {acc_lim_theta} to {amount}')
    elif value == 13:
        rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_theta', amount)
        rospy.loginfo(f'Updated parameter max_vel_theta from {max_vel_theta} to {amount}')
    elif value == 14:
        rospy.set_param('/move_base/TrajectoryPlannerROS/min_vel_theta', amount)
        rospy.loginfo(f'Updated parameter min_vel_theta from {min_vel_theta} to {amount}')
    else:
        rospy.logwarn("Invalid value: %d", value)
    
def subscriber_node():
    rospy.init_node('subscriber_node')
    rospy.Subscriber('my_topic', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass
