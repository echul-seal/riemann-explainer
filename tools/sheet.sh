#!/bin/sh
# usage: sheet.sh NAME SCENE...  -> NAME.jpg : one row of 6 frames per scene (320x180 each)
cd /home/sprite/rh
name=$1; shift
mkdir -p sh/$name; rm -f sh/$name/*
r=0
for s in "$@"; do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 out/$s.mp4)
  for i in 0 1 2 3 4 5; do
    t=$(python3 -c "print(($i+0.5)*$d/6)")
    ffmpeg -loglevel error -y -ss $t -i out/$s.mp4 -frames:v 1 -vf scale=480:270 sh/$name/$(printf %02d $r)_$i.png
  done
  r=$((r+1))
done
ffmpeg -loglevel error -y -pattern_type glob -i "sh/$name/*.png" -vf "tile=6x$r" -frames:v 1 -pix_fmt yuvj420p -q:v 3 $name.jpg
stat -c %s $name.jpg
