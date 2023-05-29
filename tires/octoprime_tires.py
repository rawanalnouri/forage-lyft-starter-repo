from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tires):
        super().__init__(tires)

    def needs_service(self):
        if isinstance(self.tires, list):
            return sum(self.tires) >= 3
        else:
            return False