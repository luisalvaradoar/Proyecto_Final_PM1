import socket
import subprocess

class Internet():
    def internet(self, host="8.8.8.8", port = 53, timeout = 600):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host,port))
            return  True
        except Exception:
            return False