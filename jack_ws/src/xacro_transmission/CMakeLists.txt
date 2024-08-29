cmake_minimum_required(VERSION 3.0.2)
project(xacro_transmission)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  xacro
  urdf
  rviz
)

###################################
## catkin specific configuration ##
###################################
catkin_package()

###########
## Build ##
###########

## Specify additional locations of header files
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Mark executable scripts (Python etc.) for installation
catkin_install_python(PROGRAMS
  src/xacro_publisher.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables

