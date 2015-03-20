from FactoryTestDrive.cheapCarStore import CHEAPCarStore
from FactoryTestDrive.exCarStore import EXCarStore


class FactoryTestDrive(object):
    def main():
        cheapStore = CHEAPCarStore()
        exStore = EXCarStore()
        car = cheapStore.orderCar("cheapUsCar")
        print("Here is your " + car.name + "\n")
        car = exStore.orderCar("exGerCar")
        print("Here is your " + car.name + "\n")

    main = staticmethod(main)


if __name__ == '__main__':
    FactoryTestDrive.main()