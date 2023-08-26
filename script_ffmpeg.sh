#!/bin/bash
kill -9 `pidof ffmpeg`

u=$1
key_stream="rtmp://a.rtmp.youtube.com/live2/"$you_tokens
trap printout SIGINT
printout() {
    echo ""
    echo "Finished with count=$count"
    exit
}
while :
do
    ((count++))

ffmpeg -probesize 100M -analyzeduration 20M -re -vsync 2 -i $u \
-c:v libx264 -b:a 384k -ac 2 -preset slow -crf 28 \
-profile:v high -bf 2 -pix_fmt yuvj420p \
-threads 4 -xerror \
-maxrate 5M -bufsize 10M -r 30 -g 15 -coder 1 -f flv $key_stream #2> ylog.txt

    sleep 1
done
##ffmpeg -probesize 100M -analyzeduration 20M -re -i "https://pull-f5-sg01.tiktokcdn.com/stage/stream-2131214758098501701_or4.flv" -strict -2 -c:v libx264 -pix_fmt yuv420p -c:a aac -map 0:0 -map 0:1 -ar 44100 -ab 128k -ac 2 -b:v 2567k -flags +global_header -bsf:a aac_adtstoasc -bufsize 1000k -f flv "rtmp://a.rtmp.youtube.com/live2/ms9z-mx5s-fvjg-9tmf-93ap"\n
