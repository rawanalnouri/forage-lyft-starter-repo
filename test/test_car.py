import unittest
from datetime import datetime, timedelta

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from car import Car


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=800))
        car = Car(engine, battery)

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        car = Car(engine, battery)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        engine = CapuletEngine(current_mileage=40000, last_service_mileage=5000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        car = Car(engine, battery)

        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        car = Car(engine, battery)

        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=20000, last_service_mileage=15000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=800))
        car = Car(engine, battery)

        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=50000, last_service_mileage=40000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        car = Car(engine, battery)

        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=80000, last_service_mileage=10000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        car = Car(engine, battery)

        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=50000, last_service_mileage=40000)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        car = Car(engine, battery)

        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=True)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        palindrome = Car(engine, battery)

        self.assertTrue(palindrome.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=False)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=100))
        palindrome = Car(engine, battery)

        self.assertFalse(palindrome.needs_service())

    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=True)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=100))
        palindrome = Car(engine, battery)

        self.assertTrue(palindrome.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=False)
        battery = SpindlerBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        palindrome = Car(engine, battery)

        self.assertFalse(palindrome.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=40000, last_service_mileage=30000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=1500))
        rorschach = Car(engine, battery)

        self.assertTrue(rorschach.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=40000, last_service_mileage=30000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        rorschach = Car(engine, battery)

        self.assertFalse(rorschach.needs_service())

    def test_engine_should_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=80000, last_service_mileage=10000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        rorschach = Car(engine, battery)

        self.assertTrue(rorschach.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = WilloughbyEngine(current_mileage=40000, last_service_mileage=30000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        rorschach = Car(engine, battery)

        self.assertFalse(rorschach.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=1500))
        thovex = Car(engine, battery)

        self.assertTrue(thovex.needs_service())

    def test_battery_should_not_be_serviced(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        thovex = Car(engine, battery)

        self.assertFalse(thovex.needs_service())

    def test_engine_should_be_serviced(self):
        engine = CapuletEngine(current_mileage=80000, last_service_mileage=10000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        thovex = Car(engine, battery)

        self.assertTrue(thovex.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = CapuletEngine(current_mileage=20000, last_service_mileage=15000)
        battery = NubbinBattery(current_date=datetime.today().date(), last_service_date=datetime.today().date() - timedelta(days=365))
        thovex = Car(engine, battery)

        self.assertFalse(thovex.needs_service())


if __name__ == '__main__':
    unittest.main()
