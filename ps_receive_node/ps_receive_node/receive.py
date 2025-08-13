import rclpy
from rclpy.node import Node
from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
from rclpy.qos import QoSProfile

import numpy as np
import time
import cv2

from mnist_cnn_interface.msg import FpgaIn
from mnist_cnn_interface.msg import Test
#from interface_msg.msg import FpgaOut

class RecNode(Node):

    def __init__(self):
        super().__init__('receive')
        profile = QoSProfile(depth=10, reliability=QoSReliabilityPolicy.RELIABLE, durability=QoSDurabilityPolicy.VOLATILE)
        self.subscription = self.create_subscription(FpgaIn,'fpga_in_topic',self.ps_sub_callback, profile)
        self.subscription
        self.publisher_=self.create_publisher(Test,'fpga_test_topic',profile)
        self.timer = self.create_timer(3.0,self.publish_image)
        self.current_image = None  
        
    def ps_sub_callback(self, msg):
        image_data = np.array(msg.image_in,dtype=np.uint8).reshape((28,28))
        self.get_logger().info('Received image data of shape:{}'.format(image_data.shape))
        cv2.imshow('PC Pub Original Image',image_data)
        cv2.waitKey(1)
        self.current_image = image_data
        
    def publish_image(self):
        if self.current_image is not None:
           msg_out = Test()
           msg_out.test_image_out = self.current_image.flatten().tolist()
           self.publisher_.publish(msg_out)
           self.get_logger().info('Published test image data to fpga_test_topic!')
        else:
           self.get_logger().info('No test image data to publish !')
        
        

def main(args=None):
    rclpy.init(args=args)

    receive = RecNode()
    rclpy.spin(receive)
    
    receive.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

