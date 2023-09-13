import asyncio
import sys_notification
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import ConnectEvent ,DisconnectEvent , LiveEndEvent
import json , time , rigle ,subprocess
import logging
lol=rigle.user_n

# TikTokApi(logging_level=logging.INFO)
# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@"+lol)
# client: TikTokLiveClient = TikTokLiveClient(unique_id="@miraharmo12")

main_arry=[]
# rigle

@client.on("live_end")
async def on_connect(event: LiveEndEvent):
    print(f"Livestream ended :(")

@client.on("disconnect")
async def on_disconnect(event: DisconnectEvent):
    print("")
    print("************")


@client.on("connect")
async def on_connect(_: ConnectEvent):
    url: dict = json.loads(client.room_info['stream_url']['live_core_sdk_data']['pull_data']['stream_data'])
    url_param: str = url['data']['origin']['main']['hls']

    if len(url_param.strip()) == 0:
        url_param: str = url['data']['origin']['main']['flv']
    url_param2: str = url['data']['origin']['main']['flv']
    # main_arry.append(url_param)
    main_arry.append(url_param2)
    client.stop()



def ffmpeg_fire_up(stream_url):
        
        try:
                pcmd = "./script_ffmpeg.sh "+stream_url
                sys_notification.send_it(lol)
                args = pcmd.split()
                process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
                for line in process.stdout:
                        if "Server returned 404 Not Found" in line:
                                print(line)
                                process.terminate()
                                redirecter_bridge()
                        if "st:1 invalid dropping" in line :
                                print(line)
                                process.terminate()
                                #input("errrrrrrrrrrrrr")
                                ffmpeg_fire_up(stream_url)

        except Exception as e:
                raise e








def go_live(stream_url):
        try:
            print(" - 🕯️ **********LIVE********** 🕯️ - ")
            print(" -🏁 **--GET URL OF LIVE  STREAM--🏁 **")
            # stream_url =get_live_url(id_room)
            ffmpeg_fire_up(stream_url)
            print(" - **--GET URL OF LIVE  STREAM--** [ "+stream_url+" ]")
        except Exception as e:
            print (str(e))


def go_da():
    main_arry.clear()

    try:
        client.run()
    except:
        main_arry.append("offline")
    return main_arry

def go_sleep():
        print(" - sleep  ZZZZZ")
        print("")
        time.sleep(60)
        redirecter_bridge()


def redirecter_bridge():
        main_arry.clear()
        print("*"*35)
        print (" - "+time.strftime("%Y-%m-%d %H:%M"))
        print("  - * ------------ > check_live : "+ lol)
        state =go_da()
        if "https" in state[0] :
                print(" - go live")
                print(' - statu { Online  }')
                go_live(state[0])
        if "offline" in state[0] :
                print(" - statu sleep ")
                print(' - statu { Offline  }')
                go_sleep()

####################################################################
if __name__ == '__main__':
    # main(client)
    redirecter_bridge()
    # go_da()
    # go_da()
    print(main_arry)



