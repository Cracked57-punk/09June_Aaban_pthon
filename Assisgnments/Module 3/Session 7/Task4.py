"""class Content:
    def display(self, title):
        print('Title:', title)

class Movie(Content):
    def display(self, title, year):
        # your code here"""

#Fix this :

class Content:
    def display(self, title):
        print('Title:', title)

class Movie(Content):
    def display(self, title, year):
        print(f"Title: {title}\nYear: {year}")

movie = Movie()
movie.display("Movie title","2026")