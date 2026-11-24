#!/bin/sh
cd /home/sprite/rh
mkdir -p logs out
rm -f logs/*.fail logs/ALL.flag
for f in s1 s2 s3 s4 s56; do grep -o '^class S[0-9]_[0-9]' $f.py | sed "s/class /$f /"; done > jobs.txt
cat jobs.txt | xargs -P 4 -L 1 sh -c '[ -e logs/$1.done ] && exit 0; manim --disable_caching --media_dir m/$1 -o $1.mp4 $0.py $1 > logs/$1.log 2>&1 && cp m/$1/videos/$0/1080p30/$1.mp4 out/ && touch logs/$1.done || touch logs/$1.fail'
touch logs/ALL.flag
