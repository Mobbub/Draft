# import json

# def remove_key_from_json(file_path, key_to_remove):
#     # Открываем JSON-файл для чтения
#     with open(file_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)

#     # Удаляем указанный ключ из словаря
#     if key_to_remove in data:
#         del data[key_to_remove]

#     # Создаем новый словарь с обновленными ключами
#     new_data = {}
#     new_data["Баланс"] = data.pop("Баланс", 0)
#     index = 0
#     for key, value in data.items():
#         new_data[str(index)] = value
#         index += 1

#     # Открываем JSON-файл для записи
#     with open(file_path, 'w', encoding='utf-8') as file:
#         json.dump(new_data, file, ensure_ascii=False, indent=4)

#     print(f"Ключ '{key_to_remove}' успешно удален из JSON-файла.")

# # Пример использования
# file_path = 'main.json'
# key_to_remove = '4'

# remove_key_from_json(file_path, key_to_remove)
import json

file_path = 'main.json'
type = 'Сумма'
novoe = 1000
index = '2'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)


if type == 'Сумма':
    if data[str(index)]['Категория'] == 'Доход':
        data['Баланс'] -= data[str(index)]['Сумма']
    elif data[str(index)]['Категория'] == 'Расход':
        data['Баланс'] += data[str(index)]['Сумма']

    if data[str(index)]['Категория'] == 'Доход':
        data['Баланс'] += novoe
    elif data[str(index)]['Категория'] == 'Расход':
        data['Баланс'] -= novoe

data[str(index)][type] = novoe

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
