Скрипт для отправки zabbix auditlog в телеграм \
Обращается к zabbix api, к объекту auditlog.get и user.get, получает данные auditlog'a, резолвит значение userid и resourcetype \
Нужно скопировать example.env в .env и указать свои данные
```commandline
USER= учетная запись в заббикс
PASSWORD= пароль учетной записи заббикс
URL= заббикс урл

# для телеграм бота

TOKEN= токен телеграмм бота 
CHAT_ID= ид чата с телеграмм ботом, можно узнать через get my id бота
```
Установить зависимости 
```
pip install -r requirements.txt
```
