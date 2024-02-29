import asyncio

from TikTokLive.client.client import TikTokLiveClient
from TikTokLive.client.logger import LogLevel
from TikTokLive.events import ConnectEvent, DisconnectEvent
import json , time , rigle ,subprocess
main_arry=[""]

lol=rigle.user_n

client: TikTokLiveClient = TikTokLiveClient(
    unique_id="@"+lol
)


@client.on(ConnectEvent)
async def on_connect(event: ConnectEvent):
    client.logger.info("Connected!")
    url: dict = json.loads(client.room_info['stream_url']['live_core_sdk_data']['pull_data']['stream_data'])
    url_param: str = url['data']['origin']['main']['hls']
    print("nppppppppppppppppp")
    if len(url_param.strip()) == 0:
        url_param: str = url['data']['origin']['main']['flv']
    url_param2: str = url['data']['origin']['main']['flv']
    main_arry.clear() 
    # main_arry.append(url_param2)
    main_arry.append(url_param2)
    print(url_param2)
    
    await asyncio.sleep(5)

    # Stop the client, we're done!
    await client.disconnect()


@client.on(DisconnectEvent)
async def on_live_end(_: DisconnectEvent):
    """Stop the download when we disconnect"""

    client.logger.info("Disconnected!")

    if client.web.fetch_video.is_recording:
        client.web.fetch_video.stop()


if __name__ == '__main__':
    # Enable download info
    client.logger.setLevel(LogLevel.INFO.value)

    # Need room info to download stream
    client.run(fetch_room_info=True)
