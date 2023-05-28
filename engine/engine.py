from abc import abstractmethod
from serviceable import Serviceable


class Engine(Serviceable):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    @abstractmethod
    def needs_service(self):
        pass
