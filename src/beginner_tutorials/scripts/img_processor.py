#!/usr/bin/env python


## This node listenes to the image topic to receive images
## from the Camera node
## the images will be processed by using a openCV Threshold un them
## Then they will be published to the processed_image topic 


import rospy
import cv2
import os
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
 

## callback for the 
##
def callback_image_received(data):    
    # making a CV image from the image message 
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')

  
    # publishing the image to the processed image topic 
    ret, cv_image = cv2.threshold(cv_image,127,255,cv2.THRESH_BINARY)
    image_topic.publish(bridge.cv2_to_imgmsg(cv_image))

    #   debugging : save the image to see it
    #   path = os.path.dirname(os.path.abspath(__file__))
    #   cv2.imwrite(path + '/../img/rec.jpg', cv_image)

    

    

def img_processor():

    # initiaze the Node
    rospy.init_node('img_processor', anonymous=True)

    #subscribing to the image-tip topic, where the camera node publishes images
    rospy.Subscriber('image_top', Image, callback_image_received)
   
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()



if __name__ == '__main__':
     ##topic for the processed image 
    image_topic = rospy.Publisher('processes_image',Image, queue_size= 3)
    img_processor()
