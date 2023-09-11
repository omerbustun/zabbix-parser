import imaplib
import email

class EmailProcessor:
    def __init__(self, config):
        self.config = config["email"]
        if self.config["protocol"].upper() == "IMAP":
            self.processor = IMAPEmailProcessor(self.config)
        elif self.config["protocol"].upper() == "EWS":
            self.processor = EWSEmailProcessor(self.config)
        else:
            raise ValueError("Unsupported email protocol specified in config.")

    def connect(self):
        return self.processor.connect()

    def fetch_emails(self):
        return self.processor.fetch_emails()

    def process_emails(self):
        return self.processor.process_emails()


class IMAPEmailProcessor:
    def __init__(self, config):
        self.config = config
        self.connection = None

    def connect(self):
        """Connect to the IMAP server."""
        try:
            self.connection = imaplib.IMAP4_SSL(self.config["server"], int(self.config["port"]))
            self.connection.login(self.config["username"], self.config["password"])
            self.connection.select('INBOX')
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def fetch_emails(self):
        """Fetch all emails."""
        emails = []
        try:
            _, selected_mails = self.connection.search(None, 'ALL')
            for num in selected_mails[0].split():
                _, data = self.connection.fetch(num, '(RFC822)')
                _, bytes_data = data[0]
                email_message = email.message_from_bytes(bytes_data)
                emails.append(email_message)
        except Exception as e:
            print(f"Error: {e}")
        return emails

    def process_emails(self):
        """Process fetched emails and return structured data."""
        emails = self.fetch_emails()
        processed_data = []
        for email_message in emails:
            data = {
                "subject": email_message["subject"],
                "date": email_message["date"],
                "content": ""
            }
            for part in email_message.walk():
                if part.get_content_type() == "text/plain" or part.get_content_type() == "text/html":
                    message = part.get_payload(decode=True)
                    data["content"] = message.decode('ISO-8859-9')
                    break
            processed_data.append(data)
        return processed_data


class EWSEmailProcessor:
    # Placeholder for the future EWS implementation
    def __init__(self, config):
        self.config = config

    def connect(self):
        print("EWS connect method is not yet implemented.")
        return False

    def fetch_emails(self):
        print("EWS fetch_emails method is not yet implemented.")
        return []

    def process_emails(self):
        print("EWS process_emails method is not yet implemented.")
        return []
