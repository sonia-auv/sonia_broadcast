from subscribers.subscriber import Subscriber

# Ajouter un subscriber dans la liste.

def get_subscribers_list(ros_connector):
    sub_list = []
    sub_list.append(Subscriber(ros_connector, '/mission_manager/mission_name_msg', 'mission_manager/MissionNameMsg'))
    sub_list.append(Subscriber(ros_connector, '/proc_control_matlab/pose', 'proc_control_matlab/Pose'))
    return sub_list
        