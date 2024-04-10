class CustomButton:

    def __init__(self, text, **kwargs):

        """ передача произвольного количества позиционных аргументов """
        self.text = text
        for key, value in kwargs.items():
            setattr(self, key, value)

    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def click(self):
        try:
            self.command()
        except AttributeError:
            print("Кнопка не настроена")
        except TypeError:
            print("Кнопка сломалась")


def func():
    print('Оно живое')


btn = CustomButton(text="Hello", bd=20, bg='#ffaaaa')
btn.click()  # Кнопка не настроена
btn.config(bd=30, bg='#ffaaaa', bsg='#ff')

btn.config(command=func)
btn.click()  # Оно живое