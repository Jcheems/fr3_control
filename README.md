# FR3_control
Welcome to my master's thesis workspace, where all the relevant files from the working period are stored, including original documents, relevant images and video. The origin dissertation can be accessed by [Master dissertation](https://github.com/Jcheems/fr3_control/blob/main/11428365.pdf).

# FR3 Manipulator Control and Simulation Project

This project focuses on the simulation, control, and remote operation of the FR3 manipulator using ROS, Gazebo, RViz, and MoveIt. The project is divided into three key components: URDF file transfer, manipulator simulation, and remote control of the real manipulator.

![image](https://github.com/Jcheems/fr3_control/blob/main/fr3.gif)

## FR3 TF Tree

![image](https://github.com/Jcheems/fr3_control/blob/main/tf_tree.png)

## Project Structure

- **URDF File Transfer**: Implements the wireless transfer of URDF files between devices. Using ROS communication mechanisms, the project enables the sharing of manipulator models across remote devices, allowing for the seamless transfer and visualization of URDF files in RViz. Image below shows how to find ip of each devce.

![iamge](https://github.com/Jcheems/fr3_control/blob/main/find%20ip%20of%20each%20device.png)

- **Manipulator Simulation**: Configures and runs a simulation environment for the FR3 manipulator. The project involves the customization of the MoveIt configuration to achieve precise control of the manipulator's end-effector. This is further extended with Python scripting to enable flexible and automated manipulation tasks. The simulation demonstrates the system's stability and responsiveness in a virtual environment.

![iamge](https://github.com/Jcheems/fr3_control/blob/main/simulation_tf.JPG)

- **Remote Control of Real Manipulator**: Enables remote operation of the FR3 manipulator through a cooperative setup involving two devices. The system facilitates the real-time monitoring and control of the manipulator via Wi-Fi, using ROS and MoveIt. This setup demonstrates the system's capability to operate in a real-world scenario, validating the reliability of the control mechanisms in practice.
- ***End effector control***
![iamge](https://github.com/Jcheems/fr3_control/blob/main/remote_control_1.png)
- ***Python control***
![iamge](https://github.com/Jcheems/fr3_control/blob/main/remote_control_2.png)

Here is an example:
<video src='https://github.com/user-attachments/assets/6a353f51-a0d2-4f26-9ad0-0df41c4e408f' width=180/>

## Getting Started

### Prerequisites

- ROS Noetic
- Gazebo
- RViz
- MoveIt
- Python 3.x

### Setting device communication

Ensure two devices connecting the same internet, check ip by:

```
show addr ip
```

This command will display information about all network interfaces.Look for the interface that corresponds to your network connection (e.g,'ethO'for a wired connection, wlan0' or 'wlp* for a wireless connection) and look for the inet entry underneath t, which shows the lPv4address. Example:

![iamge](https://github.com/Jcheems/fr3_control/blob/main/find%20ip%20of%20each%20device.png)

In the above example, the lP4 address of the wlp0s20f3'interface is 10.206.71.253 Then set ROS Master UR, on the device which is connectedto the manipulator(device A):

```
export ROS_MASTER_URI=http:/ /<IP of device A>:11311
export ROS_HOSTNAME=<IP of device A>
```

On the other device which is connected wireless(device B):

```
export ROS_MASTER_URI=http://<IP of device A> :11311
export ROS_HOSTNAME=<IP of device B>
```

11311 is the ros default interface.
You can check these variables by:

```
echo $ROS_MASTER_URI
echo $ROS_HOSTNAME
```

Test the connection by entering command on device B:

```
ping <IP of device A>
```


Or launch a node on device A and entering on device B by:

```
rostopic list
rosnode list
rosnode info /rosout
```

lf you are experiencing problems such as not being able to resolve hostnames，you need to update the '/etc/hosts' file by:

```
sudo nano /etc/hosts
```

Add the similar following lines:

```
192.168.12.45 your device name
192.168.24.78 your device name
```

### URDF Transmission
Start roscore on device A:

```
roscore
```

Start the publisher in another termnial:

```
rosrun xacro_transmission xacro_publisher.py

```
Start the receiver on device B:

```
rosrun xacro_receiver xacro_receiver.py
```

Device B will automatically open RViz and displays the model.

### Manipulator Simulation
Start a simple demo created by Movelt:

```
roslaunch fr3_moveit_config demo. launch
```

Python control:

```
rosrun fr3_moveit_config move_fr3.py
```

![iamge](https://github.com/Jcheems/fr3_control/blob/main/end%20effector%20control.png)

### Remote Control
Connect device A with FR3 manipulator FCl, start roscore:

```
roscore
```

In another terminal, run:

```
roslaunch panda_moveit_config franka_control.launch arm_id:=fr3
```

You can see and control the manipulator through RViz:

![iamge](https://github.com/Jcheems/fr3_control/blob/main/remote_control_1.png)

On device B, start RViz:

```
RViz
```

You can also run your python code with proper interface:

Python control 1 | Python control 2
:-: | :-:
<video src='https://github.com/user-attachments/assets/c92e218d-6cd5-4ec3-a745-399b819a0d58' width=180/> | <video src='https://github.com/user-attachments/assets/6eafc434-a1d5-42bd-9057-7c8a6386fa2c' width=180/>

For more item descriptions and instructions check out [Master dissertation](https://github.com/Jcheems/fr3_control/blob/main/11428365.pdf).
