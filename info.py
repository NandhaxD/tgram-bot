import os


class BotConfig:
       token = os.getenv('TOKEN', '')
       bot_id = int(token.split(':')[1])
       
