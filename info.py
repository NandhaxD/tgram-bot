import os



class ExtConfig:
       support = "NandhaSupport"
       update = "NandhaBots"
       parse_mode = "Markdown"

class BotConfig:
       token = os.getenv('TOKEN', '')
       bot_id = int(token.split(':')[1])
       
