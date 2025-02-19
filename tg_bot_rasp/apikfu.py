import requests
import openpyxl
from db.crud import add_week
import re
from datetime import datetime

# working with a file
class WWaF():
    def __init__(self, TodayDate):
        self.url = 'https://schedule-cloud.cfuv.ru/index.php/s/YLoTDF3GqDjnDbR/download/09.03.01%20%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%20%D0%B8%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0,09.03.04%20%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%B0%D1%8F%20%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%8F%20%281-4%29.xlsx'  # Замените ссылку на нужный файл
        self.filename = f'shedules/{TodayDate}_DownloadedFile.xlsx'
        self.cells_weeks_address = ['I1', 'A1']
        self.year = '2024'
    
    # download file
    def _download_file(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            with open(self.filename, 'wb') as file:
                file.write(response.content)
            return True
        return False
    
    def _parse_exel_weeks(self, sheet):
        for cell in self.cells_weeks_address:
            week_counter = 0
            cell_value = sheet[cell].value
            dates = re.findall(r'\d{2}\.\d{2}', cell_value)
            for date in dates:
                day, month = date.split('.')
                formatted_date = f"{day}.{month}.{self.year}"
                add_week(formatted_date, week_counter)
            week_counter+=1
        return True
                
    def _parse_exel_file(self):
        workbook = openpyxl.load_workbook(self.filename)
        sheet = workbook.worksheets[2]
        if self._parse_exel_weeks(sheet):
            pass
    
    def acceptance_information(self):
        if self._download_file() and self._parse_exel_file():
            # print(self._parse_exel_file)
            return True
        
if __name__ == '__main__':
    a = WWaF('23.01.2025')
    a.acceptance_information()