import os

class Creds:
    def __init__(self):
        self.custusername = os.environ.get('CUSTNAME')
        self.custpassword = os.environ.get('CUSTPASSWORD')
        self.resellerusername = os.environ.get('RESELLERNAME')
        self.resellerpassword = os.environ.get('RESELLERPASSWORD')
