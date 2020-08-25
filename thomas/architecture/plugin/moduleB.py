from PyQt5 import QtWidgets, uic

class Plugin():

    def identifier():
        return "id2"

    def author(self):
        return "mail_4u@gmx.de"

    def version(self):
        return "1.1.0"

    def __init__(self):
        print("__init__")