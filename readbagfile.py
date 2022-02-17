from numpy import float64
import rosbag
import matplotlib.pyplot as plt
import numpy as np

def convert_bag_data(data_path = "/home/gumiho/project/BTVN_ROS/src/bt2/data/data.txt"):
    bag = rosbag.Bag('/home/gumiho/project/BTVN_ROS/src/bagfiles/full_dataset.bag')
    for topic, msg, t in bag.read_messages(topics=["/sonar_micron"]):
        f = open(data_path,"a")
        f.write(str(msg))
    bag.close()
    return

def prepare_visualization(data_path = "/home/gumiho/project/BTVN_ROS/src/bt2/data/data_visualization.txt"):
    bag = rosbag.Bag('/home/gumiho/project/BTVN_ROS/src/bagfiles/full_dataset.bag')    
    for topic, msg, t in bag.read_messages(topics=["/sonar_micron"]):
        f = open(data_path,"a")
        beam_data=str(msg).split("\n")[-1]
        data_visual = beam_data.split(" ")[-1]
        f.writelines(str(data_visual))
    bag.close()
    return 
def data_visualization(data_path = "/home/gumiho/project/BTVN_ROS/src/bt2/data/data_visualization.txt"):
    bag = rosbag.Bag('/home/gumiho/project/BTVN_ROS/src/bagfiles/full_dataset.bag')  
    i = 0  
    beam = []
    angle = []
    for topic, msg, t in bag.read_messages(topics=[]):
        data=str(msg).split("\n")
        for line in data:

            if "beam_data" in line:
                line = line.replace("beam_data: [","")
                line = line.replace("]header: ","")
                line = line.replace("]","")
                arr = line.split(", ")
                #arr = np.array(arr, dtype=np.int32)
                beam.append(arr)
            if "angle_min:" in line:
                line = line.replace("angle_min: ","")
                rad = float64(line)
                angle.append(np.array([20*np.cos(rad),20*np.sin(rad)]))
        i+=1
        if i ==300*3:
            break

    bag.close()
    return beam, angle
if __name__ == "__main__":
  #  prepare_visualization()
    beam, coordinate =data_visualization()
    beam_np = np.asanyarray(beam)
    coordinate = np.asanyarray(coordinate, dtype=np.float32)
   # np.expand_dims(beam_np)
    x = coordinate[:,0]
    y = coordinate[:,1]
    x_list = []
    y_list = []
    beam_list = []
    for i in range(len(beam_np)):
        for j in range(len(beam_np[i])):
            beam_list.append(int(beam_np[i][j]))
        scale = len(beam_np[i])
        for j in range(scale):
            x_list.append(x[i]/scale*(j+1))
            y_list.append(y[i]/scale*(j+1))
    # print(len(x_list))
    # print(len(y_list))
    # print(len(beam_list))

    fig, ax = plt.subplots()
    ax.scatter(x_list, y_list, c=beam_list, s=100)
    plt.show()



