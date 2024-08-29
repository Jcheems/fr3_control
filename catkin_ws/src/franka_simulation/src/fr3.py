#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import numpy as np

def move_arm():
    rospy.init_node('fr3_arm_controller')

    # 创建一个发布者，发布到 /fr3/joint_states 命名空间
    pub = rospy.Publisher('/franka_state_controller/joint_states', JointState, queue_size=10)

    rate = rospy.Rate(10)  # 10Hz

    # 初始化关节状态
    joint_state = JointState()
    joint_state.header = Header()
    joint_state.name = ['fr3_joint1', 'fr3_joint2', 'fr3_joint3', 
                        'fr3_joint4', 'fr3_joint5', 'fr3_joint6', 'fr3_joint7']
    
    # 初始关节角度
    joint_state.position = [-0.00015, -0.7855, 0.0, -2.356, 0.0, 1.571, 0.785]
    joint_state.velocity = [0.0] * 7
    joint_state.effort = [0.0] * 7

    # 每次移动的角度幅度
    delta_angle = 0.1

    while not rospy.is_shutdown():
        # 模拟运动：简单的正弦波运动
        joint_state.header.stamp = rospy.Time.now()

        joint_state.position = [
            joint_state.position[0] + delta_angle * np.sin(rospy.get_time()),
            joint_state.position[1] + delta_angle * np.sin(rospy.get_time() + np.pi / 4),
            joint_state.position[2] + delta_angle * np.sin(rospy.get_time() + np.pi / 2),
            joint_state.position[3] + delta_angle * np.sin(rospy.get_time() + 3 * np.pi / 4),
            joint_state.position[4] + delta_angle * np.sin(rospy.get_time() + np.pi),
            joint_state.position[5] + delta_angle * np.sin(rospy.get_time() + 5 * np.pi / 4),
            joint_state.position[6] + delta_angle * np.sin(rospy.get_time() + 3 * np.pi / 2)
        ]

        # 发布关节状态
        pub.publish(joint_state)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_arm()
    except rospy.ROSInterruptException:
        pass
