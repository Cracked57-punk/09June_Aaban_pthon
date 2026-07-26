class InstaStory:
    def share(self):
        print("Sharing an image story")

class WhatsAppStory(InstaStory):
    def share(self):
        print("Sharing a text status")

inststry = InstaStory()
inststry.share()

whatsappstry = WhatsAppStory()
whatsappstry.share()