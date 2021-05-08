#!/usr/bin/env python3


## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
import random
from std_msgs.msg import String 
from std_msgs.msg import Int32
from sensor_msgs.msg import Image
import os, os.path
from PIL import Image

def talker():
    chatter_topic = rospy.Publisher('chatter', String, queue_size=10)
    rand_in_topic = rospy.Publisher('rand_int', Int32, queue_size=10)
    image_topic = rospy.Publisher('image',Image, queue_size= 3)    
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        m_hello_str = "hello world %s" % rospy.get_time()
        m_rand_int = random.randint(1, 101)
        path = "~/Schreibtisch/ROS-Schein/src/beginner_tutorials/imgg/testimg.jpg"
        m_image = Image.open(path)
        rospy.loginfo(hello_str)
        rospy.loginfo(rand_int)
        chatter_topic.publish(m_hello_str)
        rand_in_topic.publish(m_rand_int)
        image_topic.publish(send_im)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


  