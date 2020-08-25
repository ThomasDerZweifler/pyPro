from PyQt5 import QtWidgets, uic

class Plugin():

    def identifier():
        return "id1"

    def author(self):
        return "thomas.funke@googlemail.com"

    def version(self):
        return "1.0.0"

    def __init__(self):
        print("__init__")
