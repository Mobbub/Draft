import requests

def biograf(fio, dr, ds, mr, ms, supr, obr, rd, graj, deti, vnuki, dost):
    prompt = {
        'modelUri': 'gpt://ключ польза/yandexgpt-lite',
        'completionOptions': {
            'stream': False,
            'temperature': 0.6,
            'maxTokens': '2000'
        },

        'message': [
            {
                'role': 'system',
                'text': 'Ты биограф, который составляет биографию о человеке.'
            },
            {
                'role': 'user',
                'text': 'Привет! Я бы хотел, чтоб ты составил биографию о человеке, сможешь сделать?'
            },
            {
                'role': 'biograf',
                'text': 'Привет! Хорошо, расскажи мне что нибудь о нём'
            },
            {
                'role': 'user',
                'text': f'Его зовут {fio}, его дата смерти'
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

print(biograf('Иван'))
