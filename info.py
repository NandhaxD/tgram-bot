import os



class ExtConfig:
       parse_mode = "Markdown"

class BotConfig:
       token = os.getenv('TOKEN', '')
       bot_id = int(token.split(':')[1])
       
