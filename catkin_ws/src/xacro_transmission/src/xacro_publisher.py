import rospy
from std_msgs.msg import String

def xacro_publisher():
    rospy.init_node('xacro_publisher', anonymous=True)
    xacro_pub = rospy.Publisher('robot_xacro', String, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    with open('/opt/ros/noetic/share/franka_description/robots/fr3/fr3.urdf.xacro', 'r') as xacro_file:
        xacro_content = xacro_file.read()

    rospy.loginfo("xacro_publisher node started and publishing Xacro file")

    while not rospy.is_shutdown():
        xacro_pub.publish(xacro_content)
        rate.sleep()

if __name__ == '__main__':
    try:
        xacro_publisher()
    except rospy.ROSInterruptException:
        pass
