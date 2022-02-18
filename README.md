![GitHub last commit](https://img.shields.io/github/last-commit/omerbustun/zabbix-parser?logo=Github)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/omerbustun/zabbix-parser?logo=Github)
![GitHub Repo stars](https://img.shields.io/github/stars/omerbustun/zabbix-parser?style=social)
# zabbix-parser
Tool for parsing and piping e-mail alerts to Zabbix.

## Usage

Create a config.txt file in the main directory and populate it with the parameters below.

```
[settings]
server = <imap-server>
port = <imap-port>
user = <mailbox-user>
pass = <password>
sender = <alert-adress>

[zabbix]
server = <zabbix-server>
port = <port> #10051 by default
user = <zabbix-user>
pass = <password>
```

