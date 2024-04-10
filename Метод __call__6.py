class RenderList:

    def __init__(self, list_1):
        self.list_1 = list_1 if list_1 in ('ul', 'ol') else 'ul'

    def __call__(self, string, *args, **kwargs):
        return '\n'.join([f'<{self.list_1}>', *map(lambda x: f'<li> {x} </li>', string), f'</{self.list_1}>'])


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)

print(html)