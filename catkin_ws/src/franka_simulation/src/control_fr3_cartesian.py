#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PoseStamped
import tf.transformations as tft
import numpy as np

class FrankaCartesianController:
    def __init__(self):
        rospy.init_node('franka_cartesian_controller', anonymous=True)

        # 订阅关节状态
        rospy.Subscriber('/franka_state_controller/joint_states', JointState, self.joint_states_callback)

        # 发布目标末端位置
        self.pose_pub = rospy.Publisher('/cartesian_impedance_example_controller/equilibrium_pose', PoseStamped, queue_size=10)

        self.current_joint_states = None

        rospy.sleep(2)  # 确保有足够的时间来获取初始姿态

    def joint_states_callback(self, msg):
        self.current_joint_states = msg

        # 如果需要，可以在这里打印当前关节状态
        rospy.loginfo(f"Current Joint States -> {msg.position}")

    def forward_kinematics(self, joint_states):
        # 简单的正向运动学求解（需用URDF或DH参数表）
        # 这里仅作为占位符，假设返回一个简单的4x4变换矩阵
        # 请替换为适合你的机械臂的实际运动学求解
        return np.eye(4)

    def move_to(self, target_pose):
        # 发布目标末端位置
        self.pose_pub.publish(target_pose)
        rospy.loginfo(f'Moving to x: {target_pose.pose.position.x}, y: {target_pose.pose.position.y}, z: {target_pose.pose.position.z}')

    def execute(self):
        rate = rospy.Rate(10)  # 10 Hz

        while not rospy.is_shutdown():
            if self.current_joint_states is not None:
                # 使用当前关节状态计算末端位置
                end_effector_pose = self.forward_kinematics(self.current_joint_states.position)

                # 假设末端移动目标位置（当前z增加0.1米）
                target_pose = PoseStamped()
                target_pose.header.frame_id = "fr3_link0"
                target_pose.header.stamp = rospy.Time.now()
                target_pose.pose.position.x = end_effector_pose[0, 3]  # 从矩阵中提取位置
                target_pose.pose.position.y = end_effector_pose[1, 3]
                target_pose.pose.position.z = end_effector_pose[2, 3] + 0.1  # 增加高度

                # 使用当前方向（从矩阵提取）
                quat = tft.quaternion_from_matrix(end_effector_pose)
                target_pose.pose.orientation.x = quat[0]
                target_pose.pose.orientation.y = quat[1]
                target_pose.pose.orientation.z = quat[2]
                target_pose.pose.orientation.w = quat[3]

                self.move_to(target_pose)

            rate.sleep()

if __name__ == '__main__':
    try:
        controller = FrankaCartesianController()
        controller.execute()
    except rospy.ROSInterruptException:
        pass
