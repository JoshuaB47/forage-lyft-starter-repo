from datetime import datetime

from New_Design.car import Car
# import the various engines, can change to import *
# in future though explicit listing is probably good
# for now
from New_Design.battery import SpindlerBattery, NubbinBattery
from New_Design.engine import CapuletEngine, WilloughbyEngine, SternmanEngine
# do same for batteries


class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
                    CapuletEngine(current_mileage, last_service_mileage),
                    SpindlerBattery(last_service_date, current_date)
        )

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
                    WilloughbyEngine(current_mileage, last_service_mileage),
                    SpindlerBattery(last_service_date, current_date)
        )

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        return Car(
                    SternmanEngine(warning_light_on),
                    SpindlerBattery(last_service_date, current_date)
        )

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
                    WilloughbyEngine(current_mileage, last_service_mileage),
                    NubbinBattery(last_service_date, current_date)
        )

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
                    CapuletEngine(current_mileage, last_service_mileage),
                    NubbinBattery(last_service_date, current_date)
        )

