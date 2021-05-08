;; Auto-generated. Do not edit!


(when (boundp 'beginner_tutorials::Num)
  (if (not (find-package "BEGINNER_TUTORIALS"))
    (make-package "BEGINNER_TUTORIALS"))
  (shadow 'Num (find-package "BEGINNER_TUTORIALS")))
(unless (find-package "BEGINNER_TUTORIALS::NUM")
  (make-package "BEGINNER_TUTORIALS::NUM"))

(in-package "ROS")
;;//! \htmlinclude Num.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass beginner_tutorials::Num
  :super ros::object
  :slots (_header _num ))

(defmethod beginner_tutorials::Num
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:num __num) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _num (round __num))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:num
   (&optional __num)
   (if __num (setq _num __num)) _num)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int32 _num
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int32 _num
       (write-long _num s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int32 _num
     (setq _num (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get beginner_tutorials::Num :md5sum-) "aeeda2956bdcc9d4f37a4aa337a4c7c0")
(setf (get beginner_tutorials::Num :datatype-) "beginner_tutorials/Num")
(setf (get beginner_tutorials::Num :definition-)
      "Header header
int32 num
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :beginner_tutorials/Num "aeeda2956bdcc9d4f37a4aa337a4c7c0")


