from imbox import Imbox

class Inbox:
    def __init__(self, host, username, password, port):
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def check_mails(self):
        with Imbox(self.host, self.username, self.password, port=self.port) as imbox:
            messages = imbox.messages(unread=True, folder='INBOX')

            for uid, message in messages:
                if hasattr(message, 'subject'):
                    print(message.subject)

                for attachment in message.attachments:
                    with open(attachment['filename'], 'wb') as file:
                        file.write(attachment['content'].getvalue())

                imbox.mark_seen(uid)