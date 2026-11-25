# class Room:
#     def __init__(self, temp, watering, square):
#         self.temp = temp
#         self.watering = watering
#         self.square = square

#     def metod(self):
#         if self.temp > 20:
#             print('В комнате тепло')
#         else:
#             print('В комнате холодно')


# room_one = Room(21, 5, 50)
# room_one.metod()
# room_two = Room(15, 5, 15)
# room_two.metod()



# import datetime as dt
# import time

# class Quest:
#     def __init__(self, name, description, goal):
#         self.name = name
#         self.description = description
#         self.goal = goal
#         self.start_time = None
#         self.end_time = None

#     def __str__(self):
#         if self.end_time is not None:
#             return 'Квест выполнен'
#         elif self.start_time is not None:
#             return 'Квест выполняется'
#         else:
#             return 'Квест еще не начат'

#     def accept_quest(self):
#         if self.end_time is not None:
#             return 'С этим испытанием вы уже справились'
#         if self.start_time is not None:
#             return 'Вы уже приняли этот квест'
#         self.start_time = dt.datetime.now()
#         return f'Начало {self.name} положено'

#     def pass_quest(self):
#         if self.end_time is not None:
#             return f'С этим испытание вы уже справились'
#         self.end_time = dt.datetime.now()
#         completion_time = self.end_time - self.start_time
#         return (f'Квест {self.name} окончен. '
#                 f'Время выполнения квеста: {completion_time}')


# quest_name = 'Сбор пиксельники'
# quest_goal = 'Соберите 12 ягод пиксельники.'
# quest_description = '''
# В древнем лесу Кодоборье растёт ягода "пиксельника".
# Она нужна для приготовления целебных снадобий.
# Соберите 12 ягод пиксельники.'''

# new_quest = Quest(quest_name, quest_description, quest_goal)
# print(new_quest)
# print(new_quest.accept_quest())
# print(new_quest)
# time.sleep(2)

# print(new_quest.pass_quest())
# print(new_quest)


class Human:
    def __init__(self, name):
        self.name = name

    # ответ по умолчанию для всех одинаковый, можно 
    # доверить его родительскому классу
    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю')


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос; 
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        self.question = question
        # напечатайте на экран вопрос в нужном формате
        print(self.name, self.question)
        # запросите ответ на вопрос у someone
        someone.answer_question(question)
        print()  # этот print выводит разделительную пустую строку 


class Curator(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Задан непредусмотренный вопрос — для него подойдёт ответ по умолчанию')
        else:
            super().answer_question(question)

        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса


class Mentor(Human):
    def answer_question(self, question):
        if question == 'как устроиться работать питонистом?':
            print('Задан непредусмотренный вопрос — для него подойдёт ответ по умолчанию')
        else:
            super().answer_question(question)


class CodeReviewer(Human):
    def answer_question(self, question):
        if question == 'когда каникулы?':
            print('Задан непредусмотренный вопрос — для него подойдёт ответ по умолчанию')
        elif question == 'что не так с моим проектом?':
            print('Задан непредусмотренный вопрос — для него подойдёт ответ по умолчанию')
        else:
            super().answer_question(question)

# объявите и реализуйте классы CodeReviewer и Mentor

# следующий код менять не нужно, он работает, мы проверяли


student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')
student1.ask_question(mentor, 'как научиться програмировать?')