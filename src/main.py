import yaml
from modules.email_processor import EmailProcessor
from modules.zabbix_integration import ZabbixIntegration

def load_config():
    """Load the configuration from config.yaml."""
    with open("config.yaml", 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None

def main():
    # Load the configuration
    config = load_config()
    if not config:
        print("Failed to load configuration. Exiting.")
        return

    # Process emails
    email_processor = EmailProcessor(config)
    email_processor.connect()
    processed_emails = email_processor.process_emails()

    # TODO: Decide how to use the processed_emails with Zabbix or other systems.
    print("Processed Emails:", processed_emails)

    # Zabbix integration (placeholder)
    zabbix = ZabbixIntegration(config)

if __name__ == "__main__":
    main()
