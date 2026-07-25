class InstagramPost:
    def __init__(self,caption,likes,comments):
        self.caption = caption
        self.likes = int(likes)
        self.comments = comments 
        print(f"{self.likes},{self.comments}")

    def add_comment(self, comment_text):
        self.comments.append(comment_text)
        self.likes += 1
    

post1=InstagramPost("Cool Caption",49,["Nice photo","nice caption bro!"])
post1.add_comment(input("Enter you comment:"))
