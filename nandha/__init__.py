
import logging


from info import BotConfig, ExtConfig
from tgram import TgBot

FORMAT = f"[Bot] %(message)s"
logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'), logging.StreamHandler()], format=FORMAT)
logging.getLogger('httpx').setLevel(logging.WARNING)

bot = TgBot(
  bot_token=BotConfig.token,
  parse_mode=ExtConfig.parse_mode,
  plugins="nandha/plugins"
)
