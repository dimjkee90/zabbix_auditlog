Script to send zabbix auditlog to telegram.
Accesses through zabbix api, to the auditlog.get and user.get object, gets the auditlog, resolves the value of userid and resourcetype
You need to copy example.env to .env and provide your details

install
```
pip install -r requirements.txt
```
