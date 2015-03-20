import abc


class CarStore(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def createCar(self, item):
        return

    def orderCar(self, type):

        car = self.createCar(type)
        print(car)

        car.construct()
        car.wash()
        car.dry()
        car.ship()
        return car
