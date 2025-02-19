from db.database import create_tables
from db.crud import get_information_couples

if __name__ == "__main__":
    create_tables()
    # debug_week_determinant()
    print(get_information_couples('Понедельник', 1, {}))
    get_information_couples('Понедельник', 0, {})
    # log_message()
    # debug_week_determinant() 
    # start_bot()