import os

class Creds:
    def __init__(self):
        self.custusername = os.getenv('custname')
        self.custpassword = os.getenv('custpassword')
        self.resellerusername = os.getenv('resellername')
        self.resellerpassword = os.getenv('resellerpassword')
