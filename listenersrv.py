import rospy
from std_msgs.msg import Int64
from bt2.srv import CheckCompleted
from bt2.msg import intstr
import sys
def receive_clients(x):
    rospy.wait_for_service("Send_data")
    try:
        receive = rospy.ServiceProxy("Send_data", CheckCompleted)
        response1 = receive(x)
        return response1.inci, response1.state
    except rospy.ServiceException as e:
        print("Service call failed: "+e)

if __name__ =="__main__":
    if len(sys.argv) ==2:
        x = int(sys.argv[1])
    else:
        print(sys.argv[0],"-------")
        sys.exit(1)
    
    srv = receive_clients(x)
    print("file path ", sys.argv[0])
    print("Requesting number ", srv[0])
    print("Requesting state", srv[1])