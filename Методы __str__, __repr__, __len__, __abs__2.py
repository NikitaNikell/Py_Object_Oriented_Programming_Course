class Model:

    def query(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        result = "Model: "
        for k, v in self.__dict__.items():
            result += f"{k} = {v}, "

        return result[:-2]



model = Model()

model.query(id=1, fio='Sergey', old=33)

print(model)
