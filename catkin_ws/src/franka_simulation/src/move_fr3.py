#!/usr/bin/env python

import sys
import rospy
import moveit_commander
import geometry_msgs.msg

def move_forward():
    # MoveIt API
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_fr3', anonymous=True)

    # robot interface
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    group_name = "fr3_arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)

    # 获取当前的末端位置
    current_pose = move_group.get_current_pose().pose

    rospy.loginfo("Current Pose: {}".format(current_pose))

    # 定义目标位置
    target_pose = geometry_msgs.msg.Pose()
    target_pose.orientation = current_pose.orientation
    target_pose.position.x = current_pose.position.x - 0.1
    target_pose.position.y = current_pose.position.y
    target_pose.position.z = current_pose.position.z

    # 设置目标位姿
    move_group.set_pose_target(target_pose)

    # 规划路径
    plan = move_group.plan()

    if plan and plan[1]:
        rospy.loginfo("Executing plan...")
        move_group.execute(plan[1], wait=True)

    # 停止运动
    move_group.stop()

    # 清除目标位姿
    move_group.clear_pose_targets()

    # 打印姿态信息
    new_pose = move_group.get_current_pose().pose
    rospy.loginfo("New Pose: {}".format(new_pose))

    rospy.sleep(2)

if __name__ == "__main__":
    try:
        move_forward()
    except rospy.ROSInterruptException:
        pass
