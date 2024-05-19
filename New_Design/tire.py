from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service(self):
        pass

class CarriganTire(Tire):
    def __init__(self, tire_wear_arr):
        super(Tire, self).__init__()
        self.tire_wear_arr = tire_wear_arr

    def needs_service(self):
        # need service if any tire has at least 0.9 wear
        return any(tire >= 0.9 for tire in self.tire_wear_arr)

class OctoprimeTire(Tire):
    def __init__(self, tire_wear_arr):
        super(Tire, self).__init__()
        self.tire_wear_arr = tire_wear_arr

    def needs_service(self):
        # need service if the total amount of wear is at least 3
        return sum(self.tire_wear_arr) >= 3