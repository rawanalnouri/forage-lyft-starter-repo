from engine import Engine


class SternmanEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage, warning_light_is_on):
        super().__init__(current_mileage, last_service_mileage)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.warning_light_is_on
