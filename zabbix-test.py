import configparser
from pyzabbix.api import ZabbixAPI

# Giriş bilgilerini yapılandırma dosyasından oku
config   = configparser.ConfigParser()
config.read('config.txt')
zabbix_server   = config.get('zabbix', 'server')
zabbix_user     = config.get('zabbix', 'user')
zabbix_password = config.get('zabbix', 'pass')

# Zabbix sunucusuyla bir oturum oluştur
zapi = ZabbixAPI(url = zabbix_server, user = zabbix_user, password = zabbix_password)

# Zabbix ile izlenen hostların listesini al
result = zapi.host.get(monitored_hosts=1, output='extend')
hostnames = [host['host'] for host in result]

# Host listesini yazdır
print(*hostnames, sep='\n')

# Oturumu kapat
zapi.user.logout()
