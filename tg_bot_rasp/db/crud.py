from .database import get_session
from .models import WeekDeterminant, OddWeek, EvenWeek

def check_date_counter(date_string: str):
    session = get_session()
    try:
        week_determinant = session.query(WeekDeterminant).filter(WeekDeterminant.week_date == date_string).first()
        if week_determinant:
            return week_determinant.week_counter
        else:
            print(f"Не найдена запись с week_date = '{date_string}'")
    except Exception as e:
       print(f"Произошла ошибка: {e}")
    finally:
        session.close()

def get_information_couples(week_day: str, week_counter: int, response: dict):
    session = get_session()
    if week_counter:
        evenweek = session.query(EvenWeek).filter(EvenWeek.week_day == week_day).first()
        if evenweek:
            response[1] = evenweek.first_pair
            response[2] = evenweek.second_pair
            response[3] = evenweek.third_pair
            response[4] = evenweek.fourth_pair
            response[5] = evenweek.fifth_pair
            return response
    else:
        oddweek = session.query(OddWeek).filter(OddWeek.week_day == week_day).first()
        if oddweek:
            response[1] = oddweek.first_pair
            response[2] = oddweek.second_pair
            response[3] = oddweek.third_pair
            response[4] = oddweek.fourth_pair
            response[5] = oddweek.fifth_pair
            return response
        
    session.close()

def add_week(week_date, week_counter):
    session = get_session()
    new_week = WeekDeterminant(
        week_date=week_date,
        week_counter=week_counter
    )
    session.add(new_week)
    session.commit()
    session.close()