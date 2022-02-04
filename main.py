#!/usr/bin/env python

import imaplib
import email
import configparser

# Import credentials from config.txt
config = configparser.ConfigParser()
config.read('config.txt')
server   = config.get('settings', 'server')
port     = config.get('settings', 'port')
username = config.get('settings', 'user')
password = config.get('settings', 'pass')

