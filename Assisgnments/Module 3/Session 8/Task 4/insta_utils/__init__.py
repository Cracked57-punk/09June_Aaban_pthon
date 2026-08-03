"""A package in Python is just a folder that Python recognizes as something it can import from. What makes a folder a package (in the classic sense) is an __init__.py file inside it — even an empty one signals 'treat me as a package.'
"""
from .likes import like_count
from .comments import comment_count