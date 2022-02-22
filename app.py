#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base64 import decode
import imaplib
import email
import configparser
from email.header import decode_header

# Giriş bilgilerini yapılandırma dosyasından oku
config   = configparser.ConfigParser()
config.read('config.txt')
server   = config.get('settings', 'server')
port     = config.get('settings', 'port')
username = config.get('settings', 'user')
password = config.get('settings', 'pass')
sender   = config.get('settings', 'sender')

## Türkçe karakterleri kullanılabilir hale getir
# tr2eng =str.maketrans('çÇğĞıİöÖşŞüÜ', 'cCgGiIoOsSuU')

# Giriş yap ve posta kutusunu seç
imap = imaplib.IMAP4_SSL(server, port)
imap.login(username, password)
imap.select('INBOX')

# Uygulamanın uyarı gönderdiği e-posta adresinden gelen e-postaları ayır 
_, selected_mails = imap.search(None, '(FROM ' + sender + ')', '(SUBJECT "Uyari")')


for num in selected_mails[0].split():
    _, data = imap.fetch(num , '(RFC822)')
    _, bytes_data = data[0]

    # Gelen e-posta içeriğini oku
    email_message = email.message_from_bytes(bytes_data)
    print("\n===========================================")

    # E-posta içeriğini yazdır
    print("Subject: ", email_message["subject"])
    # print("To:", email_message["to"])
    # print("From: ", email_message["from"])
    print("Date: ", email_message["date"])
    for part in email_message.walk():
        if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
            message = part.get_payload(decode=True)
            print("Message: \n", message.decode('ISO-8859-9'))
            print("==========================================\n")
            break

imap.close()
imap.logout()