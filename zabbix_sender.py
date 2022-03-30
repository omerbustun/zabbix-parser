#!/usr/bin/python
import configparser
import logging
import sys
from pyzabbix import ZabbixMetric, ZabbixSender

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# Giriş bilgilerini yapılandırma dosyasından oku
config   = configparser.ConfigParser()
config.read('config.txt')
zabbix_server   = config.get('zabbix', 'server')
zabbix_port     = config.get('zabbix', 'port')


def zabbix_send(host_id, key, value):
    # Paketi Zabbix trapper'a gönderilmek üzere hazırla
    packet = [ZabbixMetric(host_id, key, value)]
    # Paketi gönder
    result = ZabbixSender(zabbix_server, int(zabbix_port), use_config=None).send(packet)
    # Sonucu yazdır
    print(result)