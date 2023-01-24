from datetime import datetime
from battery.battery import Battery



class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 2
        )
        if datetime.today().date() > service_threshold_date:
            return True
        else:
            return False