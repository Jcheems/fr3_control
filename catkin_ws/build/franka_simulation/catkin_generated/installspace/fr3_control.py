#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Header

def move_robot():
    rospy.init_node('fr3_control', anonymous=True)
    pub = rospy.Publisher('/cartesian_impedance_example_controller/equilibrium_pose', PoseStamped, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    # 设置目标末端位置 (假设以fr3_link0为参考系)
    target_pose = PoseStamped()
    target_pose.header = Header()
    target_pose.header.frame_id = "fr3_link0"

    # 设置位置 (以米为单位)
    target_pose.pose.position.x = 0.4
    target_pose.pose.position.y = 0.0
    target_pose.pose.position.z = 0.4

    # 设置方向 (四元数表示)
    target_pose.pose.orientation.x = 0.0
    target_pose.pose.orientation.y = 0.0
    target_pose.pose.orientation.z = 0.0
    target_pose.pose.orientation.w = 1.0

    rospy.loginfo("Publishing target pose to /cartesian_impedance_example_controller/equilibrium_pose")

    while not rospy.is_shutdown():
        # 发布目标位置
        pub.publish(target_pose)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass
