import telegram.ext

token = "7361762818:AAGgwufmMPjSv8ejwwwEXoiHWsF-AOzwKAQ"
updater = telegram.ext.updater(token,use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    update.message.reply_text("Hello! Welcome To My 1st Bot")


def help(update, context):
    update.message.reply_text(
        '''
        /start -> Welcome to this channel
        /help -> This particular message
        /content -> About various playlists
        /Python -> The first video of Python
        /SQL -> The first video of SQL
        /Java -> The first video of Java
        /contact -> Contact info
        '''
    )


def content(update, context):
    update.message.reply_text("We have various playlists")


def content(update, context):
    update.message.reply_text("We have various playlists")


def python(update, context):
    update.message.reply_text("link: https://youtu.be/227uk4kDTM8?si=72DqixYNgfgJBdMp")


def sql(update, context):
    update.message.reply_text("Link: https://youtu.be/PyDn2gU9DJo?si=IJO3EO9QSRLmYC7s")


def java(update, context):
    update.message.reply_text("Link: https://youtu.be/GR6mTKCXqgY?si=P3meocMKmkC4cH9F")


def contact(update, context):
    update.message.reply_text("Don't contact me!")


dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('python', python))
dispatcher.add_handler(telegram.ext.CommandHandler('sql', sql))
dispatcher.add_handler(telegram.ext.CommandHandler('java', java))
dispatcher.add_handler(telegram.ext.CommandHandler('contact', contact))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('content', content))

updater.start.polling()
updater.idle()