from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass

# engine which needs service every 30000 miles
class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        super(Engine, self).__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        # if we go 30000 miles without service, then we need service
        return self.current_mileage - self.last_service_mileage > 30000

# engine which needs service every 60000 miles
class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        super(Engine, self).__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        # if we go 60000 miles without service, then we need service
        return self.current_mileage - self.last_service_mileage > 60000

# engine that needs only be replaced if its engine light is on
class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        super(Engine, self).__init__()
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return self.warning_light_is_on
