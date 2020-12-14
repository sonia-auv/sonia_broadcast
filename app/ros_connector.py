# coding: utf-8
import time
import roslibpy

from subscribers.subscribers_list import get_subscribers_list

class RosConnector(object):
    """ Cette classe permet de se connecter à ROSBridge. """
    def __init__(self,parent):
        self.__parent = parent
        self.__ros = None
        self.sub_list = get_subscribers_list(self)
        self.subscribers = {}

    def __str__(self):
        pass

    def connection_to_rosbridge(self,host,port):
        if not self.__ros:
            self.__ros = roslibpy.Ros(host = host, port = port)
            try:
                self.__ros.run()
                time.sleep(1)
            except: 
                self.__parent.print_console("Problème de connexion a RosBridge")
                self.deconnection_to_rosbridge()

    def deconnection_to_rosbridge(self):
        if self.__ros:
            try:
                self.__ros.terminate()
            except:
                self.__parent.print_console("Problème de déconnexion a RosBridge")
            

    def is_connected(self):
        if self.__ros:
            return self.__ros.is_connected
        return False

    def publish(self, topic, message_type, message):
        try:
            publisher = roslibpy.Topic(self.__ros, topic, message_type)
            publisher.publish(roslibpy.Message(message))
        except:
            self.parent.print_console("Erreur avec la publication de votre message.")

    def subscribe_all(self):
        for sub in self.sub_list:
            if sub.topic not in self.subscribers.keys():
                s = roslibpy.Topic(self.__ros, sub.topic, sub.message_type)
                try:
                    s.subscribe(sub.sub_callback)  
                    self.subscribers[sub.topic] = s 
                except:
                    self.__parent.print_console('Impossible de subscribe au topic: ' + sub.topic)
                # print(str(len(self.subscribers))) 

    def send_msg_to_network(self, msg):
        self.__parent.send_msg_to_network(msg)

    def get_sub_count(self):
        return len(self.subscribers)

    def get_pub_count(self):
        return 0
