import unittest
from datetime import datetime, timedelta

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires
from car import Car


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=1200))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        engine = CapuletEngine(current_mileage=40000, last_service_mileage=5000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=20000, last_service_mileage=15000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=1200))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=50000, last_service_mileage=40000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=80000, last_service_mileage=10000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=50000, last_service_mileage=40000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=True)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=False)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=100))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=True)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=100))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=False)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=40000, last_service_mileage=30000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=1500))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=40000, last_service_mileage=30000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=80000, last_service_mileage=10000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=40000, last_service_mileage=30000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=1500))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        engine = CapuletEngine(current_mileage=80000, last_service_mileage=10000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.8, 0.8, 0.8])
        car = Car(engine, battery, tires)

        self.assertFalse(car.needs_service())

    
class TestTires(unittest.TestCase):
    def test_carrigan_tires_need_service(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.8, 0.9, 0.95, 0.85])
        car = Car(engine, battery, tires)

        self.assertTrue(car.needs_service())

    def test_carrigan_tires_do_not_need_service(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = CarriganTires([0.7, 0.8, 0.85, 0.75])
        car = Car(engine, battery, tires)

        self.assertFalse(car.needs_service())

    def test_octoprime_tires_need_service(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = OctoprimeTires([0.9, 1.2, 0.8, 1.1])
        car = Car(engine, battery, tires)

        self.assertTrue(car.needs_service())

    def test_octoprime_tires_do_not_need_service(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        tires = OctoprimeTires([0.3, 0.5, 0.5, 0.2])
        car = Car(engine, battery, tires)

        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
