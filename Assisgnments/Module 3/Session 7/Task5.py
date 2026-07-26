class Notification:
    def send(self):
        print("Sending a generic notification")

class EmailNotification(Notification):
    def send(self):
        print("Sending an Email notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending an SMS notification")

notif = Notification()
notif.send()

email = EmailNotification()
email.send()

sms = SMSNotification()
sms.send()

"""EmailNotification and SMSNotification inherit from Notification but redefine send() with their own message, so calling send() on each object runs the version defined in that object's own class rather than the parent's that is method overriding.simple."""