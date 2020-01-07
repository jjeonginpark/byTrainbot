import sys
import time
import telepot
import korail2

#----------------------------------------------------------
def Determine(bot, unread):
    n = len(unread)

    for i in range(n):
        msg = unread[i]['message']
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id, msg['text'])
        if(msg['text'] == '가위'):
            bot.sendMessage(chat_id, '보')

        if(msg['text'] == '바위'):
            bot.sendMessage(chat_id, '가위')

        if(msg['text'] == '보'):
            bot.sendMessage(chat_id, '바위')


TOKEN = sys.argv[1]  # get token from command-line
bot = telepot.Bot(TOKEN)

print ('Listening...')
# Keep the program running.
update_id = 0
while 1:
    unread = bot.getUpdates(offset=update_id + 1)
    if unread:
        update_id = unread[len(unread)-1]['update_id']
    else:
        update_id = 0
   
    if unread:
        Determine(bot, unread)

    time.sleep(0.5)