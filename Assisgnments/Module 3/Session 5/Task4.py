"""class Movie:
    def __init__(self, title, rating):
        title = title
        rating = rating

m = Movie('Jawan', 4.5)
print(m.title, m.rating)"""

#Fix this code:

class Movie:
    def __init__(self, title, rating):
        self.title = title               #simple fix of adding self. to access the argument.
        self.rating = rating

m = Movie('Jawan', 4.5)
print(m.title, m.rating)