#!/usr/bin/env python


## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
import random
from std_msgs.msg import String 
from std_msgs.msg import Int32
from sensor_msgs.msg import Image
import cv2
import os
from cv_bridge import CvBridge


def talker():

    # Create Topics 
    #chatter_topic = rospy.Publisher('chatter', String, queue_size=10)
   # rand_in_topic = rospy.Publisher('rand_int', Int32, queue_size=10)
    image_topic = rospy.Publisher('image_top',Image, queue_size= 3)  

    # Init the publisher
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz


    while not rospy.is_shutdown():

        # Creating the messages 
        #m_hello_str = "hello world %s" % rospy.get_time()
       # m_rand_int = random.randint(1, 101)
        bridge = CvBridge()
        path = os.path.dirname(os.path.abspath(__file__))
        m_image = bridge.cv2_to_imgmsg(cv2.imread(path + '/../img/testimg.jpg'), encoding="passthrough")
     
        # Sendin the messages 
        #chatter_topic.publish(m_hello_str)
        #rand_in_topic.publish(m_rand_int)
        image_topic.publish(m_image)

        # Wait 
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


  