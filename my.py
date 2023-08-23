import requests as req
from enums import Mode, Error, StatusCode, TimeOut

import time
import json
import requests as req
import re
import os
import shutil
import ffmpeg
import sys

aa = sys.argv[1]
#aa="souraya700"
#"tumpolinaaa"
#"liaeljoni1"
tokens_y="ms9z-mx5s-fvjg-9tmf-93ap"
to_you="rtmp://a.rtmp.youtube.com/live2"
headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Referer": "https://www.tiktok.com/",
            }
def is_user_in_live(room_id):
    try:
            url = f"https://www.tiktok.com/api/live/detail/?aid=1988&roomID={room_id}"
            content = req.get(url).text
            #print(content)

            return '"status":4' not in content
    except :
            print('not')



def get_i0d(user):
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
            print("[*] URL FLV", live_url_flv)
            json_formatted_str_2 = json.dumps(json_data['data']['stream_url'], indent=2)
            print("[*] URL FLV", live_url_flv_2)
            #print("[*] URL FLV", json_formatted_str_2)

            return live_url_flv
        except Exception as ex:
            print(ex)





#lol = get_i0d("babajackson84")
# lol=get_i0d("polinaxxklobbey")
lol=get_i0d(aa)
# lol=get_id("mohamedabbesaissa")
#lol="7269147481902992134"
is_user_in_live(lol)
print(lol)
live_url=get_live_url(lol)
stream = ffmpeg.input(live_url)
# https://www.tiktok.com/api/live/detail/?aid=1988&roomID=7249314395203930906
 # ffmpeg -re -i https://pull-flv-l1-sg01.tiktokcdn.com/stage/stream-2419430691477127214_or4.flv -c:v copy -c:a aac -ar 44100 -ab 128k -ac 2 -strict -2 -flags +global_header -bsf:a aac_adtstoasc -bufsize 3000k -f flv "rtmp://a.rtmp.youtube.com/live2/ms9z-mx5s-fvjg-9tmf-93ap"
