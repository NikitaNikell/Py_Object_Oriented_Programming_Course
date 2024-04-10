class Index:
    START_INDEX = 0

    def __init__(self):
        self.id = Index.START_INDEX
        Index.START_INDEX += 1

    def __hash__(self):
        return hash(str(self.id))


id1 = Index()
id2 = Index()
d = {id1: id1, id2: id2} #  словарь будет успешно создан и к его значениям можно обращаться, например, командой: d[id1].id


print(d)