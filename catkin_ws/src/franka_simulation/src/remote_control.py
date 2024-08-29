#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from moveit_commander import MoveGroupCommander

def pose_callback(msg):
    move_group.set_pose_target(msg)
    move_group.go(wait=True)

if __name__ == '__main__':
    rospy.init_node('remote_franka_control')
    move_group = MoveGroupCommander('panda')

    rospy.Subscriber('/desired_pose', PoseStamped, pose_callback)
    rospy.spin()
