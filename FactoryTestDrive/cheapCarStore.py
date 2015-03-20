from FactoryTestDrive.cheapFreCar import cheapFreCar
from FactoryTestDrive.cheapJpCar import cheapJpCar
from FactoryTestDrive.cheapUsCar import cheapUsCar
from FactoryTestDrive.CarStore import CarStore


class CHEAPCarStore(CarStore):

    def createCar(self, item):
        if item == "cheapJpCar":
            return cheapJpCar()
        elif item == "cheapFreCar":
            return cheapFreCar()
        elif item == "cheapUsCar":
            return cheapUsCar()
        else:
            return None

CarStore.register(CHEAPCarStore)
