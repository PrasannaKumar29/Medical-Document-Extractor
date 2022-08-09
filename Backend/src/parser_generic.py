import abc #importing abstract classes


class MedicalDocParser(metaclass=abc.ABCMeta):
    def __init__(self,text):
        self.text=text

    @abc.abstractmethod #this says parse is a abstract method. i.e this method will not be seen its child classes
    def parse(self):
        pass