
import time
import requests as req
import re
import os
import shutil
import ffmpeg
import sys
import rigle ,json ,subprocess
from enums import Mode, Error, StatusCode, TimeOut

headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Referer": "https://www.tiktok.com/",
            }



def ffmpeg_fire_up(stream_url):
        try:
                pcmd = "./script_ffmpeg.sh "+stream_url
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
                                input("errrrrrrrrrrrrr")

        except Exception as e:
                raise e
        







def get_live_url(room_id):
        """
        I get the cdn (flv or m3u8) of the streaming
        """
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Referer": "https://www.tiktok.com/",
            }
            url = f"https://webcast.tiktok.com/webcast/room/info/?aid=1988&room_id={room_id}"
            json_data = req.get(url, headers=headers).json()
            # print(json_data)
            json_formatted_str = json.dumps(json_data, indent=2)
            #print(json_formatted_str)

            #live_url_m3u8 = json['data']['stream_url']['hls_pull_url']
            live_url_flv = json_data['data']['stream_url']['rtmp_pull_url']
            live_url_flv_2 = json_data['data']['stream_url']['flv_pull_url']
            # print("[*] URL FLV", live_url_flv)
            json_formatted_str_2 = json.dumps(json_data['data']['stream_url'], indent=2)
            # print("[*] URL FLV", live_url_flv_2)
            #print("[*] URL FLV", json_formatted_str_2)

            return live_url_flv
        except Exception as ex:
            print(ex)



def get_room_id(user):
        try:
            response = req.get(f"https://www.tiktok.com/@{user}/live", allow_redirects=False , timeout=8 , headers=headers)
            if response.status_code == StatusCode.REDIRECT:
                raise req.HTTPError()

            content = response.text
            #print(content)
            if "room_id" not in content:
                raise ValueError()

            return re.findall("room_id=(.*?)\"/>", content)[0]
        except req.HTTPError:
            raise req.HTTPError(Error.HTTP_ERROR)


def is_user_in_live(user):
        print(" - * ------------ > check_live : "+ user)
        
        try:
                response = req.get(f"https://www.tiktok.com/@{user}/live", headers =headers)#, allow_redirects=False)
                content = response.text
                # print(content)
                if "room_id" not in content:
                        raise ValueError('no room id')
                read_1=re.findall("room_id=(.*?)\"/>", content)[0]
                print(" - User [ "+user+ " ] ***** [ "+read_1+" ] ")
                return read_1
        except Exception as ex:
                print(ex)



def go_go ():
        state="init"
        try:
                #lol="tumpolinaaa"
                print(" - "+rigle.user_n)
                lol=rigle.user_n
                # id_room=is_user_in_live("liaeljoni1")
                id_room=is_user_in_live(lol)
                url = f"https://www.tiktok.com/api/live/detail/?aid=1988&roomID={id_room}"
                content = req.get(url).text
                #content = response.text
                if '"status":4' in content:
                        print(' - statu { Offline }')
                        state="off"
                elif '"status":4' not in content:
                        print(' - statu { Online }')
                        state="on"
                return state ,id_room

        except Exception as op:
                print(op)

def go_sleep():
        print(" - sleep  ZZZZZ")
        time.sleep(60)
        redirecter_bridge()


def go_live(id_room):
        try:
            print(" - **********LIVE********** - ")
            input(" - **--GET URL OF LIVE  STREAM--**")
            stream_url =get_live_url(id_room)
            ffmpeg_fire_up(stream_url)
            input(" - **--GET URL OF LIVE  STREAM--** [ "+stream_url+" ]")
        except Exception as e:
            print (str(e))






def redirecter_bridge():
        print("*"*35)
        print (" - "+time.strftime("%Y-%m-%d %H:%M"))
        state , id_room=go_go ()
        if "on" in state:
                print(" - go live")
                go_live(id_room)
        if "off" in state :
                print(" - statu sleep ")
                go_sleep()

redirecter_bridge()

