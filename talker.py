import rospy
from std_msgs.msg import Int64
from bt2.msg import intstr
from bt2.srv import CheckCompleted
def talker(Reset = True, i = 0, max=101):
    pub = rospy.Publisher("chatter", intstr, queue_size=10)
    rospy.init_node("initializer",anonymous=True)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        message = i 
        rospy.loginfo(message)
        pub.publish(message, "done")
        i+=1
        if i == max and Reset:
            i=0
        rate.sleep()

if __name__ =="__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass 
