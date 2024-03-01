import os

class Creds:
  def __init__(self):
    self.custusername = os.environ['custname']
    self.custpassword = os.environ['custpassword']
    self.resellerusername = os.environ['resellername']
    self.resellerpassword = os.environ['resellerpassword']
