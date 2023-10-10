#!/usr/bin/env python3
#Librerias de ROS2
import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory , JointTrajectoryPoint
#Librerias de Python
import math

class JointTrajectoryPublisher(Node):
    def __init__(self):
        super().__init__("joint_trajectory_publisher")
        
        self.joint_group_trajectory_publisher = self.create_publisher(
            JointTrajectory, 
            "/joint_trajectory_controller/joint_trajectory", 
            10
        )
        
        self.timer = self.create_timer(0.1, self.publish_trajectory_in_joints)
        self.joint_group_names = ["rueda_der_joint", "rueda_izq_joint", "polea_der_joint", "polea_izq_joint"]
        self.goal_positions = [math.radians(900), math.radians(900), math.radians(900), math.radians(900)]

        self.joint_group_trajectory_msg = JointTrajectory()
        
    def publish_trajectory_in_joints(self):
        self.joint_group_trajectory_msg.joint_names = self.joint_group_names
        
        goal_point = JointTrajectoryPoint()
        goal_point.positions = self.goal_positions
        goal_point.time_from_start = Duration(sec = 10)

        self.joint_group_trajectory_msg.points.append(goal_point)

        self.joint_group_trajectory_publisher.publish(self.joint_group_trajectory_msg)

def main(args=None):
    rclpy.init(args=args)
    joint_group_trajectory_publisher_node = JointTrajectoryPublisher()
    try:
        rclpy.spin(joint_group_trajectory_publisher_node)
    except KeyboardInterrupt:
        joint_group_trajectory_publisher_node.destroy_node()
        rclpy.try_shutdown()

if __name__ == '__main__':
    main()
