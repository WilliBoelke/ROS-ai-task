#!/usr/bin/env python

## This Node Publishes a image to the image_topic
## Its also publishes a nUm msg to the num_topic
## the Num.ms can be found in msg/Num.msg and has a header

import rospy
import random
from std_msgs.msg import String 
from std_msgs.msg import Int32
from beginner_tutorials.msg import Num
from sensor_msgs.msg import Image
import cv2
import os
from cv_bridge import CvBridge


def camera():

    # Create Topics 
    # chatter_topic = rospy.Publisher('chatter', String, queue_size=10)
    # rand_in_topic = rospy.Publisher('rand_int', Int32, queue_size=10)
    image_topic = rospy.Publisher('image_top',Image, queue_size= 3)  
    num_topic = rospy.Publisher('num_topic', Num ,queue_size = 10)
    # Init the publisher
    rospy.init_node('camera', anonymous=True)
    rate = rospy.Rate(10) # 10hz


    while not rospy.is_shutdown():

        # Creating the messages 

        # image : 
        bridge = CvBridge()
        path = os.path.dirname(os.path.abspath(__file__))
        m_image = bridge.cv2_to_imgmsg(cv2.imread(path + '/../img/testimg.jpg'), encoding="passthrough")


        # Num 
        m_num = Num()
        m_num.num = 32

        # Publish the messages 
        image_topic.publish(m_image)
        num_topic.publish(m_num)


        # Wait 
        rate.sleep()


if __name__ == '__main__':
    try:
        camera()
    except rospy.ROSInterruptException:
        pass


  