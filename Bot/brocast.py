from aiogram_broadcaster import TextBroadcaster
import asyncio
import conf
import requests

messageText="Уже 500🙋! І 270 локацій🏡! https://orxid.in.ua/ "
Token = conf.TOKEN
Users = requests.get('https://vmi957205.contaboserver.net/terinfobot/ep/allid/').json()
#Users  = [1080587853, 1345627008, 766917106]
async def main():

    # Initialize a text broadcaster (you can directly pass a token)
    broadcaster = TextBroadcaster(Users, messageText, bot_token=Token)
    
    try:
        await broadcaster.run()
    finally:
        await broadcaster.close_bot()

if __name__ == '__main__':
    asyncio.run(main())