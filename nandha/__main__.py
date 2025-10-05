import asyncio

from nandha import bot
from info import ExtConfig

async def main():
    await bot.run_for_updates()
    await bot.send_message(
         chat_id=ExtConfig.support,
         text="Bot Re-Started!"
    )


if __name__ == "__main__":
    asyncio.run(main())
    
