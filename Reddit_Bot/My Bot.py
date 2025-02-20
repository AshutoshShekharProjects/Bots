import os.path
import praw
import config
import time


def bot_login():
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="Sad-Macaroon-1166's dog comment responder V0.1")
    return r


def run_bot(r, comments_replied_to):
    for comment in r.subreddit('Test').comments(limit=25):
        if 'Cat' in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print ("String Found " + comment.id)
            comment.reply("Dog caught! [Here](https://www.pexels.com/photo/two-yellow-labrador-retriever-puppies"
                          "-1108099/) See one")
            print("Replied to comment " + comment.id)
            #comments_replied_to.append(comment.id)
            with open("comments_replied_to.txt","a") as f:
                f.write(comment.id + "\n")
            print(comment.author)
            print(r.user.me())


def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        with open('comments_replied_to.txt','w'):
            pass
    else:
        with open('comments_replied_to.txt','r') as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))
    return comments_replied_to


r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)
#while True:
run_bot(r, comments_replied_to)
