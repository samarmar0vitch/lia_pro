import asyncio
#import sys_notification
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import ConnectEvent ,DisconnectEvent , LiveEndEvent
import json , time , rigle ,subprocess
# import logging
# lol=rigle.user_n
lol=rigle.user_n

client: TikTokLiveClient = TikTokLiveClient(unique_id="@"+lol)
# client: TikTokLiveClient = TikTokLiveClient(unique_id="@user22920940181975")
# client: TikTokLiveClient = TikTokLiveClient(unique_id="@liaeljoni1")

main_arry=[""]
# rigle


# @client.on("disconnect")
# async def on_disconnect(event: DisconnectEvent):
#     print("")
#     print("************")
#     # print(main_arry)


@client.on("connect")
async def on_connect(_: ConnectEvent):
    # print("connected")
    url: dict = json.loads(client.room_info['stream_url']['live_core_sdk_data']['pull_data']['stream_data'])
    url_param: str = url['data']['origin']['main']['hls']

    if len(url_param.strip()) == 0:
        url_param: str = url['data']['origin']['main']['flv']
    url_param2: str = url['data']['origin']['main']['flv']
    main_arry.clear() 
    # main_arry.append(url_param2)
    main_arry.append(url_param2)
    client.stop()
    


def go_da():
    # print(main_arry)
    main_arry.clear()
    try:
        client.run()
    except:
        main_arry.append("offline")
    client.stop()

# if __name__ == '__main__':
#     # main(client)
#     redirecter_bridge()
#     # go_da()
#     # go_da()
#     print(main_arry)
go_da()
print(main_arry[0], end='')
