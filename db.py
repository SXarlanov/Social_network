import sqlite3

# Если в текущей директории нет файла db.sqlite - 
# он будет создан; сразу же будет создано и соединение с базой.
# Если файл существует, функция connect просто подключится к базе.
con = sqlite3.connect('Table.sqlite')

# Создаём специальный объект cursor для работы с БД.
# Вся дальнейшая работа будет вестись через методы этого объекта.
cur = con.cursor()

# Готовим SQL-запросы.
# Для читаемости кода запрос обрамлён в тройные кавычки и разбит построчно.
cur.execute('''
CREATE TABLE IF NOT EXISTS directors(
    id INTEGER PRIMARY KEY,
    name TEXT,
    birthday_year INTEGER
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    type_id INTEGER,
    release_year INTEGER,
    FOREIGN KEY(type_id) REFERENCES types(id)
);
''')

directors = [
    (1, 'Текс Эйвери', 1908),
    (2, 'Роберт Земекис', 1952),
    (3, 'Джерри Чиникей', 1912),
]
movies = [
     (1, 'Весёлые мелодии', 2, 1930),
    (2, 'Кто подставил кролика Роджера', 1, 1988),
    (3, 'Безумные Мелодии Луни Тюнз', 2, 1931),
    (4, 'Розовая пантера: Контроль за вредителями', 3, 1969),
]

# cur.executemany('INSERT INTO directors Values(?, ?, ?);', directors)
cur.executemany('INSERT INTO movies Values(?, ?, ?, ?);', movies)



# Применяем запросы.
# Запросы, переданные в cur.execute(), не будут выполнены до тех пор,
# пока не вызван метод commit().
con.commit()
# Закрываем соединение с БД.
con.close()