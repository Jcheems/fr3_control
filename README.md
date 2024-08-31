# fr3_control
Welcome to my master's thesis workspace, where all the relevant files from the working period are stored, including original documents, relevant images and video.

# FR3 Manipulator Control and Simulation Project

This project focuses on the simulation, control, and remote operation of the FR3 manipulator using ROS, Gazebo, RViz, and MoveIt. The project is divided into three key components: URDF file transfer, manipulator simulation, and remote control of the real manipulator.

![image](https://github.com/Jcheems/fr3_control/blob/main/fr3.gif)
## Project Structure

- **URDF File Transfer**: Implements the wireless transfer of URDF files between devices. Using ROS communication mechanisms, the project enables the sharing of manipulator models across remote devices, allowing for the seamless transfer and visualization of URDF files in RViz. Image below shows how to find ip of each devce.

- ![iamge](https://github.com/Jcheems/fr3_control/blob/main/find%20ip%20of%20each%20device.png)

- **Manipulator Simulation**: Configures and runs a simulation environment for the FR3 manipulator. The project involves the customization of the MoveIt configuration to achieve precise control of the manipulator's end-effector. This is further extended with Python scripting to enable flexible and automated manipulation tasks. The simulation demonstrates the system's stability and responsiveness in a virtual environment.

- ![iamge](https://github.com/Jcheems/fr3_control/blob/main/simulation_tf.JPG)

- **Remote Control of Real Manipulator**: Enables remote operation of the FR3 manipulator through a cooperative setup involving two devices. The system facilitates the real-time monitoring and control of the manipulator via Wi-Fi, using ROS and MoveIt. This setup demonstrates the system's capability to operate in a real-world scenario, validating the reliability of the control mechanisms in practice.
- ***End effector control
- ![iamge](https://github.com/Jcheems/fr3_control/blob/main/remote_control_1.png)
- ***Python control
- ![iamge](https://github.com/Jcheems/fr3_control/blob/main/remote_control_2.png)

## Getting Started

### Prerequisites

- ROS Noetic
- Gazebo
- RViz
- MoveIt
- Python 3.x
