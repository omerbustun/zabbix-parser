from pyzabbix import ZabbixAPI
import urllib3

class ZabbixIntegration:
    def __init__(self, config):
        self.server = config["zabbix"]["server"]
        self.user = config["zabbix"]["user"]
        self.password = config["zabbix"]["password"]
        self.zapi = self.connect()

    def connect(self):
        zapi = ZabbixAPI(self.server)
        zapi.session.verify = False  # Disable SSL certificate verification
        urllib3.disable_warnings()  # Disable SSL warnings
        zapi.login(self.user, self.password)
        return zapi
