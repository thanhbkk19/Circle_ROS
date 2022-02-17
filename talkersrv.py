import rospy
from std_msgs.msg import Int64
from bt2.msg import intstr
from bt2.srv import CheckCompleted, CheckCompletedResponse

def handle_talker(req):
    print(f"send data {req.a}")
    resp = CheckCompletedResponse()
    resp.inci = str(req.a +1)
    resp.state = "done"
    return resp
def talker():
    rospy.init_node("initializer",anonymous=True)
    s = rospy.Service('Send_data', CheckCompleted, handle_talker)
    print("ready to send data ")
    rospy.spin()
    
if __name__ =="__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass 
