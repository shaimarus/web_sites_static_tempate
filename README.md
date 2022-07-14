## Шаблон по статическому веб сервису, каждое посещение на сайте логируется и записывается в базу данных. Далее ежедненвно (на кроне) отправляется по телеграм отчет о кол-ве посещении.

## 1. Запуск контейнра docker-compose up --build -d
## 2.Необходимо в поднятом БД(на postgres) создать таблицу logs (не прописано в докере): <br/>
CREATE TABLE logs (id serial PRIMARY KEY, <br/>
                    ip varchar (150) NOT NULL, <br/>
                    time1  varchar (150) NOT NULL, <br/>
                    day1  varchar (150) NOT NULL); <br/>
                    
Можно подключиться через DBeaver хост - (AWS-public ip, если запускаем на AWS) и там создать таблицу

надо не забыть открыт порт 5432 в AWS в EC2 Dashboard->Security groups>Inbounds rules иначе не увидим
![Image alt](https://github.com/shaimarus/web_sites_static_tempate/blob/main/AWS_security_group.jpg)

## 3.ДЛя телеграм канала необходимо завести свои данные по токену и CHAT_ID:
TOKEN = '5510341962:AAHdg5oh6-o4jDWLoBEsCpOsACVSnGTqFdE'
CHAT_ID = '491737145'

подробнее тут
https://stackoverflow.com/questions/29003305/sending-telegram-message-from-python
## 4.Настройка cron для ежедневного запуска
Заходим в контейнер web.
apt update
apt-get install vim -y
apt-get install -y cron

Создаем в /opt/web файл run.sh. Прописываем для него chmod +x run.sh, внутрь пишем

![Image alt](https://github.com/shaimarus/web_sites_static_tempate/blob/main/crontab.jpg)
