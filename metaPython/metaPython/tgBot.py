import telegram
from telegram.error import NetworkError, Unauthorized

def main():
  global update_id
  bot = telegram.Bot(':')

  try:
    update_id = bot.get_updates()[0].update_id
  except IndexError:
    update_id = None

  while True:
    try:
      echo(bot)
    except NetworkError:
      sleep(1)
    except Unauthorized:
      update_id += 1

def echo(bot):
  global update_id
  for update in bot.get_updates(offset=update_id, timeout=10):
    update_id = update.update_id + 1

    if update.message:
      if "сука" in str(update.message.text):
        print(update.message)
        #update.message.reply_text("сам ты сука, сука")
        
if __name__ == '__main__':
    main()