class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def __call__(self, message):
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')


from datetime import datetime

logger = Logger('my_log_file.txt')


def get_information():
    logger(f'Start work in get_information: {datetime.now()}')
    # do some work
    logger(f'Finished work in get_information: : {datetime.now()}')


def delete_files():
    logger(f'Start work in {delete_files.__name__}: {datetime.now()}')
    # do some work
    logger(f'Finished work in {delete_files.__name__}: : {datetime.now()}')


print(get_information())
print(delete_files())

"""Предположим, что у вас есть программа с несколькими модулями и функциями, выполнение которых вы хотите регистрировать. 
Вместо создания отдельного экземпляра ведения журнала для каждого модуля или функции вы можете создать класс ведения 
журнала с методом __call__, который можно использовать для регистрации сообщений с помощью одной строки кода.

В этом примере logger вызывается со строкой сообщения, которая записывается в указанный файл журнала логирования. 
Это упрощает отслеживание того, что происходит в разных частях программы, без необходимости создавать несколько 
экземпляров журнала и управлять ими.
"""
