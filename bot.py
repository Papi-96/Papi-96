from pyrogram import Client, filters
chemistry = "chemistry"
biology = "biology"
physics = "physics"
english = "english"
maths = "mathematics"
bot = Client(
    "cptn",
    api_id = 16941804,
    api_hash="d4514cc5d7ba9eca696c6dde4c1928e0",
    bot_token="6869594582:AAGB33Y0J0OUXB2S6xLHXeqDnNkB8HuqzVc"
)

@bot.on_message(filters.command('start') & filters.private)
def command1(bot, message):
    bot.send_message(message.chat.id, 'Hey,I am the bot Cptn'
                     ' my master is papi:)')



@bot.on_message(filters.command(chemistry.upper()))
def command1(bot,message):
    bot.send_message(message.chat.id, "document file id")

@bot.on_message(filters.command(biology.upper()))
def command1(bot,message):
    bot.send_message(message.chat.id, "document file id")

@bot.on_message(filters.command(english.upper()))
def command1(bot,message):
    bot.send_message(message.chat.id, "document file id")
print('i am live')
bot.run()