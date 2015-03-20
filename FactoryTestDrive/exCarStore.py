import abc
from FactoryTestDrive.CarStore import CarStore
from FactoryTestDrive.exGerCar import exGerCar
from FactoryTestDrive.exItaCar import exItaCar


class EXCarStore(CarStore):

    def createCar(self, item):
        if item == "exItaCar":
            return exItaCar()
        elif item == "exGerCar":
            return exGerCar()
        else:
            return None

CarStore.register(EXCarStore)
