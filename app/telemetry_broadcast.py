import time
from view.view import View
from app.ros_connector import RosConnector
from app.connector import Connector

class TelemetryBroadcast(object):
    """ Cette classe est la classe principale du broadcast de la télémétrie de SONIA. 
        Elle orchestre le pont entre ROSBridge et la télémétrie. 
    """
    def __init__(self):
        self.__view = View(self)
        self.__ros_connector = RosConnector(self)
        self.__host = '0.0.0.0'
        self.__port = 9090

        self.__connector = None

        self.__run()

    def __run(self):
        self.__ros_connector.connection_to_rosbridge(self.__host, self.__port)
        if self.__ros_connector.is_connected():
            self.__ros_connector.subscribe_all()
            self.__connection_to_connector()
        try:
            while self.__ros_connector.is_connected():
                self.__view.print_console("Ok")
                time.sleep(0.5)
            self.__ros_connector.deconnection_to_rosbridge()
        except KeyboardInterrupt:
            self.__ros_connector.deconnection_to_rosbridge()

    def __connection_to_connector(self):
        if not self.__connector:
            self.__connector = Connector(self)
            self.__connector.daemon = True
            self.__connector.start()

    def send_msg_to_network(self, msg):
        self.__connector.send_msg(msg)

    def publish(self, topic, message_type, message):
        self.__ros_connector.publish(topic, message_type, message)       

    def print_console(self, message):
        """ Cette fonction permet d'afficher à la console. """
        self.__view.print_console(message)
    
    def test_publish():
        self.publish('/mission_manager/mission_name_msg',
                        'mission_manager/MissionNameMsg',
                        {'name': 'Example'}) 
