import csv
import smtplib
from email.mime.text import MIMEText
from user_fetcher import UserFetcher


class Mailer():
    def send(self, sender, recipients, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipients
        s = smtplib.SMTP('localhost', 1025)
        s.send_message(msg)
        s.quit()


class Logger():

    def output(message):
        print("[Logger]\n{}".format(message))


class LoggerAdapter():

    def __init__(self, what_i_have):
        self.what_i_have = what_i_have

    def send(self, sender, recipient, subject, message):
        log_message = "From: {}\nTo: {}\nSubject: {}\nMessage: {}".format(
            sender,
            recipient,
            subject,
            message
            )
        self.what_i_have.output(log_message)

    def __getattr__(self, attr):
        return getattr(self.what_i_have, attr)


if __name__ == "__main__":
    user_fetcher = UserFetcher('users.csv')
    users = user_fetcher.fetch_users()
    mailer = Mailer()
    logger = LoggerAdapter(Logger)
    for user in users:
        logger.send(
            'me@example.com',
            user["email"],
            "This is your message",
            "Have a good day"
        )
        mailer.send(
            'me@example.com',
            user["email"],
            "This is your message",
            "Have a good day"
        )
