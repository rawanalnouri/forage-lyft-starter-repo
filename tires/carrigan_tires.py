from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tires):
        super().__init__(tires)

    def needs_service(self):
        if isinstance(self.tires, list):
            return any(wear >= 0.9 for wear in self.tires)
        else:
            return False