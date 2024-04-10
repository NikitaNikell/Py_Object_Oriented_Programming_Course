
class FileAcceptor:

    def __init__(self, *args):
        self.file = set(args)

    def __add__(self, other):
        return FileAcceptor(*(self.file | other.file))

    def __call__(self, filename):
        file_extension = filename.split(".")[-1]
        return file_extension in self.file


acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]

filenames = list(filter(acceptor_images + acceptor_docs, filenames))


print(filenames)