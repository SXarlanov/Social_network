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

import datetime as dt
import time

class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None

    def __str__(self):
        if self.end_time is not None:
            return f'Квест выполнен'
            
        elif:

            return f'Квест выполняется'
     

    def accept_quest(self):
        self.start_time = dt.datetime.now()
        if self.end_time is not None:
            return f'С этим испытанием вы уже справились'
        
        return f'Начало {self.name} положено'
        

    def pass_quest(self):
        # if self.end_time == None:
        #     # return f'С этим испытание вы уже справились'
        self.end_time = dt.datetime.now()
        completion_time = self.end_time - self.start_time
        return f'Квест {self.name} окончен. Время выполнения квеста: {completion_time}'
       


quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

new_quest = Quest(quest_name, quest_goal, quest_description)
print(new_quest)
print(new_quest.accept_quest())
print(new_quest)
time.sleep(2)

print(new_quest.pass_quest())

print(new_quest)
