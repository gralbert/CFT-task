class Car:
    def __init__(self, year, producer, model, body_type):
        self.year = year
        self.producer = producer
        self.model = model
        self.body_type = body_type

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        string = '|{:^10}|{:^14}|{:^12}|{:^12}'\
            .format(self.year, self.producer,
                    self.model, self.body_type)
        return string
