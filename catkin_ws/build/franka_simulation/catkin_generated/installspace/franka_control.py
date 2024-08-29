#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
import geometry_msgs.msg
from moveit_commander import MoveGroupCommander

def move_to_position():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_fr3', anonymous=True)

    arm = MoveGroupCommander("panda_arm")
    arm.set_named_target("ready")
    arm.go()

    waypoints = []

    # Define start pose
    start_pose = arm.get_current_pose().pose
    waypoints.append(start_pose)

    # Define new pose
    new_pose = geometry_msgs.msg.Pose()
    new_pose.position.x = start_pose.position.x + 0.1
    new_pose.position.y = start_pose.position.y + 0.1
    new_pose.position.z = start_pose.position.z + 0.1
    new_pose.orientation = start_pose.orientation

    waypoints.append(new_pose)

    # Plan and execute
    (plan, fraction) = arm.compute_cartesian_path(waypoints, 0.01, 0.0)
    arm.execute(plan, wait=True)

    # Ensure that there is no residual movement
    arm.stop()
    arm.clear_pose_targets()

    rospy.sleep(5)
    moveit_commander.roscpp_shutdown()

if __name__ == "__main__":
    try:
        move_to_position()
    except rospy.ROSInterruptException:
        pass
