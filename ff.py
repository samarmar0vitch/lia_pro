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

@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    client.logger.info("Connected!")
    url: dict = json.loads(client.room_info['stream_url']['live_core_sdk_data']['pull_data']['stream_data'])
    url_param: str = url['data']['origin']['main']['hls']
    print(url_param)
    print(url)

    if len(url_param.strip()) == 0:
        url_param: str = url['data']['origin']['main']['flv']
    url_param2: str = url['data']['origin']['main']['flv']
    main_arry.clear()
    # main_arry.append(url_param2)
    main_arry.append(url_param2)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(main_arry[1])
    print(main_arry[1], end='')


    # Start a recording
    #client.web.fetch_video.start(
    #   output_fp=f"{event.unique_id}.mp4",
    #    room_info=client.room_info,
    #    output_format="mp4"
    #)

    await asyncio.sleep(5)

    # Stop the client, we're done!
    await client.disconnect()





#
    


def go_da():
    # print(main_arry) client.disconnect()
    main_arry.clear()
    try:
        client.logger.setLevel(LogLevel.INFO.value)
        client.run(fetch_room_info=True)
    except:
        main_arry.append("offline")
    client.disconnect()

# if __name__ == '__main__':
#     # main(client)
#     redirecter_bridge()
#     # go_da()
#     # go_da()
#     print(main_arry)
go_da()
print(main_arry[0], end='')
print(TikTokLive.__version__)
