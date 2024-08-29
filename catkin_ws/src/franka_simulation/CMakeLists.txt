cmake_minimum_required(VERSION 3.0.2)
project(franka_simulation)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
  geometry_msgs
  moveit_core
  moveit_ros_planning_interface
  franka_control
  franka_description
  franka_gazebo
  franka_hw
  franka_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/fr3_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
