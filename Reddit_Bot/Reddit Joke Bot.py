import praw
import os
import config
import time
import requests


def bot_login():
    print("Logging in...")
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "Sad-Macaroon-1166's !Joke comment responder V0.1")
    print("Logged in!")
    return r


def run_bot(r,comment_replied_to):
    print("Obtaining 25 comments...")
    for comment in r.subreddit('test').comments(limit=10):
        if '!joke' in comment.body and comment.id not in comment_replied_to and comment.author != r.user.me():
            print("Comment with \"!joke\" found with id="+comment.id)
            comment_reply = 'You requested for a Chuck Noris Joke, here it is:\n\n'
            joke = requests.get('https://api.chucknorris.io/jokes/random').json()['value']
            comment_reply += ">" + joke
            comment_reply += "\n\nThis Joke came from [chucknorris.io](https://api.chucknorris.io)."
            comment.reply(comment_reply)
            print("Replied to comment:"+comment.id)
            with open("comments_replied_to.txt","a") as f:
                f.write(comment.id + "\n")
    print("Sleeping for 10 seconds...")
    time.sleep(10)


def get_save_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        with open("comments_replied_to.txt","w"):
            pass
    else:
        with open("comments_replied_to.txt","r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None,comments_replied_to))
    return comments_replied_to


r = bot_login()
comments_replied_to = get_save_comments()
print(comments_replied_to)
while True:
    run_bot(r, comments_replied_to)


