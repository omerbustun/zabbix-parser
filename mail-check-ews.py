from exchangelib import Account, Credentials, Message, Mailbox, DELEGATE, Configuration,EWSTimeZone,EWSDateTime
import configparser

config   = configparser.ConfigParser()
config.read('config.txt')
server   = config.get('mail-ews', 'server')
port     = config.get('mail-ews', 'port')
username = config.get('mail-ews', 'user')
password = config.get('mail-ews', 'pass')
account  = config.get('mail-ews', 'account')
sender   = config.get('mail-ews', 'sender')


cred = Credentials(username=username,password=password)
conf = Configuration(server=server, credentials=cred)
account = Account(account, credentials=cred, config=conf)

i = 1
for item in account.inbox.filter(is_read=False, subject__contains='HATA'):
    print('\n')
    print(i, item.subject, item.datetime_received)
    print('\n')
    i = i + 1
