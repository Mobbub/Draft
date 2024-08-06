


// Получаем ссылку на поле выбора файла
const fileInput = document.getElementById('input__file');

// Создание нового элемента div для отображения в нём сообщения с сервера
var mes_cuc = document.createElement('div');
mes_cuc.className += ' flex cuc-regi messeg';

var mes_eror = document.createElement('div');
mes_eror.className += ' flex errors messeg';

// Получаем ссылку на div с формой
var mainWrapper = document.querySelector(".upload-wrapper");

// Получаем ссылку на секцию
const main = document.querySelector(".section-upload");

// Получаем ссылку на общий div
const container = document.querySelector(".section-upload_container");

// Счётчик обюработанных файлов
var scors = 0;

// Добавляем обработчик события 'change' на поле ввода файла
fileInput.addEventListener('change', (event) => {

    // Готовим файл к отправки на сервер
    const formData = new FormData();
    const files = document.getElementById("input__file");
    formData.append("file", files.files[0]);

    // Создание div с отображением "загрузки"
    var loadBar = create('<div class="flex loadBar"><img class="loadBar_img" src="../static/pictures/load.gif" alt="Загрузка"><p class="loadBar_text">Обработка запроса...</p></div>');

    // Удаляет div с формой 
    document.querySelector(".upload-wrapper").remove();

    // Установка "загрузки" на место формы
    container.prepend(loadBar);

    // Создание параметров запроса
    const requestOptions = {

        mode: "no-cors",
        method: "POST",
        files: files.files[0],
        body: formData,
    };

    // Отправление первого пост запроса на сервер для сохранение файла
    fetch("/up_db", requestOptions)
        .then((response) => response.json())
        .then((response) => {

            // Проверка что ответ корректный, иначе вывод сообщение об ошибке и выход из addEventListener
            if (response['status'] != 200) {

                // Вставка полученого от сервера сообщения в созданный div
                mes_eror.innerHTML = response['message'];

                // Вставка div в начало main
                main.prepend(mes_eror);

                // Удаление "загрузки"
                document.querySelector(".loadBar").remove();

                // Вставка div для загрузки пользовательского изображения и обнуление его значения
                container.prepend(mainWrapper);
                document.getElementById("input__file").value = '';

                return;
            }

            // Создание контейнера для результатов обработки и вставление его в низ секции
            var container_result = create('<div class="container-result" id="container-result-' + scors + '"></div>');
            main.append(container_result);

            // Получение ссылки на контейнер для отображение результатов
            var container_result = document.getElementById("container-result-" + scors);


        }
        );

});


// Функция для создания html объекта из строки
function create(htmlStr) {
    var frag = document.createDocumentFragment(),
        temp = document.createElement('div');
    temp.innerHTML = htmlStr;
    while (temp.firstChild) {
        frag.appendChild(temp.firstChild);
    }
    return frag;
}


// Слушатель кнопки для скачивания файла
$('body').delegate('.download', 'click', function (e) {
    var id = e.currentTarget.getAttribute('id');
    var link = document.createElement('a');
    link.setAttribute('href', 'static/result/' + id);
    link.setAttribute('download', id);
    link.click();
    return false;
});

//Слушатель для кнопки выхода
$('body').delegate('.exit', 'click', function (e) {

    // Создание нового элемента div для отображения в нём сообщения с сервера
    var mes_cuc = document.createElement('div');
    mes_cuc.className += ' flex cuc-regi messeg';


    request = {};
    request['index_action'] = -1;
    console.log(request);

    fetch("/exit", {
        method: 'POST',
        // body: new FormData(form)
        body: JSON.stringify(request),
        headers: {
            'Content-Type': 'application/json'
        }
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);

            // Если сообщение уже есть, удалить текущее
            if (document.querySelector(".messeg") != null) {
                document.querySelector(".messeg").remove();
            }

            // Выделение элемента main, для последующей вставки в его начало сообщений
            const main = document.querySelector(".main-section");

            if (data['status'] == 200) {

                // Вставка полученого от сервера сообщения в созданный div
                mes_cuc.innerHTML = data['message'];



                // Вставка div в начало main
                main.before(mes_cuc);

                window.setTimeout(function () { window.location = "/authorization"; }, 4000);

            } else {

                // Вставка полученого от сервера сообщения в созданный div
                mes_cuc.innerHTML = data['message'];

                // Вставка div в начало main
                main.before(mes_cuc);
            }



        });
});

// Функция для заполнения таблицы
function createTable(url, table) {

    fetch(url)
        .then(response => response.text())
        .then(data => {
            let rows = data.split("\n");
            for (let i = 0; i < rows.length; i++) {
                let cells = rows[i].split(",");
                let row = table.insertRow();
                for (let j = 0; j < cells.length; j++) {
                    let cell = row.insertCell();
                    cell.innerText = cells[j];
                }
            }
        })
        .catch(error => console.log(error));
}




