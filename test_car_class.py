import car_class
import unittest

class CarClassTest(unittest.TestCase):
    """docstring for CarClassTest"""

    def test_car_instance(self):
        honda = car_class.Car('Honda')
        self.assertIsInstance(honda, car_class.Car, msg='The object should be an instance of the `Car` class')

    def test_object_type(self):
        honda = car_class.Car('Honda')
        self.assertTrue((type(honda) is car_class.Car), msg='The object should be a type of `Car`')

    def test_default_car_name(self):
        gm = car_class.Car()
        self.assertEqual('General', gm.name,
                         msg='The car should be called `General` if no name was passed as an argument')

    def test_default_car_model(self):
        gm = car_class.Car()
        self.assertEqual('GM', gm.model, msg="The car's model should be called `GM` if no model was passed as an argument")

    def test_car_properties(self):
        toyota = car_class.Car('Toyota', 'Corolla')
        self.assertListEqual(['Toyota', 'Corolla'],
                             [toyota.name, toyota.model],
                             msg='The car name and model should be a property of the car')

    def test_car_doors(self):
        opel = car_class.Car('Opel', 'Omega 3')
        porshe = car_class.Car('Porshe', '911 Turbo')
        self.assertListEqual([opel.num_of_doors,
                             porshe.num_of_doors,
                             car_class.Car('Koenigsegg', 'Agera R').num_of_doors],
                             [4, 2, 2],
                             msg='The car shoud have four (4) doors except its a Porshe or Koenigsegg')

    def test_car_wheels(self):
        man = car_class.Car('MAN', 'Truck', 'trailer')
        koenigsegg = car_class.Car('Koenigsegg', 'Agera R')
        self.assertEqual([8, 4], [man.num_of_wheels, koenigsegg.num_of_wheels],
                         msg='The car shoud have four (4) wheels except its a type of trailer')

    def test_car_type(self):
        koenigsegg = car_class.Car('Koenigsegg', 'Agera R')
        self.assertTrue(koenigsegg.is_saloon(),
                        msg='The car type should be saloon if it is not a trailer')

    def test_car_speed(self):
        man = car_class.Car('MAN', 'Truck', 'trailer')
        parked_speed = man.speed
        moving_speed = man.drive(7).speed

        self.assertListEqual([parked_speed, moving_speed],
                             [0, 77],
                             msg='The Trailer should have speed 0 km/h until you put `the pedal to the metal`')

    def test_car_speed2(self):
        man = car_class.Car('Mercedes', 'SLR500')
        parked_speed = man.speed
        moving_speed = man.drive(3).speed

        self.assertListEqual([parked_speed, moving_speed],
                             [0, 1000],
                             msg='The Mercedes should have speed 0 km/h until you put `the pedal to the metal`')

    def test_drive_car(self):
        man = car_class.Car('MAN', 'Truck', 'trailer')
        moving_man = man.drive(7)
        moving_man_instance = isinstance(moving_man, car_class.Car)
        moving_man_type = type(moving_man) is car_class.Car
        self.assertListEqual([True, True, man.speed],
                             [moving_man_instance, moving_man_type, moving_man.speed],
                             msg='The car drive function should return the instance of the Car class')


if __name__ == '__main__':
    unittest.main()
