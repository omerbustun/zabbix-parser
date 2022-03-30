from exchangelib import Account, Credentials, Message, Mailbox, DELEGATE, Configuration,EWSTimeZone,EWSDateTime
import configparser

config   = configparser.ConfigParser()
config.read('config.txt')
server   = config.get('mail-ews', 'server')
username = config.get('mail-ews', 'user')
password = config.get('mail-ews', 'pass')
account  = config.get('mail-ews', 'account')

cred = Credentials(username=username,password=password)
conf = Configuration(server=server, credentials=cred)
account = Account(account, credentials=cred, config=conf)

for item in account.inbox.filter(is_read=False):
    #print('\n')
    #print(i, item.subject, item.datetime_received)
    #print('\n')
    #i = i + 1
    if item.subject.__contains__('HATA'):
        print(item.subject)
