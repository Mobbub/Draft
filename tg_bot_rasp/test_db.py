# import os
# from sqlalchemy import create_engine, inspect
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv, find_dotenv

# # Загружаем переменные окружения из файла .env
# load_dotenv(find_dotenv(usecwd=True))

# # Строка подключения к базе данных
# DATABASE_URL = os.getenv("DATABASE_URL")
# if DATABASE_URL is None:
#     print('Ошибка: строка подключения не найдена!')
#     exit(1)

# # Создаем подключение к базе данных
# engine = create_engine(DATABASE_URL)

# # Создаем сессию
# Session = sessionmaker(bind=engine)
# session = Session()

# # Получаем инспектор для работы с метаданными
# inspector = inspect(engine)

# # Проверяем все таблицы в базе данных
# try:
#     # Указываем имя схемы (базы данных)
#     schema_name = 'shedule_ics'
    
#     # Получение списка всех таблиц в указанной схеме
#     tables = inspector.get_table_names(schema=schema_name)
#     if tables:
#         print(f"Таблицы в схеме '{schema_name}':")
#         for table in tables:
#             print(table)
#     else:
#         print(f"В схеме '{schema_name}' нет таблиц.")
# except Exception as e:
#     print(f'Ошибка при получении таблиц: {e}')
# finally:
#     session.close()

import os
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv(find_dotenv(usecwd=True))

# Строка подключения к базе данных
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    print('Ошибка: строка подключения не найдена!')
    exit(1)

# Создаем подключение к базе данных
engine = create_engine(DATABASE_URL)

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# Получаем инспектор для работы с метаданными
inspector = inspect(engine)

try:
    # Указываем имя схемы (базы данных)
    schema_name = 'shedule_ics'
    
    # Получаем список всех таблиц в схеме
    tables = inspector.get_table_names(schema=schema_name)
    if tables:
        for table in tables:
            print(f"\nСодержимое таблицы '{table}':")
            
            # Выполняем запрос для получения всех записей из текущей таблицы
            query = text(f"SELECT * FROM {schema_name}.{table}")
            results = session.execute(query).fetchall()
            
            if results:
                # Получаем имена столбцов
                column_names = [col[0] for col in session.execute(query).cursor.description]
                print(f"1{column_names}")
                
                # Выводим результаты
                for row in results:
                    print(2,row)
            else:
                print(f"Таблица '{table}' пуста.")
    else:
        print(f"В схеме '{schema_name}' нет таблиц.")
except Exception as e:
    print(f'Ошибка при получении данных: {e}')
finally:
    session.close()
