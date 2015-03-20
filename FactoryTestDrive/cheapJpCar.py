from Car import Car


class cheapJpCar(Car):
    def __init__(self):
        super(cheapJpCar, self).__init__()

        self.name = "cheapJpCar"
        self.parts.append("light Metal")
        self.parts.append("good Tires")