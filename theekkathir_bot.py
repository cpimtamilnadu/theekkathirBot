import logging
import telegram
import feedparser


LAST_UPDATE_ID = None

d = feedparser.parse('http://theekkathir.in/feed/')

latest_update = d.entries[0].title + " " + d.entries[0].link

def main():
    global LAST_UPDATE_ID

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Telegram Bot Authorization Token
    bot = telegram.Bot('place your token')

    # This will be our global variable to keep the latest update_id when requesting
    # for updates. It starts with the latest update_id if available.
    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None

    while True:
        echo(bot)


def echo(bot):
    global LAST_UPDATE_ID

    # Request updates after the last updated_id
    for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
        # chat_id is required to reply any message
        
        chat_id = update.message.chat_id
        message = update.message.text.encode('utf-8')
        

        if (message == '/latest'):
            # Reply the message
            bot.sendMessage(chat_id=chat_id,
                            text=latest_update)

            # Updates global offset to get the new updates
            LAST_UPDATE_ID = update.update_id + 1
        else:
            message = "Wrong Value"


if __name__ == '__main__':
    main()
    
    