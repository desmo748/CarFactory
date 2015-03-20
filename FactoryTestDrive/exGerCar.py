from Car import Car

class exGerCar(Car):
    def __init__(self):
        super(exGerCar, self).__init__()

        self.name = "exGerCar"
        self.parts.append("good Engine")
        self.parts.append("good Sound")
