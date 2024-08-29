import zmq
import numpy as np

def connect_to_sim():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:19997")
    return socket

def send_request(socket, request):
    socket.send_string(request)
    response = socket.recv_string()
    return response

socket = connect_to_sim()

joint_names = [
    'Franka_joint1', 'Franka_joint2', 'Franka_joint3',
    'Franka_joint4', 'Franka_joint5', 'Franka_joint6',
    'Franka_joint7'
]

joint_handles = []
for name in joint_names:
    request = f"simxGetObjectHandle {name} -1"
    response = send_request(socket, request)
    joint_handle = int(response.split(' ')[-1])
    joint_handles.append(joint_handle)

def set_joint_position(joint_handle, position):
    request = f"simxSetJointTargetPosition {joint_handle} {position} -1"
    send_request(socket, request)

# 示例：设置所有关节到特定位置
target_positions = [0.0, -0.5, 0.5, -1.0, 0.0, 0.5, 0.0]
for handle, position in zip(joint_handles, target_positions):
    set_joint_position(handle, position)

def start_simulation():
    request = "simxStartSimulation"
    send_request(socket, request)

def stop_simulation():
    request = "simxStopSimulation"
    send_request(socket, request)

start_simulation()

# 等待一段时间让仿真运行
import time
time.sleep(5)

stop_simulation()
