from New_Design.engine import Engine
from New_Design.battery import Battery


class Car():
    def __init__(self, engine, battery):
        self.battery = battery
        self.engine = engine
        self.components = [self.battery, self.engine]

    def needs_service(self):
        # if any of the components in the car need service, then the car does
        return any(comp.needs_service() for comp in self.components)