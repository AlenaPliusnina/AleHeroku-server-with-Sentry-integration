# Heroku server with Sentry integration

Чтобы проверить работу сервера на heroku перейдите по ссылке: https://blooming-beyond-37568.herokuapp.com/ 

Описание:

1. При переходе по адресу https://blooming-beyond-37568.herokuapp.com/success сервер возвращает статус - HTTP 200 OK

![Ответ сервера success](https://github.com/AlenaPliusnina/Heroku-server-with-Sentry-integration/blob/master/screenshots/success.png)

2. При переходе по адресу https://blooming-beyond-37568.herokuapp.com/fail сервер возвращает статус - Error: 500 Internal Server Error. 

![Ответ сервера fail](https://github.com/AlenaPliusnina/Heroku-server-with-Sentry-integration/blob/master/screenshots/fail.png)

При этом все ошибки приложения попадают в информационную панель Sentry.io (https://sentry.io/welcome/) — комплексного инструмента для сбора и анализа ошибок приложения. 

![Логи в Sentry](https://github.com/AlenaPliusnina/Heroku-server-with-Sentry-integration/blob/master/screenshots/sentry_1.png)

![Логи в Sentry](https://github.com/AlenaPliusnina/Heroku-server-with-Sentry-integration/blob/master/screenshots/sentry_2.png)


Разворачиваем проект локально:

1. Скачайте репозиторий

2. Создайт виртуальное окружение:

       python -m venv env

3. Активируйте виртуальное окружение:

       source env/bin/activate
      
4. Чтобы установить требуемые зависимости выполните команду:

       pip install -r requirements.txt

5. Чтобы запустить сервер локально введите в консоли команду: 
        
       python server.py

