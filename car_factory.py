from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from car import Car

class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery, tires)
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery, tires)
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery, tires)
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery, tires)
    
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tires):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery, tires)