from datetime import datetime
from battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super().__init__(current_date, last_service_date)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        current_date = datetime.today().date()
        return service_threshold_date < current_date