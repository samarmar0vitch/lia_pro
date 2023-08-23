#!/bin/bash
u=$1
#https://pull-flv-l11-va01.tiktokcdn.com/stage/stream-2995889464288477225_ld.flv"
#u="https://pull-flv-l11-va01.tiktokcdn.com/stage/stream-2995889464288477225_or4.flv"
#u="https://pull-flv-l10-sg01.tiktokcdn.com/stage/stream-2131194588457074889_or4.flv"
#"https://pull-flv-l11-sg01.tiktokcdn.com/stage/stream-2131194051112730667_or4.flv"
#u="https://pull-flv-l11-va01.tiktokcdn.com/stage/stream-2995884191939821609_or4.flv"
#u="https://pull-flv-l1-sg01.tiktokcdn.com/stage/stream-2419421850622230574_or4.flv"
#https://pull-flv-l11-sg01.tiktokcdn.com/stage/stream-2419421421996343339_or4.flv"
#https://pull-flv-l11-sg01.tiktokcdn.com/stage/stream-2419419025472749611_uhd.flv"
#"https://pull-flv-l11-va01.tiktokcdn.com/stage/stream-2995880381150920745_or4.flv"
#url_tik="https://pull-flv-l11-sg01.tiktokcdn.com/stage/stream-2419419712398032939_or4.flv"
key_stream="rtmp://a.rtmp.youtube.com/live2/ms9z-mx5s-fvjg-9tmf-93ap"
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
