#!/usr/bin/env python3
#Librerias de ROS2
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
#Librerias de Python
import math

class JointGroupVelocityPublisher(Node):
    def __init__(self):
        super().__init__('joint_group_velocity_publisher')

        self.current_velocity_in_degrees = 90

        self.velocity_publisher = self.create_publisher(
            Float64MultiArray, 
            "/joint_group_velocity_controller/commands", 
            10
        )
         
        self.velocity_msg = Float64MultiArray()
        self.velocity_timer = self.create_timer(0.01, self.publish_velocity_in_joints)
    
    def publish_velocity_in_joints(self):
        self.current_velocity_in_radians = math.radians(self.current_velocity_in_degrees)
        self.velocity_msg.data = [
             self.current_velocity_in_radians,
             self.current_velocity_in_radians,
             self.current_velocity_in_radians,
             self.current_velocity_in_radians
        ]
        self.velocity_publisher.publish(self.velocity_msg)

def main(args=None):
    rclpy.init(args=args)
    joint_angle_velocity_publisher_node = JointGroupVelocityPublisher()
    try:
        rclpy.spin(joint_angle_velocity_publisher_node)
    except KeyboardInterrupt:
        joint_angle_velocity_publisher_node.destroy_node()
        rclpy.try_shutdown()

if __name__ == "__main__":
    main()