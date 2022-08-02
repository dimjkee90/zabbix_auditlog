from datetime import datetime
from pyzabbix import ZabbixAPI
import time
from list import action, resourcetype
import telebot
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USER')
password = os.getenv('PASSWORD')
url = os.getenv('URL')
token = os.getenv('TOKEN')
chat_id = os.getenv('CHAT_ID')


#time_till = int(time.mktime(datetime.now().timetuple()))
time_till = int(time.time())
time_from = int(time_till) - 2629743


zapi = ZabbixAPI(url)
zapi.login(username, password)

auditlog = zapi.auditlog.get(output="extend",
                             sortfield="clock",
                             sortorder="DESC",
                             limit=5,
                             time_from=f"{time_from}",
                             time_till=f"{time_till}",
                             #filter={"userid": 27}
                             )


def zabbixUser(id):
    zbuser = zapi.user.get(
        output=["username"],
        userids=f"{id}",
    )
    return zbuser


def getLog():
    result = ''
    for logs in auditlog:
        """Convert timestamp to datetime"""
        timestamp = logs.get('clock')
        logs['clock'] = datetime.fromtimestamp(int(timestamp)).strftime("%d/%m/%Y, %H:%M:%S")

        """get action number"""
        num = int(logs['action'])

        """Resolve action number to action name"""
        logs['action'] = action[num]

        """get userid"""
        userid = logs['userid']

        """convert user id to username"""
        userzabbix = zabbixUser(userid)
        userzabbix = (userzabbix[0])
        userzabbix = userzabbix['username']
        logs['userid'] = userzabbix

        """get resource type and convert to resource name"""
        resourcetypeid = int(logs['resourcetype'])
        logs['resourcetype'] = resourcetype[resourcetypeid]

        result += str(logs) + '\n'
    return result

"""prepare"""
logprepare = (str(getLog()))

"""save file"""
with open('logs.txt', 'w') as file:
    file.write(logprepare)

"""send file to telegram"""
bot = telebot.TeleBot(token)
with open('logs.txt', 'r') as sendFile:
    bot.send_document(chat_id, sendFile)

"""remove file"""
os.remove('logs.txt')