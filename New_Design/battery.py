from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass


# specific battery that needs to be replaced every 3 years
class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super(Battery, self).__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        # needs to be replaced every 3 years
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        # if it's after the date that we would need service, then we need it
        return service_threshold_date < self.current_date

# specific battery that needs to be replaced every 4 years
class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super(Battery, self).__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        # needs to be replaced every 2 years
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        # if it's after the date that we would need service, then we need it
        return service_threshold_date < self.current_date