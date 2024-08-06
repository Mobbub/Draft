Архитектура:
Описание: сайт, в котором есть аккаунты для экспобанка и всех партнёров. Основная суть будет заключаться в загрузке своей бд на сайт и вывода статы по всем пользователям + по каждому отдельному пользователю.

Модули:
Фронт: 2 страницы:
1) Обычная страница авторизации.
2) Страница с кнопкой (загрузить бд или какое то другое название). После загрузки бд должна выводиться статистика по всем пользователям из этой бд (часть бэка, которая будет передать json с данными) и форма, где можно будет ввести id или фио пользователя. После выбора пользователя должна появляться или как то ещё таблица, в которой будет какая та стата (которую бэк также будет передавать данными в json)

Работа с бд. Файл db.py: то, что я уже скинул максу + надо добавить функции для авторизации, как это делали в ekfbam. Некоторые функции, которые надо сделать или переделать описаны в основном сценарии.

Модуль составления статы. Файл bus_logic.py: Тут я сам всё сделаю. Ну а так будет происходить сравнение данных пользователь. Мета данные переведём в веса от 0 до 100 и будем сравнивать. Также будет функция, которая будет считать просто общую статистику. Будет функция связки. Заранее запишем услуги и товары, которые между собой связаны, которые можно приобрести после приобретения другой.

Основной сценарий работы сайта:
Работник заходит на сайт, вводит логин и пароль, происходит авторизация также, как и в ekfbam и его перекидывает на нашу основную страницу с работой. После нажатия на кнопки загрузки бд, происходит сохранение бд в определённой папке проекта и вызывается функция из db.py (где будет 2 параметра: 1) путь к бд; 2) название бд), которая должна распарсить данную бд, чтоб её можно было использовать дальше и вернуть ответ в виде json:
{
    "index_result": 200, #при успешном добавлении
    1: {
        "id_user": 'его id',
        "client_name": "его имя",
        "client_middle_name": "его отчество",
        "client_sirnam": "его фамилия",
        "client_birthdate": "его д.р.",
        "client_birthplace": "его место рождения",
        "client_mobile_phone": "его мобильный телефон",
        "client_take_products": {
            # всё, что выше - самое последнее, что приобретал пользователь и далее по датам тип. Учитывается момент, что при загрузке нового бд от работника, будет какой столбец с инфой о всех приобретениях пользователя, где будет идти такая же тема, что чем выше какой то товар или услуга, тем позднее всего она приобреталась 
            1: 'Автомобиль', # пример
            2: 'Автокредит' # пример
        }
        # и так далее по инфе с бд
    },
    2: {
        "id_user": 'его id',
        "client_name": "его имя",
        "client_middle_name": "его отчество",
        "client_sirnam": "его фамилия",
        "client_birthdate": "его д.р.",
        "client_birthplace": "его место рождения",
        "client_mobile_phone": "его мобильный телефон",
        "client_take_products": {
            # всё, что выше - самое последнее, что приобретал пользователь и далее по датам тип. Учитывается момент, что при загрузке нового бд от работника, будет какой столбец с инфой о всех приобретениях пользователя, где будет идти такая же тема, что чем выше какой то товар или услуга, тем позднее всего она приобреталась 
            1: 'Автомобиль', # пример
            2: 'Автокредит' # пример
        }
        # и так далее по инфе с бд
    },
    3: {
        "id_user": 'его id',
        "client_name": "его имя",
        "client_middle_name": "его отчество",
        "client_sirnam": "его фамилия",
        "client_birthdate": "его д.р.",
        "client_birthplace": "его место рождения",
        "client_mobile_phone": "его мобильный телефон",
        "client_take_products": {
            # всё, что выше - самое последнее, что приобретал пользователь и далее по датам тип. Учитывается момент, что при загрузке нового бд от работника, будет какой столбец с инфой о всех приобретениях пользователя, где будет идти такая же тема, что чем выше какой то товар или услуга, тем позднее всего она приобреталась 
            1: 'Автомобиль', # пример
            2: 'Автокредит' # пример
        }
        # и так далее по инфе с бд
    },
    4: {
        "id_user": 'его id',
        "client_name": "его имя",
        "client_middle_name": "его отчество",
        "client_sirnam": "его фамилия",
        "client_birthdate": "его д.р.",
        "client_birthplace": "его место рождения",
        "client_mobile_phone": "его мобильный телефон",
        "client_take_products": {
            # всё, что выше - самое последнее, что приобретал пользователь и далее по датам тип. Учитывается момент, что при загрузке нового бд от работника, будет какой столбец с инфой о всех приобретениях пользователя, где будет идти такая же тема, что чем выше какой то товар или услуга, тем позднее всего она приобреталась 
            1: 'Автомобиль', # пример
            2: 'Автокредит' # пример
        }
        # и так далее по инфе с бд
    },
    5: {
        "id_user": 'его id',
        "client_name": "его имя",
        "client_middle_name": "его отчество",
        "client_sirnam": "его фамилия",
        "client_birthdate": "его д.р.",
        "client_birthplace": "его место рождения",
        "client_mobile_phone": "его мобильный телефон",
        "client_take_products": {
            # всё, что выше - самое последнее, что приобретал пользователь и далее по датам тип. Учитывается момент, что при загрузке нового бд от работника, будет какой столбец с инфой о всех приобретениях пользователя, где будет идти такая же тема, что чем выше какой то товар или услуга, тем позднее всего она приобреталась 
            1: 'Автомобиль', # пример
            2: 'Автокредит' # пример
        }
        # и так далее по инфе с бд
    },
    6: {
        "id_user": 'его id',
        "client_name": "его имя",
        "client_middle_name": "его отчество",
        "client_sirnam": "его фамилия",
        "client_birthdate": "его д.р.",
        "client_birthplace": "его место рождения",
        "client_mobile_phone": "его мобильный телефон",
        "client_take_products": {
            # всё, что выше - самое последнее, что приобретал пользователь и далее по датам тип. Учитывается момент, что при загрузке нового бд от работника, будет какой столбец с инфой о всех приобретениях пользователя, где будет идти такая же тема, что чем выше какой то товар или услуга, тем позднее всего она приобреталась 
            1: 'Автомобиль', # пример
            2: 'Автокредит' # пример
        }
        # и так далее по инфе с бд
    }
}


Ответом на запрос от сервера со стороны фронта на сохранение файла будет json с общей статой и айдишниками + фио пользователей:
{
    'index_result': 200,
    'stat': { # тут приведены примерные данные
        'num_users': 200, # кол-во всех пользователей
        'popular_product': {
            'name': 'Автомобиль', # название самого популярного товара
            'num_sales': 150, # кол-во юзеров, которые приобрели товар
            'percentage_take_produckt': 75 # % 150 от 200
        },
        'top_10_product': {
            1: 'Автомобиль',
            2: 'Автокредит',
            3: 'Инвестиционное консультирование',
            4: 'Зарплатный проект',
            5: 'Операционная аренда автомобилей',
            6: 'Услуга "помощь на дороге"',
            7: 'Продажа и лизинг грузовых транспортных средств',
            8: 'Страхование грузовых транспортных средств',
            9: '',
            10: ''
        }
    },
    'users': {
        1: {
            'id': '112312323321',
            'FIO': 'Иванов Иван Иванович'
        },
        2: {
            'id': '123321333',
            'FIO': 'Иванов Иван Иванович'
        },
        3: {
            'id': '122222222223321',
            'FIO': 'Иванов Иван Иванович'
        },
        4: {
            'id': '123ааааааа321',
            'FIO': 'Иванов Иван Иванович'
        },
        5: {
            'id': '12332555555551',
            'FIO': 'Иванов Иван Иванович'
        },
        6: {
            'id': '18888888823321',
            'FIO': 'Иванов Иван Иванович'
        },
        7: {
            'id': '1235465465465321',
            'FIO': 'Иванов Иван Иванович'
        },
        8: {
            'id': '12332666661',
            'FIO': 'Иванов Иван Иванович'
        },
        9: {
            'id': '1233288888881',
            'FIO': 'Иванов Иван Иванович'
        },
        10: {
            'id': '12339999999921',
            'FIO': 'Иванов Иван Иванович'
        },
        11: {
            'id': '1233211111111111',
            'FIO': 'Иванов Иван Иванович'
        },
        # и так далее до 200 юзеров
    }
}

Когда работник выберет какого то пользователя, то должен отправиться json запрос на роут ‘/stat_user’, с инфой о id юзера и индексом действия:
{
    'index_action': 1,
    'id_user': '112312323321'
}
Потом роут вызывает функцию из db.py с 2 параметрами ( 1) Название бд; 2) id юзера), которая должна дать инфу об этом пользователе в формате json:
{
    "index_result": 200, #при успешном добавлении
    "id_user": '123321',
    "client_name": "его имя",
    "client_middle_name": "его отчество",
    "client_sirnam": "его фамилия",
    "client_birthdate": "его д.р.",
    "client_birthplace": "его место рождения",
    "client_mobile_phone": "его мобильный телефон",
    "client_take_products": {
        # всё, что выше - самое последнее, что приобретал пользователь и далее по датам тип. Учитывается момент, что при загрузке нового бд от работника, будет какой столбец с инфой о всех приобретениях пользователя, где будет идти такая же тема, что чем выше какой то товар или услуга, тем позднее всего она приобреталась 
        1: 'Автомобиль',
        2: 'Автокредит'
    }
    # и так далее по инфе с бд
}
Дальше происходят манипуляции в bus_logic.py и ответом от сервера на запрос с инфой о пользователе будет json:
{
    'index_result': 200,
    'FIO': 'Иванов Иван Иванович',
    'id_user': '123321',
    'product_take_future': {
        1: {
            'name': 'Автокредит',
            'percent': 100
        },
        2: {
            'name': 'Ещё какая та хуйня',
            'percent': 75
        },
        3: {
            'name': 'Автокредит', # то, что нашли с помощью связки 
            'percent': 100 # эти % не надо показывать, просто карточку эту
        }
    }
}
На этой странице или как то ещё, надо показать пользователя и составить какие то карточки, где будет название продукта или услуги и проценты приобретения.

Запуск проекта:
Скачиваем зависимости:
pip install flask
pip install mysql.connector
pip install bcrypt
pip install Werkzeug

Запускаем файл app.py (при этом находясь в корневой папке) командой python app.py