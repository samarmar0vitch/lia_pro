#!/bin/bash

#pkill ffmpeg
u=$1
echo $you_tokens
echo $1
key_stream="https://a.upload.youtube.com/http_upload_hls?cid="$you_tokens"&copy=0&file=master.m3u8"
trap printout SIGINT
printout() {
    echo ""
    echo "Finished with count=$count"
    exit
}
while :
do
    ((count++))
   # ffmpeg -hide_banner -re -fflags +genpts -i $u -flags +global_header -c:v copy -tag:v hvc1 -codec:a copy -hls_init_time 6.000 -hls_time 6.000 -strftime 1 -master_pl_name master.m3u8 -http_persistent 1 -f hls -segment_wrap 1 -method POST "https://a.upload.youtube.com/http_upload_hls?cid="$you_tokens"&copy=0&file=master.m3u8"
    ffmpeg -hide_banner  -re -fflags +genpts -i $u -vf "drawtext=fontfile=/usr/share/fonts/truetype/ttf-bitstream-vera/Vera.ttf: text='%{localtime\:%Y/%m/%d %H\\\\\:%M\\\\\:%S}': fontcolor=white@1: x=2: y=8" -flags +global_header -c:v libx264 -tag:v hvc1 -c:a copy -hls_init_time 4.000 -hls_time 4.000 -strftime 1 -master_pl_name master.m3u8 -http_persistent 1 -f hls -segment_wrap 1 -method POST $key_stream

   kill -9 `pidof ffmpeg`
   sleep 0.5
   
done
##ffmpeg -probesize 100M -analyzeduration 20M -re -i "https://pull-f5-sg01.tiktokcdn.com/stage/stream-2131214758098501701_or4.flv" -strict -2 -c:v libx264 -pix_fmt yuv420p -c:a aac -map 0:0 -map 0:1 -ar 44100 -ab 128k -ac 2 -b:v 2567k -flags +global_header -bsf:a aac_adtstoasc -bufsize 1000k -f flv "rtmp://a.rtmp.youtube.com/live2/ms9z-mx5s-fvjg-9tmf-93ap"\n
#ffmpeg -probesize 100M -analyzeduration 20M -re -vsync 2 -i $u \
#-c:v libx264 -b:a 384k -ac 2 -preset slow -crf 28 \
#-profile:v high -bf 2 -pix_fmt yuvj420p \
#-threads 4 -xerror \ sleep 1
#-maxrate 5M -bufsize 10M -r 30 -g 15 -coder 1 -f flv $key_stream #2> ylog.txt
