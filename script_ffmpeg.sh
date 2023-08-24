#!/bin/bash
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

ffmpeg  -i $u \
-c:v libx264 -b:a 384k -ac 2 -preset slow -crf 28 \
-profile:v high -bf 2 -pix_fmt yuv420p \
-threads 4 -xerror \
-vstats_file MFRfile.txt -maxrate 5M -bufsize 10M -r 30 -g 15 -coder 1 -f flv $key_stream #2> ylog.txt

    sleep 1
done
