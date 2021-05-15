#!/usr/bin/env python


import rospy
import random
from std_msgs.msg import String 
from std_msgs.msg import Int32
from beginner_tutorials.msg import Num
from sensor_msgs.msg import Image
import cv2
import os
from beginner_tutorials.msg import Num
import message_filters
from cv_bridge import CvBridge



def synchronized_callback(image, num):
    nums.append(num.num)
    images.append(image)
    deb = "listLenghts number = "  + str(len(nums)) + ", " + str(len(images))
    rospy.loginfo(deb)


def controller():

    # initiaze the Node
    rospy.init_node('controller', anonymous=True)

    #subscribing to the image-tip topic, where the camera node publishes images
    image_sub = message_filters.Subscriber('processed_image', Image)

    #subscribing to the num-tip topic, where the camera node publishes images
    num_sub = message_filters.Subscriber('num_topic', Num)
   
    ts = message_filters.TimeSynchronizer([image_sub, num_sub], 10)
    ts.registerCallback(synchronized_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()



if __name__ == '__main__':
    nums = list()
    images = list()
    controller()
