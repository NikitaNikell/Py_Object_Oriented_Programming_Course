class Model:
    def query(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        if self.__dict__:
            return f"Model: {self._representation()}"
        return "Model"

    def _representation(self):
        return ', '.join([f"{name} = {value}" for name, value in self.__dict__.items()])


model = Model()

model.query(id=1, fio='Sergey', old=33)

print(model)