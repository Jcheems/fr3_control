#!/usr/bin/env python

import sys
import rospy
import moveit_commander
import geometry_msgs.msg
from moveit_commander import MoveGroupCommander, RobotCommander, PlanningSceneInterface

def move_to_pose():
    # 初始化MoveIt API
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_fr3', anonymous=True)

    # 初始化机器人的控制接口
    robot = RobotCommander()
    scene = PlanningSceneInterface()

    # 初始化MoveGroupCommander，用于控制规划组
    group_name = "fr3_arm"  # 你的机械臂规划组名称
    move_group = MoveGroupCommander(group_name)

    # 设置目标位姿
    target_pose = geometry_msgs.msg.Pose()
    target_pose.orientation.w = 1.0
    target_pose.position.x = 0.4
    target_pose.position.y = 0.1
    target_pose.position.z = 0.4

    # 设置目标位姿
    move_group.set_pose_target(target_pose)

    # 规划并执行运动
    plan = move_group.go(wait=True)

    # 停止运动
    move_group.stop()

    # 清除目标位姿
    move_group.clear_pose_targets()

    rospy.sleep(2)

if __name__ == "__main__":
    try:
        move_to_pose()
    except rospy.ROSInterruptException:
        pass

