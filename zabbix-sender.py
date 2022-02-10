import configparser
from pyzabbix import ZabbixSender, ZabbixAPI    

# Giriş bilgilerini yapılandırma dosyasından oku
config   = configparser.ConfigParser()
config.read('config.txt')
zabbix_server   = config.get('zabbix', 'server')
zabbix_port     = config.get('zabbix', 'port')
zabbix_user     = config.get('zabbix', 'user')
zabbix_password = config.get('zabbix', 'pass')

# Zabbix sunucusuyla bir oturum oluştur
zsend = ZabbixSender(zabbix_server = zabbix_server, zabbix_port = zabbix_port, use_config = False)


zsend.send('ZabbixSender test')