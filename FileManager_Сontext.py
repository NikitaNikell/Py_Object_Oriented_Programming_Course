class FileManager:

    """ Ниже представлен класс FileManager для работы с файлами, который закрывает файл после окончания работы
    и обрабатывает ошибки при открытии файла:"""

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except FileNotFoundError:
            print("Error: File not found")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with FileManager("test.txt", "r") as f:
    if f:
        print(f.read())


""" В этом примере __enter__() открывает файл и возвращает объект файла. Если файл не может быть открыт, он возвращает None.

__exit__() закрывает файл. Если при работе с файлом возникли ошибки, exc_type, exc_value и traceback содержат информацию об ошибке.

В этом примере контекстный менеджер открывает файл "test.txt" для чтения и закрывает его после окончания работы. 
Если файл не найден, выводится сообщение об ошибке. Если файл успешно открыт, он выводится на экран."""