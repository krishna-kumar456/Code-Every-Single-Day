""" Journal Program.
    Deploy over Heroku.
"""
from pymongo import MongoClient
from mongoengine import *
import datetime

AUTHOR = 'Krishna'

connect()


class Post_new(Document):
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)


if __name__ == '__main__':



    choice = input('1. Add entry to the journal, 2. View all entries, 3. Quit' )

    if choice == '1':
        input_content = input('Please enter the content for the entry ')
        input_author = AUTHOR
        input_post = Post_new(content=input_content, author=input_author)
        input_post.save()

    elif choice == '2':
        for post in Post_new.objects:
            print(post.content)
            print('=' * 50)
            print(post.author + ' on ' + str(post.published))
            print('=' * 50)

    elif choice == '3':
        exit()
