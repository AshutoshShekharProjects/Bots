import praw
import sys
import config
import time


def bot_login():
    print("Loging in...")
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent="Sad-Macaroon-1166's Reply/Notification BotV0.1")
    print("Logged in...")
    return r


def get_username(filename):
    try:
        with open(filename, "r") as f:
            usernames = f.read()
            usernames = usernames.split('\n')
            usernames = list(filter(None, usernames))
    except IOError:
        print("Error: File " + filename + " not found in the current directory")
        quit()
    return usernames


def send_message(r, username, subject, body):
    try:
        r.redditor(username).message(subject=subject, message=body)
    except praw.exceptions.APIException as e:
        #if "USER_DOESNT_EXIST" in e.args[0]:
        print("Redittor " + username + " not found.")
        return
    print("Sent message to: " + username + "!")


if len(sys.argv) != 4:
    print("Usage: Reply_Bot.py filename \"subject\" \"body\"")
filename = sys.argv[1]
subject = sys.argv[2]
body = sys.argv[3]
r = bot_login()
usernames = get_username(filename)
print(usernames)
for username in usernames:

    send_message(r, username, subject, body)
    time.sleep(5)
