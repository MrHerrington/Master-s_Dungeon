class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Приветствую, {self.name}!')

    def __exit__(self, *args, **kwargs):
        print(f'До встречи, {self.name}!')


with Greeter('Михаил Г.') as greeter:
    print(
        '\nКак бессонница в час ночной\n'
        'Меняет, нелюдимая, облик твой,\n'
        'Чьих невольница ты идей?\n'
        'Зачем тебе охотиться на людей?\n'
    )
