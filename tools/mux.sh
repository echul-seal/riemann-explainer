#!/bin/sh
# mux each scene with its narration (audio starts at 0, padded with silence to video length), then concat
cd /home/sprite/rh
mkdir -p mux
: > mux/list.txt
for f in s1 s2 s3 s4 s56; do grep -o '^class S[0-9]_[0-9]' $f.py | sed 's/class //'; done > order.txt
for s in $(cat order.txt); do
  k=$(echo $s | tr A-Z a-z)
  ffmpeg -loglevel error -y -i out/$s.mp4 -i audio/$k.dec.mp3 -filter_complex "[1:a]aresample=48000,apad[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -ac 2 -shortest mux/$s.mp4 || echo "MUXFAIL $s"
  echo "file '$s.mp4'" >> mux/list.txt
done
ffmpeg -loglevel error -y -f concat -safe 0 -i mux/list.txt -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -movflags +faststart final.mp4 || echo CONCATFAIL
ffprobe -v error -show_entries format=duration:stream=codec_type,duration -of compact final.mp4
stat -c %s final.mp4
touch mux.flag
