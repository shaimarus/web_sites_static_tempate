## Шаблон по статическому веб сервису, каждое посещение на сайте логируется и записывается в базу данных. Далее ежедненвно (на кроне) отправляется в группу на telegram отчет о кол-ве посещении.

## 1. Запуск контейнра docker-compose up --build -d
## 2.Необходимо в поднятом БД(на postgres) создать таблицу logs (не дописал в скрипте): <br/>
CREATE TABLE logs (id serial PRIMARY KEY, <br/>
                    ip varchar (150) NOT NULL, <br/>
                    time1  varchar (150) NOT NULL, <br/>
                    day1  varchar (150) NOT NULL); <br/>
                    
Можно подключиться через DBeaver хост - (AWS-public ip, если запускаем на AWS) и там создать таблицу

надо не забыть открыт порт 5432 в AWS в EC2 Dashboard->Security groups>Inbounds rules иначе не увидим
![Image alt](https://github.com/shaimarus/web_sites_static_tempate/blob/main/AWS_security_group.jpg)

## 3.Для телеграм канала необходимо завести свои данные по токену и CHAT_ID:
TOKEN = '5510341962:AAHdg5oh6-o4jDWLoBEsCpOsACVSnGTqFdE'
CHAT_ID = '491737145'

подробнее тут
https://stackoverflow.com/questions/29003305/sending-telegram-message-from-python
## 4.Настройка cron для ежедневного запуска
Заходим в контейнер web. <br/>
apt update <br/>
apt-get install vim -y <br/>
apt-get install -y cron <br/>

Создаем в /opt/web файл run.sh. Прописываем для него chmod +x run.sh, внутрь пишем

![Image alt](https://github.com/shaimarus/web_sites_static_tempate/blob/main/crontab.jpg)

## 5. Возможные проблемки
Если выйдет проблема когда контейнеры не видят друг друга <br/>
https://pgcookbook.ru/article/could_not_connect_to_server_connection_refused.html <br/>

find / -name postgresql.conf 2> /dev/null <br/>
проходим по этому пути октрывем через vi и открываем порт 5432 и далее контейтер с postgres перезагружаем, т.е. делаем docker restart <br/>

Не удалось отправку через gmail, google недавно с 30.05.2022 убрал функцию по отправки через логи и пароли для безопасности<br/>

Не удалось записывать логи через from flask_track_usage import TrackUsage, т.к. при ее подключении слетают CSS не знаю как победить, вроде менял "{{ url_for('static',filename='assets/css/fontawesome.css') }}" и т.д. не помогло <br/>

Возможно больше отклик страницы т.к. делает инсерт в БД <br/>


## TODO: <br/>
Все описанное выше запихать в докер и чтобы писать только docker-compose up --build -d.


