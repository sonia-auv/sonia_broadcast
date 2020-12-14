class Subscriber(object):
    """
    Cette classe définie la structure de tous les subscribers.
    """
    def __init__(self, parent, topic, message_type):
        self.__parent = parent
        self.__topic = topic
        self.__message_type = message_type

    def sub_callback(self, msg):
        self.__parent.send_msg_to_network({self.__topic : {'data' : msg}})
        # print("Message: " + str(msg))

    def prepare_for_network():
        pass

    @property
    def message_type(self):
        return self.__message_type

    @property
    def topic(self):
        return self.__topic
