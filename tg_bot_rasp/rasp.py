from datetime import datetime, timedelta
import os
from apikfu import WWaF
from db.crud import check_date_counter, get_information_couples

class ScheduleTwoDays():
    def __init__(self):
        self.TodayDate = (datetime.now()).strftime('%d.%m.%Y')
        self.TomorrowDate = ((datetime.now()) + timedelta(days=1)).strftime('%d.%m.%Y')
        self.index_action = [0, 1]
        self.WorkFileClass = WWaF(self.TodayDate, self.TomorrowDate)
        self.response = {
            1: '',
            2: '',
            3: '',
            4: '',
            5: ''
        }
    
    def _get_file_names_from_folder(self):
        folder_path = 'shedules'
        file_names = []

        for filename in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, filename)):
                file_names.append(filename)

        for file_name in file_names:
            if str(self.TodayDate) in file_name[:file_name.find('_')]:
                return True
        return False
    
    def _last_monday(self, dateC):
        date = datetime.strptime(dateC, "%d.%m.%Y")
        days_to_subtract = (date.weekday() + 7) % 7
        last_monday_date = date - timedelta(days=days_to_subtract)
        
        return last_monday_date.strftime("%d.%m.%Y")
    
    def _name_day_week(self, date):
        date_object = datetime.strptime(date, "%d.%m.%Y")
        day_number = date_object.weekday()
        days_in_russian = {
            0: "Понедельник",
            1: "Вторник",
            2: "Среда",
            3: "Четверг",
            4: "Пятница",
            5: "Суббота",
            6: "Воскресенье"
        }

        return days_in_russian[day_number]
    
    def schedule_today(self):
        if self._get_file_names_from_folder():
            counter_week = check_date_counter(self.TodayDate)
            data = get_information_couples(self._name_day_week(self.TodayDate), counter_week, self.response)
            return f'{self.TodayDate}\nЧётность недели: {counter_week}\n{self._name_day_week(self.TodayDate)}\nПары:\n1. {data[1]}\n2. {data[2]}\n3. {data[3]}\n4. {data[4]}\n5. {data[5]}'
        
        file_work = WWaF(self.TodayDate)
        if file_work.acceptance_information():
            counter_week = check_date_counter(self.TodayDate)
            data = get_information_couples(self._name_day_week(self.TodayDate), counter_week, self.response)
            return f'{self.TodayDate}\nЧётность недели: {counter_week}\n{self._name_day_week(self.TodayDate)}\nПары:\n1. {data[1]}\n2. {data[2]}\n3. {data[3]}\n4. {data[4]}\n5. {data[5]}'
        
    def schedule_tomorrow(self):
        pass

if __name__ == '__main__':
    classtest = ScheduleTwoDays()
    print(classtest.schedule_today())