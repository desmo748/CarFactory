from Car import Car


class cheapUsCar(Car):
    def __init__(self):
        super(cheapUsCar, self).__init__()

        self.name = "cheapUsCar"
        self.parts.append("heavy Metal")
        self.parts.append("good Engine")