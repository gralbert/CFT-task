class Car:
    def __init__(self, data):
        self._aid = data['_aid']
        self._year = data['_year']
        self._producer = data['_producer']
        self._model = data['_model']
        self._body_type = data['_body_type']

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        string = '|{:^8}|{:^12}|{:^18}|{:^16}|{:^16}|'\
            .format(self._aid, self._year, self._producer,
                    self._model, self._body_type)
        return string

    @property
    def aid(self):
        return self._aid

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def producer(self):
        return self._producer

    @producer.setter
    def producer(self, value):
        self._producer = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def body_type(self):
        return self._body_type

    @body_type.setter
    def body_type(self, value):
        self._body_type = value
