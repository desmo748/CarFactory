from Car import Car

class exItaCar(Car):
    def __init__(self):
        super(exItaCar, self).__init__()

        self.name = "exItaCar"
        self.parts.append("good Looking")
        self.parts.append("good Engine")