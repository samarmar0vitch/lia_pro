import asyncio
#import sys_notification
from TikTokLive import TikTokLiveClient
#from TikTokLive.events import ConnectEvent ,DisconnectEvent , LiveEndEvent
from TikTokLive.client.logger import LogLevel
from TikTokLive.events import ConnectEvent, DisconnectEvent
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


@client.on("ConnectEvent")
async def on_connect(_: ConnectEvent):
    # print("connected")
    url: dict = json.loads(client.room_info['stream_url']['live_core_sdk_data']['pull_data']['stream_data'])
    url_param: str = url['data']['origin']['main']['hls']

    
