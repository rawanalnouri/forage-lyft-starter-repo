from abc import abstractmethod
from serviceable import Serviceable


class Tires(Serviceable):
    def __init__(self, tires):
        self.tires = tires

    @abstractmethod
    def needs_service(self):
        pass