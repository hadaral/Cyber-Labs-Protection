import psutil


class pro:
    def __init__(self, name,pid):
        self.name = name
        self.pid = pid

    def to_string(self):
        return "pid: "+ self.pid + "\tname: " + self.name+ "\t";