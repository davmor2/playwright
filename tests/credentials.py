import os

class Creds:
    def __init__(self):
        self.custusername = os.environ.get('custname')
        self.custpassword = os.environ.get('custpassword')
        self.resellerusername = os.environ.get('resellername')
        self.resellerpassword = os.environ.get('resellerpassword')
