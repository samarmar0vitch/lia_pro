import asyncio
#import sys_notification
from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent ,DisconnectEvent , LiveEndEvent
import json , time , rigle ,subprocess ,os ,re
import logging
from subprocess import PIPE, Popen

lol=rigle.user_n
def ok_ok():
    command = "python3 ff.py"
    with Popen(command, stdout=PIPE, stderr=None, shell=True) as process:
        outputoo = process.communicate()[0].decode("utf-8")
        print(outputoo)
        #state = re.search("(?P<url>https?://[^\s]+)", outputoo).group("url")
        #print(state)
    return outputoo


# client: TikTokLiveClient = TikTokLiveClient(unique_id="@"+lol)
# client: TikTokLiveClient = TikTokLiveClient(unique_id="@miraharmo12")



def ffmpeg_fire_up(stream_url):
        os.system("ps aux | grep -i ffmpeg | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
        try:
                pcmd = "./script_ffmpeg.sh "+stream_url
                #sys_notification.send_it(lol)
                args = pcmd.split()
                process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False ,universal_newlines=True ,preexec_fn=os.setsid)
                for line in process.stdout:
                        if "404 Not Found" in line:
                                print(line)
                                process.terminate()
                                redirecter_bridge()
                        if "st:1 invalid dropping" in line :
                                print(line)
                                print("errrror")
                                time.sleep(1)
                                process.kill()
                                os.system("ps aux | grep -i ffmpeg | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
                                #process.kill()
                                #os.killpg(os.getpgid(self.proc.pid), signal.SIGHUP)
                                #os.killpg(os.getpgid(self.proc.pid), signal.SIGTERM)
                                print("errrrrrrrrrrrrr")
                                os.system("supervisorctl restart start-sync-stream")
                                #ffmpeg_fire_up(stream_url)

        except Exception as e:
                print("ffmpeg_fire_up issue")


def go_live(stream_url):
        try:
            print(" - 🕯️ **********LIVE********** 🕯️ - ")
            print(" -🏁 **--GET URL OF LIVE  STREAM--🏁 **")
            # stream_url =get_live_url(id_room)
            ffmpeg_fire_up(stream_url)
            print(" - **--GET URL OF LIVE  STREAM--** [ "+stream_url+" ]")
        except Exception as e:
            print (str(e))


# def go_da():
#     print(main_arry)
#     main_arry.clear()

#     try:
#         client.run()
#     except:
#         main_arry.append("offline")
#     return main_arry

def go_sleep():
        print(" - sleep  ZZZZZ")
        print("")
        time.sleep(180)
        redirecter_bridge()


def redirecter_bridge():
        os.system("pkill ffmpeg")
        # main_arry.clear()
        print("*"*35)
        print (" - "+time.strftime("%Y-%m-%d %H:%M"))
        print("  - * ------------ > check_live : "+ lol)
        state =ok_ok()
        try:
            state0 = re.search("(?P<url>https?://[^\s]+)", state).group("url")
        except:
            state0="offline"
            
        print(state0)
        #os.system('curl ipinfo.io')
        
        print(state0)
        
        if "https" in state0 :
                #state0 = re.search("(?P<url>https?://[^\s]+)", state).group("url")
                print(" - go live")
                print(' - statu { Online  }')
                go_live(state0)
        if "offline" in state0 :
                print(" - statu sleep ")
                print(' - statu { Offline XD }')
                go_sleep()

####################################################################
redirecter_bridge()
#if __name__ == '__main__':
    # main(client)
    #redirecter_bridge()
    # go_da()
    # go_da()
    # print(main_arry)
