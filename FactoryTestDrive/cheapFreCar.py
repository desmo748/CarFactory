from Car import Car


class cheapFreCar(Car):
    def __init__(self):
        super(cheapFreCar, self).__init__()

        self.name = "cheapFreCar"
        self.parts.append("good Engine")
        self.parts.append("good Sound")