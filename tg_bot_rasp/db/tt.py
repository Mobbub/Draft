from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import get_enginge
from models import EvenWeek

engine = get_enginge()
Session = sessionmaker(bind=engine)
session = Session()

# Пример использования:
try:
    # Предположим, что в таблице есть данные
    even_week_record = session.query(EvenWeek).first()  # Получаем первую запись из таблицы
    if even_week_record:
        print(even_week_record.id, even_week_record.week_day,
              even_week_record.first_pair, even_week_record.second_pair,
              even_week_record.third_pair, even_week_record.fourth_pair,
              even_week_record.fifth_pair)
    else:
       print('Нет записей в таблице')
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    session.close()
