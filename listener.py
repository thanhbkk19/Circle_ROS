import rospy
from std_msgs.msg import Int64
from bt2.srv import CheckCompleted
from bt2.msg import intstr
x_list = []
y_list = []
def call_black(msg):
    rospy.loginfo(rospy.get_caller_id() + " hear "+ str(msg.A))
    if msg.A ==100:
        rospy.loginfo(rospy.get_caller_id() + " "+ msg.s)

def listener():
    rospy.init_node("drawer", anonymous=True)
    rospy.Subscriber("chatter",intstr,callback=call_black)
    rospy.spin()

if __name__ =="__main__":
    listener()  