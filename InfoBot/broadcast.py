import sys
from aiogram_broadcaster import TextBroadcaster
import asyncio
import Bot.conf

messageText = sys.argv[1]
Token = Bot.conf.TOKEN
Users = Bot.conf.ADMIN_IDS


async def main():
    # Initialize a text broadcaster (you can directly pass a token)
    broadcaster = TextBroadcaster(Users, messageText, bot_token=Token)

    try:
        await broadcaster.run()
    finally:
        await broadcaster.close_bot()


if __name__ == '__main__':
    asyncio.run(main())
