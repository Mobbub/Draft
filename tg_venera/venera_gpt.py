import requests


# fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost - ключи словаря
def get_yandexgpt_response(person_info: dict, request_subject: str) -> str:
    ai_role = ''
    if request_subject == 'биография':
        ai_role = 'биограф'
    elif request_subject == 'эпитафия':
        ai_role = 'надгробный писатель'

    prompt = {
        'modelUri': 'gpt://ключ/yandexgpt-lite',
        'completionOptions': {
            'stream': False,
            'temperature': 0.6,
            'maxTokens': '2000'
        },

        'messages': [
            {
                'role': 'system',
                'text': f'Ты {ai_role}, который составляет {request_subject} о человеке.'
            },
            {
                'role': 'user',
                'text': f'Привет! Я бы хотел, чтобы ты составил {request_subject} о человеке, сможешь сделать?'
            },
            {
                'role': 'assistant',
                'text': 'Привет! Хорошо, расскажи мне что-нибудь о нём.'
            },
            {
                'role': 'user',
                'text': f'"Этого человека зовут {person_info['fio']}, он родился {person_info['dr']} '
                        f'в {person_info['mr']} и умер {person_info['ds']} в {person_info['ms']}. '
                        f'Его супругом(супругой) был(была) {person_info['supr']}. Этот человек окончил '
                        f'{person_info['obr']}. Его родом деятельности было {person_info['rd']}. Его гражданство - '
                        f'{person_info['graj']}. Из детей у него(неё) были {person_info['deti']}, а из внуков - '
                        f'{person_info['vnuki']}.'
            }
        ]
    }

    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Api-Key ключ'
    }

    response = requests.post(url, headers=headers, json=prompt)

    return response.text
