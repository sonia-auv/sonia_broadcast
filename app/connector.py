import socket
import json
from threading import Thread
import time

class Connector(Thread):
    def __init__(self, parent, port = 9098):
        super(Connector,self).__init__()
        self.__parent = parent
        self.__udp_socket = None
        self.__host = self.__find_my_ip()
        self.__port = port
        self.__client_socket = None
        self.__bufsize = 1024
        self.__test_data = b'ABC'
        self.__ok_data = b'ok'
        self.__client_list = [('192.168.1.8', 9098)]

        self.__init_socket()
    
    def __str__(self):
        return '\nAdresse du serveur: {} | Port d\'accès: {}'.format(self.__host, self.__port)

    def run(self):
        """ Fonction qui gère la réception des messages fait par les clients. """
        while self.__udp_socket:
            [msg, addr] = self.__udp_socket.recvfrom(self.__bufsize)
            print("Recu: " + str(msg))

    def __init_socket(self):
        """ Cette fonction initialise le socket UDP """
        try:
            self.__udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            address = (self.__host,self.__port)
            self.__udp_socket.bind(address)
            self.__parent.print_console(self.__str__())
        except:
            self.__udp_socket = None
            self.__parent.print_console("Erreur dans la création du socket UDP")

    def send_msg(self, msg):
        self.__parent.print_console(str(msg).encode())
        if self.__udp_socket:
            bytes_to_send = str(msg).encode()
            for client_addr in self.__client_list:
                self.__udp_socket.sendto(bytes_to_send, client_addr)
    
    def __find_my_ip(self):
        """ Cette fonction permet au serveur de trouver l'adresse IP de la machine sur
        laquelle il est. Cette fonction retourne l'adresse ip sous forme de string
        utilisable avec les sockets et le format AF_INET. """
        try:
            mon_ip = ""
            temp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            temp_s.connect(("gmail.com",80))
            mon_ip = temp_s.getsockname()[0] # Addresse IP -> getsockname() retourne (Host, port)
            temp_s.shutdown(socket.SHUT_RDWR)
            temp_s.close()
        except:
            mon_ip = "127.0.0.1"
        return str(mon_ip)

    def __close__connection(self):
        if self.__udp_socket:
            self.__udp_socket.close()
            self.__udp_socket = None
            time.sleep(2) # Attente pour que le socket se ferme.