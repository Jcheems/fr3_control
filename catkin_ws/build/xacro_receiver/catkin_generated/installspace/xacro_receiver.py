import rospy
from std_msgs.msg import String
import subprocess
import os
import signal

def xacro_callback(data):
    xacro_content = data.data
    xacro_file_path = '/tmp/received_fr3.xacro'
    urdf_file_path = '/tmp/received_fr3.urdf'

    # 保存新的Xacro内容
    with open(xacro_file_path, 'w') as xacro_file:
        xacro_file.write(xacro_content)

    rospy.loginfo("Xacro received and saved to /tmp/received_fr3.xacro")

    # Convert Xacro to URDF with proper arguments
    try:
        subprocess.check_call([
            'rosrun', 'xacro', 'xacro', 
            xacro_file_path, 
            '-o', urdf_file_path, 
            '--inorder', 
            'arm_id:=fr3'
        ])
        rospy.loginfo("Successfully converted Xacro to URDF")
    except subprocess.CalledProcessError as e:
        rospy.logerr("Failed to convert Xacro to URDF: {}".format(e))
        return

    # Launch RViz
    rviz_process = subprocess.Popen(['roslaunch', 'urdf_tutorial', 'display.launch', 'model:={}'.format(urdf_file_path)])

    try:
        rviz_process.wait()  # Wait for RViz to close
    except KeyboardInterrupt:
        rviz_process.send_signal(signal.SIGINT)  # Handle Ctrl+C gracefully

def xacro_receiver():
    rospy.init_node('xacro_receiver', anonymous=True)
    rospy.Subscriber('robot_xacro', String, xacro_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        xacro_receiver()
    except rospy.ROSInterruptException:
        pass
