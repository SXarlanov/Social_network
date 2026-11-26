
from random import randint

# from graphic_arts.start_game_banner import run_screensaver
STANDART_ATTACK = 5
STANDART_DEFENCE = 10
STANDART_SPECIAL = 80


class Character:

    MIN_ATTACK = 0
    MAX_ATTACK = 0
    MIN_DEFENCE = 0
    MAX_DEFENCE = 0
    SPECIAL_STRING = ''

    def __init__(self, name):
        self.name = name


    def attack(self):
        return f'{self.name} нанес противнику урон, равный {STANDART_ATTACK + randint(self.MIN_ATTACK, self.MAX_ATTACK)}'

    def defence(self):
        return (f'{self.name} блокировал {10 + randint(self.MIN_DEFENCE, self.MAX_DEFENCE)} урона')

    def special(self):
        return f'{self.name} применил специальное умение {self.SPECIAL_STRING}'


class Warrior(Character):
    MIN_ATTACK = 3
    MAX_ATTACK = 5
    MIN_DEFENCE = 15
    MAX_DEFENCE = 25
    SPECIAL_STRING = f'Атака {STANDART_ATTACK + 40}'

class Mage(Character):
    MIN_DEFENCE = 5
    MAX_DEFENCE = 10
    MIN_ATTACK = 6
    MAX_ATTACK = 15
    SPECIAL_STRING = f'Выносливость {STANDART_SPECIAL + 25}'


class Healer(Character):
    MIN_DEFENCE = 3
    MAX_DEFENCE = 6
    MIN_ATTACK = 4
    MAX_ATTACK = 10
    SPECIAL_STRING = f'Защита {STANDART_DEFENCE + 30}'


healer = Healer('Никита')
warrior = Warrior('Павел')
print(warrior)
mage = Mage('Артур')
print(warrior.special())
print(mage.special())
print(healer.special())


# def attack(char_name, char_class) -> str:
#     if char_class == 'warrior':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(3, 5)}')
#     if char_class == 'mage':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(5, 10)}')
#     if char_class == 'healer':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(-3, -1)}')
#     raise ValueError(f'Неизвестный класс: {char_class}')


# def defence(char_name, char_class) -> str:
#     if char_class == 'warrior':
#         return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
#     if char_class == 'mage':
#         return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
#     if char_class == 'healer':
#         return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
#     raise ValueError(f'Неизвестный класс: {char_class}')


# def special(char_name, char_class) -> str:
#     if char_class == 'warrior':
#         return (f'{char_name} применил специальное умение «Выносливость '
#                 f'{80 + 25}»')
#     if char_class == 'mage':
#         return (f'{char_name} применил специальное умение «Атака {5 + 40}»')
#     if char_class == 'healer':
#         return (f'{char_name} применил специальное умение «Защита {10 + 30}»')
#     raise ValueError(f'Неизвестный класс: {char_class}')


# def start_training(char_name, char_class) -> str:
#     if char_class == 'warrior':
#         print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
#     if char_class == 'mage':
#         print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
#     if char_class == 'healer':
#         print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
#     print('Потренируйся управлять своими навыками.')
#     print('Введи одну из команд: attack — '
#           'чтобы атаковать противника, defence — '
#           'чтобы блокировать атаку противника или special — '
#           'чтобы использовать свою суперсилу.')
#     print('Если не хочешь тренироваться, введи команду skip.')
#     cmd = None
#     while cmd != 'skip':
#         cmd = input('Введи команду: ')
#         if cmd == 'attack':
#             print(attack(char_name, char_class))
#         if cmd == 'defence':
#             print(defence(char_name, char_class))
#         if cmd == 'special':
#             print(special(char_name, char_class))
#     return 'Тренировка окончена.'


# def choice_char_class() -> str:
#     approve_choice = ''
#     char_class = ''
#     while approve_choice != 'y':
#         char_class = input('Введи название '
#                            'персонажа, за которого хочешь играть: '
#                            'Воитель — warrior, Маг — mage, Лекарь — healer: ')
#         if char_class == 'warrior':
#             print('Воитель — '
#                   'дерзкий воин ближнего боя. '
#                   'Сильный, выносливый и отважный.')
#         if char_class == 'mage':
#             print('Маг — находчивый воин дальнего боя. '
#                   'Обладает высоким интеллектом.')
#         if char_class == 'healer':
#             print('Лекарь — могущественный заклинатель. '
#                   'Черпает силы из природы, веры и духов.')
#         approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или '
#                                'любую другую кнопку, чтобы '
#                                'выбрать другого персонажа ').lower()
#     return char_class


# def main() -> None:
#     # run_screensaver()
#     print('Приветствую тебя, искатель приключений!')
#     print('Прежде чем начать игру...')
#     char_name: str = input('...назови себя: ')
#     print(f'Здравствуй, {char_name}! '
#           'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
#     print('Ты можешь выбрать один из трёх путей силы:')
#     print('Воитель, Маг, Лекарь')
#     char_class: str = choice_char_class()
#     print(start_training(char_name, char_class))


# main()
