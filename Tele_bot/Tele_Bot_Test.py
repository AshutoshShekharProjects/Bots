from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

token = "7361762818:AAGgwufmMPjSv8ejwwwEXoiHWsF-AOzwKAQ"
application = ApplicationBuilder().token(token).build()


async def start(update, context):
    await update.message.reply_text("Hello! Welcome To My 1st Bot")


async def help(update, context):
    await update.message.reply_text(
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


async def content(update, context):
    await update.message.reply_text("We have various playlists")


async def content(update, context):
    await update.message.reply_text("We have various playlists")


async def python(update, context):
    await update.message.reply_text("link: https://youtu.be/227uk4kDTM8?si=72DqixYNgfgJBdMp")


async def sql(update, context):
    await update.message.reply_text("Link: https://youtu.be/PyDn2gU9DJo?si=IJO3EO9QSRLmYC7s")


async def java(update, context):
    await update.message.reply_text("Link: https://youtu.be/GR6mTKCXqgY?si=P3meocMKmkC4cH9F")


async def contact(update, context):
    await update.message.reply_text("Don't contact me!")


application.add_handler(CommandHandler('start', start))

application.add_handler(CommandHandler('python', python))
application.add_handler(CommandHandler('sql', sql))
application.add_handler(CommandHandler('java', java))
application.add_handler(CommandHandler('contact', contact))
application.add_handler(CommandHandler('help', help))
application.add_handler(CommandHandler('content', content))

application.run_polling()
#dispatcher.idle()