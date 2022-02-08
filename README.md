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
```