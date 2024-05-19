from datetime import datetime

from car import Car
# import the various engines, can change to import *
# in future though explicit listing is probably good
# for now
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
# do same for batteries
from battery import SpindlerBattery, NubbinBattery

class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
                    CapuletEngine(current_mileage, last_service_mileage),
                    SpindlerBattery(last_service_date, current_date)
        )

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
                    WilloughbyEngine(current_mileage, last_service_mileage),
                    SpindlerBattery(last_service_date, current_date)
        )

    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(
                    SternmanEngine(warning_light_on),
                    SpindlerBattery(last_service_date, current_date)
        )

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
                    WilloughbyEngine(current_mileage, last_service_mileage),
                    NubbinBattery(last_service_date, current_date)
        )

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
                    CapuletEngine(current_mileage, last_service_mileage),
                    NubbinBattery(last_service_date, current_date)
        )

